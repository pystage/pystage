"""The converter reports what it could not convert."""
import ast
import json
import zipfile
from pathlib import Path

import pytest

from pystage.convert import sb3

from .. import make_projects
from .test_convert_untrusted import EVIL, assert_harmless, block, convert, make_sb3, project
from .test_convert_blocks import say_blocks, number_input

SPECIAL = make_projects.BASE / "special_projects" / "unsupported.sb3"


def intermediate(path_or_data, tmp_path=None):
    if isinstance(path_or_data, dict):
        path_or_data = make_sb3(tmp_path, path_or_data)
    return sb3.get_intermediate(sb3.get_sb3_data(path_or_data), sb3.to_filename(Path(path_or_data).stem))


def messages(project_, kind=None):
    return [w["message"] for w in project_["warnings"] if kind is None or w["kind"] == kind]


def by_target(project_, kind):
    return {w["target"]: w["message"] for w in project_["warnings"] if w["kind"] == kind}


def test_special_project_is_up_to_date():
    # make_projects.py writes the same project again
    assert SPECIAL.exists()
    expected = make_projects.unsupported_project().data()
    with zipfile.ZipFile(SPECIAL) as archive:
        assert json.loads(archive.read("project.json")) == json.loads(json.dumps(expected))


def test_every_kind_of_problem_is_reported():
    project_ = intermediate(SPECIAL)
    sb3.get_python(project_, "en")
    warnings = project_["warnings"]
    assert all(set(w) == {"kind", "target", "message"} for w in warnings)
    assert {w["kind"] for w in warnings} == {"opcode", "hat", "loose_script", "monitor", "comment", "extension", "asset", "cloud"}
    # The blocks that are not supported get known when the code is written
    assert "opcode" not in {w["kind"] for w in intermediate(SPECIAL)["warnings"]}
    assert [m for m in messages(project_, "cloud")] == ["Cloud variable 'cloudy' is a normal variable, it is not stored online."]
    assert by_target(project_, "cloud") == {"Stage": messages(project_, "cloud")[0]}
    assert messages(project_, "extension") == ["The extension 'music' is not supported."]
    assert "event_whentouchingobject" in by_target(project_, "hat")["Sprite1"] and "2 scripts" in by_target(project_, "hat")["Sprite1"]
    assert by_target(project_, "loose_script").keys() == {"Sprite1", "Sprite2"}
    assert by_target(project_, "loose_script")["Sprite1"].startswith("2 script(s)")
    assert by_target(project_, "loose_script")["Sprite2"].startswith("1 script(s)")
    assert by_target(project_, "comment") == {"Sprite2": "1 comment(s) belong to blocks that were left out."}
    monitors = " ".join(messages(project_, "monitor"))
    assert "sensing_timer" in monitors and "sensing_answer" in monitors and "motion_xposition" in monitors
    assert "slider of variable 'plain'" in monitors
    assert "sensing_username" not in monitors, "hidden monitors are not a problem"
    assert any("photo" in m and "webp" in m for m in messages(project_, "asset"))


def test_unsupported_blocks_are_counted_when_the_code_is_written():
    project_ = intermediate(SPECIAL)
    code = sb3.get_python(project_, "en")
    opcodes = {(w["target"], w["message"]) for w in project_["warnings"] if w["kind"] == "opcode"}
    assert ("Sprite1", "Block 'sensing_loud' is not supported, it was replaced by a text (2 times).") in opcodes
    assert ("Stage", "Block 'sensing_loud' is not supported, it was replaced by a text.") in opcodes
    assert any("music_playDrumForBeats" in m and "extension 'music'" in m for _, m in opcodes)
    assert any("control_while" in m for _, m in opcodes)
    assert code.count("NOT SUPPORTED: sensing_loud") == 3


def test_warnings_are_written_as_comments_at_the_top():
    project_ = intermediate(SPECIAL)
    code = sb3.get_python(project_, "en")
    lines = code.splitlines()
    assert lines[0] == "# unsupported (pyStage, converted from Scratch 3)"
    assert lines[1] == "#"
    assert lines[2] == "# Not everything of the Scratch project could be converted:"
    comments = [line for line in lines[3:] if line.startswith("# - ")]
    assert len(comments) == len(project_["warnings"])
    assert all(line.startswith("#") for line in lines[:3 + len(comments)])
    assert lines[3 + len(comments)] == "" and lines[4 + len(comments)].startswith("from pystage.en import")
    assert "# - [hat] Sprite1: Scripts with the hat block 'event_whentouchingobject'" in code
    ast.parse(code)
    # With a link, the warnings come after the header lines
    code = sb3.get_python(project_, "en", project_link="https://example.org/1")
    assert code.splitlines()[0].startswith("# Online Converter, URL:") and code.splitlines()[2] == "#"


def test_no_warnings_no_comment_block(tmp_path):
    code = convert(tmp_path, project(blocks=say_blocks("operator_divide", number_input(1), number_input(2))))
    assert "Not everything" not in code
    assert code.startswith("# test (pyStage, converted from Scratch 3)\n\nfrom pystage.en import")


def test_warnings_belong_to_one_conversion(tmp_path):
    first = intermediate(SPECIAL)
    for language in ("core", "en", "de"):
        sb3.get_python(first, language)
    count = len(first["warnings"])
    assert count > 10
    sb3.get_python(first, "en")
    assert len(first["warnings"]) == count, "converting again does not add the same warnings again"
    second = intermediate(project(), tmp_path)
    assert second["warnings"] == []
    sb3.get_python(second, "en")
    assert second["warnings"] == []
    # and the first project is not touched by the second
    assert len(first["warnings"]) == count


def test_unattached_comments_are_converted_and_loose_scripts_are_not(tmp_path):
    blocks = {
        "a": block("event_whenflagclicked", next="b", top=True),
        "b": block("looks_say", parent="a", inputs={"MESSAGE": [1, [10, "hi"]]}),
        "loose": block("motion_movesteps", top=True, inputs={"STEPS": [1, [4, "99"]]}),
    }
    comments = {
        "c1": {"blockId": None, "x": 0, "y": 0, "width": 1, "height": 1, "minimized": False, "text": "free\nsecond line"},
        "c2": {"blockId": "loose", "x": 0, "y": 0, "width": 1, "height": 1, "minimized": False, "text": "on a loose block"},
        "c3": {"blockId": "b", "x": 0, "y": 0, "width": 1, "height": 1, "minimized": False, "text": "on say"},
    }
    data = project(blocks=blocks, sprite={"comments": comments})
    project_ = intermediate(data, tmp_path)
    assert project_["sprites"][0]["comments"] == ["free\nsecond line"]
    code = sb3.get_python(project_, "en")
    assert "# Scratch Blocks for 'sprite1'\n# Comment: free\n# second line\n" in code
    assert "# on say\n    self.say(\"hi\")" in code
    assert "move(99)" not in code and "on a loose block" not in code.split("def ")[1]
    assert by_target(project_, "loose_script") == {"Sprite1": by_target(project_, "loose_script")["Sprite1"]}
    assert by_target(project_, "comment") == {"Sprite1": "1 comment(s) belong to blocks that were left out."}


def test_only_comments_still_make_a_section(tmp_path):
    comments = {"c": {"blockId": None, "x": 0, "y": 0, "width": 1, "height": 1, "minimized": False, "text": "only a note"}}
    code = convert(tmp_path, project(stage={"comments": comments}))
    assert "# Scratch Blocks for 'stage'\n# Comment: only a note\n" in code


def test_hat_blocks_that_are_not_supported(tmp_path):
    blocks = {
        "a": block("event_whentouchingobject", next="b", top=True, inputs={"TOUCHINGOBJECTMENU": [1, "m"]}),
        "b": block("looks_say", parent="a"),
        "m": block("event_touchingobjectmenu", fields={"TOUCHINGOBJECTMENU": ["_edge_", None]}, shadow=True),
        "x": block("makeymakey_whenMakeyKeyPressed", top=True),
        "y": block("event_whenflagclicked", top=True),
    }
    project_ = intermediate(project(blocks=blocks), tmp_path)
    assert len(project_["sprites"][0]["blocks"]) == 1, "only the flag script is converted"
    assert messages(project_, "hat") == [
        "Scripts with the hat block 'event_whentouchingobject' are not supported and were left out.",
        "Scripts with the hat block 'makeymakey_whenMakeyKeyPressed' are not supported and were left out."]
    assert messages(project_, "loose_script") == [], "menu blocks and hats are not loose scripts"


def test_texts_of_the_project_can_not_break_the_report(tmp_path):
    evil = EVIL + "\nimport os\r#  x"
    blocks = {
        "a": block("event_whenflagclicked", next="b", top=True),
        "b": block("music_play", parent="a"),
        "c": block("bad opcode;" + EVIL, top=True),
        "d": block("looks_say", top=True),
    }
    data = project(blocks=blocks, sprite={"name": evil}, stage={"variables": {"v": [evil, 0, True]}})
    data["extensions"] = ["pen", evil]
    data["monitors"] = [{"opcode": "sensing_" + EVIL, "params": {"X": 1}, "visible": True, "mode": "default",
                         "spriteName": evil}]
    path = make_sb3(tmp_path, data)
    project_ = sb3.get_intermediate(sb3.get_sb3_data(path), "test")
    code = sb3.get_python(project_, "en")
    assert_harmless(code)
    assert project_["warnings"]
    for warning in project_["warnings"]:
        for text in (warning["message"], warning["target"] or ""):
            assert "\n" not in text and "\r" not in text and " " not in text and len(text) < 200
    header = code.split("\nfrom pystage")[0].splitlines()
    assert all(line.startswith("#") for line in header)
    # also in the output of the command line
    import io
    out = io.StringIO()
    sb3.print_warnings(project_, out)
    assert all(line.startswith("  ") or line.startswith("Not everything") for line in out.getvalue().splitlines())


def test_missing_files_are_reported_in_the_created_project(tmp_path):
    project_ = intermediate(SPECIAL)
    sb3.create_project(SPECIAL, project_["name"], project_, tmp_path / "out", "en")
    missing = [m for m in messages(project_, "asset") if "missing" in m]
    assert missing == ["The file meow.wav is missing in the project file."]
    code = (tmp_path / "out" / "unsupported.py").read_text(encoding="utf-8")
    assert "# - [asset] The file meow.wav is missing in the project file." in code


def test_command_line_prints_the_warnings_to_stderr(tmp_path, capsys):
    assert sb3.main([str(SPECIAL), "-d", str(tmp_path / "out"), "-l", "de"]) == 0
    captured = capsys.readouterr()
    assert "Not everything could be converted" in captured.err
    assert "[hat] Sprite1:" in captured.err and "[cloud] Stage:" in captured.err
    assert "Not everything" not in captured.out
    assert "Exporting to:" in captured.out
    assert (tmp_path / "out" / "unsupported.py").exists()
    # printing the code: the code on stdout, the warnings on stderr
    assert sb3.main([str(SPECIAL), "-p"]) == 0
    captured = capsys.readouterr()
    assert captured.out.startswith("# unsupported (pyStage") and "[monitor]" in captured.err


def test_no_output_on_stderr_without_warnings(tmp_path, capsys):
    path = make_sb3(tmp_path, project())
    assert sb3.main([str(path), "-p"]) == 0
    assert capsys.readouterr().err == ""


def test_the_structure_is_documented():
    source = open(sb3.__file__, encoding="utf-8").read()
    assert '"warnings": [' in source and "kinds:" in source
