import requests
import json
import re

_translations = {}

square_bracketed_variable = re.compile(r"\[[^\]]*\]")
percent_variable = re.compile(r"%[0-9]")
to_underscore = re.compile(r"[ -:/,%]")
to_delete = re.compile(r"[%?]")
multiple_underscores = re.compile(r"_+")
deleteself = re.compile(r"self[, ]*")


def fetch_translations(lang="en"):
    if lang in _translations:
        return _translations[lang]

    blocks = json.loads(requests.get(f"https://raw.githubusercontent.com/LLK/scratch-l10n/master/editor/blocks/{lang}.json").text)
    extensions = json.loads(requests.get(f"https://raw.githubusercontent.com/pystage/scratch-l10n/master/editor/extensions/{lang}.json").text)
    interface = json.loads(requests.get(f"https://raw.githubusercontent.com/pystage/scratch-l10n/master/editor/interface/{lang}.json").text)
    res = {}
    for key in blocks:
        res[key.upper()] = blocks[key] 
    for key in extensions:
        res[key.upper().replace(".", "_")] = extensions[key] 
    for key in interface:
        res[key.upper()] = interface[key] 
    res["MOTION_TURNLEFT"] = res["MOTION_TURNLEFT"].replace("%1", res["BOOST_TILTDIRECTION_LEFT"])
    res["MOTION_TURNRIGHT"] = res["MOTION_TURNRIGHT"].replace("%1", res["BOOST_TILTDIRECTION_RIGHT"])
    res["EVENT_WHENFLAGCLICKED"] = res["EVENT_WHENFLAGCLICKED"].replace("%1", "<greenflag>")
    res["EVENT_WHENGREATERTHAN"] = res["EVENT_WHENGREATERTHAN"].replace(">", "<greater>")
    # Another inconsistency where not the opcode is used (typo?)...
    res["SOUND_SETEFFECTTO"] = res["SOUND_SETEFFECTO"]
    _translations[lang] = res
    return res

def trans(key, lang):
    translations = fetch_translations(lang)
    key = key.upper()
    if key in translations:
        return translations[key]
    return f"MISSING_TRANSLATION: {key}"

def funcname(translation, lang):
    translation = square_bracketed_variable.sub("", translation)
    translation = to_underscore.sub("_", translation)
    translation = percent_variable.sub("", translation)
    translation = to_delete.sub("", translation)
    translation = translation.replace("#", trans("LOOKS_NUMBERNAME_NUMBER", lang))
    translation = multiple_underscores.sub("_", translation)
    translation = translation.strip("_").lower()
    translation = translation.replace("<greenflag>", "GREENFLAG")
    translation = translation.replace("<greater>", "GREATERTHAN")
    return translation
