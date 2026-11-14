"""Builds Scratch 3 projects (.sb3) for the converter tests.

Scratch can't be used to create test projects automatically, so this
script writes projects with the same structure that Scratch 3 saves:
project.json with targets, blocks (including shadow and menu blocks),
variables, lists, monitors and comments, plus a tiny PNG for every
costume/backdrop and a tiny WAV for every sound.

The projects exercise the blocks that the real test projects in
tests/src/scratch_projects do not contain (pen, timer, stage scripts,
custom blocks, ...). Together, they cover every block that the converter
supports, see tests/tests/test_coverage.py.

Usage (from the tests directory):

    python make_projects.py

writes the projects into src/scratch_projects/generated (they are converted
and played by test_convert.py) and src/special_projects (projects that are
not meant to convert without warnings). Afterwards, create the expected
results with `python generate.py -a` and review the diff.

The output is reproducible: Running the script twice gives identical files.
"""
import hashlib
import io
import json
import struct
import sys
import wave
import zipfile
import zlib
from pathlib import Path

BASE = Path(__file__).resolve().parent / "src"


##
# Assets
#

def png(width, height, rgba):
    """A PNG file with one color."""
    def chunk(kind, data):
        content = kind + data
        return struct.pack(">I", len(data)) + content + struct.pack(">I", zlib.crc32(content))
    row = b"\x00" + bytes(rgba) * width
    return (b"\x89PNG\r\n\x1a\n"
            + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(row * height, 9))
            + chunk(b"IEND", b""))


def wav(frames=1102, rate=22050):
    """A short WAV file with silence."""
    buffer = io.BytesIO()
    with wave.open(buffer, "wb") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(rate)
        f.writeframes(b"\x00\x00" * frames)
    return buffer.getvalue()


class Assets:
    """The files of a project: md5 of the content is the name, like in Scratch."""

    def __init__(self):
        self.files = {}

    def add(self, extension, content):
        md5 = hashlib.md5(content).hexdigest()
        self.files[f"{md5}.{extension}"] = content
        return md5

    def costume(self, name, color, size=(40, 40)):
        md5 = self.add("png", png(size[0], size[1], color))
        return {"name": name, "bitmapResolution": 1, "dataFormat": "png", "assetId": md5,
                "md5ext": f"{md5}.png", "rotationCenterX": size[0] // 2, "rotationCenterY": size[1] // 2}

    def svg_costume(self, name, label="PLAY"):
        """A vector costume like Scratch's paint editor writes it: a button with a text."""
        svg = ('<svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="196" height="60" viewBox="0,0,196,60">'
               '<g transform="translate(-140,-154.3125)"><g fill-rule="nonzero" stroke="none">'
               '<path d="M140,214.3125v-60h196v60z" fill="#474252" stroke-width="0"/>'
               '<text transform="translate(215,191.3125) scale(0.5,0.5)" font-size="40" xml:space="preserve" '
               'fill="#dccbff" font-family="Sans Serif" font-weight="normal" text-anchor="start">'
               f'<tspan x="0" dy="0">{label}</tspan></text></g></g></svg>').encode()
        md5 = self.add("svg", svg)
        return {"name": name, "bitmapResolution": 1, "dataFormat": "svg", "assetId": md5,
                "md5ext": f"{md5}.svg", "rotationCenterX": 98, "rotationCenterY": 30}

    def backdrop(self, name, color):
        costume = self.costume(name, color, (480, 360))
        del costume["bitmapResolution"]
        return costume

    def sound(self, name, frames=1102):
        md5 = self.add("wav", wav(frames))
        return {"name": name, "assetId": md5, "dataFormat": "wav", "format": "", "rate": 22050,
                "sampleCount": frames, "md5ext": f"{md5}.wav"}


##
# Blocks
#

class Spec:
    """A block as the author writes it: opcode, inputs and fields."""

    def __init__(self, opcode, values, mutation=None):
        self.opcode = opcode
        self.values = values
        self.mutation = mutation


class T:
    """A literal with its own type of shadow block, e.g. T(9, "#ff0000") for a color."""

    def __init__(self, kind, value):
        self.kind, self.value = kind, value


class Var:
    """A variable reporter."""

    def __init__(self, name):
        self.name = name


class ListRef:
    """A list reporter."""

    def __init__(self, name):
        self.name = name


class Comment:
    """A comment, attached to a block (a Spec that is used in a script) or not."""

    def __init__(self, text, block=None):
        self.text, self.block = text, block


class Procedure:
    """The definition of a custom block."""

    def __init__(self, proccode, names, kinds, warp, body):
        self.proccode, self.names, self.kinds, self.warp, self.body = proccode, names, kinds, warp, body


# Fields instead of inputs
FIELDS = {
    "control_stop": {"STOP_OPTION"},
    "looks_seteffectto": {"EFFECT"}, "looks_changeeffectby": {"EFFECT"},
    "looks_gotofrontback": {"FRONT_BACK"}, "looks_goforwardbackwardlayers": {"FORWARD_BACKWARD"},
    "looks_costumenumbername": {"NUMBER_NAME"}, "looks_backdropnumbername": {"NUMBER_NAME"},
    "sound_seteffectto": {"EFFECT"}, "sound_changeeffectby": {"EFFECT"},
    "event_whenkeypressed": {"KEY_OPTION"}, "event_whengreaterthan": {"WHENGREATERTHANMENU"},
    "event_whenbackdropswitchesto": {"BACKDROP"}, "event_whenbroadcastreceived": {"BROADCAST_OPTION"},
    "motion_setrotationstyle": {"STYLE"}, "sensing_setdragmode": {"DRAG_MODE"},
    "sensing_current": {"CURRENTMENU"}, "sensing_of": {"PROPERTY"}, "operator_mathop": {"OPERATOR"},
    "data_setvariableto": {"VARIABLE"}, "data_changevariableby": {"VARIABLE"},
    "data_showvariable": {"VARIABLE"}, "data_hidevariable": {"VARIABLE"},
    "argument_reporter_string_number": {"VALUE"}, "argument_reporter_boolean": {"VALUE"},
}
for _opcode in ("data_addtolist", "data_deleteoflist", "data_deletealloflist", "data_insertatlist",
                "data_replaceitemoflist", "data_itemoflist", "data_itemnumoflist", "data_lengthoflist",
                "data_listcontainsitem", "data_showlist", "data_hidelist"):
    FIELDS[_opcode] = {"LIST"}

# Inputs with a dropdown: (opcode, input): (menu block, field of the menu block)
MENUS = {
    ("motion_goto", "TO"): ("motion_goto_menu", "TO"),
    ("motion_glideto", "TO"): ("motion_glideto_menu", "TO"),
    ("motion_pointtowards", "TOWARDS"): ("motion_pointtowards_menu", "TOWARDS"),
    ("looks_switchcostumeto", "COSTUME"): ("looks_costume", "COSTUME"),
    ("looks_switchbackdropto", "BACKDROP"): ("looks_backdrops", "BACKDROP"),
    ("looks_switchbackdroptoandwait", "BACKDROP"): ("looks_backdrops", "BACKDROP"),
    ("sound_play", "SOUND_MENU"): ("sound_sounds_menu", "SOUND_MENU"),
    ("sound_playuntildone", "SOUND_MENU"): ("sound_sounds_menu", "SOUND_MENU"),
    ("sensing_touchingobject", "TOUCHINGOBJECTMENU"): ("sensing_touchingobjectmenu", "TOUCHINGOBJECTMENU"),
    ("sensing_distanceto", "DISTANCETOMENU"): ("sensing_distancetomenu", "DISTANCETOMENU"),
    ("sensing_keypressed", "KEY_OPTION"): ("sensing_keyoptions", "KEY_OPTION"),
    ("sensing_of", "OBJECT"): ("sensing_of_object_menu", "OBJECT"),
    ("control_create_clone_of", "CLONE_OPTION"): ("control_create_clone_of_menu", "CLONE_OPTION"),
    ("pen_changePenColorParamBy", "COLOR_PARAM"): ("pen_menu_colorParam", "colorParam"),
    ("pen_setPenColorParamTo", "COLOR_PARAM"): ("pen_menu_colorParam", "colorParam"),
}

# The kind of shadow block for number inputs that are not simply a number (4)
INPUT_TYPES = {"DEGREES": 8, "DIRECTION": 8, "SECS": 5, "DURATION": 5, "TIMES": 6, "INDEX": 7, "NUM": 4,
               "SIZE": 4}
# Inputs of the type text. Where a reporter is plugged in, Scratch keeps a text as shadow.
TEXT_INPUTS = {"MESSAGE", "STRING", "STRING1", "STRING2", "ITEM", "QUESTION", "LETTER", "OPERAND1", "OPERAND2"}


def b(opcode, **values):
    """A block. Inputs and fields are keyword arguments, see FIELDS and MENUS."""
    mutation = values.pop("mutation", None)
    return Spec(opcode, values, mutation)


def flag(*body):
    return [b("event_whenflagclicked"), *body]


def say(value):
    return b("looks_say", MESSAGE=value)


def repeat(times, *body):
    return b("control_repeat", TIMES=times, SUBSTACK=list(body))


def forever(*body):
    return b("control_forever", SUBSTACK=list(body))


def wait(seconds):
    return b("control_wait", DURATION=seconds)


def is_boolean_input(opcode, name):
    return name == "CONDITION" or opcode in ("operator_and", "operator_or", "operator_not")


class Target:
    """A stage or sprite: collects scripts and creates the blocks of the sb3 file."""

    def __init__(self, name, assets, stage=False, costumes=(), sounds=(), **properties):
        self.name = name
        self.stage = stage
        self.prefix = "stage" if stage else name.lower()
        self.assets = assets
        self.scripts = []
        self.blocks = {}
        self.variables = {}
        self.lists = {}
        self.broadcasts = {}
        self.comments = {}
        self.procedures = {}
        # id of the Python object of a Spec: block id, to attach comments
        self.spec_ids = {}
        self.costumes = list(costumes)
        self.sounds = list(sounds)
        self.properties = properties
        self.counter = 0

    # Declarations
    def variable(self, name, value=0, cloud=False):
        entry = [name, value] + ([True] if cloud else [])
        self.variables[f"var_{self.prefix}_{name}"] = entry
        return self

    def list(self, name, items=()):
        self.lists[f"list_{self.prefix}_{name}"] = [name, list(items)]
        return self

    def script(self, *blocks):
        """A script: the first block is the hat block (or the first block of a loose script)."""
        self.scripts.append(list(blocks[0]) if isinstance(blocks[0], list) else list(blocks))
        return self

    def define(self, proccode, names=(), kinds=(), warp=False, body=()):
        """A custom block. kinds: "s" for text or number and "b" for boolean arguments."""
        kinds = kinds or "s" * len(names)
        procedure = Procedure(proccode, list(names), list(kinds), warp, list(body))
        self.procedures[proccode] = [f"{self.prefix}_arg_{len(self.procedures)}_{i}" for i in range(len(names))]
        self.scripts.append([procedure])
        return self

    def comment(self, text, block=None):
        self.scripts.append([Comment(text, block)])
        return self

    # Variable and list ids
    def var_id(self, name):
        for key, entry in self.variables.items():
            if entry[0] == name:
                return key
        return f"var_{name}"

    def list_id(self, name):
        for key, entry in self.lists.items():
            if entry[0] == name:
                return key
        return f"list_{name}"

    # Creating blocks
    def new_id(self):
        self.counter += 1
        return f"{self.prefix}_{self.counter}"

    def add(self, opcode, parent, shadow=False, top=False):
        block_id = self.new_id()
        self.blocks[block_id] = {"opcode": opcode, "next": None, "parent": parent, "inputs": {}, "fields": {},
                                 "shadow": shadow, "topLevel": top}
        return block_id

    def stack(self, specs, parent):
        """Creates the blocks of a stack, returns the id of the first."""
        first = previous = None
        for spec in specs:
            block_id = self.spec(spec, previous if previous else parent)
            if previous:
                self.blocks[previous]["next"] = block_id
            else:
                first = block_id
            previous = block_id
        return first

    def spec(self, spec, parent, top=False):
        if isinstance(spec, Procedure):
            return self.definition(spec, top)
        if spec.opcode == "procedures_call":
            block_id = self.call(spec, parent)
            self.spec_ids[id(spec)] = block_id
            return block_id
        block_id = self.add(spec.opcode, parent, top=top)
        self.spec_ids[id(spec)] = block_id
        block = self.blocks[block_id]
        fields = FIELDS.get(spec.opcode, ())
        for name, value in spec.values.items():
            if name in fields:
                block["fields"][name] = self.field(spec.opcode, name, value)
            else:
                self.input(block, block_id, name, value)
        if spec.mutation is not None:
            block["mutation"] = spec.mutation
        if spec.opcode == "control_stop":
            option = spec.values["STOP_OPTION"]
            block["mutation"] = {"tagName": "mutation", "children": [],
                                 "hasnext": "true" if option.startswith("other") else "false"}
        return block_id

    def field(self, opcode, name, value):
        if name == "VARIABLE":
            return [value, self.var_id(value)]
        if name == "LIST":
            return [value, self.list_id(value)]
        if name == "BROADCAST_OPTION":
            return [value, self.broadcast(value)]
        return [value, None]

    def broadcast(self, message):
        key = f"broadcast_{message}"
        self.broadcasts[key] = message
        return key

    def input(self, block, block_id, name, value):
        opcode = block["opcode"]
        menu = MENUS.get((opcode, name))
        if menu and not isinstance(value, Spec):
            menu_id = self.add(menu[0], block_id, shadow=True)
            self.blocks[menu_id]["fields"][menu[1]] = [value, None]
            block["inputs"][name] = [1, menu_id]
        elif menu:
            reporter = self.spec(value, block_id)
            menu_id = self.add(menu[0], block_id, shadow=True)
            self.blocks[menu_id]["fields"][menu[1]] = ["_mouse_", None]
            block["inputs"][name] = [3, reporter, menu_id]
        elif isinstance(value, Spec):
            reporter = self.spec(value, block_id)
            if is_boolean_input(opcode, name):
                block["inputs"][name] = [2, reporter]
            else:
                shadow = [10, ""] if name in TEXT_INPUTS else [4, "0"]
                block["inputs"][name] = [3, reporter, shadow]
        elif isinstance(value, list):
            if value:
                block["inputs"][name] = [2, self.stack(value, block_id)]
        elif isinstance(value, Var):
            block["inputs"][name] = [3, [12, value.name, self.var_id(value.name)], [10, ""]]
        elif isinstance(value, ListRef):
            block["inputs"][name] = [3, [13, value.name, self.list_id(value.name)], [10, ""]]
        elif isinstance(value, T):
            if value.kind == 11:
                block["inputs"][name] = [1, [11, value.value, self.broadcast(value.value)]]
            else:
                block["inputs"][name] = [1, [value.kind, str(value.value)]]
        elif isinstance(value, str):
            if opcode in ("event_broadcast", "event_broadcastandwait"):
                block["inputs"][name] = [1, [11, value, self.broadcast(value)]]
            else:
                block["inputs"][name] = [1, [10, value]]
        else:
            block["inputs"][name] = [1, [INPUT_TYPES.get(name, 4), str(value)]]

    def prototype(self, parent, procedure):
        ids = self.procedures[procedure.proccode]
        proto = self.add("procedures_prototype", parent, shadow=True)
        block = self.blocks[proto]
        for arg_id, name, kind in zip(ids, procedure.names, procedure.kinds):
            opcode = "argument_reporter_boolean" if kind == "b" else "argument_reporter_string_number"
            reporter = self.add(opcode, proto, shadow=True)
            self.blocks[reporter]["fields"]["VALUE"] = [name, None]
            block["inputs"][arg_id] = [1, reporter]
        block["mutation"] = {
            "tagName": "mutation", "children": [], "proccode": procedure.proccode,
            "argumentids": json.dumps(ids), "argumentnames": json.dumps(procedure.names),
            "argumentdefaults": json.dumps(["false" if k == "b" else "" for k in procedure.kinds]),
            "warp": "true" if procedure.warp else "false",
        }
        return proto

    def definition(self, procedure, top):
        block_id = self.add("procedures_definition", None, top=True)
        proto = self.prototype(block_id, procedure)
        self.blocks[block_id]["inputs"]["custom_block"] = [1, proto]
        self.blocks[block_id]["next"] = self.stack(procedure.body, block_id)
        return block_id

    def call(self, spec, parent):
        proccode = spec.values["proccode"]
        ids = self.procedures[proccode]
        block_id = self.add("procedures_call", parent)
        block = self.blocks[block_id]
        kinds = [part for part in proccode.split() if part in ("%s", "%b")]
        for arg_id, kind, value in zip(ids, kinds, spec.values["args"]):
            if kind == "%b":
                if isinstance(value, Spec):
                    block["inputs"][arg_id] = [2, self.spec(value, block_id)]
            else:
                self.input(block, block_id, arg_id, value)
        block["mutation"] = {"tagName": "mutation", "children": [], "proccode": proccode,
                             "argumentids": json.dumps(ids), "warp": "false"}
        return block_id

    def build(self):
        """The blocks and comments of the scripts."""
        for i, script in enumerate(self.scripts):
            if isinstance(script[0], Comment):
                continue
            first = self.spec(script[0], None, top=True)
            block = self.blocks[first]
            block["x"], block["y"] = 20 + 300 * (i % 2), 20 + 150 * (i // 2)
            if not isinstance(script[0], Procedure):
                block["next"] = self.stack(script[1:], first)
        for i, script in enumerate(self.scripts):
            if isinstance(script[0], Comment):
                comment = script[0]
                self.comments[f"comment_{self.prefix}_{i}"] = {
                    "blockId": self.spec_ids[id(comment.block)] if comment.block else None,
                    "x": 400, "y": 20 + 60 * i, "width": 200, "height": 100,
                    "minimized": False, "text": comment.text}

    def target(self, layer):
        self.build()
        res = {
            "isStage": self.stage, "name": self.name,
            "variables": self.variables, "lists": self.lists, "broadcasts": self.broadcasts,
            "blocks": self.blocks, "comments": self.comments, "currentCostume": 0,
            "costumes": self.costumes, "sounds": self.sounds, "volume": 100, "layerOrder": layer,
        }
        if self.stage:
            res.update({"tempo": 60, "videoTransparency": 50, "videoState": "on", "textToSpeechLanguage": None})
        else:
            res.update({"visible": True, "x": 0, "y": 0, "size": 100, "direction": 90, "draggable": False,
                        "rotationStyle": "all around"})
        res.update(self.properties)
        return res


def variable_monitor(target, name, mode="default", x=5, y=5, sprite=None, **more):
    return dict({
        "id": target.var_id(name), "mode": mode, "opcode": "data_variable", "params": {"VARIABLE": name},
        "spriteName": sprite, "value": 0, "width": 0, "height": 0, "x": x, "y": y, "visible": True,
        "sliderMin": 0, "sliderMax": 100, "isDiscrete": True}, **more)


def list_monitor(target, name, x=5, y=5, sprite=None):
    return {"id": target.list_id(name), "mode": "list", "opcode": "data_listcontents", "params": {"LIST": name},
            "spriteName": sprite, "value": [], "width": 150, "height": 100, "x": x, "y": y, "visible": True}


def reporter_monitor(opcode, params=None, mode="default", x=5, y=5, sprite=None):
    return {"id": opcode, "mode": mode, "opcode": opcode, "params": params or {}, "spriteName": sprite,
            "value": 0, "width": 0, "height": 0, "x": x, "y": y, "visible": True}


class Project:
    """A project with a stage and sprites."""

    def __init__(self, sprites=1):
        self.assets = Assets()
        self.stage = Target("Stage", self.assets, stage=True, costumes=[
            self.assets.backdrop("backdrop1", (255, 255, 255, 255)),
            self.assets.backdrop("backdrop2", (200, 220, 255, 255))],
            sounds=[self.assets.sound("pop", 500)])
        colors = [(255, 140, 0, 255), (0, 160, 90, 255), (160, 40, 200, 255)]
        self.sprites = [
            Target(f"Sprite{i + 1}", self.assets, costumes=[
                self.assets.costume("costume1", colors[i]),
                self.assets.costume("costume2", colors[i][::-1])],
                sounds=[self.assets.sound("meow", 800)])
            for i in range(sprites)]
        self.monitors = []
        self.extensions = []
        # Files that are listed in the project, but not stored
        self.missing = []

    def data(self):
        targets = [self.stage.target(0)] + [s.target(i + 1) for i, s in enumerate(self.sprites)]
        return {"targets": targets, "monitors": self.monitors, "extensions": self.extensions,
                "meta": {"semver": "3.0.0", "vm": "1.5.76", "agent": "make_projects.py"}}

    def write(self, path):
        data = self.data()
        files = {name: content for name, content in self.assets.files.items() if name not in self.missing}
        path.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as archive:
            for name, content in [("project.json", json.dumps(data, separators=(",", ":")).encode())] + sorted(files.items()):
                info = zipfile.ZipInfo(name, date_time=(2020, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                archive.writestr(info, content)


##
# The projects
#

EFFECTS = ["COLOR", "FISHEYE", "WHIRL", "PIXELATE", "MOSAIC", "BRIGHTNESS", "GHOST"]
MATHOPS = ["abs", "floor", "ceiling", "sqrt", "sin", "cos", "tan", "asin", "acos", "atan", "ln", "log", "e ^", "10 ^"]
CURRENT = ["YEAR", "MONTH", "DATE", "DAYOFWEEK", "HOUR", "MINUTE", "SECOND"]
COLOR_PARAMS = ["color", "saturation", "brightness", "transparency"]


def pen_project():
    p = Project()
    p.extensions = ["pen"]
    sprite = p.sprites[0]
    sprite.script(flag(
        b("pen_clear"),
        b("motion_gotoxy", X=-150, Y=0),
        b("pen_setPenColorToColor", COLOR=T(9, "#ff0000")),
        b("pen_setPenSizeTo", SIZE=5),
        b("pen_penDown"),
        b("motion_movesteps", STEPS=40),
        *[b("pen_changePenColorParamBy", COLOR_PARAM=param, VALUE=10) for param in COLOR_PARAMS],
        b("motion_movesteps", STEPS=40),
        *[b("pen_setPenColorParamTo", COLOR_PARAM=param, VALUE=50) for param in COLOR_PARAMS],
        b("pen_changePenSizeBy", SIZE=3),
        b("motion_movesteps", STEPS=40),
        b("pen_stamp"),
        b("pen_penUp"),
        b("motion_movesteps", STEPS=40),
        # Values that are not a color or number: the color of a reporter, a text for a number
        b("pen_setPenColorToColor", COLOR=b("operator_random", FROM=0, TO=16777215)),
        b("pen_setPenColorToColor", COLOR=b("operator_join", STRING1="#00", STRING2="ff00")),
        b("pen_setPenSizeTo", SIZE=b("operator_mathop", OPERATOR="sqrt", NUM=T(4, "-1"))),
        b("pen_changePenSizeBy", SIZE=b("operator_join", STRING1="1", STRING2="")),
        b("pen_setPenColorParamTo", COLOR_PARAM="color", VALUE=b("operator_join", STRING1="2", STRING2="5")),
        b("pen_changePenColorParamBy", COLOR_PARAM="brightness", VALUE=b("operator_mathop", OPERATOR="sqrt", NUM=T(4, "-1"))),
        b("pen_setPenColorToColor", COLOR=T(9, "#00aa44")),
        b("pen_penDown"),
        repeat(4, b("motion_movesteps", STEPS=10), b("motion_turnright", DEGREES=90)),
        b("pen_penUp"),
    ))
    # The stage can only erase all
    p.stage.script(flag(wait(2), b("pen_clear")))
    p.stage.script(b("event_whenstageclicked"), b("pen_clear"))
    return p


def timer_project():
    p = Project()
    sprite, stage = p.sprites[0], p.stage
    stage.variable("ticks", 0)
    sprite.script(flag(
        b("sensing_resettimer"),
        say(b("sensing_timer")),
        wait(0.5),
        b("looks_sayforsecs", MESSAGE=b("operator_round", NUM=b("sensing_timer")), SECS=1),
        say(b("sensing_loudness")),
    ))
    sprite.script(b("event_whengreaterthan", WHENGREATERTHANMENU="TIMER", VALUE=1),
                  say("The timer is greater than 1"))
    sprite.script(b("event_whengreaterthan", WHENGREATERTHANMENU="LOUDNESS", VALUE=10),
                  say("Loud!"))
    stage.script(b("event_whengreaterthan", WHENGREATERTHANMENU="TIMER", VALUE=2),
                 b("data_changevariableby", VARIABLE="ticks", VALUE=1),
                 b("sensing_resettimer"))
    stage.script(flag(b("sensing_resettimer"), b("data_setvariableto", VARIABLE="ticks", VALUE=b("sensing_timer"))))
    return p


def stage_project():
    p = Project()
    sprite, stage = p.sprites[0], p.stage
    stage.variable("score", 7).list("log", ["start"])
    stage.script(b("event_whenstageclicked"),
                 b("looks_nextbackdrop"),
                 b("data_changevariableby", VARIABLE="score", VALUE=1),
                 b("sound_play", SOUND_MENU="pop"))
    stage.script(b("event_whenbackdropswitchesto", BACKDROP="backdrop2"),
                 b("data_addtolist", LIST="log", ITEM="backdrop2"),
                 b("event_broadcast", BROADCAST_INPUT="backdrop changed"))
    stage.script(flag(
        b("looks_switchbackdropto", BACKDROP="backdrop2"),
        b("looks_switchbackdropto", BACKDROP="next backdrop"),
        b("looks_switchbackdropto", BACKDROP="previous backdrop"),
        b("looks_switchbackdropto", BACKDROP="random backdrop"),
        b("looks_switchbackdroptoandwait", BACKDROP="backdrop2"),
        b("looks_switchbackdroptoandwait", BACKDROP="backdrop1"),
        b("looks_nextbackdrop"),
        b("looks_seteffectto", EFFECT="COLOR", VALUE=25),
        b("looks_changeeffectby", EFFECT="BRIGHTNESS", CHANGE=10),
        b("looks_cleargraphiceffects"),
        b("sound_setvolumeto", VOLUME=80),
        b("data_setvariableto", VARIABLE="score", VALUE=b("sensing_of", PROPERTY="score", OBJECT="_stage_")),
        b("data_addtolist", LIST="log", ITEM=b("looks_backdropnumbername", NUMBER_NAME="name")),
        b("data_addtolist", LIST="log", ITEM=b("looks_backdropnumbername", NUMBER_NAME="number")),
        b("data_addtolist", LIST="log", ITEM=b("sensing_of", PROPERTY="backdrop #", OBJECT="_stage_")),
        b("data_addtolist", LIST="log", ITEM=b("sensing_of", PROPERTY="backdrop name", OBJECT="_stage_")),
        b("data_addtolist", LIST="log", ITEM=b("sensing_of", PROPERTY="volume", OBJECT="_stage_")),
        b("event_broadcastandwait", BROADCAST_INPUT="done"),
        b("control_stop", STOP_OPTION="other scripts in stage"),
        b("data_addtolist", LIST="log", ITEM="end"),
    ))
    stage.script(flag(forever(b("data_changevariableby", VARIABLE="score", VALUE=1), wait(0.1))))
    stage.script(b("event_whenkeypressed", KEY_OPTION="space"),
                 b("event_broadcastandwait", BROADCAST_INPUT="done"))
    stage.script(b("event_whenbroadcastreceived", BROADCAST_OPTION="done"),
                 b("data_addtolist", LIST="log", ITEM="done"))
    stage.script(flag(b("control_create_clone_of", CLONE_OPTION="Sprite1"),
                      b("sensing_askandwait", QUESTION="Name?"),
                      b("data_addtolist", LIST="log", ITEM=b("sensing_answer"))))
    sprite.script(b("event_whenbroadcastreceived", BROADCAST_OPTION="backdrop changed"),
                  say(b("looks_backdropnumbername", NUMBER_NAME="name")),
                  say(b("looks_backdropnumbername", NUMBER_NAME="number")))
    sprite.script(b("event_whenkeypressed", KEY_OPTION="enter"), say("enter"))
    p.monitors = [variable_monitor(stage, "score", x=5, y=5), list_monitor(stage, "log", x=5, y=40)]
    return p


def motion_project():
    p = Project(sprites=2)
    sprite, other = p.sprites
    sprite.variable("here", 0)
    other.script(flag(b("motion_gotoxy", X=100, Y=60), b("motion_setrotationstyle", STYLE="left-right"),
                      b("motion_turnleft", DEGREES=15)))
    sprite.script(flag(
        b("motion_gotoxy", X=-50, Y=20),
        b("motion_goto", TO="_random_"),
        b("motion_goto", TO="Sprite2"),
        b("motion_goto", TO="_mouse_"),
        b("motion_glidesecstoxy", SECS=0.5, X=20, Y=-20),
        b("motion_glideto", SECS=0.5, TO="_random_"),
        b("motion_glideto", SECS=0.5, TO="Sprite2"),
        b("motion_glideto", SECS=0.5, TO="_mouse_"),
        b("motion_pointindirection", DIRECTION=45),
        b("motion_pointtowards", TOWARDS="_mouse_"),
        b("motion_pointtowards", TOWARDS="_random_"),
        b("motion_pointtowards", TOWARDS="Sprite2"),
        b("motion_turnright", DEGREES=15),
        b("motion_turnleft", DEGREES=15),
        b("motion_movesteps", STEPS=10),
        b("motion_changexby", DX=10),
        b("motion_setx", X=-20),
        b("motion_changeyby", DY=10),
        b("motion_sety", Y=30),
        b("motion_ifonedgebounce"),
        b("motion_setrotationstyle", STYLE="all around"),
        b("motion_setrotationstyle", STYLE="don't rotate"),
        b("motion_setrotationstyle", STYLE="left-right"),
        b("data_setvariableto", VARIABLE="here", VALUE=b("operator_join", STRING1=b("motion_xposition"),
                                                         STRING2=b("motion_yposition"))),
        say(b("motion_direction")),
        repeat(30, b("motion_movesteps", STEPS=15), b("motion_ifonedgebounce")),
    ))
    return p


def svg_text_project():
    """A button with a text that is a vector costume, the text must be rendered and clickable."""
    p = Project()
    sprite = p.sprites[0]
    sprite.costumes = [p.assets.svg_costume("button")]
    sprite.script(flag(b("motion_gotoxy", X=0, Y=0)))
    sprite.script(b("event_whenthisspriteclicked"), say("clicked"))
    return p


def looks_project():
    p = Project(sprites=2)
    sprite, other = p.sprites
    sprite.variable("info", "")
    sprite.script(flag(
        b("looks_sayforsecs", MESSAGE="Hello!", SECS=0.2),
        say("Hmm"),
        b("looks_thinkforsecs", MESSAGE="Thinking", SECS=0.2),
        b("looks_think", MESSAGE="Hmm..."),
        b("looks_switchcostumeto", COSTUME="costume2"),
        b("looks_nextcostume"),
        b("looks_switchbackdropto", BACKDROP="backdrop2"),
        b("looks_nextbackdrop"),
        b("looks_changesizeby", CHANGE=10),
        b("looks_setsizeto", SIZE=120),
        b("looks_hide"),
        b("looks_show"),
        *[b("looks_seteffectto", EFFECT=effect, VALUE=20) for effect in EFFECTS],
        *[b("looks_changeeffectby", EFFECT=effect, CHANGE=5) for effect in EFFECTS],
        b("looks_cleargraphiceffects"),
        b("looks_gotofrontback", FRONT_BACK="front"),
        b("looks_gotofrontback", FRONT_BACK="back"),
        b("looks_goforwardbackwardlayers", FORWARD_BACKWARD="forward", NUM=1),
        b("looks_goforwardbackwardlayers", FORWARD_BACKWARD="backward", NUM=1),
        b("data_setvariableto", VARIABLE="info", VALUE=b("operator_join", STRING1=b("looks_costumenumbername", NUMBER_NAME="name"),
                                                         STRING2=b("looks_costumenumbername", NUMBER_NAME="number"))),
        b("data_setvariableto", VARIABLE="info", VALUE=b("operator_join", STRING1=b("looks_backdropnumbername", NUMBER_NAME="name"),
                                                         STRING2=b("looks_backdropnumbername", NUMBER_NAME="number"))),
        say(b("looks_size")),
        b("looks_switchcostumeto", COSTUME=b("operator_join", STRING1="costume", STRING2="1")),
    ))
    other.script(flag(b("motion_gotoxy", X=-120, Y=-80), b("looks_say", MESSAGE="I am behind")))
    return p


def sound_project():
    p = Project()
    sprite, stage = p.sprites[0], p.stage
    sprite.script(flag(
        b("sound_play", SOUND_MENU="meow"),
        b("sound_playuntildone", SOUND_MENU="meow"),
        b("sound_seteffectto", EFFECT="PITCH", VALUE=100),
        b("sound_seteffectto", EFFECT="PAN", VALUE=-50),
        b("sound_changeeffectby", EFFECT="PITCH", VALUE=10),
        b("sound_changeeffectby", EFFECT="PAN", VALUE=10),
        b("sound_cleareffects"),
        b("sound_changevolumeby", VOLUME=-10),
        b("sound_setvolumeto", VOLUME=70),
        say(b("sound_volume")),
        b("sound_play", SOUND_MENU="meow"),
        b("sound_stopallsounds"),
    ))
    stage.script(flag(
        b("sound_playuntildone", SOUND_MENU="pop"),
        b("sound_seteffectto", EFFECT="PAN", VALUE=20),
        b("sound_changeeffectby", EFFECT="PITCH", VALUE=5),
        b("sound_cleareffects"),
        b("sound_changevolumeby", VOLUME=-10),
        b("sound_setvolumeto", VOLUME=50),
        b("data_setvariableto", VARIABLE="loud", VALUE=b("sound_volume")),
        b("sound_stopallsounds"),
    ))
    stage.variable("loud", 0)
    return p


def operators_project():
    p = Project(sprites=2)
    sprite, other = p.sprites
    stage = p.stage
    stage.variable("zero", 0).variable("text", "abc").variable("result", 0)
    other.script(flag(b("motion_gotoxy", X=60, Y=0)))
    ops = [
        b("operator_add", NUM1=1, NUM2=b("operator_subtract", NUM1=5, NUM2=2)),
        b("operator_multiply", NUM1=3, NUM2=4),
        b("operator_divide", NUM1=10, NUM2=4),
        b("operator_divide", NUM1=1, NUM2=0),
        b("operator_divide", NUM1=1, NUM2=Var("zero")),
        b("operator_divide", NUM1=Var("text"), NUM2=2),
        b("operator_mod", NUM1=10, NUM2=3),
        b("operator_mod", NUM1=-7, NUM2=3),
        b("operator_mod", NUM1=5, NUM2=Var("zero")),
        b("operator_random", FROM=1, TO=10),
        b("operator_random", FROM=T(4, "0.5"), TO=T(4, "2.5")),
        b("operator_join", STRING1="apple ", STRING2="banana"),
        b("operator_letter_of", LETTER=2, STRING="apple"),
        b("operator_length", STRING="apple"),
        b("operator_contains", STRING1="apple", STRING2="PP"),
        b("operator_round", NUM=T(4, "2.5")),
        b("operator_gt", OPERAND1=5, OPERAND2=3),
        b("operator_lt", OPERAND1="apple", OPERAND2="Banana"),
        b("operator_equals", OPERAND1=Var("text"), OPERAND2="ABC"),
        b("operator_and", OPERAND1=b("operator_gt", OPERAND1=2, OPERAND2=1), OPERAND2=b("operator_lt", OPERAND1=1, OPERAND2=2)),
        b("operator_or", OPERAND1=b("operator_equals", OPERAND1=1, OPERAND2=2), OPERAND2=b("sensing_mousedown")),
        b("operator_not", OPERAND=b("sensing_keypressed", KEY_OPTION="space")),
        *[b("operator_mathop", OPERATOR=op, NUM=T(4, "30")) for op in MATHOPS],
    ]
    sprite.script(flag(*[b("data_setvariableto", VARIABLE="result", VALUE=op) for op in ops]))
    sprite.script(b("event_whenkeypressed", KEY_OPTION="any"),
                  b("control_if", CONDITION=b("operator_not", OPERAND=b("operator_equals", OPERAND1=1, OPERAND2=1)),
                    SUBSTACK=[say("never")]))
    sprite.variable("copy", 0)
    # Sensing
    sprite.script(flag(
        b("sensing_setdragmode", DRAG_MODE="draggable"),
        b("sensing_setdragmode", DRAG_MODE="not draggable"),
        b("data_setvariableto", VARIABLE="copy", VALUE=b("sensing_touchingobject", TOUCHINGOBJECTMENU="_mouse_")),
        b("data_setvariableto", VARIABLE="copy", VALUE=b("sensing_touchingobject", TOUCHINGOBJECTMENU="_edge_")),
        b("data_setvariableto", VARIABLE="copy", VALUE=b("sensing_touchingobject", TOUCHINGOBJECTMENU="Sprite2")),
        b("data_setvariableto", VARIABLE="copy", VALUE=b("sensing_touchingcolor", COLOR=T(9, "#ff0000"))),
        b("data_setvariableto", VARIABLE="copy", VALUE=b("sensing_coloristouchingcolor", COLOR=T(9, "#ff8c00"), COLOR2=T(9, "#00a05a"))),
        b("data_setvariableto", VARIABLE="copy", VALUE=b("sensing_distanceto", DISTANCETOMENU="_mouse_")),
        b("data_setvariableto", VARIABLE="copy", VALUE=b("sensing_distanceto", DISTANCETOMENU="Sprite2")),
        b("data_setvariableto", VARIABLE="copy", VALUE=b("sensing_mousex")),
        b("data_setvariableto", VARIABLE="copy", VALUE=b("sensing_mousey")),
        b("data_setvariableto", VARIABLE="copy", VALUE=b("sensing_mousedown")),
        b("data_setvariableto", VARIABLE="copy", VALUE=b("sensing_keypressed", KEY_OPTION="a")),
        b("data_setvariableto", VARIABLE="copy", VALUE=b("sensing_keypressed", KEY_OPTION="space")),
        b("data_setvariableto", VARIABLE="copy", VALUE=b("sensing_timer")),
        b("sensing_resettimer"),
        b("data_setvariableto", VARIABLE="copy", VALUE=b("sensing_dayssince2000")),
        b("data_setvariableto", VARIABLE="copy", VALUE=b("sensing_username")),
        b("data_setvariableto", VARIABLE="copy", VALUE=b("sensing_loudness")),
        *[b("data_setvariableto", VARIABLE="copy", VALUE=b("sensing_current", CURRENTMENU=what)) for what in CURRENT],
        *[b("data_setvariableto", VARIABLE="copy", VALUE=b("sensing_of", PROPERTY=prop, OBJECT="Sprite2"))
          for prop in ("x position", "y position", "direction", "costume #", "costume name", "size", "volume")],
        b("data_setvariableto", VARIABLE="copy", VALUE=b("sensing_of", PROPERTY="local", OBJECT="Sprite2")),
        b("data_setvariableto", VARIABLE="copy", VALUE=b("sensing_of", PROPERTY="x position", OBJECT="_stage_")),
        b("sensing_askandwait", QUESTION="What is your name?"),
        say(b("sensing_answer")),
        b("looks_say", MESSAGE=b("operator_join", STRING1="Hello ", STRING2=b("sensing_answer"))),
    ))
    other.variable("local", 5)
    return p


def lists_project():
    p = Project()
    sprite, stage = p.sprites[0], p.stage
    stage.variable("global", 1).list("fruits", ["apple", "banana", "cherry"])
    sprite.variable("local", "x").list("mine", [1, 2, 3])
    sprite.script(flag(
        b("data_setvariableto", VARIABLE="global", VALUE=5),
        b("data_changevariableby", VARIABLE="global", VALUE=2),
        b("data_setvariableto", VARIABLE="local", VALUE=Var("global")),
        b("data_showvariable", VARIABLE="local"),
        b("data_hidevariable", VARIABLE="local"),
        b("data_showvariable", VARIABLE="local"),
        b("data_addtolist", LIST="fruits", ITEM="date"),
        b("data_insertatlist", LIST="fruits", INDEX=1, ITEM="apricot"),
        b("data_insertatlist", LIST="fruits", INDEX="last", ITEM="zucchini"),
        b("data_replaceitemoflist", LIST="fruits", INDEX=2, ITEM="avocado"),
        b("data_replaceitemoflist", LIST="fruits", INDEX="random", ITEM="mango"),
        b("data_deleteoflist", LIST="fruits", INDEX=1),
        b("data_deleteoflist", LIST="fruits", INDEX="last"),
        b("data_setvariableto", VARIABLE="local", VALUE=b("data_itemoflist", LIST="fruits", INDEX=1)),
        b("data_setvariableto", VARIABLE="local", VALUE=b("data_itemoflist", LIST="fruits", INDEX="random")),
        b("data_setvariableto", VARIABLE="local", VALUE=b("data_itemnumoflist", LIST="fruits", ITEM="banana")),
        b("data_setvariableto", VARIABLE="local", VALUE=b("data_lengthoflist", LIST="fruits")),
        b("control_if", CONDITION=b("data_listcontainsitem", LIST="fruits", ITEM="banana"),
          SUBSTACK=[b("data_addtolist", LIST="mine", ITEM=ListRef("fruits"))]),
        b("data_showlist", LIST="mine"),
        b("data_hidelist", LIST="mine"),
        b("data_showlist", LIST="mine"),
        b("data_deletealloflist", LIST="mine"),
        b("data_addtolist", LIST="mine", ITEM=Var("local")),
    ))
    stage.script(flag(b("data_addtolist", LIST="fruits", ITEM=b("data_lengthoflist", LIST="fruits")),
                      b("data_hidelist", LIST="fruits"), b("data_showlist", LIST="fruits"),
                      b("data_hidevariable", VARIABLE="global"), b("data_showvariable", VARIABLE="global")))
    p.monitors = [
        variable_monitor(stage, "global", "default", x=5, y=5),
        variable_monitor(stage, "global", "large", x=5, y=40) | {"id": "monitor_large"},
        variable_monitor(sprite, "local", "slider", x=5, y=80, sprite="Sprite1"),
        list_monitor(stage, "fruits", x=200, y=5),
        list_monitor(sprite, "mine", x=200, y=150, sprite="Sprite1"),
    ]
    return p


def procedures_project():
    p = Project()
    sprite, stage = p.sprites[0], p.stage
    sprite.variable("sum", 0)
    sprite.define("jump %s times", ["count"], body=[
        repeat(b("argument_reporter_string_number", VALUE="count"), b("motion_changeyby", DY=10), wait(0.05)),
        b("motion_changeyby", DY=-50)])
    sprite.define("square %s %s", ["size", "steps"], warp=True, body=[
        repeat(b("argument_reporter_string_number", VALUE="steps"),
               b("motion_movesteps", STEPS=b("argument_reporter_string_number", VALUE="size")),
               b("motion_turnright", DEGREES=90))])
    sprite.define("say if %b", ["flag"], "b", body=[
        b("control_if_else", CONDITION=b("argument_reporter_boolean", VALUE="flag"),
          SUBSTACK=[say("yes")], SUBSTACK2=[say("no")])])
    sprite.define("add up %s", ["n"], body=[
        b("control_if", CONDITION=b("operator_gt", OPERAND1=b("argument_reporter_string_number", VALUE="n"), OPERAND2=0),
          SUBSTACK=[b("data_changevariableby", VARIABLE="sum", VALUE=b("argument_reporter_string_number", VALUE="n")),
                    b("procedures_call", proccode="add up %s", args=[b("operator_subtract", NUM1=b("argument_reporter_string_number", VALUE="n"), NUM2=1)])]),
        b("control_stop", STOP_OPTION="this script"),
        say("never")])
    sprite.define("no arguments", [], body=[b("motion_turnleft", DEGREES=1)])
    sprite.script(flag(
        b("procedures_call", proccode="jump %s times", args=[3]),
        b("procedures_call", proccode="square %s %s", args=[20, 4]),
        b("procedures_call", proccode="say if %b", args=[b("operator_gt", OPERAND1=2, OPERAND2=1)]),
        b("procedures_call", proccode="say if %b", args=[None]),
        b("procedures_call", proccode="add up %s", args=[4]),
        b("procedures_call", proccode="no arguments", args=[]),
        b("procedures_call", proccode="jump %s times", args=[Var("sum")]),
        say(Var("sum"))))
    stage.variable("count", 0)
    stage.define("count up %s", ["by"], warp=True, body=[
        b("data_changevariableby", VARIABLE="count", VALUE=b("argument_reporter_string_number", VALUE="by"))])
    stage.script(flag(b("procedures_call", proccode="count up %s", args=[2]),
                      b("procedures_call", proccode="count up %s", args=[3])))
    return p


def control_project():
    p = Project(sprites=2)
    sprite, other = p.sprites
    sprite.variable("n", 0)
    sprite.script(flag(
        repeat(3, b("motion_changexby", DX=5)),
        b("control_if_else", CONDITION=b("operator_equals", OPERAND1=Var("n"), OPERAND2=0),
          SUBSTACK=[b("data_setvariableto", VARIABLE="n", VALUE=1)],
          SUBSTACK2=[b("data_setvariableto", VARIABLE="n", VALUE=2)]),
        b("control_repeat_until", CONDITION=b("operator_gt", OPERAND1=Var("n"), OPERAND2=4),
          SUBSTACK=[b("data_changevariableby", VARIABLE="n", VALUE=1)]),
        b("control_wait_until", CONDITION=b("operator_gt", OPERAND1=b("sensing_timer"), OPERAND2=0.2)),
        wait(0.1),
        b("control_create_clone_of", CLONE_OPTION="_myself_"),
        b("control_create_clone_of", CLONE_OPTION="Sprite2"),
        b("event_broadcast", BROADCAST_INPUT="go"),
        b("control_stop", STOP_OPTION="other scripts in sprite"),
        b("control_stop", STOP_OPTION="this script"),
    ))
    sprite.script(flag(forever(b("motion_turnright", DEGREES=1), b("control_if", CONDITION=b("operator_gt", OPERAND1=Var("n"), OPERAND2=100),
                                                                 SUBSTACK=[b("control_stop", STOP_OPTION="all")]))))
    sprite.script(b("control_start_as_clone"),
                  b("motion_changeyby", DY=30),
                  wait(0.2),
                  b("control_delete_this_clone"))
    sprite.script(b("event_whenthisspriteclicked"), say("Clicked"))
    sprite.script(b("event_whenkeypressed", KEY_OPTION="space"), b("control_stop", STOP_OPTION="all"))
    other.script(b("event_whenbroadcastreceived", BROADCAST_OPTION="go"),
                 b("event_broadcastandwait", BROADCAST_INPUT="go2"),
                 b("control_stop", STOP_OPTION="all"))
    other.script(b("event_whenbroadcastreceived", BROADCAST_OPTION="go2"), wait(0.1))
    other.script(b("event_whenkeypressed", KEY_OPTION="up arrow"), b("motion_changeyby", DY=10))
    other.script(b("event_whenkeypressed", KEY_OPTION="0"), b("motion_changeyby", DY=-10))
    return p


def monitors_project():
    """Every kind of monitor in every style."""
    p = Project(sprites=2)
    one, two, stage = p.sprites[0], p.sprites[1], p.stage
    stage.variable("score", 0).variable("big", 42).variable("speed", 30).variable("temp", 0.5)
    stage.variable("long", "A very long text that is shown in a monitor, it does not fit into a column").list("fruits", ["apple", "banana", "cherry"])
    stage.list("empty", [])
    one.variable("local", 7)
    one.script(flag(
        b("data_setvariableto", VARIABLE="score", VALUE=12),
        b("motion_gotoxy", X=-60, Y=-40),
        b("motion_pointindirection", DIRECTION=45),
        b("looks_switchcostumeto", COSTUME="costume2"),
        b("looks_setsizeto", SIZE=80),
        b("sound_setvolumeto", VOLUME=60),
        b("data_addtolist", LIST="fruits", ITEM="date"),
    ))
    two.script(flag(b("motion_gotoxy", X=60, Y=-40), b("looks_changesizeby", CHANGE=20)))
    stage.script(flag(b("looks_switchbackdropto", BACKDROP="backdrop2"), b("sound_setvolumeto", VOLUME=90)))

    def current(item, y):
        return reporter_monitor("sensing_current", {"CURRENTMENU": item}, x=5, y=y)

    sensing = [reporter_monitor("sensing_timer", y=5), reporter_monitor("sensing_answer", y=27),
               reporter_monitor("sensing_loudness", y=49), reporter_monitor("sensing_username", y=71)]
    sensing += [current(item, 93 + 22 * i) for i, item in enumerate(
        ["YEAR", "MONTH", "DATE", "DAYOFWEEK", "HOUR", "MINUTE", "SECOND"])]
    sprite_one = [reporter_monitor(opcode, params, sprite="Sprite1", x=130, y=5 + 22 * i) for i, (opcode, params) in enumerate([
        ("motion_xposition", {}), ("motion_yposition", {}), ("motion_direction", {}),
        ("looks_costumenumbername", {"NUMBER_NAME": "number"}), ("looks_costumenumbername", {"NUMBER_NAME": "name"}),
        ("looks_size", {}), ("sound_volume", {})])]
    sprite_two = [reporter_monitor("motion_xposition", sprite="Sprite2", x=130, y=159, mode="large"),
                  reporter_monitor("looks_costumenumbername", {"NUMBER_NAME": "name"}, sprite="Sprite2", x=130, y=195)]
    stage_monitors = [reporter_monitor("looks_backdropnumbername", {"NUMBER_NAME": "number"}, x=130, y=217),
                      reporter_monitor("looks_backdropnumbername", {"NUMBER_NAME": "name"}, x=130, y=239),
                      reporter_monitor("sound_volume", x=130, y=261)]
    p.monitors = sensing + sprite_one + sprite_two + stage_monitors + [
        variable_monitor(stage, "score", x=312, y=5),
        variable_monitor(stage, "big", "large", x=312, y=27),
        variable_monitor(stage, "speed", "slider", x=312, y=60, sliderMin=0, sliderMax=100, isDiscrete=True),
        variable_monitor(stage, "temp", "slider", x=312, y=98, sliderMin=-10, sliderMax=10, isDiscrete=False),
        variable_monitor(one, "local", "slider", x=312, y=136, sprite="Sprite1", sliderMin=1, sliderMax=10),
        list_monitor(stage, "fruits", x=312, y=178) | {"width": 80, "height": 100},
        list_monitor(stage, "empty", x=397, y=178) | {"width": 80, "height": 100},
        variable_monitor(stage, "long", x=5, y=290),
        # Hidden monitors are not created
        reporter_monitor("sensing_timer", x=200, y=200) | {"visible": False},
    ]
    return p


GENERATED = {
    "pen": pen_project,
    "timer_events": timer_project,
    "stage_scripts": stage_project,
    "motion_all": motion_project,
    "looks_all": looks_project,
    "sound_all": sound_project,
    "operators_sensing": operators_project,
    "lists_monitors": lists_project,
    "custom_blocks": procedures_project,
    "control_clones": control_project,
    "monitors": monitors_project,
    "svg_text": svg_text_project,
}


def unsupported_project():
    """A project with things that can't be converted, to test the report."""
    p = Project(sprites=2)
    sprite, other = p.sprites
    stage = p.stage
    p.extensions = ["pen", "music"]
    stage.variable("cloudy", 0, cloud=True).variable("plain", 1)
    # An opcode that is not supported (twice), the block of an extension and a legacy block
    sprite.script(flag(
        b("sensing_loud"), b("sensing_loud"),
        b("music_playDrumForBeats", DRUM=1, BEATS=0.25),
        b("control_while", CONDITION=b("sensing_mousedown"), SUBSTACK=[say("x")]),
        say("done")))
    # A hat block that is not supported
    sprite.script(b("event_whentouchingobject", TOUCHINGOBJECTMENU="_mouse_"), say("touched"))
    sprite.script(b("event_whentouchingobject", TOUCHINGOBJECTMENU="_mouse_"), say("touched again"))
    # Scripts without hat block
    sprite.script(b("motion_movesteps", STEPS=10), b("motion_turnright", DEGREES=15))
    sprite.script(b("operator_add", NUM1=1, NUM2=2))
    # Comments: attached to blocks that are not converted, not attached
    sprite.comment("A comment that is not attached to a block")
    fine, loose = say("fine"), b("motion_movesteps", STEPS=1)
    other.script(flag(fine))
    other.script(loose)
    other.comment("A comment on a loose block", loose)
    other.comment("A comment on a block that is converted", fine)
    stage.script(flag(b("sensing_loud")))
    p.monitors = [
        # Not supported: no checkbox in Scratch for the reporters, or a reporter the stage does not have
        reporter_monitor("sensing_dayssince2000"),
        reporter_monitor("sensing_mousex"),
        reporter_monitor("motion_xposition"),
        variable_monitor(stage, "plain", "slider", x=5, y=100),
        variable_monitor(stage, "cloudy", "default", x=5, y=130),
        # not visible: no warning
        reporter_monitor("sensing_username") | {"visible": False},
    ]
    # A costume with a format that is not supported and a file that is missing
    sprite.costumes.append({"name": "photo", "bitmapResolution": 1, "dataFormat": "webp", "assetId": "00" * 16,
                            "md5ext": "00" * 16 + ".webp", "rotationCenterX": 1, "rotationCenterY": 1})
    p.missing = [sprite.sounds[0]["md5ext"]]
    return p


SPECIAL = {
    "unsupported": unsupported_project,
}


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    generated = Path(argv[0]) if argv else BASE / "scratch_projects" / "generated"
    special = Path(argv[1]) if len(argv) > 1 else BASE / "special_projects"
    for directory, projects in ((generated, GENERATED), (special, SPECIAL)):
        for name, create in projects.items():
            create().write(directory / f"{name}.sb3")
            print(f"Written {directory / (name + '.sb3')}")


if __name__ == "__main__":
    main()
