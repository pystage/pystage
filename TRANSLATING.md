# Translating PyStage

PyStage can be used in several languages (English, German, Lithuanian, ...). This page is for

- **language maintainers** who review and correct a translation (you do not need to be a programmer), and
- **project maintainers** who merge their work or add a new language.

The most important rule: **follow Scratch's official translation, and English is authoritative.**
Names of blocks in PyStage should be the words that kids see in the Scratch editor in their language.
Only where Scratch has no suitable text (or the same text for two different blocks), we use our own wording.
If the English text changes, the translations have to be checked again.

## For language maintainers

### Try your language

Install the current pre-release (this is how you get the newest translations before the official release):

```
pip install --pre pystage
```

or a specific version, e.g. `pip install pystage==0.3.0a1`. Then try a small program, here with the Lithuanian API:

```python
from pystage.lt import Scena, Veikėjas

scena = Scena()
katinas = scena.pridėk_veikėją()

def sveikink(katinas: Veikėjas):
    katinas.sakyk_sek("Labas!", 2)
    katinas.eik(50)

katinas.kai_spusteli_žalią_vėliavėlę(sveikink)
scena.paleisk()
```

Does it read well? Are the names what you would expect from the Scratch blocks? Then continue below.

### The three tables

Everything that is translated is in tab-separated text files in `src/pystage/l10n/data/<language>/`
(e.g. `src/pystage/l10n/data/lt/`). One line is one record, the first line contains the column names.

| File | What is in it |
|---|---|
| `messages.tsv` | Messages that are shown while a program runs: error messages, warnings, labels of the monitors on the stage. |
| `aliases.tsv` | Words that can be used as values in your language: key names (`space`), dropdown entries (`_mouse_`, `next backdrop`), names of reporters. One line per accepted word. |
| `api.tsv` | The names of all blocks (methods) of the sprite and the stage in your language. |

The last three columns are the same in all tables:

- **origin** tells where the text comes from:
  - `scratch`: taken word by word from Scratch's official translation,
  - `adapted`: based on Scratch, but changed (for example because the Scratch text would be the same for two blocks, or because it contains an icon or a gap),
  - `new`: Scratch has no text for this.
- **status**: `todo` means that the line still needs a review, `ok` means a language expert has checked it.
  When you have reviewed a line, set it to `ok`.
- **comment**: free text. Use it to explain a change, to ask a question or to answer the question of someone else.

The other columns:

- `messages.tsv`: `key` (identifies the message, never change it), `english` (the current English text, only for your reference, do not change it), `text` (**the translation**). Words in curly braces like `{name}` are replaced by a value while the program runs: keep them exactly as they are. In texts with several lines, `\n` means a line break; keep it.
- `aliases.tsv`: `table` and `canonical` (what the word means internally, never change them), `alias` (**the word in your language**). To add another accepted word, add a new line with the same `table` and `canonical`.
- `api.tsv`: `class` (sprite or stage), `core_method` (internal name, never change it), `english` (name in the English API, reference only), `name` (**the name in your language**), `scratch` (what the block says in the official Scratch translation, for comparison; empty if Scratch has no such block). Names can only contain letters, digits and underscores, no blanks, and every name must be unique within the sprite or the stage. Use the underscore where a Scratch block has a blank.

So you normally change **`text`, `alias` or `name`, plus `status` and `comment`**. Please do not add or remove lines (ask in a comment or an issue if something is missing), and do not use tabs or line breaks inside a cell.

### Editing on GitHub (no installation needed)

1. Open the file on GitHub, e.g. `src/pystage/l10n/data/lt/messages.tsv`. GitHub shows it as a table.
2. Click the pencil icon (*Edit this file*). In the editor, the cells are separated by tabs; change the text of the cell you want to change and take care that the tabs stay.
3. Click *Commit changes...*, choose *Create a new branch for this commit and start a pull request*, and write a short description of what you changed.
4. Open the pull request. The automatic check tells you if something is wrong (for example a lost tab or a changed placeholder); the message names the file and the line. You can fix it by editing the file again on the same branch.

### Editing in a spreadsheet

You can also download a file and edit it in LibreOffice Calc, Excel or Google Sheets (File - Import).
Open it as **UTF-8** text with **tab** as the only separator, and with **no text delimiter (no quotes)**; set all columns to *text* so that nothing is converted.
When saving, use the same settings again: *text CSV*, UTF-8, separator tab, no quotes (in LibreOffice: untick *Quote all text cells*; in Google Sheets: *Download - Tab-separated values (.tsv)*).
Then upload the file via a pull request (*Add file - Upload files* on GitHub), or send it to the maintainer.
Check that the file still has the same number of lines and columns and that Lithuanian, German, ... letters look right.

### What to write in `comment`

- Why a text differs from Scratch's, so that the next reviewer understands it.
- Open questions ("Is this the word you use at school?").
- Answers to such questions. Please do not delete comments of others.

### Docstrings (the help texts)

Every method also has a help text (docstring) in your language, in `src/pystage/<language>/sprite.py` and `stage.py`
(for example `src/pystage/lt/sprite.py`). They are the text the users see in their editor and in the documentation.
You can edit these files on GitHub in the same way (pencil icon). Only change the text between the `"""` marks and leave the code
(everything with `def` and `return`) alone. If you prefer, write your remarks as comments in the review issue of your language, and the maintainer will include them.
If you change a method *name* in `api.tsv`, you do not have to change the Python file; the maintainer does that with a tool (see below).

## Naming rules for method names

The method names in the tables follow these rules. The `comment` column of `api.tsv` refers to these rules as "naming rule N" (for example "naming rule 2").

1. Start from the official Scratch block text in your language: remove the input slots, write in lower case, replace spaces, hyphens and slashes by `_`, drop punctuation. Keep letters with diacritics (they are valid Python names). Keep Scratch's word order and verb form.
2. Blocks with a dropdown are split into one method per dropdown value; the official dropdown text is inserted where it appears in the block (e.g. `sukurk_savęs_kloną`).
3. Abbreviations are written consistently (e.g. seconds: `sek`), and numbers are kept (`dienų_skaičius_nuo_2000`).
4. If the Scratch text cannot become a name (e.g. Lithuanian Scratch writes "set" blocks as equations like `x = %1`), use a verb pattern that Scratch itself uses in your language (Lithuanian: `nustatyk_x_į`).
5. Names must be unique within the sprite and within the stage. If the Scratch text is too short or the same for two blocks, add the smallest word that tells them apart (e.g. `slėpk` vs `slėpk_kintamąjį`).
6. Blocks without words in Scratch (operators like `+`, `>`, the green flag icon) get a short, natural name.
7. PyStage methods that are not Scratch blocks (adding costumes, monitors, …) get names built from Scratch's vocabulary in your language, as imperative verbs.

## For project maintainers

### Checking a pull request

```
python -m pystage.l10n.review check <lang>     # or "all"
python -m pystage.l10n.review todo <lang>      # the rows that are still todo, grouped by table
python -m pystage.l10n.review apply <lang>     # renames the methods in src/pystage/<lang>/sprite.py and stage.py to the names in api.tsv
python -m pytest
```

`check` validates the tables: the number of columns, valid `origin` and `status` values, unknown or duplicate keys, placeholders identical to English,
the `english` columns against the current English texts (if English changed, you get "English changed, translation may be outdated"), method names that are valid and unique, and
that `api.tsv` agrees with the methods in the facade code. It also checks that an alias does not mean different things in different languages.
It prints the file and line of every problem and exits with code 1 if there are any. The test suite runs the same check for every language (`tests/tests/test_translations.py`), so a broken edit fails the CI.

When a reviewer has changed a `name` in `api.tsv`, `check` reports that the code still uses the old name. Run `apply` to rename the methods
(only the `def` name is changed, each rename is reported), then run `check` and the tests again. Remember that other code, examples and the documentation may use the old names.
Messages and aliases need no `apply`: they are loaded from the tables when pystage is imported.
If the English text or method name changes, update the `english` column of all languages (the check lists them) and set the status of the affected lines to `todo`.

Then merge. Commits in the language pull requests should only touch the files of the language. The data files are part of the package (`setup.cfg`, `package_data`).

### Adding a new language

1. Generate the facade from Scratch's translation: `python -m pystage.l10n -a -l xx` (needs network), and write the output into `src/pystage/xx/sprite.py` and `stage.py` with an `__init__.py`
   that exports `sprite_class` and `stage_class` (copy `src/pystage/lt/`). Translate the stage constructor and `__init__` signature, and the docstrings.
   Every method must remain a direct `self._core.<name>(...)` call.
2. Create `src/pystage/l10n/data/xx/` with `messages.tsv`, `aliases.tsv` and `api.tsv`. Use the German or Lithuanian files as a template (same columns, same keys).
   Set `origin` according to Scratch's translation (`scratch`, `adapted`, `new`) and `status` to `todo` for everything that nobody has reviewed. Missing messages and aliases fall back to English.
3. Run `python -m pystage.l10n.review check xx` until it is clean, and add tests like `tests/tests/test_lithuanian.py`.
4. Add the language to the documentation (`docs/source/languages.rst` and a `pystage.xx.rst` page) and, if the converter should produce this language, to the converter.
5. Add a language card on the website (`pystage.github.io`) and a line in the languages list of `README.md`.
6. Open a review issue for the language, so that the maintainer can discuss docstrings and open questions, and point the maintainer to this page.

### Pre-releases

Set the version in `setup.cfg` (e.g. `0.3.0a1`), `python -m build`, `twine check dist/*`, test in a clean virtual environment, and upload with `python -m twine upload dist/pystage-0.3.0a1*`.
`pip install --pre pystage` finds pre-releases, a plain `pip install pystage` does not.
