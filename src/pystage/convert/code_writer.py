import io
import sys
import textwrap
import re
import logging
import inspect
import ast
import importlib
import dis
from jinja2 import Template, Environment
from jinja2.exceptions import UndefinedError
logger = logging.getLogger(__name__)

from pystage.core.sprite import CoreSprite
from pystage.core.stage import CoreStage



def quoted(value):
    if not isinstance(value, str):
        return value
    if value.startswith("\""):
        return value
    else:
        return f"\"{value}\""


def unquoted(value):
    if not isinstance(value, str):
        return value
    if value.startswith("\""):
        return value.strip("\"")
    else:
        return value

def resolve(value):
    # print(f"Resolving: {value}")
    if isinstance(value, str):
        return value
    for key in value["params"]:
        res = resolve(value["params"][key])
        # print(f"Resolved value: {res}")
        return res
    raise ValueError(f"No suitable value found: {value}")




class CodeWriter():
    '''
    Helper class to write code templates
    '''
    def __init__(self, project, templates, language="core"):
        super().__init__()
        self.project = project
        self.templates = templates
        self.language = language

        self.comments = []
        self.last_id = 0
        self.current_sprite = ""
        self.jinja_environment = Environment(trim_blocks=True, lstrip_blocks=True)
        self.jinja_environment.filters["global_sound"] = lambda name: self.global_sound(name)
        self.jinja_environment.filters["global_costume"] = lambda name: self.global_costume(name)
        self.jinja_environment.filters["global_backdrop"] = lambda name: self.global_backdrop(name)
        
        logger.debug("CodeWriter created.")


    def set_sprite(self, name):
        self.current_sprite = name


    def get_sprite_var(self, name=None):
        def to_python(name: str):
            return name.lower().replace(" ", "_"). replace("-", "_")
        if name is None:
            return to_python(self.current_sprite)
        else:
            return to_python(name)

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
        # print("Getting function for opcode: " + block["opcode"])
        cls = CoreStage if block["stage"] else CoreSprite
        # print(f"Searching in class: {cls}")
        elsefunc = None
        for name, func in inspect.getmembers(cls, predicate=inspect.isfunction):
            # print(f"Testing: {name} - {func}")
            if name==block["opcode"]:
                # print(f"Matching API method: {name}")
                return func
            if hasattr(func, "opcode"):
                if func.opcode == block["opcode"]:
                    if hasattr(func, "param"):
                        if func.param in block["params"]:
                            value = unquoted(resolve(block["params"][func.param]))
                            if func.value==value:
                                # print(f"Matching API method: {name}")
                                return func
                    else:
                        elsefunc = func
        if elsefunc:
            # print(f"Matching API method: {elsefunc}")
            return elsefunc
        print(f"No API method for {block.opcode}")
        return None


    def get_translated_function(self, block, language):
        """Get translated API function for a block.

        Use the function metadata to determine the correct translated API
        function based on a given block, using opcode and params.

        Parameters
        ----------
        block : dict
            A block from the intermediate code representation.
        """
        corefunc = self.get_opcode_function(block)
        if language=="core":
            return corefunc
        if corefunc is None:
            return None
        lang = importlib.import_module(f"pystage.{language}")
        cls = lang.stage_class if block["stage"] else lang.sprite_class
        for name, func in inspect.getmembers(cls, predicate=inspect.isfunction):
            for i in dis.Bytecode(func):
                if (i.opname=="LOAD_METHOD" or i.opname=="LOAD_ATTR") and i.argval==corefunc.__name__:
                    # print(f"Translated: {name}")
                    return func
        # print(f"No translated API method found for {block.opcode}")
        return None
            
        
    def get_translated_call(self, block, language):
        corefunc = self.get_opcode_function(block)
        func = self.get_translated_function(block, language)
        if func is None:
            return quoted(f"NO TRANSLATION: {block.opcode}")
        res = func.__name__ + "("
        fieldname = corefunc.param if hasattr(corefunc, "param") else None
        res += ", ".join([str(block.params[p]) for p in block.params if p != fieldname])
        res += ")"
        # print(res)
        return res


    def get_translated_template(self, block, language):
        corefunc = self.get_opcode_function(block)
        func = self.get_translated_function(block, language)
        if func is None:
            return quoted(f"NO TRANSLATION: {block.opcode}")
        res = f"self.{func.__name__}("
        fieldname = corefunc.param if hasattr(corefunc, "param") else None
        res += ", ".join(["{{" + p + "}}" for p in block.params if p != fieldname])
        res += ")"
        # print(res)
        return res



    def render_comments(self):
        res = ""
        for c in self.comments:
            for line in c.split("\n"):
                res += f"# {line}\n"
        self.comments.clear()
        return res


    def global_sound(self, name: str, quoted=True):
        name = unquoted(name)
        sprite = self.get_sprite_or_stage()
        for sound in sprite["sounds"]:
            if sound["local_name"] == name:
                q = '"' if quoted else ''
                return f'{q}{self.project["sounds"][sound["md5"]]["global_name"]}{q}'
        raise ValueError(f"No sound with name '{name}' found for sprite '{sprite['name']}'")
        

    def global_costume(self, name, quoted=True):
        name = unquoted(name)
        sprite = self.get_sprite_or_stage()
        for costume in sprite["costumes"]:
            if costume["local_name"] == name:
                q = '"' if quoted else ''
                return f'{q}{self.project["costumes"][costume["md5"]]["global_name"]}{q}'
        raise ValueError(f"No costume with name '{name}' found for sprite '{sprite['name']}'")


    def global_backdrop(self, name, quoted=True):
        name = unquoted(name)
        sprite = self.project["stage"]
        for costume in sprite["costumes"]:
            if costume["local_name"] == name:
                q = '"' if quoted else ''
                return f'{q}{self.project["costumes"][costume["md5"]]["global_name"]}{q}'
        raise ValueError(f"No backdrop with name '{name}' found for stage.")


    def process(self, block):
        if not isinstance(block, dict):
            # We have a simple value
            return str(block)
        else:
            # First we add comments to the queue
            if "comments" in block:
                self.comments.extend(block["comments"])
            # If the block has its own template, we simply render it.
            if block["opcode"] in self.templates:
                template = self.templates[block["opcode"]]
                context = {}
                # if the template needs a translated function name, we deliver it
                if "{{func}}" in template:
                    func = self.get_translated_function(block, self.language)
                    context["func"] = func.__name__ if func is not None else f"<<NO_FUNCTION-{block['opcode']}>>"
                return self.render(block, template, context)
            else:
                # We use the default template mechanism
                default_template = self.get_translated_template(block, self.language)
                return self.render(block, default_template)


    def render(self, block, text, context={}):
        text = textwrap.dedent(text)
        if block["next"]:
            context["NEXT"] = self.process(block["next"])
            if not "NEXT" in text:
                text += "\n{{NEXT}}"
        for param in block["params"]:
            context[param] = self.process(block["params"][param])
        context["CURRENT_SPRITE"] = self.get_sprite_var()
        if "{{ID}}" in text:
            context["ID"] = self.get_id()
        template = self.jinja_environment.from_string(text)
        try:
            text = template.render(context)
        except UndefinedError as e:
            print(f"Template variable not available: {e}")
        return text

