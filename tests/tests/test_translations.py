"""The translation tables must be consistent (see TRANSLATING.md)."""
import pytest

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
    lines[1] = lines[1].replace("\ttodo\t", "\tmaybe\t")
    lines[2] = lines[2].replace("\t", "\t\t", 1)
    path.write_text("\n".join(lines), encoding="utf-8")
    report = review.check("lt")
    text = "\n".join(report.errors)
    assert "line 2" in text and "status is 'maybe'" in text
    assert "line 3" in text and "columns" in text
