"""Tests for the monitors of reporters, sliders and the monitors of converted projects."""
import pygame
import pytest

from pystage.convert import sb3
from pystage.convert.sb3 import MONITOR_REPORTERS
from pystage.core import i18n
from pystage.core._variables import REPORTERS
from pystage.core.monitors import Monitor
from pystage.de import Bühne
from pystage.en import Stage

FRAME = 1 / 60

# Code blocks are compiled again, they can only use globals
clicks = []


def clicked(self):
    clicks.append(1)


def run(stage, frames=1):
    for _ in range(frames):
        stage._core._frame(FRAME)


@pytest.fixture
def stage():
    return Stage()


@pytest.fixture
def sprite(stage):
    return stage.add_a_sprite()


def visible(stage):
    return stage._core.monitor_group.sprites()


# Monitors of reporters

def test_reporter_monitor_shows_and_updates(stage, sprite):
    sprite.show_monitor("x position")
    sprite.set_value_monitor_position("x position", -100, 100)
    run(stage)
    [monitor] = visible(stage)
    assert monitor._title == "Sprite: x position"
    assert monitor._value == 0
    assert monitor.rect.topleft == (140, 80)
    sprite.go_to_x_y(25, 0)
    run(stage)
    assert monitor._value == 25
    sprite.set_name("Zombie")
    run(stage)
    assert monitor._title == "Zombie: x position"


def test_reporter_monitor_hide_and_show(stage, sprite):
    sprite.show_monitor("size")
    sprite.hide_monitor("size")
    assert visible(stage) == []
    sprite.show_monitor("size")
    assert len(visible(stage)) == 1
    # Showing twice is fine, hiding something that was never shown too
    sprite.show_monitor("size")
    sprite.hide_monitor("direction")
    assert len(visible(stage)) == 1


def test_position_and_style_before_show_keep_it_hidden(stage, sprite):
    sprite.set_value_monitor_position("direction", 10, 10)
    sprite.set_value_monitor_style("direction", "large")
    assert visible(stage) == []
    sprite.show_monitor("direction")
    [monitor] = visible(stage)
    assert monitor._style == Monitor.LARGE and monitor.rect.topleft == (250, 170)


def test_global_monitors_belong_to_the_stage(stage, sprite):
    sprite.show_monitor("year")
    stage.show_monitor("year")
    run(stage)
    [monitor] = visible(stage)
    assert monitor._title == "year"
    assert monitor._value > 2000
    stage.hide_monitor("year")
    assert visible(stage) == []


def test_stage_monitors(stage):
    stage.add_backdrop("backdrop1")
    stage.show_monitor("backdrop name")
    stage.show_monitor("volume")
    run(stage)
    titles = {m._title: m._value for m in visible(stage)}
    assert titles == {"Stage: backdrop name": "backdrop1", "Stage: volume": 100}
    with pytest.raises(ValueError, match="does not exist for this sprite or stage"):
        stage.show_monitor("x position")


def test_sprite_cannot_show_stage_monitor(sprite):
    with pytest.raises(ValueError, match="does not exist"):
        sprite.show_monitor("backdrop number")
    with pytest.raises(ValueError, match="Unknown reporter"):
        sprite.show_monitor("nonsense")


def test_every_reporter_has_a_value_label_and_German_name(stage, sprite):
    core_stage = stage._core
    for reporter, (method, color, scope) in REPORTERS.items():
        target = core_stage if scope == "stage" else sprite._core
        target.pystage_showmonitor(reporter)
        target.pystage_setreportermonitorposition(reporter, 0, 0)
        run(stage)
        target.pystage_hidemonitor(reporter)
        assert f"reporter:{reporter}" in i18n.MESSAGES["de"] and f"reporter:{reporter}" in i18n.MESSAGES["en"]
        for table in i18n.ALIASES["reporters"].values():
            assert reporter in table
    assert visible(stage) == []
    assert {k: v[2] for k, v in REPORTERS.items()} == MONITOR_REPORTERS


def test_german_reporter_names_and_labels():
    stage = Bühne()
    try:
        figur = stage.füge_eine_figur_hinzu()
        figur.zeige_monitor("x-Position")
        figur.zeige_monitor("Größe")
        stage.zeige_monitor("Stoppuhr")
        stage._core._frame(FRAME)
        titles = sorted(m._title for m in stage._core.monitor_group)
        assert titles == ["Sprite: Größe", "Sprite: x-Position", "Stoppuhr"]
        stage._core.pystage_showmonitor("looks_backdropnumbername:number")
        assert any(m._title == "Bühne: Bühnenbild Nummer" for m in stage._core.monitor_group)
    finally:
        i18n.set_language("en")


def test_clones_share_the_monitors(stage, sprite):
    sprite.show_monitor("size")
    clone_core = sprite._core
    sprite.create_clone_of_myself()
    clone = [s for s in stage._core.sprites if s.is_clone][0]
    assert clone.reporter_monitors is clone_core.reporter_monitors


# Sliders

@pytest.fixture
def slider(stage):
    stage.create_variable("v", 30)
    stage.show_variable("v")
    stage.set_monitor_position("v", -100, 100)
    stage.set_monitor_style_slider("v", 0, 100, True)
    run(stage)
    monitor = stage._core.var_monitors["v"]
    return stage, monitor


def slider_x(monitor, fraction):
    area = monitor._slider_rect.move(monitor.rect.topleft)
    return area.left + fraction * area.width, area.centery


def test_slider_is_rendered_with_handle(slider):
    stage, monitor = slider
    assert monitor.is_slider()
    assert monitor.rect.height > Monitor.LIGHT_FONT_9.get_height() + 10
    # the handle moves with the value
    before = monitor.image.copy()
    stage._core.variables["v"] = 80
    run(stage)
    assert pygame.image.tobytes(before, "RGBA") != pygame.image.tobytes(monitor.image, "RGBA")


def test_slider_drag_sets_variable(slider):
    stage, monitor = slider
    core = stage._core
    assert core._press_slider(slider_x(monitor, 0.5))
    assert core.variables["v"] == 50
    core._dragged_monitor.drag_to(slider_x(monitor, 0.9)[0])
    assert core.variables["v"] == 90
    # beyond the ends
    monitor.drag_to(-1000)
    assert core.variables["v"] == 0
    monitor.drag_to(1000)
    assert core.variables["v"] == 100
    run(stage)
    assert monitor._value == 100


def test_slider_range_and_decimals(stage):
    stage.create_variable("t", 0)
    stage.show_variable("t")
    stage.set_monitor_style_slider("t", -10, 10, False)
    monitor = stage._core.var_monitors["t"]
    monitor.drag_to(monitor.rect.x + monitor._slider_rect.left + monitor._slider_rect.width * 0.7)
    assert stage._core.variables["t"] == 4
    monitor.drag_to(monitor.rect.x + monitor._slider_rect.left + monitor._slider_rect.width * 0.7123)
    assert stage._core.variables["t"] == pytest.approx(4.25, abs=0.01)
    # a swapped range is repaired, text values do not break the rendering
    stage.set_monitor_style_slider("t", 5, -5, True)
    stage._core.variables["t"] = "hello"
    run(stage)


def test_slider_is_dragged_by_events_and_does_not_touch_sprites(stage, sprite, slider, monkeypatch):
    _, monitor = slider
    core = stage._core
    clicks.clear()
    sprite.when_this_sprite_clicked(clicked)
    sprite._core.sensing_setdragmode_draggable()
    stage.when_stage_clicked(clicked)
    # Put the sprite under the slider
    sprite.go_to_x_y(*[round(c) for c in (monitor.rect.centerx - 240, 180 - monitor.rect.centery)])
    run(stage)
    mouse = {"pos": pygame.Vector2(slider_x(monitor, 0.25))}
    monkeypatch.setattr(core, "_mouse_pos", lambda: mouse["pos"])
    start = sprite._core._pos.copy()
    pygame.event.clear()
    pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=(0, 0)))
    core._process_events()
    assert core.variables["v"] == 25
    mouse["pos"] = pygame.Vector2(slider_x(monitor, 0.75))
    core._process_events()
    assert core.variables["v"] == 75
    run(stage, 3)
    assert clicks == [] and sprite._core._pos == start
    pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONUP, button=1, pos=(0, 0)))
    core._process_events()
    # after releasing, moving the mouse does nothing
    mouse["pos"] = pygame.Vector2(slider_x(monitor, 0.1))
    core._process_events()
    assert core.variables["v"] == 75
    # elsewhere, the sprite is clicked and dragged again
    sprite.go_to_x_y(0, -100)
    run(stage)
    mouse["pos"] = pygame.Vector2(sprite._core.rect.center)
    pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=(0, 0)))
    core._process_events()
    run(stage)
    assert core._dragged_monitor is None and clicks == [1]


def test_hidden_slider_cannot_be_dragged(slider):
    stage, monitor = slider
    stage.hide_variable("v")
    assert not stage._core._press_slider(slider_x(monitor, 0.5))
    assert stage._core.variables["v"] == 30


def test_normal_monitor_is_not_draggable(stage):
    stage.create_variable("n", 5)
    stage.show_variable("n")
    run(stage)
    monitor = stage._core.var_monitors["n"]
    assert not monitor.slider_hit(monitor.rect.center)
    monitor.drag_to(0)
    assert stage._core.variables["n"] == 5


# Rendering

@pytest.mark.parametrize("value", [0, -3.14159, 10**30, "", "text", "x" * 300, "ä€ 😀", True, float("inf")])
def test_rendering_values(stage, value):
    stage.create_variable("v", value)
    for style in ("normal", "large", "slider"):
        stage.show_variable("v")
        getattr(stage, "set_monitor_style_" + style)("v")
        run(stage, 2)
        assert stage._core.var_monitors["v"].image.get_width() > 0


def test_rendering_lists(stage):
    for name, values in (("empty", []), ("long", list(range(500))), ("text", ["x" * 400, "", "ä"])):
        stage.create_list(name, values)
        stage.show_list(name)
        stage.set_list_monitor_position(name, -200, 150, 100, 60)
        run(stage, 2)
        assert stage._core.list_monitors[name].image.get_width() >= 40
    stage.set_list_monitor_position("empty", 0, 0, 5, 5)
    run(stage)


def test_german_list_texts():
    stage = Bühne()
    try:
        stage.erzeuge_liste("l")
        stage.zeige_liste("l")
        stage._core._frame(FRAME)
        assert stage._core.list_monitors["l"]._title == "l"
    finally:
        i18n.set_language("en")


# Converter

def test_converted_monitors_project():
    from pathlib import Path
    path = Path(__file__).parent.parent / "src" / "scratch_projects" / "generated" / "monitors.sb3"
    project = sb3.get_intermediate(sb3.get_sb3_data(str(path)), "monitors")
    assert project["warnings"] == [w for w in project["warnings"] if w["kind"] != "monitor"]
    code = sb3.get_python(project, "en")
    for reporter in MONITOR_REPORTERS:
        assert f'"{reporter}"' in code, reporter
    assert 'set_monitor_style_slider("temp", -10, 10, False)' in code
    assert 'set_monitor_style_slider("speed", 0, 100, True)' in code
    assert 'set_value_monitor_style("sprite2' not in code
    assert code.count("set_monitor_style_large") == 1
    assert 'sprite2.set_value_monitor_style("motion_xposition", "large")' in code
    assert "set_list_monitor_position(\"fruits\", 72, -2, 80, 100)" in code or "set_list_monitor_position(\"fruits\"" in code
    german = sb3.get_python(project, "de")
    assert "zeige_monitor(" in german and "setze_monitor_stil_regler(" in german


def test_unsupported_monitor_values_are_left_out():
    project = {"monitors": [
        {"opcode": "sensing_current", "params": {"CURRENTMENU": "CENTURY"}, "visible": True, "mode": "default", "x": 0, "y": 0},
        {"opcode": "sensing_current", "params": {"CURRENTMENU": ["YEAR"]}, "visible": True, "mode": "default", "x": 0, "y": 0},
        {"opcode": "motion_xposition", "params": {}, "visible": True, "mode": "slider", "x": 0, "y": 0},
    ]}
    assert sb3.monitor_reporter("sensing_current", {"CURRENTMENU": "CENTURY"}, True) is None
    assert sb3.monitor_reporter("sensing_current", {"CURRENTMENU": ["YEAR"]}, True) is None
    assert sb3.monitor_reporter("motion_xposition", {}, True) is None
    assert sb3.monitor_reporter("motion_xposition", {}, False) == "motion_xposition"
    assert sb3.monitor_reporter(["x"], {}, False) is None
    assert project
