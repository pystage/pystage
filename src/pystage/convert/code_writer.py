import builtins
import dis
import importlib
import inspect
import json
import keyword
import logging
import re
import textwrap

from jinja2 import Undefined
from jinja2.exceptions import UndefinedError
from jinja2.sandbox import SandboxedEnvironment

from pystage.core.sprite import CoreSprite
from pystage.core.stage import CoreStage

logger = logging.getLogger(__name__)

to_underscore = re.compile(r"[^A-Za-z0-9_]")
valid_variable_start = re.compile(r"[a-zA-Z_]")
multiple_underscores = re.compile(r"_+")
identifier = re.compile(r"[A-Za-z_][A-Za-z0-9_]*\Z")
integer_literal = re.compile(r"[0-9]+\Z")

# Characters that end a line for Python or for str.splitlines.
# They must never be written literally into the generated code.
_line_breaks = re.compile("[\x00-\x1f\x7f\x85  ]")

# Names that can't be used for sprites or custom blocks
RESERVED = set(keyword.kwlist) | set(dir(builtins)) | {"self"}

# Inputs that contain a stack of blocks and not a value
SUBSTACKS = ("SUBSTACK", "SUBSTACK2")


def py_str(value):
    """A Python string literal for any value.

    Everything that comes from a Scratch project has to go through this
    function (or to_identifier) before it is written into Python code.
    """
    text = json.dumps("" if value is None else str(value), ensure_ascii=False)
    return _line_breaks.sub(lambda m: "\\u%04x" % ord(m.group()), text)


def quoted(value):
    if not isinstance(value, str):
        return value
    if value.startswith("\""):
        return value
    else:
        return py_str(value)


def unquoted(value):
    if not isinstance(value, str):
        return value
    if value.startswith("\""):
        try:
            return json.loads(value)
        except ValueError:
            return value.strip("\"")
    else:
        return value


def to_identifier(name, default="x"):
    """A valid Python name that resembles the given name."""
    umlauts = {"ö": "oe", "ü": "ue", "ä": "ae", "ß": "ss"}
    vname = str(name).lower().strip()
    for c in umlauts:
        vname = vname.replace(c, umlauts[c])
    # Replace everything that is not allowed in a
    # variable name with underscores
    vname = to_underscore.sub("_", vname)
    vname = multiple_underscores.sub("_", vname)[:60]
    if vname.strip("_") == "":
        vname = default
    # Check of the variable does not start with a number
    if not valid_variable_start.fullmatch(vname[0]):
        vname = "_" + vname
    return vname


def unique_identifier(name, used, default="x"):
    """Like to_identifier, but the name is not in used afterwards. Adds it to used."""
    base = to_identifier(name, default)
    vname = base
    i = 2
    while vname in used or vname in RESERVED:
        vname = f"{base}_{i}"
        i += 1
    used.add(vname)
    return vname


def comment_lines(text):
    """Python comment lines for a text."""
    lines = _line_breaks.sub("\n", str(text)).split("\n")
    return "".join(f"# {line.strip()}\n" for line in lines if line.strip())


def resolve(value):
    """The value of the first field of a (menu) block."""
    depth = 0
    while not isinstance(value, str):
        if not isinstance(value, dict) or not value["params"] or depth > 10:
            raise ValueError(f"No suitable value found: {value}")
        value = next(iter(value["params"].values()))
        depth += 1
    return value


##
# Lookup of API functions. This is done very often, so we use indexes.
#

# class: {name: function}
_functions = {}
# class: {opcode: [function, ...]}
_opcodes = {}
# class: {core name: translated function}
_translated = {}


def _get_functions(cls):
    if cls not in _functions:
        _functions[cls] = dict(inspect.getmembers(cls, predicate=inspect.isfunction))
        by_opcode = {}
        for func in _functions[cls].values():
            if hasattr(func, "opcode"):
                by_opcode.setdefault(func.opcode, []).append(func)
        _opcodes[cls] = by_opcode
    return _functions[cls]


def _get_translated(cls):
    if cls not in _translated:
        res = {}
        for name, func in inspect.getmembers(cls, predicate=inspect.isfunction):
            for i in dis.Bytecode(func):
                if (i.opname == "LOAD_METHOD" or i.opname == "LOAD_ATTR") and i.argval != "_core":
                    res.setdefault(i.argval, func)
        _translated[cls] = res
    return _translated[cls]


class EmptyInput(Undefined):
    """Inputs of a block that are not filled are an empty text."""

    def __str__(self):
        return '""'

    def __bool__(self):
        return False


COMPARISONS = ("operator_gt", "operator_lt", "operator_equals")
# Divisions: Python raises an error for a divisor of 0
DIVISIONS = ("operator_divide", "operator_mod")


class CodeWriter():
    '''
    Helper class to write code templates
    '''
    def __init__(self, project, templates, language="core"):
        super().__init__()
        self.project = project
        self.templates = templates
        self.language = language
        self.lang_module = importlib.import_module(f"pystage.{language}")

        self.comments = []
        self.last_id = 0
        self.current_sprite = ""
        # The custom block that is currently written
        self.current_procedure = None
        # sprite name: {proccode: procedure}
        self.procedures = {}
        self.jinja_environment = SandboxedEnvironment(trim_blocks=True, lstrip_blocks=True, undefined=EmptyInput)
        self.jinja_environment.filters["global_sound"] = lambda name: self.global_sound(name)
        self.jinja_environment.filters["global_costume"] = lambda name: self.global_costume(name)
        self.jinja_environment.filters["global_backdrop"] = lambda name: self.global_backdrop(name)
        self.jinja_environment.filters["global_sprite"] = lambda name: self.global_sprite(name)
        self.jinja_environment.filters["if_missing"] = lambda x, extra: x or extra
        self.jinja_environment.filters["as_int"] = lambda x: x if integer_literal.match(str(x)) else f"int({x})"
        self._compiled = {}

        # Python names for stage, sprites and custom blocks have to be unique
        self.used_names = {"stage"}
        self.sprite_vars = {project["stage"]["name"]: "stage"}
        for sprite in project["sprites"]:
            if sprite["name"] not in self.sprite_vars:
                self.sprite_vars[sprite["name"]] = unique_identifier(sprite["name"], self.used_names, "sprite")
        for sprite in [project["stage"]] + project["sprites"]:
            self._collect_procedures(sprite)

        logger.debug("CodeWriter created.")


    def _collect_procedures(self, sprite):
        procedures = self.procedures.setdefault(sprite["name"], {})
        sprite_var = self.sprite_vars[sprite["name"]]
        for block in sprite["blocks"]:
            if block["opcode"] != "procedures_definition" or "procedure" not in block:
                continue
            proc = block["procedure"]
            if proc["proccode"] in procedures:
                continue
            title = re.sub(r"%[sbn]", " ", proc["proccode"])
            used_args = set()
            procedures[proc["proccode"]] = {
                "name": unique_identifier(f"{sprite_var}_{title}", self.used_names, "block"),
                "args": {name: unique_identifier(name, used_args, "arg") for name in proc["args"]},
                "warp": proc["warp"],
            }


    def set_sprite(self, name):
        self.current_sprite = name


    def get_sprite_var(self, name=None):
        if name is None:
            name = self.current_sprite
        if name in self.sprite_vars:
            return self.sprite_vars[name]
        return None


    def global_sprite(self, name):
        """The Python expression for a sprite selected in a menu."""
        name = unquoted(name)
        if name == "_stage_":
            return "stage"
        if name == "_myself_":
            return "self"
        var = self.get_sprite_var(name)
        if var is None:
            # Special values like _mouse_ or an unknown sprite
            return py_str(name)
        return var


    def get_sprite_or_stage(self, name=None):
        if not name:
            name = self.current_sprite
        if self.project["stage"]["name"] == name:
            return self.project["stage"]
        for sprite in self.project["sprites"]:
            if sprite["name"]==name:
                return sprite
        raise ValueError(f"No stage or sprite found with name '{name}'.")

    def get_id(self):
        """Helper to create unique names.

        """
        self.last_id += 1
        return self.last_id


    def get_opcode_function(self, block):
        """Get core API function for a block.

        Use the function metadata to determine the correct core API
        function based on a given block, using opcode and params.

        Parameters
        ----------
        block : dict
            A block from the intermediate code representation.
        """
        cls = CoreStage if block["stage"] else CoreSprite
        functions = _get_functions(cls)
        opcode = block["opcode"]
        if opcode in functions:
            return functions[opcode]
        elsefunc = None
        for func in _opcodes[cls].get(opcode, []):
            if hasattr(func, "param"):
                if func.param in block["params"]:
                    try:
                        value = unquoted(resolve(block["params"][func.param]))
                    except ValueError:
                        continue
                    # Projects from Scratch 2 use lower case, e.g. for effects
                    if str(func.value).lower() == str(value).lower():
                        return func
            else:
                elsefunc = func
        if elsefunc:
            return elsefunc
        logger.info(f"No API method for {opcode}")
        return None


    def get_translated_name(self, corefunc, stage=False):
        """The name of a core function in the API of the target language."""
        cls = self.lang_module.stage_class if stage else self.lang_module.sprite_class
        if self.language == "core":
            return corefunc if hasattr(cls, corefunc) else None
        func = _get_translated(cls).get(corefunc)
        return func.__name__ if func else None


    def get_translated_function(self, block, language=None):
        """Get the name of the translated API function for a block.

        Use the function metadata to determine the correct translated API
        function based on a given block, using opcode and params.

        Parameters
        ----------
        block : dict
            A block from the intermediate code representation.
        """
        corefunc = self.get_opcode_function(block)
        if corefunc is None:
            return None
        return self.get_translated_name(corefunc.__name__, block["stage"])


    def get_translated_template(self, block):
        corefunc = self.get_opcode_function(block)
        func = self.get_translated_function(block)
        if func is None:
            # A text is valid as value and as statement
            return py_str(f"NOT SUPPORTED: {block['opcode']}")
        fieldname = corefunc.param if hasattr(corefunc, "param") else None
        res = f"self.{func}("
        res += ", ".join(["{{" + p + "}}" for p in block["params"] if p != fieldname and p not in SUBSTACKS])
        res += ")"
        return res


    def global_sound(self, name: str, quoted=True):
        name = unquoted(name)
        sprite = self.get_sprite_or_stage()
        for sound in sprite["sounds"]:
            if sound["local_name"] == name:
                global_name = self.project["sounds"][sound["md5"]]["global_name"]
                return py_str(global_name) if quoted else global_name
        # Unknown sounds are ignored when the program is played
        return py_str(name) if quoted else name


    def global_costume(self, name, quoted=True):
        name = unquoted(name)
        sprite = self.get_sprite_or_stage()
        for costume in sprite["costumes"]:
            if costume["local_name"] == name:
                global_name = self.project["costumes"][costume["md5"]]["global_name"]
                return py_str(global_name) if quoted else global_name
        return py_str(name) if quoted else name


    def global_backdrop(self, name, quoted=True):
        name = unquoted(name)
        sprite = self.project["stage"]
        for costume in sprite["costumes"]:
            if costume["local_name"] == name:
                global_name = self.project["costumes"][costume["md5"]]["global_name"]
                return py_str(global_name) if quoted else global_name
        # e.g. "next backdrop", "random backdrop", "previous backdrop"
        return py_str(name) if quoted else name


    def process(self, value):
        """The Python code for a value: A literal or a (reporter) block."""
        if not isinstance(value, dict):
            return str(value)
        return self.process_stack(value, statements=False)


    def process_stack(self, block, statements=True):
        """The Python code for a block and all blocks that follow."""
        texts = []
        while block:
            text, next_included = self.render(block, statements)
            texts.append(text)
            if next_included:
                break
            block = block["next"]
        return "\n".join(texts)


    def render(self, block, statement=True):
        """The code for a single block.

        Returns
        -------
        The code and a flag telling if the following blocks are included.
        """
        # Comments are written in front of the next statement.
        self.comments.extend(block.get("comments", []))

        opcode = block["opcode"]
        if opcode == "procedures_definition":
            return self.render_procedure_definition(block), True
        # Code that is already complete must never be used as template!
        if opcode == "procedures_call":
            return self._with_comments(self.render_procedure_call(block), statement), False
        if opcode in ("argument_reporter_string_number", "argument_reporter_boolean"):
            return self._with_comments(self.render_argument(block), statement), False

        context = {}
        if f"{opcode}.scratch" in self.templates and self.needs_scratch_division(block):
            # The Python operator is not safe, the core method follows Scratch.
            text = textwrap.dedent(self.templates[f"{opcode}.scratch"])
            context["func"] = self.get_translated_function(block)
            if context["func"] is None:
                return self._with_comments(py_str(f"NOT SUPPORTED: {opcode}"), statement), False
        elif opcode in self.templates and not self.needs_scratch_comparison(block):
            # If the block has its own template, we simply render it.
            text = textwrap.dedent(self.templates[opcode])
            # if the template needs a translated function name, we deliver it
            if "{{func}}" in text:
                context["func"] = self.get_translated_function(block)
                if context["func"] is None:
                    return self._with_comments(py_str(f"NOT SUPPORTED: {opcode}"), statement), False
        else:
            # We use the default template mechanism
            text = self.get_translated_template(block)

        is_hat = "NEXT" in text
        if is_hat:
            # The comments of a hat block belong in front of the function
            own_comments, self.comments = self.comments, []
            if block["next"]:
                context["NEXT"] = self.process_stack(block["next"])
        for param in block["params"]:
            if param in SUBSTACKS:
                context[param] = self.process_stack(block["params"][param])
            else:
                context[param] = self.process(block["params"][param])
        context["CURRENT_SPRITE"] = self.get_sprite_var()
        if "{{ID}}" in text:
            context["ID"] = self.get_id()

        # if {{NEXT | indent (4)}} is still in text, but there is no
        # NEXT in context, then it means the Scratch “hat” block is empty,
        # so set NEXT to "pass", so the function is essentially empty.
        if "indent(4)" in text:
            for key in ("NEXT",) + SUBSTACKS:
                if key in text and not (context.get(key) or "").strip():
                    context[key] = "pass"
        if "{{CONDITION}}" in text and not context.get("CONDITION"):
            context["CONDITION"] = "None"
        if text not in self._compiled:
            self._compiled[text] = self.jinja_environment.from_string(text)
        try:
            text = self._compiled[text].render(context)
        except UndefinedError as e:
            logger.warning(f"Template variable not available: {e}")
            text = py_str(f"NOT SUPPORTED: {opcode}")

        if is_hat:
            if own_comments:
                text = "\n" + "".join(comment_lines(c) for c in own_comments) + text.lstrip("\n")
            return text, True
        return self._with_comments(text, statement), False


    def needs_scratch_comparison(self, block):
        """Python operators are only safe if no text literal is compared.

        Scratch compares a number with a text by comparing texts, Python
        raises a TypeError. So those comparisons call the core method.
        """
        if block["opcode"] not in COMPARISONS:
            return False
        return any(isinstance(value, str) and value.startswith('"') for value in block["params"].values())


    def needs_scratch_division(self, block):
        """Python operators for / and mod are only safe for a divisor other than 0.

        In Scratch, dividing by 0 gives Infinity, -Infinity or NaN. So the
        core method is called unless the divisor is a number literal that
        is not 0 and the dividend is not a text literal.
        """
        if block["opcode"] not in DIVISIONS:
            return False
        dividend, divisor = block["params"].get("NUM1"), block["params"].get("NUM2")
        is_number = lambda value: isinstance(value, (int, float)) and not isinstance(value, bool)
        return not (is_number(divisor) and divisor != 0 and (is_number(dividend) or isinstance(dividend, dict)))

    def _with_comments(self, text, statement):
        """Write the collected comments in front of a statement."""
        if statement and self.comments:
            text = "".join(comment_lines(c) for c in self.comments) + text
            self.comments = []
        return text


    def get_no_refresh_name(self):
        """The name of the no_refresh decorator in the target language."""
        from pystage.core.code_block import no_refresh
        for name, obj in vars(self.lang_module).items():
            if obj is no_refresh:
                return name
        return None


    def uses_no_refresh(self):
        return any(proc["warp"] for procedures in self.procedures.values() for proc in procedures.values())


    def render_procedure_definition(self, block):
        proc = self.procedures[self.current_sprite].get(block.get("procedure", {}).get("proccode"))
        if proc is None or proc.get("written"):
            # Broken definition or the block is defined twice
            self.comments = []
            return ""
        proc["written"] = True
        own_comments, self.comments = self.comments, []
        self.current_procedure = proc
        body = self.process_stack(block["next"]) if block["next"] else ""
        self.current_procedure = None
        if not body.strip():
            body = "pass"
        text = "\n"
        text += "".join(comment_lines(c) for c in own_comments)
        if proc["warp"] and self.get_no_refresh_name():
            text += f"@{self.get_no_refresh_name()}\n"
        text += f"def {proc['name']}({', '.join(['self'] + list(proc['args'].values()))}):\n"
        text += textwrap.indent(body, "    ", lambda line: line.strip() != "")
        return text.rstrip("\n") + "\n\n"


    def render_procedure_call(self, block):
        proc = self.procedures[self.current_sprite].get(block.get("proccode"))
        if proc is None:
            return py_str(f"NOT SUPPORTED: unknown custom block {block.get('proccode')}")
        args = [self.process(arg) for arg in block.get("args", [])]
        # Missing or additional arguments do not hurt in Scratch
        args = (args + ['""'] * len(proc["args"]))[:len(proc["args"])]
        return f"{proc['name']}({', '.join(['self'] + args)})"


    def render_argument(self, block):
        name = unquoted(block["params"].get("VALUE", ""))
        if self.current_procedure and name in self.current_procedure["args"]:
            return self.current_procedure["args"][name]
        # Arguments that are used outside of their custom block are 0 in Scratch
        return "0"
