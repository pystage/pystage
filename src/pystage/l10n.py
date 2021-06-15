import argparse
import inspect
import json
import requests

from pystage.core.sprite import Sprite
from pystage.core.stage import Stage

    

def get_translations(lang="en"):
    blocks = json.loads(requests.get(f"https://raw.githubusercontent.com/LLK/scratch-l10n/master/editor/blocks/{lang}.json").text)
    extensions = json.loads(requests.get(f"https://raw.githubusercontent.com/pystage/scratch-l10n/master/editor/extensions/{lang}.json").text)
    res = {}
    for key in blocks:
        res[key.upper()] = blocks[key] 
    for key in extensions:
        res[key.upper().replace(".", "_")] = extensions[key] 
    return res


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="python -m pystage.l10n",
        description="Manage translations")
    parser.add_argument("-o", "--opcodes", action="store_true", help="List pyStage opcodes")
    parser.add_argument("-s", "--stage", action="store_true", help="List pyStage opcodes")
    parser.add_argument("-l", "--language", metavar="LANG", type=str, help="API language, 2-letter ISO code, e.g. en, de, ...", nargs="?", default="en")
    args = parser.parse_args()

    if args.opcodes:
        cls = Stage if args.stage else Sprite
        translations = get_translations(args.language)
        for name, func in inspect.getmembers(cls, predicate=inspect.isfunction):
            if name.startswith("_"):
                continue
            params = [key for key in inspect.signature(func).parameters]
            params.remove("self")
            params = f"({', '.join(params)})"
            opcode = name.upper()
            outer_key = None
            trans_key = name.upper()
            if hasattr(func, "opcode"):
                opcode = func.opcode.upper()
                if name.upper() in translations:
                    outer_key = opcode
                    trans_key = name.upper()
                else:
                    trans_key = opcode
            if hasattr(func, "translation"):
                trans_key = func.translation.upper()
            trans = ""
            if trans_key in translations:
                trans = translations[trans_key]
            if opcode != trans_key and opcode in translations:
                outer_key = opcode
            if outer_key:
                trans = translations[outer_key]
                if "%1" in trans:
                    trans = trans.replace("%1", translations[trans_key])
                else:
                    trans += f" {translations[trans_key]}"
            print(f"{name}{params} - {trans}\n")


