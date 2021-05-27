import argparse
import zipfile
import json
import math
from pathlib import Path
import sys
import os
import textwrap


from pystage.convert import CodeWriter, sb3_templates


'''
For the conversion, we create a simplified version of the 
block trees that is used in the code template functions.
'''

# Target (intermediate) structure
# project = {
#         "stage": {
#               "name": "Stage",
#               "blocks": [],
#           }
#         "sprites": [
#             {
#                 "name": "Sprite1",
#                 "blocks": [
#                     { # BLOCK
#                         "opcode": "event_whenthisspriteclicked",
#                         "params": {
#                             "BROADCAST_INPUT": {"start",
#                             "COSTUME": "BLOCK"
#                             }
#                         "next": "BLOCK",
#                         "comments": ["text"],
#                         }
#                     ]
#                 },
# 
#             ],
# 
#         }

class DictClass(dict):
    '''
    A dictionary that can be accessed via dot notation for convenience.
    '''

    def __init__(self):
        super().__init__()

    def __getattr__(self, item):
        return self[item]

def get_input_value(i):
    '''
    Extracts values from sb3 input representations.
    '''
    # 4: number, 5: positive number, 6: positive integer
    # 7: integer, 8: angle, 9: color, 10: string
    # 11: broadcast, 12: variable, 13: list

    input_type = i[0]
    value = i[1]

    if input_type in [4, 5, 8]:
        if value.strip()=='':
            value = 0
        else:
            value = float(value)
    elif input_type in [6, 7]:
        if value.strip()=='':
            value = 0
        else:
            value = int(value)
    elif input_type == 9:
        h = value.lstrip("#")
        value = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    elif input_type in [10, 11, 12, 13]:
        try:
            f = float(value)
            if math.floor(f) == f:
                f = int(f)
            value = f
        except:
            value = f'"{value}"'
    return value




def get_block(block, blocks):
    '''
    Recursively turns the sb3 structure into our intermediate representation.
    '''
    res = DictClass()
    res.update({
            "opcode": block["opcode"],
            "params": DictClass(),
            "next": False,
            })
    for f in block["fields"]:
        res["params"][f] = f'"{block["fields"][f][0]}"'
    for i in block["inputs"]:
        value = block["inputs"][i][1]
        if isinstance(value, list):
            res["params"][i] = get_input_value(value)
        else:
            res["params"][i] = get_block(blocks[value], blocks)
    if block["next"]:
        res["next"] = get_block(blocks[block["next"]], blocks) 
    return res


def get_intermediate(data, name):
    hat_blocks = [
        "event_whenthisspriteclicked", 
        "event_whenbroadcastreceived", 
        "event_whenflagclicked",
        "event_whenkeypressed",
        # TODO: list all
        ]

    project = DictClass()
    project.update({
            "name": name,
            "sprites": [],
            })

    for target in data["targets"]:
        sprite = DictClass()
        sprite.update({
                "name": target['name'],
                "blocks": [],
                })
        if target["isStage"]:
            project["stage"] = sprite
        else:
            project["sprites"].append(sprite)
        blocks = target["blocks"]
        for key in blocks:
            b = blocks[key]
            if b["opcode"] in hat_blocks:
                block = get_block(b, blocks)
                sprite["blocks"].append(block)
    return project


def get_python(project):
    res = textwrap.dedent(f'''\
            # {project['name']} (pyStage, converted from Scratch 3)
            
            from pystage import Sprite, Stage
            
            ''')
    writer = CodeWriter(project, sb3_templates.templates) 
    writer.set_sprite(project["stage"]["name"]) 
    res += textwrap.dedent(f'''\
            {writer.get_sprite_var()} = Stage()
            ''')
    for block in project["stage"]["blocks"]:
        res += writer.process(block)
    for sprite in project["sprites"]:
        writer.set_sprite(sprite["name"]) 
        res += textwrap.dedent(f'''\
                {writer.get_sprite_var()} = stage.create_sprite()
                ''')
        for block in sprite["blocks"]:
            res += writer.process(block)
    return res


def print_python(project):
    print(get_python(project))


##
# Main
#


parser = argparse.ArgumentParser(
        prog="python -m pystage.convert.sb3",
        description="Convert Scratch 3 (sb3) files to Python.")
parser.add_argument("file", metavar="FILE", type=str, help="the sb3 file to be converted")
parser.add_argument("-i", "--intermediate", action="store_true", help="print intermediate code representation")
parser.add_argument("-s", "--sb3-json", action="store_true", help="print sb3 project.json")
parser.add_argument("-p", "--python", action="store_true", help="print python code")
parser.add_argument("-d", "--directory", metavar="DIR", type=str, help="the project directory")
args = parser.parse_args()


archive = zipfile.ZipFile(args.file, 'r')
with archive.open("project.json") as f:
    project_name = Path(args.file).stem
    data = json.loads(f.read())
    project = get_intermediate(data, project_name)
    if args.intermediate:
        print(json.dumps(project, indent=2))
    elif args.sb3_json:
        print(json.dumps(data, indent=2))
    elif args.python:
        print_python(project)
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
        elif not dp.exists():
            print(f"Creating directory: {dp}")
            os.mkdir(dp)
        os.mkdir(dp / "images")
        os.mkdir(dp / "sounds")



