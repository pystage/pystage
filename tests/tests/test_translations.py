"""The translation tables must be consistent (see TRANSLATING.md)."""
import os

import pytest

from pystage.core import i18n

from pystage.l10n import review


@pytest.mark.parametrize("lang", review.languages())
def test_tables_are_valid(lang):
    report = review.check(lang)
    assert not report.errors, "\n" + "\n".join(report.errors)


def test_languages_found():
    assert {"de", "lt"} <= set(review.languages())


def test_check_reports_damage(tmp_path, monkeypatch):
    # A table with a wrong column count and a bad status is reported with a line number.
    import shutil
    shutil.copytree(review.DATA_DIR, tmp_path / "data")
    monkeypatch.setattr(review, "DATA_DIR", str(tmp_path / "data"))
    path = tmp_path / "data" / "lt" / "messages.tsv"
    lines = path.read_text(encoding="utf-8").split("\n")
    lines[1] = lines[1].replace("\ttodo\t", "\tmaybe\t").replace("\tok\t", "\tmaybe\t")
    lines[2] = lines[2].replace("\t", "\t\t", 1)
    path.write_text("\n".join(lines), encoding="utf-8")
    report = review.check("lt")
    text = "\n".join(report.errors)
    assert "line 2" in text and "status is 'maybe'" in text
    assert "line 3" in text and "columns" in text


FIXTURE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "src", "translations", "messages.spreadsheet.tsv")


@pytest.mark.parametrize("lang", review.languages())
def test_repository_files_are_canonical(lang):
    for table in review.TABLES:
        path = os.path.join(review.DATA_DIR, lang, table + ".tsv")
        header, rows = i18n.read_table(path)
        with open(path, "rb") as f:
            assert f.read() == i18n.format_table(header, [r for n, r in rows]).encode("utf-8"), path


def test_spreadsheet_export_is_read():
    # CRLF, quoted fields with doubled quotes (as exported by spreadsheets)
    header, rows = i18n.read_table(FIXTURE)
    assert header[0] == "key"
    assert [r[0] for n, r in rows] == ["variable_exists", "sprite_unknown"]
    assert rows[0][1][2] == 'Kintamasis vardu "{name}" jau yra.'
    assert rows[0][1][5] == '"quoted" start'
    assert rows[1][1][2] == "Žinomas {sprite}\\nantra"
    assert rows[1][0] == 3


def test_bom_and_lf(tmp_path):
    path = tmp_path / "t.tsv"
    path.write_bytes("\ufeffa\tb\nx\ty\n\nz\t\"q\"\n".encode("utf-8"))
    assert i18n.read_table(str(path)) == (["a", "b"], [(2, ["x", "y"]), (4, ["z", "q"])])


def test_format_roundtrip(tmp_path):
    rows = [['"start', "mid\"dle", "plain"], ["a\tb", "c\nd", ""]]
    text = i18n.format_table(["a", "b", "c"], rows)
    assert text.startswith("a\tb\tc\n") and "\r" not in text
    path = tmp_path / "t.tsv"
    path.write_text(text, encoding="utf-8", newline="")
    assert i18n.read_table(str(path))[1] == [(2, rows[0]), (3, rows[1])]


def test_check_flags_spreadsheet_export(tmp_path, monkeypatch):
    import shutil
    shutil.copytree(review.DATA_DIR, tmp_path / "data")
    monkeypatch.setattr(review, "DATA_DIR", str(tmp_path / "data"))
    path = tmp_path / "data" / "lt" / "messages.tsv"
    text = path.read_text(encoding="utf-8")
    path.write_text(text.replace("\n", "\r\n"), encoding="utf-8", newline="")
    report = review.check("lt")
    assert not report.errors
    assert any("normalize" in w for w in report.warnings)
    # a text that is still double-quoted is an error
    header, rows = i18n.read_table(str(path))
    rows[0][1][2] = '"' + rows[0][1][2] + '"'
    path.write_text(i18n.format_table(header, [r for n, r in rows]), encoding="utf-8", newline="")
    assert any("double-quoted" in e for e in review.check("lt").errors)
    # normalize fixes the format and is then a no-op
    path.write_text(text.replace("\n", "\r\n"), encoding="utf-8", newline="")
    assert review.normalize("lt") == [str(path)]
    assert path.read_bytes().decode("utf-8") == text
    assert review.normalize("lt") == []
