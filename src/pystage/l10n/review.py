"""Tools for the review of translations.

The translations of a language live in tab-separated tables in
``pystage/l10n/data/<lang>/`` (see TRANSLATING.md in the repository)::

    python -m pystage.l10n.review check <lang>   # find mistakes in the tables
    python -m pystage.l10n.review apply <lang>   # rename facade methods to the names in api.tsv
    python -m pystage.l10n.review todo <lang>    # list the rows that still need a review
    python -m pystage.l10n.review normalize <lang>   # rewrite the tables in canonical form

``<lang>`` is a language code like ``de`` or ``lt``; ``check`` and ``todo``
also accept ``all``, ``normalize`` as well. English is the authoritative source: the ``english``
columns are compared with the current English texts and method names.
"""

import argparse
import importlib
import inspect
import keyword
import os
import re
import sys

from pystage.core import i18n
from pystage.l10n.api import _get_core_names

DATA_DIR = i18n._DATA_DIR
ORIGINS = ("scratch", "adapted", "new")
STATUSES = ("todo", "ok")
CLASSES = ("sprite", "stage")

TABLES = {
    "messages": ["key", "english", "text", "origin", "status", "comment"],
    "aliases": ["table", "canonical", "alias", "origin", "status", "comment"],
    "api": ["class", "core_method", "english", "name", "scratch", "origin", "status", "comment"],
}

_PLACEHOLDER = re.compile(r"\{([^{}]*)\}")


def languages():
    """The language codes that have a data directory."""
    if not os.path.isdir(DATA_DIR):
        return []
    return sorted(d for d in os.listdir(DATA_DIR) if os.path.isdir(os.path.join(DATA_DIR, d)))


def _shown(path):
    """A path as short as possible for messages."""
    rel = os.path.relpath(path)
    return path if rel.startswith("..") else rel


class Report:
    """Collects the problems found in the tables."""

    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, path, line, text):
        self.errors.append(f"{_shown(path)}" + (f", line {line}" if line else "") + f": {text}")

    def warn(self, path, line, text):
        self.warnings.append(f"{_shown(path)}" + (f", line {line}" if line else "") + f": {text}")


def _read(lang, table, report):
    """Read a table; returns a list of (line number, dict) with well-formed rows only."""
    path = os.path.join(DATA_DIR, lang, table + ".tsv")
    if not os.path.isfile(path):
        report.error(path, None, "this file is missing.")
        return path, []
    try:
        header, rows = i18n.read_table(path)
    except UnicodeDecodeError:
        report.error(path, None, "the file is not saved as UTF-8. Please save it again as UTF-8 text.")
        return path, []
    _check_format(path, report)
    expected = TABLES[table]
    if header != expected:
        report.error(path, 1, "the first line must be the column names: " + " <TAB> ".join(expected)
                     + ". Do not rename, remove or reorder columns.")
        return path, []
    result = []
    for number, fields in rows:
        if len(fields) != len(expected):
            report.error(path, number, f"this line has {len(fields)} columns, but there must be {len(expected)}. "
                         "Check for a missing or an extra tab, and do not put line breaks or tabs inside a cell.")
            continue
        result.append((number, dict(zip(expected, fields))))
    return path, result


def _check_format(path, report):
    """Warn if the file is not in canonical form (a spreadsheet may have saved it)."""
    try:
        with open(path, "rb") as f:
            raw = f.read()
        header, rows = i18n.read_table(path)
    except (OSError, UnicodeDecodeError):
        return
    if raw != i18n.format_table(header, [fields for number, fields in rows]).encode("utf-8"):
        report.warn(path, None, "the file is not in the canonical form (BOM, CRLF line endings, quotes or empty "
                    "lines). Saved by a spreadsheet? Run 'python -m pystage.l10n.review normalize <lang>'.")


def _check_quotes(path, number, text, column, report):
    """Quotes around a whole text or doubled quotes are almost always an export artefact."""
    if (len(text) > 1 and text.startswith('"') and text.endswith('"')) or '""' in text:
        report.error(path, number, f"the {column} '{text}' looks double-quoted. This is probably an artefact of "
                     "the spreadsheet export; run 'python -m pystage.l10n.review normalize <lang>' and "
                     "check the text.")


def normalize(lang):
    """Rewrite the tables of a language in canonical form. Returns the paths that changed."""
    changed = []
    for table in TABLES:
        path = os.path.join(DATA_DIR, lang, table + ".tsv")
        if not os.path.isfile(path):
            continue
        with open(path, "rb") as f:
            raw = f.read()
        header, rows = i18n.read_table(path)
        new = i18n.format_table(header, [fields for number, fields in rows]).encode("utf-8")
        if new != raw:
            with open(path, "wb") as f:
                f.write(new)
            changed.append(path)
    return changed


def _check_common(path, number, row, report):
    if row["origin"] not in ORIGINS:
        report.error(path, number, f"origin is '{row['origin']}', but must be one of: {', '.join(ORIGINS)}.")
    if row["status"] not in STATUSES:
        report.error(path, number, f"status is '{row['status']}', but must be one of: {', '.join(STATUSES)}.")


def _placeholders(text):
    return sorted(_PLACEHOLDER.findall(text.replace("{{", "").replace("}}", "")))


def check_messages(lang, report):
    path, rows = _read(lang, "messages", report)
    english = i18n.MESSAGES["en"]
    seen = {}
    for number, row in rows:
        key = row["key"]
        _check_common(path, number, row, report)
        if key not in english:
            report.error(path, number, f"the key '{key}' does not exist. Keys must not be changed or added.")
            continue
        if key in seen:
            report.error(path, number, f"the key '{key}' appears twice (first in line {seen[key]}).")
            continue
        seen[key] = number
        current = english[key].replace("\n", "\\n")
        if row["english"] != current:
            report.error(path, number, f"English changed, translation may be outdated. The table has "
                         f"'{row['english']}', the current English text is '{current}'. Check the translation, "
                         "then copy the new English text into the english column.")
        _check_quotes(path, number, row["text"], "text", report)
        text = row["text"].replace("\\n", "\n")
        if not text.strip():
            report.error(path, number, "the text is empty.")
            continue
        if _placeholders(text) != _placeholders(english[key]):
            report.error(path, number, "the placeholders in curly braces must be exactly the same as in English "
                         f"({', '.join('{' + p + '}' for p in _placeholders(english[key])) or 'none'}). "
                         "They are replaced by values while the program runs; do not translate them.")
        else:
            try:
                text.format(**{p: "" for p in _placeholders(text)})
            except (ValueError, IndexError, KeyError):
                report.error(path, number, "curly braces are not used correctly; a literal brace must be doubled.")
    missing = sorted(set(english) - set(seen))
    if missing:
        report.warn(path, None, "not translated yet (English is used instead): " + ", ".join(missing))


def check_aliases(lang, report):
    path, rows = _read(lang, "aliases", report)
    seen = {}
    for number, row in rows:
        _check_common(path, number, row, report)
        table, canonical, alias = row["table"], row["canonical"], row["alias"]
        if table not in i18n.ALIASES:
            report.error(path, number, f"the table '{table}' does not exist. Known tables: "
                         f"{', '.join(sorted(i18n.ALIASES))}.")
            continue
        if not canonical.strip() or not alias.strip():
            report.error(path, number, "canonical and alias must not be empty.")
            continue
        _check_quotes(path, number, alias, "alias", report)
        if alias != alias.strip():
            report.error(path, number, f"the alias '{alias}' starts or ends with a blank.")
        folded = (table, alias.strip().casefold())
        if folded in seen:
            report.error(path, number, f"the alias '{alias}' is already used in line {seen[folded][0]}.")
            continue
        seen[folded] = (number, canonical)
    # canonical values must be known (from the English table or another language)
    known = {}
    for tbl, langs in i18n.ALIASES.items():
        for other, entries in langs.items():
            if other != lang:
                known.setdefault(tbl, set()).update(entries)
    # collisions with the other languages
    for other in languages() + ["en"]:
        if other == lang:
            continue
        for tbl, langs in i18n.ALIASES.items():
            for canonical, names in langs.get(other, {}).items():
                for name in names:
                    mine = seen.get((tbl, name.strip().casefold()))
                    if mine and mine[1] != canonical:
                        report.error(path, mine[0], f"the alias '{name}' means '{mine[1]}' here, but '{canonical}' "
                                     f"in the language '{other}'. An alias must mean the same in all languages.")


def _facade(lang):
    module = importlib.import_module(f"pystage.{lang}")
    return {"sprite": module.sprite_class, "stage": module.stage_class}


def facade_files(lang):
    return {kind: inspect.getsourcefile(cls) for kind, cls in _facade(lang).items()}


def check_api(lang, report):
    path, rows = _read(lang, "api", report)
    try:
        mine = _facade(lang)
    except ImportError:
        report.error(path, None, f"there is no Python package pystage.{lang} for this language.")
        return
    english = _facade("en")
    mapping = {kind: _get_core_names(cls) for kind, cls in mine.items()}  # name -> core
    to_name = {kind: {core: name for name, core in names.items()} for kind, names in mapping.items()}
    to_english = {kind: {core: name for name, core in _get_core_names(cls).items()}
                  for kind, cls in english.items()}
    seen = {}
    names_used = {kind: {} for kind in CLASSES}
    for number, row in rows:
        _check_common(path, number, row, report)
        kind, core, name = row["class"], row["core_method"], row["name"]
        if kind not in CLASSES:
            report.error(path, number, f"class is '{kind}', but must be sprite or stage.")
            continue
        if core not in to_english[kind]:
            report.error(path, number, f"the core method '{core}' does not exist for {kind}. "
                         "Do not change this column.")
            continue
        if (kind, core) in seen:
            report.error(path, number, f"'{core}' appears twice (first in line {seen[(kind, core)]}).")
            continue
        seen[(kind, core)] = number
        if row["english"] != to_english[kind][core]:
            report.error(path, number, f"English changed, translation may be outdated. The table has "
                         f"'{row['english']}', the English method is now '{to_english[kind][core]}'. "
                         "Check the translation, then copy the new English name into the english column.")
        if not name.isidentifier() or keyword.iskeyword(name):
            report.error(path, number, f"'{name}' cannot be used as a method name. Use only letters, digits and "
                         "underscores, no blanks, and do not start with a digit.")
            continue
        if name in names_used[kind]:
            report.error(path, number, f"the name '{name}' is already used in line {names_used[kind][name]}. "
                         "Every name must be unique.")
            continue
        names_used[kind][name] = number
        actual = to_name[kind].get(core)
        if actual != name:
            report.error(path, number, f"the table says '{name}', but the code calls this method '{actual}'. "
                         f"The maintainer must run 'python -m pystage.l10n.review apply {lang}' to change the code.")
    for kind in CLASSES:
        for core in sorted(to_name[kind]):
            if (kind, core) not in seen:
                report.error(path, None, f"the {kind} method '{to_name[kind][core]}' ({core}) has no row in the table.")


def check(lang):
    """Check all tables of a language, returns a Report."""
    report = Report()
    if lang not in languages():
        report.error(os.path.join(DATA_DIR, lang), None, f"there is no data directory for '{lang}'. "
                     f"Available: {', '.join(languages())}.")
        return report
    check_messages(lang, report)
    check_aliases(lang, report)
    check_api(lang, report)
    return report


def apply(lang):
    """Rename the facade methods to the names in api.tsv. Returns (renames, errors)."""
    report = Report()
    path, rows = _read(lang, "api", report)
    if report.errors:
        return [], report.errors
    files = facade_files(lang)
    classes = _facade(lang)
    renames = []
    errors = []
    for kind in CLASSES:
        mapping = _get_core_names(classes[kind])
        to_name = {core: name for name, core in mapping.items()}
        wanted = {}
        for number, row in rows:
            if row["class"] == kind and row["core_method"] in to_name and row["name"] != to_name[row["core_method"]]:
                new = row["name"]
                if not new.isidentifier() or keyword.iskeyword(new):
                    errors.append(f"{_shown(path)}, line {number}: '{new}' cannot be used as a method name.")
                else:
                    wanted[to_name[row["core_method"]]] = (new, number)
        if not wanted:
            continue
        final = [wanted[n][0] if n in wanted else n for n in mapping]
        for new in set(final):
            if final.count(new) > 1:
                errors.append(f"{_shown(path)}: the name '{new}' would be used twice in the {kind} class.")
        existing = set(dir(classes[kind])) - set(mapping)
        for old, (new, number) in wanted.items():
            if new in existing:
                errors.append(f"{_shown(path)}, line {number}: '{new}' is already a different member of the {kind} class.")
        if errors:
            continue
        source = open(files[kind], encoding="utf-8").read()
        for old, (new, number) in wanted.items():
            pattern = re.compile(rf"^(\s+def ){re.escape(old)}(\s*\()", re.M)
            if len(pattern.findall(source)) != 1:
                errors.append(f"{_shown(files[kind])}: could not find the definition of '{old}'.")
        if errors:
            continue
        pattern = re.compile(r"^(\s+def )(\w+)(\s*\()", re.M)

        def sub(match):
            name = match.group(2)
            return match.group(1) + (wanted[name][0] if name in wanted else name) + match.group(3)

        with open(files[kind], "w", encoding="utf-8", newline="") as f:
            f.write(pattern.sub(sub, source))
        for old, (new, number) in wanted.items():
            renames.append(f"{_shown(files[kind])}: {old} -> {new}")
    return renames, errors


def todo(lang):
    """The open rows of a language as text lines."""
    report = Report()
    out = []
    shown = {"messages": ("key", "text"), "aliases": ("table", "canonical", "alias"),
             "api": ("class", "core_method", "name")}
    for table in TABLES:
        path, rows = _read(lang, table, report)
        open_rows = [(n, r) for n, r in rows if r["status"] == "todo"]
        out.append(f"{table}.tsv: {len(open_rows)} open")
        for number, row in open_rows:
            cells = [row[c] for c in shown[table]]
            line = f"  line {number}: " + "  |  ".join(cells) + f"  [{row['origin']}]"
            if row["comment"]:
                line += f"  -- {row['comment']}"
            out.append(line)
        out.append("")
    return out + [f"Problems while reading: {e}" for e in report.errors]


def main(argv=None):
    parser = argparse.ArgumentParser(prog="python -m pystage.l10n.review", description=__doc__.split("\n\n")[0])
    sub = parser.add_subparsers(dest="command", required=True)
    for name, text in (("check", "check the tables of a language (or 'all')"),
                       ("apply", "rename the facade methods to the names in api.tsv"),
                       ("todo", "list the rows that still need a review"),
                       ("normalize", "rewrite the tables in canonical form")):
        p = sub.add_parser(name, help=text)
        p.add_argument("lang", help="language code, e.g. de or lt" + ("" if name == "apply" else ", or 'all'"))
    args = parser.parse_args(argv)
    langs = languages() if args.lang == "all" and args.command != "apply" else [args.lang]
    status = 0
    if args.command == "normalize":
        for lang in langs:
            changed = normalize(lang)
            for path in changed:
                print("Rewrote " + _shown(path))
            if not changed:
                print(f"{lang}: nothing to change, the tables are already in canonical form.")
        return 0
    if args.command == "check":
        for lang in langs:
            report = check(lang)
            for text in report.warnings:
                print("Note: " + text)
            for text in report.errors:
                print("Error: " + text)
            if report.errors:
                print(f"{lang}: {len(report.errors)} problem(s) found.")
                status = 1
            else:
                print(f"{lang}: the tables are fine.")
    elif args.command == "apply":
        renames, errors = apply(args.lang)
        for text in renames:
            print("Renamed " + text)
        for text in errors:
            print("Error: " + text)
        if errors:
            status = 1
        elif not renames:
            print("Nothing to do, the code already uses the names of the table.")
    else:
        for lang in langs:
            print(f"== {lang} ==")
            print("\n".join(todo(lang)))
    return status


if __name__ == "__main__":
    sys.exit(main())
