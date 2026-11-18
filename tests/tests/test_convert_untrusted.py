"""Scratch projects are untrusted input, e.g. in the online converter.

Whatever is in a project file: The conversion must either fail with a
ConversionError or produce harmless Python code, and files must only be
written into the project directory.
"""
import ast
import io
import json
import zipfile

import pytest

from pystage.convert import sb3

EVIL = '"\n\'); import os; os.system("touch /tmp/pwned") #\\'
TEMPLATE = "{{ ''.__class__.__mro__ }}{% for x in range(9999999) %}x{% endfor %}"


def make_sb3(tmp_path, project, files=None):
    path = tmp_path / "project.sb3"
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("project.json", project if isinstance(project, (str, bytes)) else json.dumps(project))
        for name, content in (files or {}).items():
            archive.writestr(name, content)
    return path


def block(opcode, next=None, parent=None, inputs=None, fields=None, top=False, **more):
    res = {"opcode": opcode, "next": next, "parent": parent, "inputs": inputs or {},
           "fields": fields or {}, "shadow": False, "topLevel": top}
    res.update(more)
    return res


def project(blocks=None, sprite=None, stage=None, monitors=None):
    stage_target = {
        "isStage": True, "name": "Stage", "variables": {}, "lists": {}, "blocks": {},
        "comments": {}, "currentCostume": 0, "costumes": [], "sounds": [], "layerOrder": 0,
    }
    stage_target.update(stage or {})
    sprite_target = {
        "isStage": False, "name": "Sprite1", "variables": {}, "lists": {}, "blocks": blocks or {},
        "comments": {}, "currentCostume": 0, "costumes": [], "sounds": [], "layerOrder": 1,
        "visible": True, "x": 0, "y": 0, "size": 100, "direction": 90, "draggable": False,
        "rotationStyle": "all around",
    }
    sprite_target.update(sprite or {})
    return {"targets": [stage_target, sprite_target], "monitors": monitors or [], "extensions": [], "meta": {}}


def convert(tmp_path, data, language="en"):
    path = make_sb3(tmp_path, data)
    intermediate = sb3.get_intermediate(sb3.get_sb3_data(path), "test")
    return sb3.get_python(intermediate, language)


def assert_harmless(code):
    """The code must only consist of what the converter writes itself."""
    tree = ast.parse(code)
    # Sprites and functions defined by the converter
    own = {"self", "stage", "Stage", "range", "int"}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            own.update(target.id for target in node.targets)
        elif isinstance(node, ast.FunctionDef):
            own.add(node.name)
            own.update(arg.arg for arg in node.args.args)
    assert all(name.isidentifier() and not name.startswith("__") for name in own)
    for node in ast.walk(tree):
        assert not isinstance(node, ast.Import), "no additional imports"
        if isinstance(node, ast.ImportFrom):
            assert node.module.startswith("pystage.")
        if isinstance(node, ast.Name):
            assert node.id in own, node.id


def test_texts_can_not_inject_code(tmp_path):
    blocks = {
        "a": block("event_whenflagclicked", next="b", top=True),
        "b": block("looks_say", parent="a", next="c", inputs={"MESSAGE": [1, [10, EVIL]]}),
        "c": block("data_setvariableto", parent="b", next="d", inputs={"VALUE": [1, [10, EVIL]]}, fields={"VARIABLE": [EVIL, "id"]}),
        "d": block("event_broadcast", parent="c", next="e", inputs={"BROADCAST_INPUT": [1, [11, EVIL, "id"]]}),
        "e": block("motion_movesteps", parent="d", next="f", inputs={"STEPS": [1, [4, EVIL]]}),
        "f": block("looks_switchcostumeto", parent="e", next="g", inputs={"COSTUME": [1, "menu"]}),
        "menu": block("looks_costume", parent="f", fields={"COSTUME": [EVIL, None]}),
        "g": block("pen_setPenColorToColor", parent="f", inputs={"COLOR": [1, [9, EVIL]]}),
    }
    data = project(
        blocks,
        sprite={
            "name": EVIL,
            "variables": {"id": [EVIL, EVIL]},
            "lists": {"id2": [EVIL, [EVIL, 1, None, {"a": 1}]]},
            "comments": {"c1": {"blockId": "b", "text": EVIL}, "c2": {"blockId": "a", "text": "x import os"}},
            "x": EVIL, "y": "1); import os #", "size": EVIL, "direction": EVIL, "layerOrder": EVIL,
            "currentCostume": EVIL, "rotationStyle": EVIL,
            "costumes": [{"assetId": "abc", "name": EVIL, "dataFormat": "png", "rotationCenterX": EVIL, "rotationCenterY": "2", "bitmapResolution": EVIL}],
            "sounds": [{"assetId": "def", "name": EVIL, "dataFormat": "wav"}],
        },
        monitors=[{"opcode": "data_variable", "params": {"VARIABLE": EVIL}, "spriteName": EVIL, "visible": True, "mode": EVIL, "x": EVIL, "y": 3}],
    )
    for language in ("en", "de", "lt", "core"):
        code = convert(tmp_path, data, language)
        if language == "en":
            assert_harmless(code)
        else:
            ast.parse(code)
    # The texts are still there, but as texts.
    assert "touch /tmp/pwned" in code


def test_names_can_not_inject_templates_or_code(tmp_path):
    blocks = {
        "a": block("event_whenflagclicked", next="b", top=True),
        "b": block("looks_say", parent="a", next="c", inputs={TEMPLATE: [1, [10, "x"]], "MESSAGE": [1, [10, TEMPLATE]]}, fields={TEMPLATE: ["x", None]}),
        "c": block(TEMPLATE, parent="b", next="d"),
        "d": block("procedures_call", parent="c", next="e", mutation={"proccode": TEMPLATE, "argumentids": "[\"x\"]"}, inputs={"x": [1, [10, TEMPLATE]]}),
        "e": block("procedures_call", parent="d", mutation={"proccode": "known %s", "argumentids": "[\"x\"]"}, inputs={"x": [1, [10, TEMPLATE]]}),
        "def": block("procedures_definition", top=True, inputs={"custom_block": [1, "proto"]}, next="body"),
        "proto": block("procedures_prototype", parent="def", mutation={"proccode": "known %s", "argumentnames": json.dumps([EVIL]), "argumentids": "[\"x\"]", "warp": "true"}),
        "body": block("looks_say", parent="def", inputs={"MESSAGE": [1, "arg"]}),
        "arg": block("argument_reporter_string_number", parent="body", fields={"VALUE": [EVIL, None]}),
    }
    code = convert(tmp_path, project(blocks))
    tree = ast.parse(code)
    names = {node.id for node in ast.walk(tree) if isinstance(node, ast.Name)}
    assert not any("class" in name or "mro" in name for name in names)
    # Templates in texts are not executed
    assert "__mro__" in code
    assert "xxxx" not in code


def test_assets_stay_in_the_project_directory(tmp_path):
    data = project(sprite={
        "costumes": [
            {"assetId": "abc", "name": "../../evil", "dataFormat": "/../../../evil", "rotationCenterX": 1, "rotationCenterY": 1},
            {"assetId": "../../abc", "name": "ok", "dataFormat": "png", "rotationCenterX": 1, "rotationCenterY": 1},
            {"assetId": "good", "name": "../up", "dataFormat": "png", "rotationCenterX": 1, "rotationCenterY": 1},
        ],
        "sounds": [{"assetId": "snd", "name": "/etc/passwd", "dataFormat": "wav"}],
    })
    path = make_sb3(tmp_path, data, {"good.png": b"image", "snd.wav": b"sound", "../../abc.png": b"evil"})
    intermediate = sb3.get_intermediate(sb3.get_sb3_data(path), "../../name")
    target = tmp_path / "out"
    sb3.create_project(path, "../../name", intermediate, target, "en")
    files = sorted(str(f.relative_to(tmp_path)) for f in tmp_path.rglob("*") if f.is_file())
    assert files == ["out/_name.py", "out/images/_up.png", "out/sounds/_etc_passwd.wav", "project.sb3"]


def test_damaged_projects_fail_cleanly(tmp_path):
    bad = [
        "no json", "[]", "{}", '{"targets": 5}', '{"targets": []}', "[" * 100000,
        json.dumps({"targets": [None, 5, "x", {"isStage": True, "blocks": 7, "costumes": {"a": 1}, "variables": []}]}),
    ]
    for content in bad:
        path = make_sb3(tmp_path, content)
        try:
            intermediate = sb3.get_intermediate(sb3.get_sb3_data(path), "test")
            ast.parse(sb3.get_python(intermediate, "en"))
        except sb3.ConversionError:
            pass
    with pytest.raises(sb3.ConversionError):
        sb3.get_sb3_data(io.BytesIO(b"this is not a zip file"))
    with pytest.raises(sb3.ConversionError):
        empty = tmp_path / "empty.sb3"
        zipfile.ZipFile(empty, "w").close()
        sb3.get_sb3_data(empty)


def test_cyclic_and_deep_blocks(tmp_path):
    cyclic = {
        "a": block("event_whenflagclicked", next="b", top=True),
        "b": block("looks_show", parent="a", next="c"),
        "c": block("looks_hide", parent="b", next="b"),
    }
    with pytest.raises(sb3.ConversionError):
        convert(tmp_path, project(cyclic))

    nested = {"a": block("event_whenflagclicked", next="n0", top=True)}
    for i in range(1000):
        nested[f"n{i}"] = block("control_forever", inputs={"SUBSTACK": [2, f"n{i + 1}"]})
    with pytest.raises(sb3.ConversionError):
        convert(tmp_path, project(nested))

    # Long scripts are no problem
    long = {"a": block("event_whenflagclicked", next="n0", top=True)}
    for i in range(5000):
        long[f"n{i}"] = block("looks_show", next=f"n{i + 1}" if i < 4999 else None)
    code = convert(tmp_path, project(long))
    assert code.count("self.show()") == 5000


def test_size_limits(tmp_path):
    path = make_sb3(tmp_path, project(sprite={
        "costumes": [{"assetId": "big", "name": "big", "dataFormat": "png", "rotationCenterX": 1, "rotationCenterY": 1}],
    }), {"big.png": b"0" * 5000})
    limits = sb3.Limits(asset=1000)
    intermediate = sb3.get_intermediate(sb3.get_sb3_data(path, limits), "test", limits)
    with pytest.raises(sb3.ConversionError):
        sb3.create_project(path, "test", intermediate, tmp_path / "out", "en", limits=limits)
    with pytest.raises(sb3.ConversionError):
        sb3.get_sb3_data(path, sb3.Limits(project_json=10))
    with pytest.raises(sb3.ConversionError):
        sb3.get_sb3_data(path, sb3.Limits(total=1000))


def test_conversions_do_not_influence_each_other(tmp_path):
    data = project(sprite={"costumes": [{"assetId": "abc", "name": "cat", "dataFormat": "png", "rotationCenterX": 1, "rotationCenterY": 1}]})
    assert convert(tmp_path, data) == convert(tmp_path, data)
    assert 'add_costume("cat"' in convert(tmp_path, data)


def test_name_clashes(tmp_path):
    data = project(sprite={"name": "class"})
    data["targets"].append(dict(data["targets"][1], name="Stage "))
    data["targets"].append(dict(data["targets"][1], name="CLASS"))
    code = convert(tmp_path, data)
    ast.parse(code)
    assert "class_2 = stage.add_a_sprite" in code
    assert "stage_2 = stage.add_a_sprite" in code
    assert "class_3 = stage.add_a_sprite" in code


def test_comparisons_with_text_use_scratch_semantics(tmp_path):
    def comparison(opcode, a, b):
        blocks = {
            "a": block("event_whenflagclicked", next="b", top=True),
            "b": block("control_if", parent="a", inputs={"CONDITION": [2, "c"], "SUBSTACK": [2, "d"]}),
            "c": block(opcode, parent="b", inputs={"OPERAND1": a, "OPERAND2": b}),
            "d": block("looks_hide", parent="b"),
        }
        return convert(tmp_path, project(blocks, sprite={"variables": {"v": ["v", 1]}}))
    var = [3, [12, "v", "v"], [10, ""]]
    text = [1, [10, ""]]
    number = [1, [4, "5"]]
    code = comparison("operator_gt", var, text)
    assert 'self.greater_than(self.get_variable("v"), "")' in code
    assert "self.less_than(" in comparison("operator_lt", var, text)
    assert 'self.equals(self.get_variable("v"), "")' in comparison("operator_equals", var, text)
    assert 'self.equals("", self.get_variable("v"))' in comparison("operator_equals", text, var)
    # Without text literals the Python operators are used.
    code = comparison("operator_gt", var, number)
    assert 'self.get_variable("v") > 5' in code and "greater_than" not in code
    assert "equals(" not in comparison("operator_equals", var, number)
    assert "größer_als" in convert(tmp_path, project({
        "a": block("event_whenflagclicked", next="b", top=True),
        "b": block("control_if", parent="a", inputs={"CONDITION": [2, "c"]}),
        "c": block("operator_gt", parent="b", inputs={"OPERAND1": var, "OPERAND2": text}),
    }), "de")
