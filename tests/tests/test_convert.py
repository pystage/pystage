"""Converts all Scratch projects in tests/src/scratch_projects.

Each project is
- converted for all languages, the code has to be valid Python,
- compared to the expected result in tests/src/correct_results,
- played for a few seconds without window.

To update the expected results after an intended change of the converter,
run `python generate.py -a` in the tests directory and review the diff.
"""
import difflib
import os
import runpy
import sys
from pathlib import Path

import pygame
import pytest

from pystage.convert import sb3
from pystage.core.stage import CoreStage

BASE = Path(__file__).parent.parent / "src"
PROJECTS = sorted((BASE / "scratch_projects").glob("*/*.sb3"))
LANGUAGES = ["core", "en", "de"]


def project_id(path):
    return f"{path.parent.name}/{path.stem}"


def convert(path, language="en"):
    data = sb3.get_sb3_data(path)
    project = sb3.get_intermediate(data, sb3.to_filename(path.stem))
    return project, sb3.get_python(project, language)


@pytest.mark.parametrize("path", PROJECTS, ids=project_id)
@pytest.mark.parametrize("language", LANGUAGES)
def test_code_is_valid(path, language):
    _, code = convert(path, language)
    compile(code, str(path), "exec")
    assert "NOT SUPPORTED" not in code


@pytest.mark.parametrize("path", PROJECTS, ids=project_id)
def test_expected_result(path):
    name = sb3.to_filename(path.stem)
    expected = BASE / "correct_results" / path.parent.name / name / f"{name}.py"
    _, code = convert(path)
    diff = difflib.unified_diff(
        expected.read_text(encoding="utf-8").splitlines(),
        code.splitlines(),
        "expected", "converted", lineterm="")
    assert "\n".join(diff) == ""


def play(stage, frames=90):
    for i in range(frames):
        if i == 10:
            # Simulate some user input
            for code_manager in stage._all_code_managers():
                code_manager.process_key_pressed(pygame.K_SPACE)
                code_manager.process_click()
        if stage.input_manager.is_active() and i % 20 == 0:
            stage.input_manager._queue[0].close()
            stage.input_manager.accept_answer("7")
        stage._frame(1 / 30)


@pytest.mark.parametrize("path", PROJECTS, ids=project_id)
def test_converted_project_runs(path, tmp_path, monkeypatch, capsys):
    project, _ = convert(path)
    directory = tmp_path / "project"
    sb3.create_project(path, project["name"], project, directory, "en")
    script = directory / f"{project['name']}.py"

    monkeypatch.setattr(CoreStage, "pystage_play", play)
    monkeypatch.setattr(sys, "argv", [str(script)])
    monkeypatch.chdir(directory)
    runpy.run_path(str(script), run_name="__main__")
    assert "not found" not in capsys.readouterr().out
