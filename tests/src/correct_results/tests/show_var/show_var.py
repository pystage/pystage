# show_var (pyStage, converted from Scratch 3)
#
# Not everything of the Scratch project could be converted:
# - [monitor] Stage: The monitor for 'sensing_timer' is not supported and was left out.
# - [monitor] Sprite1: The monitor for 'motion_xposition' is not supported and was left out.
# - [monitor] Sprite1: The monitor for 'motion_yposition' is not supported and was left out.
# - [monitor] Sprite1: The monitor for 'motion_direction' is not supported and was left out.
# - [monitor] Sprite1: The monitor for 'looks_costumenumbername' is not supported and was left out (2 monitors).
# - [monitor] Stage: The monitor for 'looks_backdropnumbername' is not supported and was left out (2 monitors).
# - [monitor] Sprite1: The monitor for 'looks_size' is not supported and was left out.
# - [monitor] Sprite1: The monitor for 'sound_volume' is not supported and was left out.
# - [monitor] Stage: The monitor for 'sensing_answer' is not supported and was left out.
# - [monitor] Stage: The monitor for 'sensing_loudness' is not supported and was left out.
# - [monitor] Stage: The monitor for 'sensing_current' is not supported and was left out (7 monitors).
# - [monitor] Stage: The monitor for 'sensing_username' is not supported and was left out.

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1", center_x=240, center_y=180)
stage.add_sound("pop")
stage.create_variable("my variable", 29)
stage.create_list("list", ["asdfasdfasdfasdfasdfasfd"])
stage.show_variable("my variable")
stage.set_monitor_position("my variable", -35, 94)
stage.show_list("list")
stage.set_list_monitor_position("list", 82, 64, 100, 200)

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.go_to_x_y(-32, -12)
sprite1.add_costume("costume1", center_x=48, center_y=50)
sprite1.add_costume("costume2", center_x=46, center_y=53)
sprite1.add_sound("meow")
sprite1.create_list("a", [], all_sprites=False)

# Scratch Blocks for 'sprite1'

def when_program_starts_1(self):
    self.set_variable("my variable", 10)

sprite1.when_program_starts(when_program_starts_1)

stage.play()
