"""Localisation of values and messages.

The core of pyStage is language neutral: it only knows canonical (English)
values like ``"space"``, ``"last"`` or ``"_mouse_"`` and English messages.
This module is the only place that knows about other languages. It contains

1. **Alias tables**: user facing values of the Scratch editor in another
   language (``"Leertaste"``, ``"letztes"``, ``"Mauszeiger"``) mapped to the
   canonical value. Aliases are accepted *regardless* of the language of the
   API in use and compared case-insensitively, so a German program can use
   English values and the other way around. Use :func:`canonical` in core
   code that receives such a value as a string.
2. **A message catalogue** for everything that is shown to the user at
   runtime (exception texts, warnings on the console, texts on the stage).
   Use :func:`tr` with a key and parameters. The language of the messages is
   the language of the facade in use: ``CoreStage(language=...)`` calls
   :func:`set_language`, the English API is the default.

The German and Lithuanian strings are taken from Scratch's own translation (scratch-l10n,
``editor/blocks/de.json``) wherever Scratch has them; the rest is marked
below. Messages and aliases that are missing for a language fall back to
English, so a translation can be added step by step.

Adding a language
-----------------
Add a language code to ``ALIASES[<table>]`` for every table and to
``MESSAGES``. Nothing else needs to change.
"""

# The language of the messages, see set_language().
_language = "en"


def set_language(language):
    """Select the language of runtime messages (e.g. "en" or "de")."""
    global _language
    if language not in MESSAGES:
        raise ValueError(f"Unknown language {language!r}. Available: {', '.join(sorted(MESSAGES))}.")
    _language = language


def get_language():
    """The language of runtime messages."""
    return _language


##
# Alias tables: ALIASES[table][language][canonical value] = [aliases]
#

ALIASES = {
    # Keys for when_key_pressed and key_pressed.
    # Scratch DE: EVENT_WHENKEYPRESSED_SPACE/_LEFT/_RIGHT/_DOWN/_UP/_ANY.
    # "Eingabetaste" and "beliebige Taste" are not in Scratch's file (the
    # Scratch editor has no such entries), they are the usual German names.
    "keys": {
        "en": {
            "any": ["any key"],
        },
        "de": {
            "space": ["Leertaste"],
            "left arrow": ["Pfeil nach links"],
            "right arrow": ["Pfeil nach rechts"],
            "up arrow": ["Pfeil nach oben"],
            "down arrow": ["Pfeil nach unten"],
            "any": ["beliebiges", "beliebige", "beliebige Taste"],
            "enter": ["Eingabetaste"],
        },
        # Scratch LT: EVENT_WHENKEYPRESSED_SPACE "tarpą", _LEFT "<--", _RIGHT "-->",
        # _DOWN "⬇️", _UP "⬆️", _ANY "bet kurį". Not from Scratch: "tarpas",
        # the word forms of the arrows, "bet kuris", "bet kuris klavišas"
        # and "įvesties klavišas".
        "lt": {
            "space": ["tarpą", "tarpas"],
            "left arrow": ["<--", "rodyklė kairėn"],
            "right arrow": ["-->", "rodyklė dešinėn"],
            "up arrow": ["⬆️", "rodyklė aukštyn"],
            "down arrow": ["⬇️", "rodyklė žemyn"],
            "any": ["bet kurį", "bet kuris", "bet kuris klavišas"],
            "enter": ["įvesties klavišas"],
        },
    },

    # Functions of the "[abs] of ()" operator, canonical values are the
    # ones in the Scratch project files. Scratch DE: OPERATORS_MATHOP_*.
    # (sin, cos, tan, asin, acos, atan, ln, log are the same.)
    "math": {
        "en": {
            "e ^": ["e^"],
            "10 ^": ["10^"],
        },
        "de": {
            "abs": ["Betrag"],
            "floor": ["abrunden"],
            "ceiling": ["aufrunden"],
            "sqrt": ["Wurzel"],
        },
        # Scratch LT: OPERATORS_MATHOP_*.
        "lt": {
            "abs": ["teigiama reikšmė"],
            "floor": ["apvalinimas žemyn"],
            "ceiling": ["apvalinimas aukštyn"],
            "sqrt": ["kvadratinė šaknis"],
            "tan": ["tg"],
            "asin": ["arcsin"],
            "acos": ["arccos"],
            "atan": ["arctg"],
        },
    },

    # Positions in lists. Scratch DE: DATA_INDEX_ALL/_LAST/_RANDOM.
    # "any" is an English alias of "random" already in the core.
    "list_positions": {
        "en": {},
        "de": {
            "all": ["alles"],
            "last": ["letztes"],
            "random": ["zufälliges", "zufällig"],
        },
        # Scratch LT: DATA_INDEX_ALL/_LAST/_RANDOM.
        "lt": {
            "all": ["viskas"],
            "last": ["paskutinis"],
            "random": ["atsitiktinis"],
        },
    },

    # Special backdrops. Scratch DE: LOOKS_NEXTBACKDROP etc.
    "backdrops": {
        "en": {},
        "de": {
            "next backdrop": ["nächstes Bühnenbild"],
            "previous backdrop": ["vorheriges Bühnenbild"],
            "random backdrop": ["zufälliges Bühnenbild"],
        },
        # Scratch LT: LOOKS_NEXTBACKDROP etc. (the official text of the next
        # backdrop has two blanks, "kitas  fonas"; both spellings work).
        "lt": {
            "next backdrop": ["kitas fonas", "kitas  fonas"],
            "previous backdrop": ["ankstesnis fonas"],
            "random backdrop": ["atsitiktinis fonas"],
        },
    },

    # Special "sprites" in the dropdowns of motion, sensing and control
    # blocks. Scratch DE: *_POINTER, *_RANDOM, SENSING_TOUCHINGOBJECT_EDGE,
    # CONTROL_CREATECLONEOF_MYSELF, SENSING_OF_STAGE.
    # A sprite with such a name wins over the alias, see CoreStage._special.
    "sprites": {
        "en": {},
        "de": {
            "_mouse_": ["Mauszeiger"],
            "_random_": ["Zufallsposition", "Zufallsrichtung"],
            "_edge_": ["Rand"],
            "_myself_": ["mir selbst"],
            "_stage_": ["Bühne"],
        },
        # Scratch LT: *_POINTER (several cases), *_RANDOM,
        # SENSING_TOUCHINGOBJECT_EDGE, CONTROL_CREATECLONEOF_MYSELF,
        # SENSING_OF_STAGE. Not from Scratch: "kraštas" (nominative).
        "lt": {
            "_mouse_": ["pelės žymeklis", "pelės žymeklį", "pelės žymeklio"],
            "_random_": ["atsitiktinė pozicija", "atsitiktinę kryptį"],
            "_edge_": ["kraštą", "kraštas"],
            "_myself_": ["savęs"],
            "_stage_": ["Scena"],
        },
    },

    # Reporters that can be shown as a monitor, canonical values are the
    # ids in pystage.core._variables.REPORTERS. The English names are the
    # labels of the Scratch monitors, the German ones are the words of
    # Scratch DE (SENSING_OF_*, MOTION_*, SENSING_CURRENT_*, ...). "Lautstärke"
    # is the volume of sounds; Scratch DE uses it for the microphone too, so
    # that needs another name (not from Scratch).
    "reporters": {
        "en": {
            "motion_xposition": ["x position"],
            "motion_yposition": ["y position"],
            "motion_direction": ["direction"],
            "looks_costumenumbername:number": ["costume number"],
            "looks_costumenumbername:name": ["costume name"],
            "looks_backdropnumbername:number": ["backdrop number"],
            "looks_backdropnumbername:name": ["backdrop name"],
            "looks_size": ["size"],
            "sound_volume": ["volume"],
            "sensing_answer": ["answer"],
            "sensing_loudness": ["loudness"],
            "sensing_timer": ["timer"],
            "sensing_current:YEAR": ["year"],
            "sensing_current:MONTH": ["month"],
            "sensing_current:DATE": ["date"],
            "sensing_current:DAYOFWEEK": ["day of week"],
            "sensing_current:HOUR": ["hour"],
            "sensing_current:MINUTE": ["minute"],
            "sensing_current:SECOND": ["second"],
            "sensing_username": ["username"],
        },
        "de": {
            "motion_xposition": ["x-Position"],
            "motion_yposition": ["y-Position"],
            "motion_direction": ["Richtung"],
            "looks_costumenumbername:number": ["Kostümnummer", "Kostüm Nummer"],
            "looks_costumenumbername:name": ["Kostümname", "Kostüm Name"],
            "looks_backdropnumbername:number": ["Bühnenbildnummer", "Bühnenbild Nummer"],
            "looks_backdropnumbername:name": ["Bühnenbildname", "Bühnenbild Name"],
            "looks_size": ["Größe"],
            "sound_volume": ["Lautstärke"],
            "sensing_answer": ["Antwort"],
            "sensing_loudness": ["Mikrofon-Lautstärke"],
            "sensing_timer": ["Stoppuhr"],
            "sensing_current:YEAR": ["Jahr"],
            "sensing_current:MONTH": ["Monat"],
            "sensing_current:DATE": ["Datum"],
            "sensing_current:DAYOFWEEK": ["Wochentag"],
            "sensing_current:HOUR": ["Stunde"],
            "sensing_current:MINUTE": ["Minute"],
            "sensing_current:SECOND": ["Sekunde"],
            "sensing_username": ["Benutzername"],
        },
        # Scratch LT: the words of MOTION_*, LOOKS_*, SENSING_CURRENT_* ...
        # ("kaukė numeris" etc. are the blocks "kaukė [numeris]"). Scratch LT
        # uses "garsumas" for the volume and the microphone; the microphone
        # needs another name (not from Scratch). "x koordinatė" etc. are
        # SENSING_OF_*, the monitor words are the same reporters.
        "lt": {
            "motion_xposition": ["x vieta", "x koordinatė"],
            "motion_yposition": ["y vieta", "y koordinatė"],
            "motion_direction": ["kryptis"],
            "looks_costumenumbername:number": ["kaukė numeris", "kaukės nr."],
            "looks_costumenumbername:name": ["kaukė vardas", "kaukės pavadinimas"],
            "looks_backdropnumbername:number": ["fonas numeris", "fono nr."],
            "looks_backdropnumbername:name": ["fonas vardas", "fono pavadinimas"],
            "looks_size": ["dydis"],
            "sound_volume": ["garsumas", "garsas"],
            "sensing_answer": ["atsakas"],
            "sensing_loudness": ["mikrofono garsumas"],
            "sensing_timer": ["laikmatis"],
            "sensing_current:YEAR": ["metai"],
            "sensing_current:MONTH": ["mėnuo"],
            "sensing_current:DATE": ["mėn. diena"],
            "sensing_current:DAYOFWEEK": ["savaitės diena"],
            "sensing_current:HOUR": ["valanda"],
            "sensing_current:MINUTE": ["minutė"],
            "sensing_current:SECOND": ["sekundė"],
            "sensing_username": ["vartotojo vardas"],
        },
    },
}


def _build_lookup():
    lookup = {}
    for table, languages in ALIASES.items():
        entries = lookup[table] = {}
        for aliases in languages.values():
            for value, names in aliases.items():
                for name in names:
                    entries[name.casefold()] = value
    return lookup


_LOOKUP = _build_lookup()


def canonical(table, value):
    """The canonical value for a user value, e.g. ``"Leertaste"`` -> ``"space"``.

    Values that are no alias (including values that are not strings) are
    returned unchanged. The comparison ignores case and surrounding blanks.
    """
    if not isinstance(value, str):
        return value
    return _LOOKUP[table].get(value.strip().casefold(), value)


def canonical_key(key):
    """The canonical (lower case) name of a key, e.g. "Pfeil nach oben" -> "up arrow"."""
    key = str(key)
    if key == " ":
        return key
    return canonical("keys", key).strip().lower()


##
# Messages
#
# Parameters are inserted with str.format, so literal braces must be doubled.

MESSAGES = {
    "en": {
        "variable_missing": "The variable {name} does not exist.",
        "list_missing": "The list {name} does not exist.",
        "variable_exists": "The variable {name} already exists!",
        "list_exists": "The list {name} already exists!",
        "bad_key": "Bad key: {key}. Allowed are a-z, 0-9, space, enter, the arrow keys (e.g. 'left arrow') and any.",
        "operator_unsupported": "Operator {operator} not supported.",
        "sprite_unknown": "Sprite {sprite} unknown.",
        "effect_range": "Invalid value. Must be between 0 and 200.",
        "block_parameters": "Your code block '{name}' needs zero or one parameter. The parameter is usually called self.",
        "block_no_refresh": "Your code block '{name}' is set to no refresh. In this case, yield must not be used.",
        "block_not_def": "'{name}' must be a normal function defined with def.",
        "sound_unavailable": "WARNING: No sound available. ({error})",
        "sound_no_channel": "WARNING: No more free sound channels. Can't play '{name}'.",
        "sound_not_found": "WARNING: Sound '{name}' not found.",
        "sound_not_loaded": "WARNING: Sound '{name}' can't be loaded, try to convert it to wav or ogg format. ({error})",
        "svg_notice": "\nWARNING: SVG conversion is for convenience only\n"
                      "and might not work as expected. It is recommended\n"
                      "to manually convert to bitmap graphics (png or jpg).\n",
        "pygame_version": "pygame-ce version 2 or higher is required for PyStage.\n"
                          "Remove classic pygame and install pygame-ce:\n"
                          "pip uninstall pygame && pip install --upgrade pygame-ce",
        "error_in": "Error in {file}, line {line}",
        "monitor_length": "length {length}",
        "monitor_empty": "(empty)",
        "reporter_unknown": "Unknown reporter: {reporter}.",
        "reporter_unavailable": "The reporter {reporter} does not exist for this sprite or stage.",
        "stage_name": "Stage",
        "reporter:motion_xposition": "x position",
        "reporter:motion_yposition": "y position",
        "reporter:motion_direction": "direction",
        "reporter:looks_costumenumbername:number": "costume number",
        "reporter:looks_costumenumbername:name": "costume name",
        "reporter:looks_backdropnumbername:number": "backdrop number",
        "reporter:looks_backdropnumbername:name": "backdrop name",
        "reporter:looks_size": "size",
        "reporter:sound_volume": "volume",
        "reporter:sensing_answer": "answer",
        "reporter:sensing_loudness": "loudness",
        "reporter:sensing_timer": "timer",
        "reporter:sensing_current:YEAR": "year",
        "reporter:sensing_current:MONTH": "month",
        "reporter:sensing_current:DATE": "date",
        "reporter:sensing_current:DAYOFWEEK": "day of week",
        "reporter:sensing_current:HOUR": "hour",
        "reporter:sensing_current:MINUTE": "minute",
        "reporter:sensing_current:SECOND": "second",
        "reporter:sensing_username": "username",
    },
    "de": {
        "variable_missing": "Die Variable {name} gibt es nicht.",
        "list_missing": "Die Liste {name} gibt es nicht.",
        "variable_exists": "Die Variable {name} gibt es schon!",
        "list_exists": "Die Liste {name} gibt es schon!",
        "bad_key": "Ungültige Taste: {key}. Erlaubt sind a-z, 0-9, Leertaste, Eingabetaste, die Pfeiltasten (z. B. 'Pfeil nach links') und beliebige Taste.",
        "operator_unsupported": "Die Funktion {operator} wird nicht unterstützt.",
        "sprite_unknown": "Die Figur {sprite} ist unbekannt.",
        "effect_range": "Ungültiger Wert. Er muss zwischen 0 und 200 liegen.",
        "block_parameters": "Dein Codeblock '{name}' braucht keinen oder einen Parameter. Der Parameter heißt normalerweise self.",
        "block_no_refresh": "Dein Codeblock '{name}' ist auf \"ohne Bildschirmaktualisierung\" gesetzt. Dann darf yield nicht verwendet werden.",
        "block_not_def": "'{name}' muss eine normale, mit def definierte Funktion sein.",
        "sound_unavailable": "WARNUNG: Kein Ton verfügbar. ({error})",
        "sound_no_channel": "WARNUNG: Keine freien Tonkanäle mehr. '{name}' kann nicht gespielt werden.",
        "sound_not_found": "WARNUNG: Der Klang '{name}' wurde nicht gefunden.",
        "sound_not_loaded": "WARNUNG: Der Klang '{name}' kann nicht geladen werden, versuche ihn in das wav- oder ogg-Format umzuwandeln. ({error})",
        "svg_notice": "\nWARNUNG: Die SVG-Umwandlung ist nur eine Hilfe\n"
                      "und funktioniert vielleicht nicht wie erwartet. Am besten\n"
                      "wandelst du die Grafik selbst in eine Bitmap-Grafik (png oder jpg) um.\n",
        "pygame_version": "Für PyStage wird pygame-ce ab Version 2 benötigt.\n"
                          "Entferne das klassische pygame und installiere pygame-ce:\n"
                          "pip uninstall pygame && pip install --upgrade pygame-ce",
        "error_in": "Fehler in {file}, Zeile {line}",
        "monitor_length": "Länge {length}",
        "monitor_empty": "(leer)",
        "reporter_unknown": "Unbekannter Wert: {reporter}.",
        "reporter_unavailable": "Den Wert {reporter} gibt es für diese Figur oder Bühne nicht.",
        "stage_name": "Bühne",
        "reporter:motion_xposition": "x-Position",
        "reporter:motion_yposition": "y-Position",
        "reporter:motion_direction": "Richtung",
        "reporter:looks_costumenumbername:number": "Kostüm Nummer",
        "reporter:looks_costumenumbername:name": "Kostüm Name",
        "reporter:looks_backdropnumbername:number": "Bühnenbild Nummer",
        "reporter:looks_backdropnumbername:name": "Bühnenbild Name",
        "reporter:looks_size": "Größe",
        "reporter:sound_volume": "Lautstärke",
        "reporter:sensing_answer": "Antwort",
        "reporter:sensing_loudness": "Lautstärke",
        "reporter:sensing_timer": "Stoppuhr",
        "reporter:sensing_current:YEAR": "Jahr",
        "reporter:sensing_current:MONTH": "Monat",
        "reporter:sensing_current:DATE": "Datum",
        "reporter:sensing_current:DAYOFWEEK": "Wochentag",
        "reporter:sensing_current:HOUR": "Stunde",
        "reporter:sensing_current:MINUTE": "Minute",
        "reporter:sensing_current:SECOND": "Sekunde",
        "reporter:sensing_username": "Benutzername",
    },
    # Lithuanian: official Scratch texts for monitor_length (gui.monitor.listMonitor.listLength),
    # monitor_empty, variable_exists (VARIABLE_ALREADY_EXISTS), list_exists
    # (LIST_ALREADY_EXISTS), stage_name and the reporter labels; the rest is
    # not from Scratch. "reporter:sensing_loudness" is "garsumas" like in Scratch.
    "lt": {
        "variable_missing": "Kintamojo {name} nėra.",
        "list_missing": "Sąrašo {name} nėra.",
        "variable_exists": "Kintamasis vardu \"{name}\" jau yra.",
        "list_exists": "Jau egzistuoja sąrašas pavadintas \"{name}\".",
        "bad_key": "Netinkamas klavišas: {key}. Leidžiami a-z, 0-9, tarpas, įvesties klavišas, rodyklių klavišai (pvz., 'rodyklė kairėn') ir bet kuris klavišas.",
        "operator_unsupported": "Funkcija {operator} nepalaikoma.",
        "sprite_unknown": "Veikėjas {sprite} nežinomas.",
        "effect_range": "Netinkama reikšmė. Ji turi būti nuo 0 iki 200.",
        "block_parameters": "Tavo kodo blokui '{name}' reikia nulio arba vieno parametro. Parametras paprastai vadinasi self.",
        "block_no_refresh": "Tavo kodo blokas '{name}' nustatytas be ekrano atnaujinimo. Tuomet negalima naudoti yield.",
        "block_not_def": "'{name}' turi būti paprasta funkcija, apibrėžta su def.",
        "sound_unavailable": "ĮSPĖJIMAS: Garso nėra. ({error})",
        "sound_no_channel": "ĮSPĖJIMAS: Nebėra laisvų garso kanalų. '{name}' negalima paleisti.",
        "sound_not_found": "ĮSPĖJIMAS: Garso '{name}' nerasta.",
        "sound_not_loaded": "ĮSPĖJIMAS: Garso '{name}' nepavyksta įkelti, pabandyk jį konvertuoti į wav arba ogg formatą. ({error})",
        "svg_notice": "\nĮSPĖJIMAS: SVG konvertavimas skirtas tik patogumui\n"
                      "ir gali veikti ne taip, kaip tikimasi. Geriausia\n"
                      "pačiam konvertuoti į rastrinę grafiką (png arba jpg).\n",
        "pygame_version": "PyStage reikalauja pygame-ce 2 ar naujesnės versijos.\n"
                          "Pašalink klasikinį pygame ir įdiek pygame-ce:\n"
                          "pip uninstall pygame && pip install --upgrade pygame-ce",
        "error_in": "Klaida faile {file}, eilutėje {line}",
        "monitor_length": "ilgis {length}",
        "monitor_empty": "(tuščia)",
        "reporter_unknown": "Nežinoma reikšmė: {reporter}.",
        "reporter_unavailable": "Reikšmės {reporter} šiam veikėjui ar scenai nėra.",
        "stage_name": "Scena",
        "reporter:motion_xposition": "x vieta",
        "reporter:motion_yposition": "y vieta",
        "reporter:motion_direction": "kryptis",
        "reporter:looks_costumenumbername:number": "kaukė numeris",
        "reporter:looks_costumenumbername:name": "kaukė vardas",
        "reporter:looks_backdropnumbername:number": "fonas numeris",
        "reporter:looks_backdropnumbername:name": "fonas vardas",
        "reporter:looks_size": "dydis",
        "reporter:sound_volume": "garsumas",
        "reporter:sensing_answer": "atsakas",
        "reporter:sensing_loudness": "garsumas",
        "reporter:sensing_timer": "laikmatis",
        "reporter:sensing_current:YEAR": "metai",
        "reporter:sensing_current:MONTH": "mėnuo",
        "reporter:sensing_current:DATE": "mėn. diena",
        "reporter:sensing_current:DAYOFWEEK": "savaitės diena",
        "reporter:sensing_current:HOUR": "valanda",
        "reporter:sensing_current:MINUTE": "minutė",
        "reporter:sensing_current:SECOND": "sekundė",
        "reporter:sensing_username": "vartotojo vardas",
    },
}


def tr(message_key, /, **params):
    """The message for message_key in the current language, with the parameters inserted.

    Falls back to English if the language has no text for the key.
    """
    text = MESSAGES[_language].get(message_key) or MESSAGES["en"][message_key]
    return text.format(**params) if params else text
