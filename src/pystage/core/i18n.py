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

Only the English alias tables and messages are defined in this file. Every
other language is a directory ``l10n/data/<lang>/`` with the tables
``messages.tsv`` and ``aliases.tsv`` that are loaded when this module is
imported; their ``origin`` column tells which strings are taken from Scratch's
own translation (scratch-l10n) and which are not. Messages and aliases that
are missing for a language fall back to English, so a translation can be
added step by step.

Adding a language
-----------------
Add the directory ``l10n/data/<lang>/`` with ``messages.tsv`` and
``aliases.tsv``. Nothing else needs to change (see TRANSLATING.md).
"""

import csv
import os

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

# Only the English aliases are defined here; the aliases of every other
# language are loaded from l10n/data/<lang>/aliases.tsv below.
ALIASES = {
    # Keys for when_key_pressed and key_pressed.
    "keys": {
        "en": {
            "any": ["any key"],
        },
    },

    # Functions of the "[abs] of ()" operator, canonical values are the
    # ones in the Scratch project files.
    "math": {
        "en": {
            "e ^": ["e^"],
            "10 ^": ["10^"],
        },
    },

    # Positions in lists. "any" is an English alias of "random" already in the core.
    "list_positions": {
        "en": {},
    },

    # Special backdrops.
    "backdrops": {
        "en": {},
    },

    # Special "sprites" in the dropdowns of motion, sensing and control
    # blocks.
    # A sprite with such a name wins over the alias, see CoreStage._special.
    "sprites": {
        "en": {},
    },

    # Reporters that can be shown as a monitor, canonical values are the
    # ids in pystage.core._variables.REPORTERS. The English names are the
    # labels of the Scratch monitors.
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
    },
}


##
# Translation tables
#
# Every language other than English lives in tab-separated tables in
# pystage/l10n/data/<lang>/ (see TRANSLATING.md). They are loaded here.

_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "l10n", "data")


def read_table(path):
    """Read a translation table as standard tab-separated text.

    Returns ``(header, rows)``; ``rows`` is a list of ``(line number, fields)``
    (the line number is where the row starts). ``\\n`` in texts is not yet resolved.
    The file is UTF-8 (with or without BOM), lines end with LF or CRLF, and
    fields may be quoted the way spreadsheets export them (``"..."`` with inner
    quotes doubled). The first line is the header, empty lines are skipped.
    Broken quoting never raises, the rows are returned as far as they can be read.
    """
    with open(path, encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f, delimiter="\t", quotechar='"')
        records = []
        start = 1
        try:
            for fields in reader:
                records.append((start, fields))
                start = reader.line_num + 1
        except csv.Error:
            pass
    if not records:
        return [], []
    header = records[0][1]
    rows = [(number, fields) for number, fields in records[1:] if any(c.strip() for c in fields)]
    return header, rows


def format_table(header, rows):
    """The canonical text of a table: LF, tab-separated, quotes only where needed.

    A field is quoted only if it starts with a quote or contains a tab or a line
    break, so that it reads back unchanged with :func:`read_table`.
    """
    def cell(field):
        if field.startswith('"') or any(c in field for c in "\t\r\n"):
            return '"' + field.replace('"', '""') + '"'
        return field

    return "".join("\t".join(cell(c) for c in fields) + "\n" for fields in [header] + [list(r) for r in rows])


def _load_table(path, columns):
    """Like read_table, but returns a list of dicts.

    Damaged rows (and files without the needed columns) are skipped, so that a
    wrong edit never makes pystage unimportable; ``python -m pystage.l10n.review
    check`` reports them.
    """
    header, rows = read_table(path)
    if not set(columns) <= set(header):
        return []
    return [dict(zip(header, fields)) for number, fields in rows if len(fields) == len(header)]


def _load_languages():
    if not os.path.isdir(_DATA_DIR):
        return
    for lang in sorted(os.listdir(_DATA_DIR)):
        folder = os.path.join(_DATA_DIR, lang)
        messages = os.path.join(folder, "messages.tsv")
        if os.path.isfile(messages):
            MESSAGES[lang] = {row["key"]: row["text"].replace("\\n", "\n") for row in _load_table(messages, ("key", "text"))}
        aliases = os.path.join(folder, "aliases.tsv")
        if os.path.isfile(aliases):
            for row in _load_table(aliases, ("table", "canonical", "alias")):
                if row["table"] not in ALIASES:
                    continue
                table = ALIASES[row["table"]].setdefault(lang, {})
                table.setdefault(row["canonical"], []).append(row["alias"])


def _build_lookup():
    lookup = {}
    for table, languages in ALIASES.items():
        entries = lookup[table] = {}
        for aliases in languages.values():
            for value, names in aliases.items():
                for name in names:
                    entries[name.casefold()] = value
    return lookup


_LOOKUP = None  # built after the messages are defined


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
}


_load_languages()
_LOOKUP = _build_lookup()


def tr(message_key, /, **params):
    """The message for message_key in the current language, with the parameters inserted.

    Falls back to English if the language has no text for the key.
    """
    text = MESSAGES[_language].get(message_key) or MESSAGES["en"][message_key]
    return text.format(**params) if params else text
