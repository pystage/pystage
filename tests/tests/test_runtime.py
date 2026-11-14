"""Tests for the runtime: code blocks, events and the blocks itself.

The stage is not played, the frames are executed step by step instead.
"""
import pygame
import pytest

from pystage.en import Stage, no_refresh

FRAME = 1 / 60

log = []
counter = 0


def run(stage, seconds=None, frames=None):
    if frames is None:
        frames = int(round(seconds / FRAME))
    for _ in range(frames):
        stage._core._frame(FRAME)


@pytest.fixture
def stage():
    global counter
    log.clear()
    counter = 0
    return Stage()


@pytest.fixture
def sprite(stage):
    return stage.add_a_sprite()


# Motion

def square(self):
    for _ in range(4):
        self.move(10)
        self.turn_left(90)


def test_loops_refresh_the_screen(stage, sprite):
    sprite.when_program_starts(square)
    run(stage, frames=1)
    assert (sprite.x_position(), sprite.y_position()) == (10, 0)
    run(stage, frames=3)
    assert sprite.x_position() == pytest.approx(0)
    assert sprite.y_position() == pytest.approx(0)
    assert sprite.direction() == pytest.approx(90)


def test_no_refresh_runs_in_one_go(stage, sprite):
    sprite.when_program_starts(square, no_refresh=True)
    sprite.set_x(100)
    run(stage, frames=1)
    assert sprite.x_position() == pytest.approx(100)
    assert sprite.direction() == pytest.approx(90)


def wait_and_move(self):
    self.wait(0.5)
    self.set_x(50)


def test_wait(stage, sprite):
    sprite.when_program_starts(wait_and_move)
    run(stage, 0.4)
    assert sprite.x_position() == 0
    run(stage, 0.2)
    assert sprite.x_position() == 50


def glide(self):
    self.glide_to_x_y(1, 100, -50)
    log.append("arrived")


def test_glide(stage, sprite):
    sprite.when_program_starts(glide)
    run(stage, 0.5)
    assert 40 < sprite.x_position() < 60
    assert log == []
    run(stage, 0.6)
    assert (sprite.x_position(), sprite.y_position()) == (100, -50)
    assert log == ["arrived"]


def test_go_to_and_point_towards_sprite(stage, sprite):
    other = stage.add_a_sprite()
    other.go_to_x_y(30, 40)
    sprite.point_towards_sprite(other)
    assert sprite.distance_to_sprite(other) == pytest.approx(50)
    sprite.move(50)
    assert sprite.x_position() == pytest.approx(30)
    assert sprite.y_position() == pytest.approx(40)
    sprite.go_to_x_y(0, 0)
    sprite.go_to_sprite(other)
    assert (sprite.x_position(), sprite.y_position()) == (30, 40)


# Helper functions (custom blocks)

def helper(self, steps):
    for _ in range(steps):
        self.change_x_by(1)
    self.wait(0.1)
    log.append("helper done")


@no_refresh
def fast_helper(self, steps):
    for _ in range(steps):
        self.change_x_by(1)


def uses_helpers(self):
    global counter
    counter += 1
    helper(self, 3)
    fast_helper(self, 100)
    log.append("done")


def test_helper_functions_behave_like_custom_blocks(stage, sprite):
    sprite.when_program_starts(uses_helpers)
    run(stage, frames=2)
    assert sprite.x_position() == 2
    assert counter == 1, "global variables are shared with the code block"
    run(stage, 0.3)
    assert sprite.x_position() == 103
    assert log == ["helper done", "done"]


# Events

def receiver(self):
    self.wait(0.2)
    log.append("received")


def sender(self):
    self.broadcast_and_wait("Go")
    log.append("after wait")
    self.broadcast("go")
    log.append("after broadcast")


def test_broadcast_and_wait(stage, sprite):
    other = stage.add_a_sprite()
    other.when_i_receive_message("go", receiver)
    sprite.when_program_starts(sender)
    run(stage, 0.1)
    assert log == []
    run(stage, 0.2)
    assert log == ["received", "after wait", "after broadcast"]
    run(stage, 0.3)
    assert log == ["received", "after wait", "after broadcast", "received"]


def on_backdrop(self):
    log.append("backdrop")
    self.wait(0.1)


def switch(self):
    self.switch_backdrop_to_and_wait("b")
    log.append("switched")


def test_backdrop_events(stage, sprite):
    stage.add_backdrop("grid")
    stage._core.pystage_addbackdrop("b")
    sprite.when_backdrop_switches_to("b", on_backdrop)
    stage.when_program_starts(switch)
    run(stage, frames=3)
    assert log == ["backdrop"]
    assert stage.backdrop_name() == "b"
    run(stage, 0.2)
    assert log == ["backdrop", "switched"]


def on_timer(self):
    log.append("timer")


def test_timer_event(stage, sprite):
    sprite.when_timer_greater_than(0.2, on_timer)
    run(stage, 0.1)
    assert log == []
    run(stage, 0.5)
    assert log == ["timer"]
    sprite.reset_timer()
    run(stage, 0.5)
    assert log == ["timer", "timer"]


def on_key(self):
    log.append("key")


def test_key_events(stage, sprite):
    sprite.when_key_pressed("space", on_key)
    sprite.when_key_pressed("any", on_key)
    for code_manager in stage._core._all_code_managers():
        code_manager.process_key_pressed(pygame.K_SPACE)
    run(stage, frames=2)
    assert log == ["key", "key"]
    for code_manager in stage._core._all_code_managers():
        code_manager.process_key_pressed(pygame.K_x)
    run(stage, frames=2)
    assert log == ["key", "key", "key"]
    with pytest.raises(ValueError):
        sprite.when_key_pressed("no key", on_key)


# Control

def forever(self):
    while True:
        log.append(self._core.name)
        self.wait(0.1)


def stopper(self):
    self.wait(0.25)
    self.stop_other_scripts_in_sprite()
    log.append("stopped others")
    self.stop_this_script()
    log.append("never")


def test_stop_blocks(stage, sprite):
    other = stage.add_a_sprite()
    other._core.pystage_setname("other")
    sprite._core.pystage_setname("sprite")
    sprite.when_program_starts(forever)
    other.when_program_starts(forever)
    sprite.when_program_starts(stopper)
    run(stage, 1)
    assert "stopped others" in log and "never" not in log
    after = log[log.index("stopped others"):]
    assert "sprite" not in after, "other scripts in this sprite are stopped"
    assert "other" in after, "other sprites are not affected"
    count = len(log)
    other.stop_all()
    run(stage, 0.5)
    assert len(log) == count


def clone_script(self):
    self.change_x_by(100)
    self.wait(0.2)
    self.delete_this_clone()
    log.append("never")


def cloner(self):
    self.create_clone_of_myself()


def test_clones(stage, sprite):
    sprite.create_list("items", [1, 2], all_sprites=False)
    sprite.when_i_start_as_a_clone(clone_script)
    sprite.when_program_starts(cloner)
    run(stage, 0.1)
    sprites = stage._core.sprites.sprites()
    assert len(sprites) == 2
    clone = [s for s in sprites if s.is_clone][0]
    assert sprites.index(clone) < sprites.index(sprite._core), "clone is behind the original"
    assert clone.motion_xposition() == 100
    assert sprite.x_position() == 0
    clone.data_addtolist("items", 3)
    assert sprite.get_list("items") == [1, 2]
    run(stage, 0.3)
    assert len(stage._core.sprites.sprites()) == 1
    assert log == []
    # Deleting the original has no effect
    sprite.delete_this_clone()
    assert len(stage._core.sprites.sprites()) == 1


# Pen

def test_pen_draws_immediately(stage, sprite):
    image = stage._core.pen_image
    sprite.set_pen_color((255, 0, 0))
    sprite.set_pen_size_to(3)
    sprite.pen_down()
    sprite.go_to_x_y(50, 0)
    sprite.go_to_x_y(50, 50)
    sprite.pen_up()
    sprite.go_to_x_y(-100, -100)
    assert image.get_at((240 + 25, 180)) == (255, 0, 0, 255)
    assert image.get_at((240 + 50, 180 - 25)) == (255, 0, 0, 255)
    assert image.get_at((240 - 50, 180 + 50)).a == 0
    sprite.erase_all()
    assert image.get_at((240 + 25, 180)).a == 0


def test_stamp(stage, sprite):
    sprite.go_to_x_y(100, 100)
    sprite.stamp()
    assert stage._core.pen_image.get_bounding_rect().width > 10


# Sensing

def test_touching(stage, sprite):
    other = stage.add_a_sprite()
    assert sprite.touching(other)
    other.go_to_x_y(200, 0)
    assert not sprite.touching(other)
    other.go_to_x_y(0, 0)
    other.hide()
    assert not sprite.touching(other)
    assert not sprite.touching_edge()
    sprite.go_to_x_y(240, 0)
    assert sprite.touching_edge()


def test_touching_color(stage, sprite):
    other = stage.add_a_sprite()
    other.go_to_x_y(100, 0)
    other.set_pen_color((0, 200, 0))
    other.set_pen_size_to(20)
    other.pen_down()
    other.go_to_x_y(100, 100)
    other.hide()
    assert not sprite.touching_color((0, 200, 0))
    sprite.go_to_x_y(100, 50)
    assert sprite.touching_color((0, 200, 0))
    assert not sprite.touching_color((200, 0, 0))


def test_properties_of_other_sprites(stage, sprite):
    other = stage.add_a_sprite()
    other._core.pystage_setname("other")
    other.go_to_x_y(12, 34)
    other.create_variable("score", 5, all_sprites=False)
    core = sprite._core
    assert core.sensing_of_xposition(other) == 12
    assert core.sensing_of_yposition("other") == 34
    assert core.sensing_of_variable("score", other) == 5
    assert core.sensing_of_size(other) == 100
    assert core.sensing_of_backdropnumber() == 0


# Looks

def test_costumes_by_number_and_name(stage):
    sprite = stage.add_a_sprite(None)
    sprite.add_costume("zombie_idle")
    sprite.add_costume("zombie_walk1")
    assert sprite.costume_number() == 1
    sprite.switch_costume_to(2)
    assert sprite.costume_name() == "zombie_walk1"
    sprite.switch_costume_to("zombie_idle")
    assert sprite.costume_number() == 1
    sprite.switch_costume_to(3)
    assert sprite.costume_number() == 1
    sprite.next_costume()
    assert sprite.costume_number() == 2


def say(self):
    self.say_for_seconds(42, 0.2)
    log.append("said")


def test_say(stage, sprite):
    sprite.when_program_starts(say)
    run(stage, 0.1)
    assert sprite._core.bubble_manager.bubble.text == "42"
    assert log == []
    run(stage, 0.2)
    assert sprite._core.bubble_manager.bubble is None
    assert log == ["said"]


def test_effects_and_layers(stage, sprite):
    other = stage.add_a_sprite()
    sprite.change_brightness_effect_by(50)
    sprite.set_ghost_effect_to(50)
    sprite.set_size_to(200)
    run(stage, frames=2)
    assert sprite._core.image.get_width() > other._core.image.get_width()
    sprite.go_to_front_layer()
    assert stage._core.sprites.sprites()[-1] is sprite._core
    sprite.go_to_back_layer()
    assert stage._core.sprites.sprites()[0] is sprite._core


# Variables and operators

def test_variables_and_lists(stage, sprite):
    stage.create_variable("score", 10)
    sprite.create_variable("lives", 3, all_sprites=False)
    sprite.change_variable_by("score", "5")
    assert stage.get_variable("score") == 15
    with pytest.raises(ValueError):
        stage.get_variable("lives")
    stage.create_list("names", ["Ada"])
    sprite.add_to_list("names", "Bob")
    sprite.insert_at_list("names", "Zoe", 1)
    assert stage.get_list("names") == ["Zoe", "Ada", "Bob"]
    assert sprite.item_number_in_list("names", "ada") == 2
    assert sprite.item_of_list("names", "last") == "Bob"
    assert sprite.list_contains("names", "BOB")
    sprite.delete_item_of_list("names", "all")
    assert sprite.length_of_list("names") == 0
    sprite.show_list("names")
    sprite.show_variable("lives")
    run(stage, frames=2)


def test_operators(sprite):
    assert sprite.join("a", 1.0) == "a1"
    assert sprite.letter_of(2, "abc") == "b"
    assert sprite.letter_of(5, "abc") == ""
    assert sprite.length_of(1234) == 4
    assert sprite.contains("Hello", "ELL")
    assert sprite.round(2.5) == 3
    assert isinstance(sprite.pick_random(1, 10), int)
    assert isinstance(sprite.pick_random(1, 10.5), float)
    assert 1 <= sprite.pick_random(10, 1) <= 10


# Sound

def play(self):
    self.play_sound_until_done("no such sound")
    log.append("played")


def test_missing_sound_does_not_crash(stage, sprite):
    sprite.when_program_starts(play)
    sprite.set_volume_to(50)
    sprite.change_pitch_effect_by(10)
    run(stage, frames=3)
    assert log == ["played"]
    assert sprite.volume() == 50


# Values

def test_texts_behave_like_in_scratch(stage, sprite):
    stage.create_variable("text", "abc")
    stage.create_variable("number", "5")
    stage.create_variable("empty", "")
    text, number, empty = (sprite.get_variable(name) for name in ("text", "number", "empty"))
    assert isinstance(text, str) and text == "ABC" and text != "abd"
    assert number + 1 == 6 and 1 + number == 6 and number * 2 == 10 and number - 1 == 4
    assert text + 1 == 1 and empty + 1 == 1
    assert number + "x" == "5x" and "x" + number == "x5"
    assert number == 5 and number > 4 and 4 < number and not (number < 5)
    assert not (empty > 0) and (text > 5) and not (5 > text)
    assert int(number) == 5 and int(text) == 0 and float(number) == 5.0
    assert number + number == 10
    assert sprite.join("1", "2") + 1 == 13
    assert {number: 1}[5] == 1
    stage.create_list("items", ["Apple", "7"])
    assert sprite.item_of_list("items", 2) + 1 == 8
    assert sprite.item_of_list("items", 1) == "apple"


def test_comparison_operators(stage, sprite):
    stage.create_variable("id", 5)
    value = sprite.get_variable("id")
    assert sprite.greater_than(5, "") and sprite.greater_than(value, "")
    assert not sprite.less_than(value, "")
    assert sprite.less_than("apple", "Banana") and sprite.greater_than(10, 9)
    assert sprite.greater_than("10", "9") and sprite.less_than(5, "a")
    assert sprite.equals("ABC", "abc") and sprite.equals("5", 5.0) and sprite.equals("", "")
    assert not sprite.equals(0, "") and not sprite.equals("a", 1)


# Stage blocks and small gaps

def test_stage_erase_all(stage, sprite):
    image = stage._core.pen_image
    sprite.pen_down()
    sprite.move(30)
    assert image.get_bounding_rect().width > 0
    stage.erase_all()
    assert image.get_bounding_rect().width == 0


def stage_erases(self):
    self.erase_all()
    log.append("erased")


def test_stage_script_can_erase_all(stage, sprite):
    sprite.pen_down()
    sprite.move(30)
    stage.when_program_starts(stage_erases)
    run(stage, frames=2)
    assert log == ["erased"]
    assert stage._core.pen_image.get_bounding_rect().width == 0


# The blocks that the Scratch editor offers for the stage (not the sprite only
# blocks), written as core opcode or method name.
STAGE_PALETTE = [
    # looks
    "looks_switchbackdropto", "looks_nextbackdrop", "looks_switchbackdroptoandwait",
    "looks_changeeffectby", "looks_seteffectto", "looks_cleargraphiceffects", "looks_backdropnumbername",
    # sound
    "sound_playuntildone", "sound_play", "sound_stopallsounds", "sound_changeeffectby", "sound_seteffectto",
    "sound_cleareffects", "sound_changevolumeby", "sound_setvolumeto", "sound_volume",
    # events
    "event_whenflagclicked", "event_whenkeypressed", "event_whenstageclicked", "event_whenbackdropswitchesto",
    "event_whengreaterthan", "event_whenbroadcastreceived", "event_broadcast", "event_broadcastandwait",
    # control
    "control_wait", "control_stop", "control_create_clone_of",
    # sensing
    "sensing_askandwait", "sensing_answer", "sensing_keypressed", "sensing_mousedown", "sensing_mousex",
    "sensing_mousey", "sensing_loudness", "sensing_timer", "sensing_resettimer", "sensing_of",
    "sensing_current", "sensing_dayssince2000", "sensing_username",
    # operators
    "operator_random", "operator_gt", "operator_lt", "operator_equals", "operator_join",
    "operator_letter_of", "operator_length", "operator_contains", "operator_mod", "operator_round",
    "operator_mathop", "operator_divide",
    # variables and lists
    "data_variable", "data_setvariableto", "data_changevariableby", "data_showvariable", "data_hidevariable",
    "data_listcontents", "data_addtolist", "data_deleteoflist", "data_deletealloflist", "data_insertatlist",
    "data_replaceitemoflist", "data_itemoflist", "data_itemnumoflist", "data_lengthoflist",
    "data_listcontainsitem", "data_showlist", "data_hidelist",
    # pen: the stage can only erase all
    "pen_clear",
]


def test_stage_has_all_blocks_of_the_stage_palette():
    from pystage.core.stage import CoreStage
    methods = [getattr(CoreStage, name) for name in dir(CoreStage) if callable(getattr(CoreStage, name))]
    available = {m.__name__ for m in methods} | {m.opcode for m in methods if hasattr(m, "opcode")}
    # Python itself does the work of these blocks
    python_native = {"data_variable", "data_listcontents"}
    missing = [opcode for opcode in STAGE_PALETTE if opcode not in available and opcode not in python_native]
    assert missing == []


def test_sprite_only_blocks_are_not_on_the_stage():
    from pystage.core.stage import CoreStage
    for name in ("pen_stamp", "pen_penDown", "motion_movesteps", "looks_say", "sensing_touchingobject_edge"):
        assert not hasattr(CoreStage, name)


def test_point_towards_random_direction(sprite):
    directions = set()
    for _ in range(100):
        sprite.point_towards_random_direction()
        assert -180 <= sprite.direction() <= 180
        directions.add(round(sprite.direction()))
    assert len(directions) > 10


def stage_stopper(self):
    self.wait(0.25)
    self.stop_other_scripts_in_stage()
    log.append("stopped others")


def stage_counter(self):
    while True:
        log.append("tick " + self._core.name if hasattr(self._core, "name") else "tick stage")
        self.wait(0.1)


def test_stop_other_scripts_in_stage(stage, sprite):
    sprite.when_program_starts(stage_counter)
    stage.when_program_starts(stage_counter)
    stage.when_program_starts(stage_stopper)
    run(stage, 0.3)
    assert "stopped others" in log
    log.clear()
    run(stage, 0.5)
    # Only the script of the sprite goes on
    assert log and set(log) == {"tick Sprite"}
    assert not hasattr(stage, "stop_other_scripts_in_sprite")
    assert not hasattr(sprite, "stop_other_scripts_in_stage")


def test_blocks_of_the_stage_as_target(stage, sprite):
    stage.create_variable("score", 7)
    sprite.create_variable("lives", 3, all_sprites=False)
    stage.add_backdrop("default")
    stage.set_volume_to(40)
    # Properties that only sprites have are 0 for the stage, like in Scratch
    for name in ("x_position_of", "y_position_of", "direction_of", "costume_of", "costume_name_of", "size_of"):
        if hasattr(sprite, name):
            assert getattr(sprite, name)("_stage_") == 0, name
    core = sprite._core
    for method in ("sensing_of_xposition", "sensing_of_yposition", "sensing_of_direction",
                   "sensing_of_costumenumber", "sensing_of_costumename", "sensing_of_size"):
        assert getattr(core, method)("_stage_") == 0, method
    # What the stage has
    assert core.sensing_of_variable("score", "_stage_") == 7
    assert core.sensing_of_variable("lives", "_stage_") == 0
    assert core.sensing_of_volume("_stage_") == 40
    assert core.sensing_of_backdropnumber("_stage_") == 1
    assert core.sensing_of_backdropname("_stage_") == "default"
    # and the other way round: sprites do not have a backdrop
    assert core.sensing_of_backdropnumber(sprite) == 0
    assert core.sensing_of_variable("lives", sprite) == 3
    assert core.sensing_of_xposition("no such sprite") == 0
    # The stage can ask for its own values, too
    assert stage._core.sensing_of_xposition("_stage_") == 0
    assert stage._core.sensing_of_variable("score", "_stage_") == 7
    assert stage._core.sensing_of_xposition(sprite) == 0


def test_division_by_zero_is_like_scratch(stage, sprite):
    inf, nan = float("inf"), float("nan")
    assert sprite.divide(1, 0) == inf
    assert sprite.divide(-1, 0) == -inf
    assert sprite.divide("5", "") == inf
    assert sprite.divide(0, 0) != sprite.divide(0, 0), "NaN"
    assert sprite.divide(6, 4) == 1.5 and sprite.divide("6", "3") == 2
    assert sprite.divide("abc", 3) == 0
    assert sprite.modulo(5, 0) != sprite.modulo(5, 0), "NaN"
    assert sprite.modulo(7, 3) == 1 and sprite.modulo(-7, 3) == 2 and sprite.modulo(7, -3) == -2
    assert sprite.modulo(5.5, 2) == 1.5 and sprite.modulo(-5.5, 2) == 0.5
    assert sprite.modulo(5, inf) == 5
    assert stage.divide(1, 0) == inf and stage.modulo(1, 0) != 0
    # Texts from variables behave the same
    stage.create_variable("zero", "0")
    stage.create_variable("one", "1")
    zero, one = sprite.get_variable("zero"), sprite.get_variable("one")
    assert one / zero == inf and -one / zero == -inf and 1 / zero == inf
    assert zero / zero != zero / zero
    assert one % zero != one % zero and 5 % zero != 5 % zero
    assert one / 4 == 0.25 and 7 % (one + 2) == 1
    # The result can be used like in Scratch
    assert sprite.join(sprite.divide(1, 0), "!") == "Infinity!"
    sprite.say(sprite.divide(1, 0))
    assert sprite.round(sprite.divide(7, 2)) == 4


def test_enter_key(stage, sprite):
    sprite.when_key_pressed("enter", on_key)
    stage.when_key_pressed("Enter", on_key)
    for code_manager in stage._core._all_code_managers():
        code_manager.process_key_pressed(pygame.K_RETURN)
    run(stage, frames=2)
    assert log == ["key", "key"]
    assert sprite.key_pressed("enter") is False


def test_all_keys_of_scratch_are_known():
    from pystage.core.constants import KEY_MAPPINGS
    scratch_keys = ["space", "up arrow", "down arrow", "right arrow", "left arrow", "enter"]
    scratch_keys += [chr(c) for c in range(ord("a"), ord("z") + 1)] + [str(d) for d in range(10)]
    assert [key for key in scratch_keys if key not in KEY_MAPPINGS] == []
    # The error message must not promise keys that do not work
    from pystage.core.i18n import MESSAGES
    for texts in MESSAGES.values():
        assert "enter" in texts["bad_key"].lower() or "eingabetaste" in texts["bad_key"].lower()
    assert "enter" in KEY_MAPPINGS


# Values that Scratch accepts but Python does not like

def test_texts_and_infinity_for_numbers(stage, sprite):
    inf = float("inf")
    stage.create_variable("text", "abc")
    stage.create_variable("infinite", "Infinity")
    text, infinite = sprite.get_variable("text"), sprite.get_variable("infinite")
    assert infinite + 1 == inf and infinite > 5 and -infinite < 5
    assert sprite.round(inf) == inf and sprite.letter_of(inf, "abc") == ""
    # Pen and sound blocks calculate with texts like the other blocks
    sprite.set_pen_size_to(text)
    sprite.change_pen_size_by("2")
    assert sprite._core.pen_size == 3
    sprite.set_pen_hue_to(text)
    sprite.change_pen_brightness_by(infinite)
    sprite.set_volume_to(text)
    assert sprite.volume() == 0
    sprite.change_volume_by("50")
    assert sprite.volume() == 50
    sprite.set_pitch_effect_to(text)
    sprite.change_pan_left_right_effect_by(infinite)
    sprite.set_pan_left_right_effect_to(text)


def test_infinity_does_not_break_the_stage(stage, sprite):
    inf = float("inf")
    sprite.go_to_x_y(inf, -inf)
    sprite.move(inf)
    sprite.turn_right(inf)
    sprite.point_in_direction(inf)
    assert sprite.direction() == 90, "like in Scratch, an infinite direction is ignored"
    sprite.set_size_to(inf)
    sprite.go_forward(inf)
    sprite.go_backward(inf)
    for effect in ("color", "fisheye", "whirl", "pixelate", "mosaic", "brightness", "ghost"):
        getattr(sprite, f"set_{effect}_effect_to")(inf)
        getattr(sprite, f"change_{effect}_effect_by")(inf)
    sprite.pen_down()
    sprite.go_to_x_y(0, 0)
    run(stage, frames=3)
    assert sprite.touching_color("#ff0000") in (True, False)


def test_colors_like_in_scratch(sprite):
    from pystage.core.values import to_color
    assert tuple(to_color((255, 0, 0))) == (255, 0, 0, 255)
    assert tuple(to_color("#00ff00")) == (0, 255, 0, 255)
    assert tuple(to_color("#f00")) == (255, 0, 0, 255)
    assert tuple(to_color(0x0000ff)) == (0, 0, 255, 255)
    assert tuple(to_color("16711680")) == (255, 0, 0, 255)
    assert tuple(to_color("no color")) == (0, 0, 0, 255)
    sprite.set_pen_color(0xff0000)
    assert tuple(sprite._core.pen_color) == (255, 0, 0, 255)
    sprite.set_pen_color("nonsense")
    assert tuple(sprite._core.pen_color) == (0, 0, 0, 255)
