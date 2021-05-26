import argparse
import zipfile
import json
import math


from pystage.convert import CodeWriter, sb3_templates


'''
For the conversion, we create a simplified version of the 
block trees that is used in the code template functions.
'''

# Target (intermediate) structure
# project = {
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


def get_intermediate(data):
    hat_blocks = [
        "event_whenthisspriteclicked", 
        "event_whenbroadcastreceived", 
        "event_whenflagclicked",
        "event_whenkeypressed",
        # TODO: list all
        ]

    project = DictClass()
    project.update({
            "sprites": [],
            })

    for target in data["targets"]:
        sprite = DictClass()
        sprite.update({
                "name": target['name'],
                "blocks": [],
                })
        project["sprites"].append(sprite)
        blocks = target["blocks"]
        for key in blocks:
            b = blocks[key]
            if b["opcode"] in hat_blocks:
                block = get_block(b, blocks)
                sprite["blocks"].append(block)
    return project

##
# Main
#


parser = argparse.ArgumentParser(
        prog="python -m pystage.convert.sb3",
        description="Convert Scratch 3 (sb3) files to Python.")
parser.add_argument("file", metavar="FILE", type=str)
parser.add_argument("--intermediate", action="store_true", help="print intermediate code representation")
args = parser.parse_args()

archive = zipfile.ZipFile(args.file, 'r')
with archive.open("project.json") as f:
    data = json.loads(f.read())
    project = get_intermediate(data)
    if args.intermediate:
        print(json.dumps(project, indent=2))
    else:
        writer = CodeWriter(project, sb3_templates.templates) 
        for sprite in project["sprites"]:
            writer.set_sprite(sprite["name"])
            for block in sprite["blocks"]:
                print(writer.process(block))



