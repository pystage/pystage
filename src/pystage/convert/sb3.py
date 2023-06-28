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
import importlib
from pystage.l10n.api import get_translated_function

from pystage.convert import CodeWriter, sb3_templates

logger = logging.getLogger(__name__)

'''
For the conversion, we create a simplified version of the
block trees that is used in the code template functions.
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
#                             "BROADCAST_INPUT": {"start",
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
#                 "currentCostume": 0
#                 },
#
#             ],
#
#         }

class DictClass(OrderedDict):
    '''
    A dictionary that can be accessed via dot notation for convenience.
    '''

    def __init__(self):
        super().__init__()

    def __getattr__(self, item):
        return self[item]


def get_input_value(i, stage):
    '''
    Extracts values from sb3 input representations.
    '''
    # 4: number, 5: positive number, 6: positive integer
    # 7: integer, 8: angle, 9: color, 10: string
    # 11: broadcast, 12: variable, 13: list

    input_type = i[0]
    value = i[1]

    if input_type in [4, 5, 8]:
        if isinstance(value, str) and value.strip() == '':
            value = 0
        else:
            value = float(value)
    elif input_type in [6, 7]:
        if isinstance(value, str) and value.strip() == '':
            value = 0
        else:
            value = int(value)
    elif input_type == 9:
        h = value.lstrip("#")
        value = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    elif input_type == 12:
        block = DictClass()
        block.update({
                "opcode": "data_variable",
                "params": {
                    "VARIABLE": f'"{value}"',
                    },
                "next": False,
                "stage": stage,
                })
        return block
    elif input_type in [10, 11, 13]:
        try:
            f = float(value)
            if math.floor(f) == f:
                f = int(f)
            value = f
        except:
            value = f'"{value}"'
    return value


def get_block(block, blocks, stage, comments=None):
    '''
    Recursively turns the sb3 structure into our intermediate representation.
    '''
    res = DictClass()
    res.update({
        "opcode": block["opcode"],
        "params": DictClass(),
        "next": False,
        "stage": stage,
        "comment": None
    })

    # add the comment attribute to the block if available
    # works for comments that are pointing to a block
    # won't work for global comments
    if (comment := block.get("comment")) and comments:
        if comment_text := comments.get(comment, {}).get("text"):
            res["comment"]= comment_text

    for f in block["fields"]:
        res["params"][f] = f'"{block["fields"][f][0]}"'
    for i in block["inputs"]:
        value = block["inputs"][i][1]
        if not value:
            # empty if condition
            continue
        if isinstance(value, list):
            res["params"][i] = get_input_value(value, stage)
        else:
            res["params"][i] = get_block(blocks[value], blocks, stage, comments)
    if block["next"]:
        res["next"] = get_block(blocks[block["next"]], blocks, stage, comments)
    return res


def to_filename(name: str):
    umlauts = {"ö": "oe", "ü": "ue", "ä": "ae", "ß": "ss"}
    name = name.lower().strip()
    for c in umlauts:
        name = name.replace(c, umlauts[c])

    # \u4e00-\u9fa5 is the range of Chinese characters
    name = re.sub(r"[^a-z0-9_\u4e00-\u9fa5]", "_", name)
    name = re.sub(r"_+", "_", name)
    return name

# Used to check for duplicate names
global_names = set()

def unique_global_name(name, ext):
    iname = name
    i = 2
    while f"{iname}.{ext}" in global_names:
        iname = f"{name}_{i}"
        i += 1
    global_names.add(f"{iname}.{ext}")
    return iname, ext

def get_intermediate(data, name):
    # Added for test, in test I will convert all the scratch files to python code.
    # So I need to clear the global_names before each running.
    global_names.clear()
    hat_blocks = [
        "event_whenthisspriteclicked",
        "event_whenbroadcastreceived",
        "event_whenflagclicked",
        "event_whenkeypressed",
        "event_whenbackdropswitchesto",
        "event_whengreaterthan",
        "control_start_as_clone",
    ]

    project = DictClass()
    project.update({
        "name": name,
        "sprites": [],
        "costumes": {},
        "sounds": {},
    })


    for target in data["targets"]:
        sprite = DictClass()
        sprite.update({
            "name": target['name'],
            "blocks": [],
            "costumes": [],
            "sounds": [],
            "variables": {}, # name: value
            "lists": {},
            "monitors": [], # name: value
            "currentCostume": target["currentCostume"],
            "layerOrder": target["layerOrder"],
            "visible": target["visible"] if "visible" in target else True,
            "x": target["x"] if "x" in target else 0,
            "y": target["y"] if "y" in target else 0,
            "size": target["size"] if "size" in target else 100,
            "volume": target["volume"] if "volume" in target else 100,
            "direction": target["direction"] if "direction" in target else 90,
            "rotationStyle": target["rotationStyle"] if "rotationStyle" in target else "all around",
            "comments": []
        })

        # add global comments
        if comments := target.get("comments"):
            for comment in comments.values():
                if comment.get("blockId"):
                    continue
                if comment_text := comment.get("text"):
                    sprite["comments"].append(comment_text)

        if target["isStage"]:
            project["stage"] = sprite
        else:
            project["sprites"].append(sprite)
        sprite["currentCostume"] = target["currentCostume"]
        blocks = target["blocks"]
        for key in blocks:
            b = blocks[key]
            if isinstance(b, list):
                # Stuff like variables, not interesting at this point
                continue
            # if b["parent"] is None:
            if b["opcode"] in hat_blocks:
                block = get_block(b, blocks, target["isStage"], target["comments"])
                sprite["blocks"].append(block)
        for c in target["costumes"]:
            if c["assetId"] not in project["costumes"]:
                name, ext = unique_global_name(to_filename(c["name"]), c["dataFormat"])
                project["costumes"][c["assetId"]] = {
                    "global_name": name,
                    "extension": ext,
                }
            sprite["costumes"].append({
                "md5": c["assetId"],
                "local_name": c["name"],
                "bitmapResolution": c["bitmapResolution"] if "bitmapResolution" in c else 1,
                "rotationCenterX": c["rotationCenterX"],
                "rotationCenterY": c["rotationCenterY"],
            })
        for s in target["sounds"]:
            if s["assetId"] not in project["sounds"]:
                name, ext = unique_global_name(to_filename(s["name"]), s["dataFormat"])
                project["sounds"][s["assetId"]] = {
                    "global_name": name,
                    "extension": ext,
                }
            sprite["sounds"].append({
                "md5": s["assetId"],
                "local_name": s["name"],
            })
        for key in target["variables"]:
            v = target["variables"][key]
            variable = {}
            sprite["variables"][v[0]] = v[1]

        for key in target["lists"]:
            l = target["lists"][key]
            sprite["lists"][l[0]] = l[1]

    for m in data["monitors"]:
        if not m["visible"]:
            continue
        monitor = {}
        if not m["spriteName"]:
            sprite = project["stage"]
        else:
            for s in project["sprites"]:
                if s["name"] == m["spriteName"]:
                    sprite = sprite
                    break
        monitor["style"] = m["mode"]
        if monitor["style"] == "default":
            monitor["style"] == "normal"
        monitor["x"] = m["x"]
        monitor["y"] = m["y"]
        monitor["opcode"] = m["opcode"]
        if "VARIABLE" in m["params"]:
            monitor["variable"] = m["params"]["VARIABLE"]
        sprite["monitors"].append(monitor)

    return project


def get_python(project, language="core"):
    lang_module = importlib.import_module(f"pystage.{language}")
    sprite_class = lang_module.sprite_class.__name__
    stage_class = lang_module.stage_class.__name__
    add_backdrop = get_translated_function("pystage_addbackdrop", language, stage=True)
    add_costume = get_translated_function("pystage_addcostume", language)
    add_sound = get_translated_function("pystage_addsound", language)
    add_variable = get_translated_function("pystage_makevariable", language)
    add_list_variable = get_translated_function("pystage_makelistvariable", language)
    create_sprite = get_translated_function("pystage_createsprite", language, stage=True)
    play = get_translated_function("pystage_play", language, stage=True)
    res = textwrap.dedent(f'''\
            # {project['name']} (pyStage, converted from Scratch 3)

            from pystage.{language} import {sprite_class}, {stage_class}

            ''')
    writer = CodeWriter(project, sb3_templates.templates, language)
    writer.set_sprite(project["stage"]["name"])
    stage_var = writer.get_sprite_var()
    # {"backdrop1": [rotationCenterX, rotationCenterY], ...}
    backdrops = {}
    for bd in project["stage"]["costumes"]:
        name = writer.global_backdrop(bd["local_name"], False)
        resolution = bd.get("bitmapResolution", 1)
        backdrops[name] = [bd.get("rotationCenterX")/resolution, bd.get("rotationCenterY")/resolution]
    # comment for stage
    if comments := project["stage"]["comments"]:
        comments = "\n".join(comments)
        # not using textwrap.dedent here because it would indent incorrectly
        # when there is more than one comment
        res += f'\n"""\n# {project["stage"]["name"]}\n\n{comments}\n"""\n'
    res += textwrap.dedent(f'''\
            {stage_var} = {stage_class}()
            ''')
    for bd in backdrops:
        res += textwrap.dedent(f'''\
                {stage_var}.{add_backdrop}('{bd}', {round(backdrops[bd][0])}, {round(backdrops[bd][1])})
                ''')
    for v in project["stage"]["variables"]:
        res += textwrap.dedent(f'''\
                {stage_var}.{add_variable}('{v}')
                ''')

    for l in project["stage"]["lists"]:
        res += textwrap.dedent(f'''\
                {stage_var}.{add_list_variable}('{l}')
                ''')
    for item in (lists := project["stage"]["lists"]):
        res += textwrap.dedent(f'''\
                {stage_var}.{add_list_variable}("{item}")
            ''')
        for val in lists[item]:
            res += textwrap.dedent(f'''\
                {stage_var}.{get_translated_function("data_addtolist", language)}("{item}", "{val}")
            ''')

    for monitor in project["stage"]["monitors"]:
        # Only variable monitors are currently implemented
        if "variable" in monitor:
            res += textwrap.dedent(f'''\
                {stage_var}.{get_translated_function("data_showvariable", language)}("{monitor["variable"]}")
                {stage_var}.{get_translated_function("pystage_setmonitorposition", language)}("{monitor["variable"]}", {-240 + monitor["x"]}, {180 - monitor["y"]})
                ''')
            if monitor["style"] == "large":
                res += textwrap.dedent(f'''\
                    {stage_var}.{get_translated_function("pystage_setmonitorstyle_large", language)}("{monitor["variable"]}")
                    ''')
        else:
            # handle builtin variable like timer, answer, xposition
            res += textwrap.dedent(f'''\
                {stage_var}.{get_translated_function("data_showbuiltinvariable", language)}("{monitor["opcode"]}")
                {stage_var}.{get_translated_function("pystage_setmonitorposition", language)}("{monitor["opcode"]}", {-240 + monitor["x"]}, {180 - monitor["y"]})
                ''')
    
    
    for block in project["stage"]["blocks"]:
        res += writer.process(block)
    for sprite in project["sprites"]:
        writer.set_sprite(sprite["name"])
        sprite_var = writer.get_sprite_var()
        costumes = [(writer.global_costume(c["local_name"], False), c) for c in sprite["costumes"]]
        sounds = [writer.global_sound(s["local_name"], False) for s in sprite["sounds"]]
        # comment for sprite
        if comments := sprite["comments"]:
            comments = "\n".join(comments)
            res += f'\n"""\n# {sprite["name"]}\n\n{comments}\n"""\n'
        res += textwrap.dedent(f'''\
                {sprite_var} = {stage_var}.{create_sprite}(None)
                {sprite_var}.{get_translated_function("pystage_setname", language)}("{sprite["name"]}")
                {sprite_var}.{get_translated_function("motion_setx", language)}({sprite["x"]})
                {sprite_var}.{get_translated_function("motion_sety", language)}({sprite["y"]})
                {sprite_var}.{get_translated_function("looks_gotofrontback_back", language)}()
                {sprite_var}.{get_translated_function("looks_goforwardbackwardlayers_forward", language)}({sprite["layerOrder"]})
                ''')
        if sprite["direction"] != 90:
            res += textwrap.dedent(f"""\
                    {sprite_var}.{get_translated_function("motion_pointindirection", language)}({sprite["direction"]})
                    """)
        if sprite["size"] != 100:
            res += textwrap.dedent(f"""\
                    {sprite_var}.{get_translated_function("looks_setsizeto", language)}({sprite["size"]})
                    """)
        if not sprite["visible"]:
            res += textwrap.dedent(f"""\
                    {sprite_var}.{get_translated_function("looks_hide", language)}()
                    """)
        if sprite["volume"] != 100:
            res += textwrap.dedent(f"""\
                    {sprite_var}.{get_translated_function("sound_setvolumeto", language)}({sprite["volume"]})
                    """)
        if sprite["rotationStyle"] != "all around":
            print("WARNING: preset rotation styles not yet implemented!")
        for c in costumes:
            factor = ""
            if c[1]["bitmapResolution"] != 1:
                factor=f", factor={c[1]['bitmapResolution']}"
            res += textwrap.dedent(f'''\
                {sprite_var}.{add_costume}('{c[0]}', center_x={c[1]["rotationCenterX"]}, center_y={c[1]["rotationCenterY"]}{factor})
                ''')
        if sprite["currentCostume"] != 0:
            for i in range(sprite["currentCostume"]):
                res += textwrap.dedent(f'''\
                    {sprite_var}.{get_translated_function("looks_nextcostume", language)}()
                    ''')

        for s in sounds:
            res += textwrap.dedent(f'''\
                {sprite_var}.{add_sound}('{s}')
                ''')

        for v in sprite["variables"]:
            res += textwrap.dedent(f'''\
                    {sprite_var}.{add_variable}('{v}')
                    ''')
            
        for item in (lists := sprite["lists"]):
            print('gp: lists = ', lists, ' item = ', item)
            res += textwrap.dedent(f'''\
                    {sprite_var}.{add_list_variable}("{item}")
                ''')
            for val in lists[item]:
                res += textwrap.dedent(f'''\
                    {sprite_var}.{get_translated_function("data_addtolist", language)}("{item}", "{val})
                ''')
            
        for monitor in sprite["monitors"]:
            # Only variable monitors are currently implemented
            if not "variable" in monitor:
                continue
            res += textwrap.dedent(f'''\
                    {sprite_var}.{get_translated_function("data_showvariable", language)}("{monitor["variable"]}")
                    {sprite_var}.{get_translated_function("pystage_setmonitorposition", language)}("{monitor["variable"]}", {-240 + monitor["x"]}, {180 - monitor["y"]})
                    ''')
            if monitor["style"] == "large":
                res += textwrap.dedent(f'''\
                        {sprite_var}.{get_translated_function("pystage_setmonitorstyle_large", language)}("{monitor["variable"]}")
                        ''')
        for block in sprite["blocks"]:
            res += writer.process(block)


    res += textwrap.dedent(f'''\

            {stage_var}.{play}()
            ''')
    return res


def print_python(project, language="core"):
    print(get_python(project, language))


##
# Main
#

if __name__ == "__main__":

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
    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    elif args.verbose:
        logging.basicConfig(level=logging.INFO)

    archive = zipfile.ZipFile(args.file, 'r')
    with archive.open("project.json") as f:
        project_name = to_filename(Path(args.file).stem)
        data = json.loads(f.read())
        if args.sb3_json:
            print(json.dumps(data, indent=2))
            sys.exit(0)
        project = get_intermediate(data, project_name)
        if args.intermediate:
            print(json.dumps(project, indent=2))
            sys.exit(1)
        elif args.python:
            print_python(project, args.language)
            sys.exit(1)
        else:
            print(f"Creating project: {project_name}")
            directory = project_name
            if args.directory:
                directory = args.directory
            print(f"Exporting to: {directory}")
            dp = Path(directory)
            if dp.exists() and not dp.is_dir:
                print("Output directory exists, but is not a directory. Use -d to specify another directory.")
                sys.exit(1)
            elif dp.exists() and next(dp.iterdir(), False):
                print("Output directory is not empty. Use -d to specify another one.")
                sys.exit(1)
            elif not dp.exists():
                print(f"Creating directory: {dp}")
                os.mkdir(dp)
            os.mkdir(dp / "images")
            os.mkdir(dp / "sounds")
            for key in project["costumes"]:
                c = project["costumes"][key]
                with archive.open(f'{key}.{c["extension"]}') as infile:
                    with open(dp / "images" / f'{c["global_name"]}.{c["extension"]}', "wb") as outfile:
                        outfile.write(infile.read())
            for key in project["sounds"]:
                s = project["sounds"][key]
                with archive.open(f'{key}.{s["extension"]}') as infile:
                    with open(dp / "sounds" / f'{s["global_name"]}.{s["extension"]}', "wb") as outfile:
                        outfile.write(infile.read())
            with open(dp / f'{project_name}.py', "w", encoding="utf-8") as pyfile:
                pyfile.write(get_python(project, language=args.language))
