"""Scratch's fence: a sprite can't leave the stage completely."""
import pygame
import pytest

from pystage.en import Stage


def make_sprite(tmp_path, width, height, stage=None, name="c"):
    stage = stage or Stage()
    path = tmp_path / f"{name}{width}x{height}.png"
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    surface.fill((255, 0, 0, 255))
    pygame.image.save(surface, str(path))
    sprite = stage.add_a_sprite()
    core = sprite._core
    core.pystage_replacecostume(0, str(path))
    return stage, core


def on_stage(core):
    """The part of the sprite that is inside the stage, in pixels."""
    core.costume_manager.update_sprite_image()
    stage_rect = pygame.Rect(0, 0, core.stage.width, core.stage.height)
    return core.rect.clip(stage_rect)


@pytest.mark.parametrize("x, y", [(500, 0), (-500, 0), (0, 500), (0, -500), (900, 900), (-900, -900)])
def test_large_sprite_keeps_15_pixels(tmp_path, x, y):
    _, core = make_sprite(tmp_path, 100, 80)
    core.motion_gotoxy(x, y)
    inside = on_stage(core)
    # 15 px in the direction of the edge it was moved over
    if abs(x) > 240:
        assert inside.width == 15
        assert core.motion_xposition() == (240 + 50 - 15 if x > 0 else -(240 + 50 - 15))
    if abs(y) > 180:
        assert inside.height == 15
        assert core.motion_yposition() == (180 + 40 - 15 if y > 0 else -(180 + 40 - 15))


def test_small_sprite_keeps_half(tmp_path):
    # 10x10: half of the smaller side, 5 px, stay inside
    _, core = make_sprite(tmp_path, 10, 10)
    core.motion_gotoxy(1000, 0)
    assert on_stage(core).width == 5
    core.motion_gotoxy(-1000, 0)
    assert on_stage(core).width == 5
    # a thin sprite: the smaller side counts
    _, core = make_sprite(tmp_path, 200, 4)
    core.motion_gotoxy(0, 1000)
    assert on_stage(core).height == 2
    core.motion_gotoxy(1000, 0)
    assert on_stage(core).width == 2


def test_reporters_return_fenced_values(tmp_path):
    _, core = make_sprite(tmp_path, 100, 80)
    core.motion_setx(500)
    assert core.motion_xposition() == 275
    core.motion_sety(-500)
    assert core.motion_yposition() == -205
    core.motion_changexby(1000)
    assert core.motion_xposition() == 275
    # moving inside is unchanged
    core.motion_gotoxy(10, 20)
    assert (core.motion_xposition(), core.motion_yposition()) == (10, 20)


def test_depends_on_size_and_rotation(tmp_path):
    _, core = make_sprite(tmp_path, 100, 20)
    core.looks_setsizeto(200)
    core.motion_gotoxy(1000, 0)
    assert core.motion_xposition() == 240 + 100 - 15
    core.motion_pointindirection(0)
    core.motion_gotoxy(1000, 0)
    # now it is 20 wide
    core.costume_manager.update_sprite_image()
    assert core.motion_xposition() == 240 + 20 - 15


def test_no_costume(tmp_path):
    stage = Stage()
    core = stage.add_a_sprite()._core
    core.costume_manager.costumes.clear()
    core.costume_manager.current_costume = -1
    core.motion_gotoxy(1000, -1000)
    # no bounding box: not fenced
    assert (core.motion_xposition(), core.motion_yposition()) == (1000, -1000)


def test_clone_and_glide_and_drag(tmp_path):
    stage, core = make_sprite(tmp_path, 100, 80)
    core.motion_gotoxy(0, 0)
    core.clone()
    clone = [s for s in stage._core.sprites if s.is_clone][0]
    clone.motion_gotoxy(-1000, 0)
    assert clone.motion_xposition() == -275
    # a drag moves the sprite via _set_pos
    core._set_pos(pygame.Vector2(2000, 180))
    assert core.motion_xposition() == 275
    core.draggable = True
    # glide to far outside
    core.motion_glidesecstoxy(0, 1000, 0)
    assert core.motion_xposition() == 275


def test_pen_draws_to_fenced_position(tmp_path):
    stage, core = make_sprite(tmp_path, 100, 80)
    core.motion_gotoxy(0, 0)
    core.pen_penDown()
    lines = []
    core._pen_line = lambda start, end: lines.append((tuple(start), tuple(end)))
    core.motion_gotoxy(1000, 0)
    assert lines == [((240, 180), (515, 180))]


def test_opt_out(tmp_path):
    stage, core = make_sprite(tmp_path, 100, 80)
    stage._core.fencing = False
    core.motion_gotoxy(1000, 1000)
    assert (core.motion_xposition(), core.motion_yposition()) == (1000, 1000)


def test_touching_edge_after_fence(tmp_path):
    _, core = make_sprite(tmp_path, 100, 80)
    core.motion_gotoxy(500, 0)
    assert core.sensing_touchingobject_edge()
