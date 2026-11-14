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

The German strings are taken from Scratch's own translation (scratch-l10n,
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
    },

    # Special backdrops. Scratch DE: LOOKS_NEXTBACKDROP etc.
    "backdrops": {
        "en": {},
        "de": {
            "next backdrop": ["nächstes Bühnenbild"],
            "previous backdrop": ["vorheriges Bühnenbild"],
            "random backdrop": ["zufälliges Bühnenbild"],
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
    },
}


def _build_lookup():
    lookup = {}
    for table, languages in ALIASES.items():
        entries = lookup[table] = {}
        for aliases in languages.values():
            for value, names in aliases.items():
                for name in names:
                    entries[name.lower()] = value
    return lookup


_LOOKUP = _build_lookup()


def canonical(table, value):
    """The canonical value for a user value, e.g. ``"Leertaste"`` -> ``"space"``.

    Values that are no alias (including values that are not strings) are
    returned unchanged. The comparison ignores case and surrounding blanks.
    """
    if not isinstance(value, str):
        return value
    return _LOOKUP[table].get(value.strip().lower(), value)


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
    },
}


def tr(message_key, /, **params):
    """The message for message_key in the current language, with the parameters inserted.

    Falls back to English if the language has no text for the key.
    """
    text = MESSAGES[_language].get(message_key) or MESSAGES["en"][message_key]
    return text.format(**params) if params else text
