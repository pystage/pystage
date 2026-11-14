"""Every block that the converter supports is used by at least one test project.

The test projects are the real Scratch projects in tests/src/scratch_projects and
the projects that tests/make_projects.py generates (in the subdirectory
generated). test_convert.py converts and plays all of them.
"""
import inspect
import json
import re
import zipfile

import pytest

from pystage.convert import sb3, sb3_templates
from pystage.core.sprite import CoreSprite
from pystage.core.stage import CoreStage

from .. import make_projects

PROJECTS = sorted((make_projects.BASE / "scratch_projects").glob("*/*.sb3"))

STANDARD = re.compile(r"^(motion|looks|sound|event|control|sensing|operator|data|pen|procedures|argument)_")

# Supported standard opcodes that no project can contain, and why.
NOT_IN_SAVED_PROJECTS = {
    # Scratch saves the broadcast name in the input of the block, the menu block is only
    # a template so that a reporter that was dropped into the menu does not break the conversion.
    "event_broadcast_menu": "saved as literal in the input of broadcast",
    # The effect is a field of the block (sound_seteffectto), the menu block is not used.
    "sound_effects_menu": "saved as field of sound_seteffectto and sound_changeeffectby",
}

# Core methods that no converted project calls, and why.
NOT_CALLED = {
    # "stop this script" is converted to return
    "control_stop_this": "return",
    # Comparison with > is a Python operator, only text comparisons call the core method
    # (operator_lt and operator_equals are called by texts in the projects).
    "operator_gt": "Python operator",
}


def supported_opcodes():
    """Opcodes that the converter can convert, derived from the API and the templates."""
    opcodes = set()
    for cls in (CoreSprite, CoreStage):
        for name, func in inspect.getmembers(cls, inspect.isfunction):
            if hasattr(func, "opcode"):
                opcodes.add(func.opcode)
            elif STANDARD.match(name):
                opcodes.add(name)
    opcodes |= {key.split(".")[0] for key in sb3_templates.templates}
    # Handled by the code writer itself
    opcodes |= {"procedures_definition", "procedures_call",
                "argument_reporter_string_number", "argument_reporter_boolean"}
    return {opcode for opcode in opcodes if STANDARD.match(opcode)}


def used_opcodes(path):
    """The opcodes of blocks and monitors in a project, including variable and list reporters."""
    data = json.loads(zipfile.ZipFile(path).read("project.json"))
    opcodes = set()
    for target in data["targets"]:
        for block in target.get("blocks", {}).values():
            if isinstance(block, list):
                # A reporter that lies around in the workspace
                opcodes.add({12: "data_variable", 13: "data_listcontents"}.get(block[0], "unknown"))
                continue
            opcodes.add(block["opcode"])
            for value in block.get("inputs", {}).values():
                for part in value[1:]:
                    if isinstance(part, list) and part and part[0] in (12, 13):
                        opcodes.add("data_variable" if part[0] == 12 else "data_listcontents")
    for monitor in data.get("monitors", []):
        opcodes.add(monitor.get("opcode"))
    return opcodes


def test_the_generated_projects_are_part_of_the_tests():
    names = {path.stem for path in PROJECTS if path.parent.name == "generated"}
    assert names == set(make_projects.GENERATED)
    assert len(PROJECTS) > 80


def test_every_supported_opcode_is_used_by_a_test_project():
    supported = supported_opcodes()
    # Reference: These are in every list of the blocks of Scratch 3
    assert {"motion_movesteps", "pen_clear", "sensing_timer", "control_stop", "procedures_call", "data_variable"} <= supported
    used = set()
    for path in PROJECTS:
        used |= used_opcodes(path)
    missing = sorted(supported - used - set(NOT_IN_SAVED_PROJECTS))
    assert missing == [], "No test project uses these blocks, add them to tests/make_projects.py"


def test_the_list_of_exceptions_is_up_to_date():
    supported = supported_opcodes()
    used = set()
    for path in PROJECTS:
        used |= used_opcodes(path)
    assert set(NOT_IN_SAVED_PROJECTS) <= supported
    assert not set(NOT_IN_SAVED_PROJECTS) & used, "These blocks are used now, remove them from the exceptions"


@pytest.mark.parametrize("stage", [False, True], ids=["sprite", "stage"])
def test_every_variant_of_a_block_is_converted_to_a_call_in_some_project(stage):
    """Blocks with a dropdown are several core methods, each one has to be used."""
    called = set()
    for path in PROJECTS:
        data = sb3.get_sb3_data(path)
        project = sb3.get_intermediate(data, "coverage")
        code = sb3.get_python(project, "core")
        called |= set(re.findall(r"\.(\w+)\(", code))
    cls = CoreStage if stage else CoreSprite
    methods = {name for name, _ in inspect.getmembers(cls, inspect.isfunction)
               if STANDARD.match(name) and not name.startswith("_")}
    missing = sorted(methods - called - set(NOT_CALLED))
    assert missing == []
    assert set(NOT_CALLED) <= {name for name, _ in inspect.getmembers(CoreSprite, inspect.isfunction)}


def test_generated_projects_are_up_to_date(tmp_path):
    """Run `python make_projects.py` in the tests directory if this fails."""
    make_projects.main([str(tmp_path / "generated"), str(tmp_path / "special")])
    for kind, directory in (("generated", make_projects.BASE / "scratch_projects" / "generated"),
                            ("special", make_projects.BASE / "special_projects")):
        for path in sorted((tmp_path / kind).glob("*.sb3")):
            assert (directory / path.name).read_bytes() == path.read_bytes(), path.name


def test_generated_projects_have_no_unsupported_blocks():
    for path in PROJECTS:
        if path.parent.name != "generated":
            continue
        project = sb3.get_intermediate(sb3.get_sb3_data(path), path.stem)
        assert "NOT SUPPORTED" not in sb3.get_python(project, "en")
        assert [w for w in project["warnings"] if w["kind"] not in ("monitor",)] == [], path.name
