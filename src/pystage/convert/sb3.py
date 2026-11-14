import argparse
import json
import logging
import math
import os
import re
import sys
import textwrap
import zipfile
from collections import OrderedDict
from pathlib import Path

from pystage.convert import CodeWriter, sb3_templates
from pystage.convert.code_writer import py_str, identifier

logger = logging.getLogger(__name__)

'''
For the conversion, we create a simplified version of the
block trees that is used in the code template functions.

Scratch projects are untrusted input. Everything that is read from a
project is validated here before it gets into the intermediate structure:
Numbers are numbers, texts are Python string literals (see py_str), names
of blocks and parameters are simple identifiers.
'''


# Target (intermediate) structure
# project = {
#         "costumes": {
#           "abcd...": {
#               "global_name": "cat1",
#               "extension": "png",
#               },
#           }
#         "sounds": {
#           "abcd...": {
#               "global_name": "meeow",
#               "extension": "wav",
#               },
#           }
#         "stage": {
#               "name": "Stage",
#               "blocks": [],
#               "costumes": [],
#               "currentCostume": 0
#           }
#         "sprites": [
#             {
#                 "name": "Sprite1",
#                 "blocks": [
#                     { # BLOCK
#                         "opcode": "event_whenthisspriteclicked",
#                         "stage": False,
#                         "params": {
#                             "BROADCAST_INPUT": "\"start\"",
#                             "COSTUME": "BLOCK"
#                             }
#                         "next": "BLOCK",
#                         "comments": ["text"],
#                         }
#                     ]
#                 "costumes": [{
#                       "md5": "abcd..."
#                       "local_name": "cat1",
#                       "rotationCenterX": 240,
#                       "rotationCenterY": 180,
#                       },
#                   ],
#                 "sounds": [{
#                       "md5": "abcd..."
#                       "local_name": "cat1",
#                       },
#                   ],
#                 "variables": {"name": 0},
#                 "lists": {"name": [1, "two"]},
#                 "currentCostume": 0
#                 },
#
#             ],
#
#         }
#
# Custom blocks:
#   definition: {"opcode": "procedures_definition", "procedure": {"proccode": "jump %s", "args": ["height"], "warp": False}, ...}
#   call:       {"opcode": "procedures_call", "proccode": "jump %s", "args": [VALUE, ...], ...}


class ConversionError(Exception):
    '''
    The project can't be converted. The message is meant for the user.
    '''


class Limits:
    '''
    Size limits for a project, in bytes (uncompressed).

    The defaults are generous, Scratch itself is stricter. They prevent
    that a manipulated file fills the memory or the disk.
    '''
    def __init__(self, project_json=50 * 2**20, asset=100 * 2**20, total=1000 * 2**20, blocks=200000):
        self.project_json = project_json
        self.asset = asset
        self.total = total
        self.blocks = blocks


DEFAULT_LIMITS = Limits()

IMAGE_FORMATS = ("svg", "png", "jpg", "jpeg", "bmp", "gif")
SOUND_FORMATS = ("wav", "mp3", "ogg")

# Blocks can be nested, but not endlessly.
MAX_DEPTH = 150

HAT_BLOCKS = [
    "event_whenthisspriteclicked",
    "event_whenstageclicked",
    "event_whenbroadcastreceived",
    "event_whenflagclicked",
    "event_whenkeypressed",
    "event_whenbackdropswitchesto",
    "event_whengreaterthan",
    "control_start_as_clone",
    "procedures_definition",
]

numeric_text = re.compile(r"[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?\Z")
color_text = re.compile(r"#[0-9a-fA-F]{6}\Z")


class DictClass(OrderedDict):
    '''
    A dictionary that can be accessed via dot notation for convenience.
    '''

    def __init__(self):
        super().__init__()

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(item)


def number(value, default=0):
    '''
    A finite int or float for a value from the project, default otherwise.
    '''
    if isinstance(value, bool):
        return default
    if isinstance(value, str):
        if not numeric_text.match(value.strip()):
            return default
        try:
            value = float(value)
        except ValueError:
            return default
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        if math.isnan(value) or math.isinf(value):
            return default
        if value == math.floor(value) and abs(value) < 1e15:
            return int(value)
        return value
    return default


def literal(value):
    '''
    Python code for a value of a variable or list: A number or a text.
    '''
    if isinstance(value, bool):
        return "True" if value else "False"
    if isinstance(value, (int, float)):
        n = number(value, None)
        return py_str(value) if n is None else repr(n)
    return py_str(value)


def get_input_value(i, stage):
    '''
    Extracts values from sb3 input representations.
    '''
    # 4: number, 5: positive number, 6: positive integer
    # 7: integer, 8: angle, 9: color, 10: string
    # 11: broadcast, 12: variable, 13: list

    if not isinstance(i, list) or len(i) < 2:
        return py_str("")
    input_type = i[0]
    value = i[1]

    if input_type in [4, 5, 6, 7, 8]:
        if isinstance(value, str) and value.strip() == '':
            return 0
        n = number(value, None)
        if n is None:
            # Scratch allows any text in number fields
            return py_str(value)
        if input_type in [6, 7] and isinstance(n, float):
            return int(round(n))
        return n
    elif input_type == 9:
        if isinstance(value, str) and color_text.match(value):
            h = value.lstrip("#")
            return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
        return (0, 0, 0)
    elif input_type in [12, 13]:
        block = DictClass()
        block.update({
                "opcode": "data_variable" if input_type == 12 else "data_listcontents",
                "params": {
                    ("VARIABLE" if input_type == 12 else "LIST"): py_str(value),
                    },
                "next": False,
                "stage": stage,
                })
        return block
    elif input_type == 10:
        n = number(value, None) if isinstance(value, (str, int, float)) else None
        if n is not None:
            return n
        return py_str(value)
    # 11 (broadcast) and everything unknown is a text
    return py_str(value)


class BlockReader:
    '''
    Turns the blocks of a target (stage or sprite) of the sb3 structure
    into our intermediate representation.
    '''

    def __init__(self, target, stage, limits):
        blocks = target.get("blocks")
        self.blocks = blocks if isinstance(blocks, dict) else {}
        self.stage = stage
        self.limits = limits
        # Every block belongs to exactly one script.
        self.seen = set()
        # block id: [text, ...]
        self.comments = {}
        comments = target.get("comments")
        if isinstance(comments, dict):
            for comment in comments.values():
                if isinstance(comment, dict) and isinstance(comment.get("text"), str) and comment["text"].strip():
                    self.comments.setdefault(comment.get("blockId"), []).append(comment["text"])

    def top_level_blocks(self):
        res = []
        for key, b in self.blocks.items():
            if not isinstance(b, dict):
                # Stuff like variables, not interesting at this point
                continue
            if b.get("opcode") in HAT_BLOCKS and not b.get("parent"):
                res.append(self.stack(key))
        return res

    def stack(self, block_id, depth=0):
        '''
        The block with the given id including all blocks that follow.
        '''
        first = None
        last = None
        while isinstance(block_id, str) and isinstance(self.blocks.get(block_id), dict):
            block = self.block(block_id, depth)
            if first is None:
                first = block
            else:
                last["next"] = block
            last = block
            block_id = self.blocks[block_id].get("next")
        return first

    def block(self, block_id, depth):
        if depth > MAX_DEPTH:
            raise ConversionError("The blocks of this project are nested too deeply.")
        if block_id in self.seen:
            raise ConversionError("The project file is damaged: A block is used twice.")
        self.seen.add(block_id)
        if len(self.seen) > self.limits.blocks:
            raise ConversionError("This project has too many blocks.")

        block = self.blocks[block_id]
        opcode = block.get("opcode")
        if not isinstance(opcode, str) or not identifier.match(opcode):
            opcode = "unknown"
        res = DictClass()
        res.update({
            "opcode": opcode,
            "params": DictClass(),
            "next": False,
            "stage": self.stage
        })
        if block_id in self.comments:
            res["comments"] = self.comments[block_id]

        fields = block.get("fields") if isinstance(block.get("fields"), dict) else {}
        inputs = block.get("inputs") if isinstance(block.get("inputs"), dict) else {}
        mutation = block.get("mutation") if isinstance(block.get("mutation"), dict) else {}

        for f, field in fields.items():
            if identifier.match(f) and isinstance(field, list) and field:
                res["params"][f] = py_str(field[0])

        if opcode == "procedures_call":
            res["proccode"] = str(mutation.get("proccode", ""))
            res["args"] = []
            for argument_id in self.json_list(mutation.get("argumentids")):
                value = self.input(inputs.get(argument_id), depth)
                res["args"].append(py_str("") if value is None else value)
            return res

        for i, inp in inputs.items():
            if not identifier.match(i):
                continue
            value = self.input(inp, depth)
            if value is not None:
                res["params"][i] = value

        if opcode == "procedures_definition":
            prototype = inputs.get("custom_block")
            prototype = self.blocks.get(prototype[1]) if isinstance(prototype, list) and len(prototype) > 1 and isinstance(prototype[1], str) else None
            mutation = prototype.get("mutation") if isinstance(prototype, dict) and isinstance(prototype.get("mutation"), dict) else {}
            res["params"].clear()
            res["procedure"] = {
                "proccode": str(mutation.get("proccode", "")),
                "args": [str(name) for name in self.json_list(mutation.get("argumentnames"))],
                "warp": mutation.get("warp") in (True, "true"),
            }
        return res

    def input(self, inp, depth):
        '''
        The value of an input: a literal, a block or None, if it is empty.
        '''
        if not isinstance(inp, list) or len(inp) < 2:
            return None
        value = inp[1]
        if value is None:
            # e.g. empty if condition
            return None
        if isinstance(value, list):
            return get_input_value(value, self.stage)
        if isinstance(value, str):
            referenced = self.blocks.get(value)
            if isinstance(referenced, list):
                return get_input_value(referenced, self.stage)
            if isinstance(referenced, dict):
                return self.stack(value, depth + 1)
        return None

    @staticmethod
    def json_list(text):
        '''
        Lists in mutations are stored as JSON text.
        '''
        try:
            res = json.loads(text) if isinstance(text, str) else text
        except ValueError:
            return []
        return res if isinstance(res, list) else []


def to_filename(name: str):
    umlauts = {"ö": "oe", "ü": "ue", "ä": "ae", "ß": "ss"}
    name = str(name).lower().strip()
    for c in umlauts:
        name = name.replace(c, umlauts[c])
    name = re.sub(r"[^a-z0-9_]", "_", name)
    name = re.sub(r"_+", "_", name)[:80]
    if name.strip("_") == "":
        name = "project"
    return name


def unique_global_name(name, ext, global_names):
    iname = name
    i = 2
    while f"{iname}.{ext}" in global_names:
        iname = f"{name}_{i}"
        i += 1
    global_names.add(f"{iname}.{ext}")
    return iname, ext


def get_sb3_data(file, limits=DEFAULT_LIMITS):
    '''
    Reads the project.json of an sb3 file.

    Parameters
    ----------
    file : str or file-like object
        The sb3 file.
    limits : Limits
        The size limits for the project.
    '''
    try:
        with zipfile.ZipFile(file, 'r') as archive:
            try:
                info = archive.getinfo("project.json")
            except KeyError:
                raise ConversionError("This is not a Scratch 3 project, there is no project.json in the file.")
            if info.file_size > limits.project_json:
                raise ConversionError("The project is too big.")
            if sum(i.file_size for i in archive.infolist()) > limits.total:
                raise ConversionError("The project is too big.")
            with archive.open(info) as f:
                raw = f.read(limits.project_json + 1)
    except FileNotFoundError:
        raise ConversionError(f"File not found: {file}")
    except (zipfile.BadZipFile, OSError, RuntimeError, NotImplementedError):
        raise ConversionError("The file can't be read. Is it really an sb3 file from Scratch 3?")
    if len(raw) > limits.project_json:
        raise ConversionError("The project is too big.")
    try:
        data = json.loads(raw)
    except (ValueError, RecursionError):
        raise ConversionError("The project file is damaged.")
    if not isinstance(data, dict) or not isinstance(data.get("targets"), list):
        raise ConversionError("This is not a Scratch 3 project.")
    return data


def _assets(target, key, formats, registry, global_names):
    '''
    Collects the costumes or sounds of a target.
    '''
    res = []
    entries = target.get(key)
    for entry in entries if isinstance(entries, list) else []:
        if not isinstance(entry, dict):
            continue
        asset_id = entry.get("assetId")
        data_format = str(entry.get("dataFormat", "")).lower()
        name = entry.get("name")
        # The asset id is the name of the file in the sb3 file.
        if not isinstance(asset_id, str) or not re.fullmatch(r"[0-9a-zA-Z]{1,64}", asset_id):
            continue
        if data_format not in formats or not isinstance(name, str):
            continue
        if asset_id not in registry:
            global_name, ext = unique_global_name(to_filename(name), data_format, global_names)
            registry[asset_id] = {
                "global_name": global_name,
                "extension": ext,
            }
        asset = {
            "md5": asset_id,
            "local_name": name,
        }
        if key == "costumes":
            resolution = number(entry.get("bitmapResolution"), 1)
            asset["bitmapResolution"] = resolution if resolution > 0 else 1
            asset["rotationCenterX"] = number(entry.get("rotationCenterX"), None)
            asset["rotationCenterY"] = number(entry.get("rotationCenterY"), None)
        res.append(asset)
    return res


def get_intermediate(data, name, limits=DEFAULT_LIMITS):
    project = DictClass()
    project.update({
        "name": to_filename(name),
        "sprites": [],
        "costumes": {},
        "sounds": {},
    })
    # Used to check for duplicate file names
    global_names = set()

    if not isinstance(data, dict) or not isinstance(data.get("targets"), list):
        raise ConversionError("This is not a Scratch 3 project.")

    try:
        for target in data["targets"]:
            if not isinstance(target, dict):
                continue
            is_stage = target.get("isStage") is True
            rotation_style = target.get("rotationStyle")
            sprite = DictClass()
            sprite.update({
                "name": str(target.get("name", "Stage" if is_stage else "Sprite")),
                "blocks": [],
                "costumes": [],
                "sounds": [],
                "variables": {}, # name: value
                "lists": {}, # name: [value, ...]
                "monitors": [],
                "currentCostume": 0,
                "layerOrder": number(target.get("layerOrder"), 0),
                "visible": target.get("visible") is not False,
                "draggable": target.get("draggable") is True,
                "x": number(target.get("x"), 0),
                "y": number(target.get("y"), 0),
                "size": number(target.get("size"), 100),
                "volume": number(target.get("volume"), 100),
                "direction": number(target.get("direction"), 90),
                "rotationStyle": rotation_style if rotation_style in ("left-right", "don't rotate") else "all around",
            })
            if is_stage:
                if "stage" in project:
                    continue
                project["stage"] = sprite
            else:
                project["sprites"].append(sprite)
            reader = BlockReader(target, is_stage, limits)
            sprite["blocks"] = reader.top_level_blocks()
            sprite["costumes"] = _assets(target, "costumes", IMAGE_FORMATS, project["costumes"], global_names)
            sprite["sounds"] = _assets(target, "sounds", SOUND_FORMATS, project["sounds"], global_names)
            current = number(target.get("currentCostume"), 0)
            if isinstance(current, int) and 0 <= current < len(sprite["costumes"]):
                sprite["currentCostume"] = current
            variables = target.get("variables")
            for v in variables.values() if isinstance(variables, dict) else []:
                if isinstance(v, list) and len(v) >= 2 and isinstance(v[0], str):
                    sprite["variables"][v[0]] = v[1] if isinstance(v[1], (int, float, str, bool)) else 0
            lists = target.get("lists")
            for v in lists.values() if isinstance(lists, dict) else []:
                if isinstance(v, list) and len(v) >= 2 and isinstance(v[0], str) and isinstance(v[1], list):
                    sprite["lists"][v[0]] = [item if isinstance(item, (int, float, str, bool)) else "" for item in v[1]]
    except RecursionError:
        raise ConversionError("The blocks of this project are nested too deeply.")

    if "stage" not in project:
        raise ConversionError("The project has no stage.")
    project["sprites"].sort(key=lambda sprite: sprite["layerOrder"])

    monitors = data.get("monitors")
    for m in monitors if isinstance(monitors, list) else []:
        if not isinstance(m, dict) or not m.get("visible") or not isinstance(m.get("params"), dict):
            continue
        sprite = project["stage"]
        if m.get("spriteName"):
            for s in project["sprites"]:
                if s["name"] == m["spriteName"]:
                    sprite = s
                    break
        monitor = {
            "x": number(m.get("x"), 0),
            "y": number(m.get("y"), 0),
            "width": number(m.get("width"), 0),
            "height": number(m.get("height"), 0),
            "style": m.get("mode") if m.get("mode") in ("large", "slider") else "normal",
        }
        if m.get("opcode") == "data_variable" and isinstance(m["params"].get("VARIABLE"), str):
            monitor["variable"] = m["params"]["VARIABLE"]
        elif m.get("opcode") == "data_listcontents" and isinstance(m["params"].get("LIST"), str):
            monitor["list"] = m["params"]["LIST"]
        else:
            # Only monitors for variables and lists are implemented
            continue
        sprite["monitors"].append(monitor)

    return project


def get_python(project, language="core", project_link=None):
    if not re.fullmatch(r"[a-z]{2,10}", language):
        raise ConversionError(f"Unknown language: {language}")
    try:
        writer = CodeWriter(project, sb3_templates.templates, language)
    except ImportError:
        raise ConversionError(f"Unknown language: {language}")
    lang_module = writer.lang_module
    sprite_class = lang_module.sprite_class.__name__
    stage_class = lang_module.stage_class.__name__

    def fn(corefunc, stage=False):
        name = writer.get_translated_name(corefunc, stage)
        if name is None:
            raise ConversionError(f"The language {language} does not support {corefunc}.")
        return name

    imports = [sprite_class, stage_class]
    if writer.uses_no_refresh() and writer.get_no_refresh_name():
        imports.append(writer.get_no_refresh_name())

    lines = []
    if project_link:
        lines.append(f"# Online Converter, URL: {re.sub(r'[^A-Za-z0-9:/._?=&%-]', '', str(project_link))}")
    lines += [
        f"# {project['name']} (pyStage, converted from Scratch 3)",
        "",
        f"from pystage.{language} import {', '.join(imports)}",
        "",
    ]

    def setup(sprite, var, is_stage):
        '''
        Assets, variables, lists and monitors of the stage or a sprite.
        '''
        writer.set_sprite(sprite["name"])
        if is_stage:
            names = [writer.global_backdrop(c["local_name"], False) for c in sprite["costumes"]]
            for name in names:
                lines.append(f"{var}.{fn('pystage_addbackdrop', True)}({py_str(name)})")
            if sprite["currentCostume"] != 0:
                lines.append(f"{var}.{fn('looks_switchbackdropto_backdrop', True)}({py_str(names[sprite['currentCostume']])})")
        else:
            names = [writer.global_costume(c["local_name"], False) for c in sprite["costumes"]]
            for name, c in zip(names, sprite["costumes"]):
                args = py_str(name)
                if c["rotationCenterX"] is not None and c["rotationCenterY"] is not None:
                    args += f", center_x={c['rotationCenterX']}, center_y={c['rotationCenterY']}"
                if c["bitmapResolution"] != 1:
                    args += f", factor={c['bitmapResolution']}"
                lines.append(f"{var}.{fn('pystage_addcostume')}({args})")
            if sprite["currentCostume"] != 0:
                lines.append(f"{var}.{fn('looks_switchcostumeto')}({py_str(names[sprite['currentCostume']])})")
        for s in sprite["sounds"]:
            lines.append(f"{var}.{fn('pystage_addsound', is_stage)}({py_str(writer.global_sound(s['local_name'], False))})")
        local = "" if is_stage else ", all_sprites=False"
        for name, value in sprite["variables"].items():
            lines.append(f"{var}.{fn('pystage_makevariable', is_stage)}({py_str(name)}, {literal(value)}{local})")
        for name, values in sprite["lists"].items():
            lines.append(f"{var}.{fn('pystage_makelistvariable', is_stage)}({py_str(name)}, [{', '.join(literal(v) for v in values)}]{local})")
        for monitor in sprite["monitors"]:
            x, y = -240 + monitor["x"], 180 - monitor["y"]
            if "variable" in monitor:
                name = py_str(monitor["variable"])
                lines.append(f"{var}.{fn('data_showvariable', is_stage)}({name})")
                lines.append(f"{var}.{fn('pystage_setmonitorposition', is_stage)}({name}, {x}, {y})")
                if monitor["style"] == "large":
                    lines.append(f"{var}.{fn('pystage_setmonitorstyle_large', is_stage)}({name})")
            else:
                name = py_str(monitor["list"])
                lines.append(f"{var}.{fn('data_showlist', is_stage)}({name})")
                lines.append(f"{var}.{fn('pystage_setlistmonitorposition', is_stage)}({name}, {x}, {y}, {monitor['width']}, {monitor['height']})")

    def scripts(sprite):
        '''
        The blocks of the stage or a sprite, custom blocks first.
        '''
        writer.set_sprite(sprite["name"])
        res = ""
        blocks = sorted(sprite["blocks"], key=lambda block: block["opcode"] != "procedures_definition")
        for block in blocks:
            res += writer.process_stack(block)
        return res

    stage = project["stage"]
    lines.append(f"stage = {stage_class}()")
    setup(stage, "stage", True)

    for sprite in project["sprites"]:
        var = writer.get_sprite_var(sprite["name"])
        lines += [
            "",
            f"# Create and initialize sprite '{var}'",
            f"{var} = stage.{fn('pystage_createsprite', True)}(None)",
            f"{var}.{fn('pystage_setname')}({py_str(sprite['name'])})",
        ]
        if sprite["x"] != 0 or sprite["y"] != 0:
            lines.append(f"{var}.{fn('motion_gotoxy')}({sprite['x']}, {sprite['y']})")
        if sprite["direction"] != 90:
            lines.append(f"{var}.{fn('motion_pointindirection')}({sprite['direction']})")
        if sprite["rotationStyle"] == "left-right":
            lines.append(f"{var}.{fn('motion_setrotationstyle_leftright')}()")
        elif sprite["rotationStyle"] == "don't rotate":
            lines.append(f"{var}.{fn('motion_setrotationstyle_dontrotate')}()")
        if sprite["size"] != 100:
            lines.append(f"{var}.{fn('looks_setsizeto')}({sprite['size']})")
        if not sprite["visible"]:
            lines.append(f"{var}.{fn('looks_hide')}()")
        if sprite["draggable"]:
            lines.append(f"{var}.{fn('sensing_setdragmode_draggable')}()")
        if sprite["volume"] != 100:
            lines.append(f"{var}.{fn('sound_setvolumeto')}({sprite['volume']})")
        setup(sprite, var, False)

    res = "\n".join(lines) + "\n"

    # Now generate the code for the stage and each sprite.
    code = scripts(stage)
    if code.strip():
        res += f"\n# Scratch Blocks for 'stage'\n{code}"
    for sprite in project["sprites"]:
        code = scripts(sprite)
        if code.strip():
            res += f"\n# Scratch Blocks for '{writer.get_sprite_var(sprite['name'])}'\n{code}"

    # At most two blank lines in a row
    res = re.sub(r"\n{4,}", "\n\n\n", res).rstrip("\n")
    res += f"\n\nstage.{fn('pystage_play', True)}()\n"
    return res


def print_python(project, language="core"):
    print(get_python(project, language))


def create_project(file_name, project_name, project, directory, language="core", project_link=None, limits=DEFAULT_LIMITS):
    '''
    Writes the Python file and all assets into a new directory.
    '''
    logger.info(f"Creating project: {project_name}")
    logger.info(f"Exporting to: {directory}")
    project_name = to_filename(project_name)
    # Create the code first, so that nothing is written if this fails.
    code = get_python(project, language=language, project_link=project_link)
    dp = Path(directory)
    if dp.exists():
        raise ConversionError("Directory must not exist at this point, but it does: {}".format(directory))
    os.mkdir(dp)
    total = 0
    with zipfile.ZipFile(file_name, 'r') as archive:
        for folder, assets in (("images", project["costumes"]), ("sounds", project["sounds"])):
            os.mkdir(dp / folder)
            for key, asset in assets.items():
                # global_name and extension are safe, see get_intermediate
                target = dp / folder / f'{asset["global_name"]}.{asset["extension"]}'
                try:
                    info = archive.getinfo(f'{key}.{asset["extension"]}')
                except KeyError:
                    logger.warning(f"Asset {key} is missing in the project file.")
                    continue
                total += info.file_size
                if info.file_size > limits.asset or total > limits.total:
                    raise ConversionError("The project is too big.")
                with archive.open(info) as infile:
                    content = infile.read(limits.asset + 1)
                if len(content) > limits.asset:
                    raise ConversionError("The project is too big.")
                with open(target, "wb") as outfile:
                    outfile.write(content)
    with open(dp / f'{project_name}.py', "w", encoding="utf-8") as pyfile:
        pyfile.write(code)



##
# Main
#


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="python -m pystage.convert.sb3",
        description="Convert Scratch 3 (sb3) files to Python.")
    parser.add_argument("file", metavar="FILE", type=str, help="the sb3 file to be converted")
    parser.add_argument("-i", "--intermediate", action="store_true", help="print intermediate code representation")
    parser.add_argument("-s", "--sb3-json", action="store_true", help="print sb3 project.json")
    parser.add_argument("-p", "--python", action="store_true", help="print python code")
    parser.add_argument("-l", "--language", metavar="LANG", type=str, help="API language, 2-letter ISO code, e.g. en, de, ...", nargs="?", default="core")
    parser.add_argument("-v", "--verbose", action="store_true", help="be verbose (info)")
    parser.add_argument("-vv", "--debug", action="store_true", help="print debug information")
    parser.add_argument("-d", "--directory", metavar="DIR", type=str, help="the project directory")
    args = parser.parse_args(argv)

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    elif args.verbose:
        logging.basicConfig(level=logging.INFO)

    try:
        project_name = to_filename(Path(args.file).stem)
        data = get_sb3_data(args.file)
        if args.sb3_json:
            print(json.dumps(data, indent=2))
            return 0
        project = get_intermediate(data, project_name)
        if args.intermediate:
            print(json.dumps(project, indent=2))
            return 0
        if args.python:
            print_python(project, args.language)
            return 0
        directory = args.directory if args.directory else project_name
        print(f"Exporting to: {directory}")
        dp = Path(directory)
        if dp.exists() and not dp.is_dir():
            print("Output directory exists, but is not a directory. Use -d to specify another directory.")
            return 1
        if dp.exists() and next(dp.iterdir(), False):
            print("Output directory is not empty. Use -d to specify another one.")
            return 1
        if dp.exists():
            dp.rmdir()
        create_project(args.file, project_name, project, directory, args.language)
    except ConversionError as e:
        print(f"Conversion failed: {e}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
