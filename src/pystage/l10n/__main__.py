import argparse
import inspect
import json
import requests
import re

from pystage.core.sprite import CoreSprite
from pystage.core.stage import CoreStage


square_bracketed_variable = re.compile(r"\[[^\]]*\]")
percent_variable = re.compile(r"%[0-9]")
to_underscore = re.compile(r"[ -:/,%]")
to_delete = re.compile(r"[%?]")
multiple_underscores = re.compile(r"_+")

def get_translations(lang="en"):
    blocks = json.loads(requests.get(f"https://raw.githubusercontent.com/LLK/scratch-l10n/master/editor/blocks/{lang}.json").text)
    extensions = json.loads(requests.get(f"https://raw.githubusercontent.com/pystage/scratch-l10n/master/editor/extensions/{lang}.json").text)
    res = {}
    for key in blocks:
        res[key.upper()] = blocks[key] 
    for key in extensions:
        res[key.upper().replace(".", "_")] = extensions[key] 
    res["MOTION_TURNLEFT"] = res["MOTION_TURNLEFT"].replace("%1", res["BOOST_TILTDIRECTION_LEFT"])
    res["MOTION_TURNRIGHT"] = res["MOTION_TURNRIGHT"].replace("%1", res["BOOST_TILTDIRECTION_RIGHT"])
    res["EVENT_WHENFLAGCLICKED"] = res["EVENT_WHENFLAGCLICKED"].replace("%1", "<greenflag>")
    res["EVENT_WHENGREATERTHAN"] = res["EVENT_WHENGREATERTHAN"].replace(">", "<greater>")
    return res


def get_translation(func, translations, lang="en"):
    name = func.__name__
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
    if hasattr(func, "outer_translation"):
        outer_key = func.outer_translation.upper()
    if outer_key:
        trans = translations[outer_key]
        position = "%1"
        if hasattr(func, "position"):
            position = func.position
        if position in trans:
            trans = trans.replace(position, translations[trans_key])
        else:
            trans += f" {translations[trans_key]}"
    return trans


def create_funcname(translation, translations):
    translation = square_bracketed_variable.sub("", translation)
    translation = to_underscore.sub("_", translation)
    translation = percent_variable.sub("", translation)
    translation = to_delete.sub("", translation)
    translation = translation.replace("#", translations["LOOKS_NUMBERNAME_NUMBER"])
    translation = multiple_underscores.sub("_", translation)
    translation = translation.strip("_").lower()
    translation = translation.replace("<greenflag>", "GREENFLAG")
    translation = translation.replace("<greater>", "GREATERTHAN")
    return translation

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="python -m pystage.l10n",
        description="Manage translations")
    parser.add_argument("-t", "--translations", action="store_true", help="List core function translations")
    parser.add_argument("-a", "--api", action="store_true", help="List translated API function suggestions")
    parser.add_argument("-s", "--stage", action="store_true", help="Use stage instead of sprite")
    parser.add_argument("-l", "--language", metavar="LANG", type=str, help="API language, 2-letter ISO code, e.g. en, de, ...", nargs="?", default="en")
    args = parser.parse_args()

    if args.translations:
        cls = CoreStage if args.stage else CoreSprite
        translations = get_translations(args.language)
        for name, func in inspect.getmembers(cls, predicate=inspect.isfunction):
            if name.startswith("_"):
                continue
            params = [key for key in inspect.signature(func).parameters]
            params.remove("self")
            params = f"({', '.join(params)})"
            trans = get_translation(func, translations, lang=args.language)
            print(f"{name}{params} - {trans}\n")
    elif args.api:
        cls = CoreStage if args.stage else CoreSprite
        translations = get_translations(args.language)
        for name, func in inspect.getmembers(cls, predicate=inspect.isfunction):
            if name.startswith("_"):
                continue
            params = [key for key in inspect.signature(func).parameters]
            params.remove("self")
            params = f"({', '.join(params)})"
            trans = create_funcname(get_translation(func, translations, lang=args.language), translations)
            print(f"{name}{params} - {trans}\n")



