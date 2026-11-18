"""Generated code for individual blocks, using tiny crafted projects."""
import ast
import math
import runpy
import sys

import pytest

from pystage.convert import sb3
from .test_convert_untrusted import block, convert, project


def script(*blocks):
    """A script on flag clicked: blocks are (id, block) pairs, chained in order."""
    res = {"hat": block("event_whenflagclicked", next=blocks[0][0], top=True)}
    previous = "hat"
    for i, (key, b) in enumerate(blocks):
        b["parent"] = previous
        b["next"] = blocks[i + 1][0] if i + 1 < len(blocks) else None
        res[key] = b
        previous = key
    return res


def menu_input(name, menu_id):
    return {name: [1, menu_id]}


def stage_code(tmp_path, blocks, language="en"):
    return convert(tmp_path, project(stage={"blocks": blocks}), language)


def number_input(value):
    return [1, [4, str(value)]]


def divide_block(opcode, a, b):
    return block(opcode, inputs={"NUM1": a, "NUM2": b})


def test_stage_erase_all(tmp_path):
    blocks = script(("a", block("pen_clear")))
    assert "self.erase_all()" in stage_code(tmp_path, blocks, "en")
    assert "self.lösche_alles()" in stage_code(tmp_path, blocks, "de")
    assert "NOT SUPPORTED" not in stage_code(tmp_path, blocks, "core")


def test_stop_other_scripts_of_stage_and_sprite(tmp_path):
    stage_blocks = script(("a", block("control_stop", fields={"STOP_OPTION": ["other scripts in stage", None]},
                                      mutation={"hasnext": "true"})))
    sprite_blocks = script(("a", block("control_stop", fields={"STOP_OPTION": ["other scripts in sprite", None]},
                                       mutation={"hasnext": "true"})))
    data = project(blocks=sprite_blocks, stage={"blocks": stage_blocks})
    for language, stage_name, sprite_name in (("en", "stop_other_scripts_in_stage", "stop_other_scripts_in_sprite"),
                                              ("de", "stoppe_andere_skripte_der_bühne", "stoppe_andere_skripte_der_figur")):
        code = convert(tmp_path, data, language)
        assert f"self.{stage_name}()" in code and f"self.{sprite_name}()" in code
        assert "NOT SUPPORTED" not in code
    assert "self.control_stop_other()" in convert(tmp_path, data, "core")


def test_point_towards_random_direction(tmp_path):
    blocks = script(("a", block("motion_pointtowards", inputs=menu_input("TOWARDS", "m"))),
                    ("b", block("motion_pointtowards", inputs=menu_input("TOWARDS", "n"))))
    blocks["m"] = block("motion_pointtowards_menu", fields={"TOWARDS": ["_random_", None]}, shadow=True)
    blocks["n"] = block("motion_pointtowards_menu", fields={"TOWARDS": ["_mouse_", None]}, shadow=True)
    data = project(blocks=blocks)
    assert "self.point_towards_random_direction()\n    self.point_towards_mouse_pointer()" in convert(tmp_path, data, "en")
    assert "self.drehe_dich_zu_zufallsrichtung()" in convert(tmp_path, data, "de")
    assert "self.motion_pointtowards_random()" in convert(tmp_path, data, "core")


def say_blocks(opcode, a, b):
    reporter = divide_block(opcode, a, b)
    reporter["parent"] = "a"
    return script(("a", block("looks_say", inputs={"MESSAGE": [3, "d", [10, ""]]}))) | {"d": reporter}


@pytest.mark.parametrize("opcode, operator, en, de", [
    ("operator_divide", "/", "divide", "geteilt_durch"),
    ("operator_mod", "%", "modulo", "modulo"),
])
def test_division_by_a_number_literal_uses_the_operator(tmp_path, opcode, operator, en, de):
    for divisor in (2, "2.5", -1, "1e-9"):
        code = convert(tmp_path, project(blocks=say_blocks(opcode, number_input(7), number_input(divisor))))
        assert f"(7 {operator} " in code and f"self.{en}(" not in code


@pytest.mark.parametrize("opcode, en, de", [
    ("operator_divide", "divide", "geteilt_durch"),
    ("operator_mod", "modulo", "modulo"),
])
def test_other_divisors_use_the_scratch_method(tmp_path, opcode, en, de):
    cases = {
        "zero": (number_input(1), number_input(0)),
        "empty": (number_input(1), [1, [4, ""]]),
        "text": (number_input(1), [1, [10, "abc"]]),
        "missing": (number_input(1), [1, None]),
        "text dividend": ([1, [10, "abc"]], number_input(2)),
        "variable": (number_input(1), [3, [12, "v", "id"], [4, "1"]]),
    }
    for name, (a, b) in cases.items():
        data = project(blocks=say_blocks(opcode, a, b))
        for language, method in (("en", en), ("de", de), ("core", "operator_divide" if opcode == "operator_divide" else "operator_mod")):
            code = convert(tmp_path, data, language)
            assert f"self.{method}(" in code, (name, language, code)
            assert "NOT SUPPORTED" not in code
            ast.parse(code)


def run_code(code, tmp_path, monkeypatch):
    """Execute generated code like converted projects do, but only for a few frames."""
    from pystage.core.stage import CoreStage

    def play(self):
        for _ in range(3):
            self._frame(1 / 60)
    script = tmp_path / "converted.py"
    script.write_text(code, encoding="utf-8")
    monkeypatch.setattr(CoreStage, "pystage_play", play)
    monkeypatch.setattr(sys, "argv", [str(script)])
    return runpy.run_path(str(script), run_name="__main__")


def test_converted_division_by_zero_runs(tmp_path, monkeypatch):
    reporter = divide_block("operator_divide", number_input(1), number_input(0))
    reporter["parent"] = "a"
    blocks = script(
        ("a", block("data_setvariableto", inputs={"VALUE": [3, "d", [10, ""]]}, fields={"VARIABLE": ["result", "vid"]})),
    ) | {"d": reporter}
    data = project(blocks=blocks, sprite={"variables": {"vid": ["result", 0]}})
    code = convert(tmp_path, data, "en")
    namespace = run_code(code, tmp_path, monkeypatch)
    assert namespace["sprite1"].get_variable("result") == math.inf


def test_menu_blocks_of_supported_blocks(tmp_path):
    blocks = script(("a", block("event_broadcast", inputs={"BROADCAST_INPUT": [3, "m", [11, "x", "id"]]})),
                    ("b", block("looks_say", inputs={"MESSAGE": [3, "n", [10, ""]]})))
    blocks["m"] = block("event_broadcast_menu", fields={"BROADCAST_OPTION": ["go", "id"]}, shadow=True)
    blocks["n"] = block("sound_effects_menu", fields={"EFFECT": ["PITCH", None]}, shadow=True)
    code = convert(tmp_path, project(blocks=blocks))
    assert 'self.broadcast("go")' in code and 'self.say("PITCH")' in code
    assert "NOT SUPPORTED" not in code


def test_music_menu_stays_unsupported(tmp_path):
    blocks = script(("a", block("looks_say", inputs={"MESSAGE": [3, "n", [10, ""]]})))
    blocks["n"] = block("sound_beats_menu", fields={"BEATS": ["1", None]}, shadow=True)
    assert "NOT SUPPORTED: sound_beats_menu" in convert(tmp_path, project(blocks=blocks))


def test_enter_key_hat(tmp_path, monkeypatch):
    blocks = {"hat": block("event_whenkeypressed", fields={"KEY_OPTION": ["enter", None]}, top=True)}
    code = convert(tmp_path, project(blocks=blocks))
    assert 'sprite1.when_key_pressed("enter"' in code
    run_code(code, tmp_path, monkeypatch)


def test_german_names_are_fixed():
    from pystage.de import Figur, Bühne
    from pystage.en import Sprite, Stage
    for name in ("gehe_schritte", "setze_drehtyp_auf_links_rechts", "wenn_das_bühnenbild_wechselt_zu",
                 "drehe_dich_zu_zufallsrichtung", "geteilt_durch", "modulo"):
        assert hasattr(Figur, name), name
    for name in ("gehe_er_schritt", "setze_drehtyp_auf_helligkeit", "wenn_das_bühnenbild_zu_wechselt"):
        assert not hasattr(Figur, name) and not hasattr(Bühne, name)
    for name in ("wenn_das_bühnenbild_wechselt_zu", "lösche_alles", "stoppe_andere_skripte_der_bühne", "geteilt_durch", "modulo"):
        assert hasattr(Bühne, name), name
    assert not hasattr(Bühne, "stoppe_andere_skripte_der_figur")
    for cls in (Stage, Bühne):
        assert not hasattr(cls, "pystage_createsprite") and not hasattr(cls, "pystage_play")
    assert Stage.add_a_sprite and Stage.play and Bühne.füge_eine_figur_hinzu and Bühne.abspielen


def test_no_facade_method_is_defined_twice():
    import pystage.de.sprite, pystage.de.stage, pystage.en.sprite, pystage.en.stage
    import pystage.lt.sprite, pystage.lt.stage
    for module in (pystage.de.sprite, pystage.de.stage, pystage.en.sprite, pystage.en.stage,
                   pystage.lt.sprite, pystage.lt.stage):
        with open(module.__file__, encoding="utf-8") as f:
            tree = ast.parse(f.read())
        for cls in [n for n in tree.body if isinstance(n, ast.ClassDef)]:
            names = [n.name for n in cls.body if isinstance(n, ast.FunctionDef)]
            assert len(names) == len(set(names)), [n for n in names if names.count(n) > 1]


def test_facades_delegate_directly_to_the_core():
    """Converter and yield injection find the core method by the bytecode."""
    from pystage.l10n.api import _get_core_names
    from pystage.de import Figur, Bühne
    from pystage.en import Sprite, Stage
    from pystage.lt import Veikėjas, Scena
    for cls in (Sprite, Stage, Figur, Bühne, Veikėjas, Scena):
        names = _get_core_names(cls)
        for name in ("divide", "modulo", "geteilt_durch", "padalinta_iš", "liekana"):
            if hasattr(cls, name):
                assert names[name] in ("operator_divide", "operator_mod")
