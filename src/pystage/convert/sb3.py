import argparse
import zipfile
import json


from pystage.convert import CodeWriter


'''
For the conversion, we create a simplified version of the 
block trees that is used in the code template functions.
'''

# Target (intermediate) structure
# project = {
#         "sprites": [
#             {
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
        value = str(value)
    return value




def get_block(block, blocks):
    '''
    Recursively turns the sb3 structure into our intermediate representation.
    '''
    res = {
            "opcode": block["opcode"],
            "params": {},
            "next": False,
            }
    for f in block["fields"]:
        res["params"][f] = block["fields"][f][0]
    for i in block["inputs"]:
        value = block["inputs"][i][1]
        if isinstance(value, list):
            res["params"][i] = get_input_value(value)
        else:
            res["params"][i] = get_block(blocks[value], blocks)
    if block["next"]:
        res["next"] = get_block(blocks[block["next"]], blocks) 
    return res



##
# Main
#


parser = argparse.ArgumentParser()
parser.add_argument("file", metavar="FILE", type=str)
args = parser.parse_args()

archive = zipfile.ZipFile(args.file, 'r')
with archive.open("project.json") as f:
    data = json.loads(f.read())

    hat_blocks = [
        "event_whenthisspriteclicked", 
        "event_whenbroadcastreceived", 
        "event_whenflagclicked",
        "event_whenkeypressed",
        # TODO: list all
        ]

    for target in data["targets"]:
        blocks = target["blocks"]
        print(f"\nBlocks: {target['name']}")
        for key in blocks:
            b = blocks[key]
            if b["opcode"] in hat_blocks:
                print("   ", b["opcode"])
                block = get_block(b, blocks)
                print(json.dumps(block, indent = 2))
