import argparse
import inspect
import json
import requests
import re
import textwrap
import importlib

from pystage.core.sprite import CoreSprite
from pystage.core.stage import CoreStage
from pystage.l10n.translations import trans, funcname


square_bracketed_variable = re.compile(r"\[[^\]]*\]")
percent_variable = re.compile(r"%[0-9]")
to_underscore = re.compile(r"[ -:/,%]")
to_delete = re.compile(r"[%?]")
multiple_underscores = re.compile(r"_+")
deleteself = re.compile(r"self[, ]*")

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
    # Another inconsistency where not the opcode is used (typo?)...
    res["SOUND_SETEFFECTTO"] = res["SOUND_SETEFFECTO"]
    return res


def get_translation(func, translations, lang="en"):
    name = func.__name__
    opcode = name.upper()
    outer_key = None
    trans_key = name.upper()
    trans_key = trans_key.replace("OPERATOR", "OPERATORS")
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
        language = args.language
        sprite_class = trans("gui.backpack.spriteLabel", language).capitalize()
        stage_class = trans("gui.stageSelector.stage", language).capitalize()

        create_sprite = funcname(trans("gui.howtos.animate-char.step_addsprite", language), language)
        add_sound = funcname(trans("gui.howtos.animate-char.step_addsound", language), language)
        play = funcname(trans("gui.playButton.play", language), language)
            
        if args.stage:
            print(f'''
from pystage.core.stage import CoreStage
from pystage.{language}.sprite import {sprite_class}


class {stage_class}():

    def __init__(self):
        self._core = CoreStage()
        self._core.facade = self
        self._core.sprite_facade_class = {sprite_class}

    def {create_sprite}(self, costume="default"):
        return self._core.pystage_createsprite(costume=costume)

    def {play}(self):
        self._core.pystage_play()
        
            ''')
        else:
            print(f'''
from pystage.core.sprite import CoreSprite


class {sprite_class}():
    def __init__(self, core_sprite):
        self._core : CoreSprite = core_sprite
        self._core.facade = self


            ''')
        translations = get_translations(args.language)
        for name, func in inspect.getmembers(cls, predicate=inspect.isfunction):
            if name.startswith("_"):
                continue
            param_keys = [key for key in inspect.signature(func).parameters]
            params = [str(inspect.signature(func).parameters[key]) for key in param_keys]
            params_call = f"({', '.join(params)})"
            trans_text = get_translation(func, translations, lang=args.language)
            trans_hint = ""
            if hasattr(func, "translation_hint"):
                trans_hint = f"""
        TODO TRANSLATORS: {func.translation_hint}
        """
            trans = create_funcname(trans_text, translations)
            if not trans:
                trans = name
            paramdoc = "\n        ".join([f"{param.split('=')[0]} : FILL" for param in params if param != "self"])
            if paramdoc:
                paramdoc = f'''
        Parameters
        ----------
        {paramdoc}
        '''
            print(f'''\
    def {trans}{params_call}:
        """{trans_text}{trans_hint}

        Translation string: {trans_text}
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        {paramdoc}

        Returns
        -------

        """
        self._core.{name}{deleteself.sub("", params_call)}
                ''')



