# motion3 (pyStage, converted from Scratch 3)
#
# Not everything of the Scratch project could be converted:
# - [monitor] Sprite1: The monitor for 'motion_xposition' is not supported and was left out.
# - [monitor] Sprite1: The monitor for 'motion_yposition' is not supported and was left out.
# - [monitor] Sprite1: The monitor for 'motion_direction' is not supported and was left out.

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1", center_x=240, center_y=180)
stage.add_sound("pop")
stage.create_variable("my variable", 0)

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.go_to_x_y(216.2211115722656, -156.0312922363281)
sprite1.point_in_direction(-82.71618147372726)
sprite1.set_rotation_style_left_right()
sprite1.add_costume("costume1", center_x=48, center_y=50)
sprite1.add_costume("costume2", center_x=46, center_y=53)
sprite1.add_sound("meow")

# Scratch Blocks for 'sprite1'

def when_program_starts_1(self):
    self.glide_to_x_y(1, -1000, -1000)
    self.if_on_edge_bounce()
    self.set_rotation_style_around()
    self.wait(1)
    self.glide_to_x_y(1, 1000, -1000)
    self.if_on_edge_bounce()
    self.set_rotation_style_left_right()
    self.wait(1)
    self.glide_to_x_y(1, 1000, -1000)
    self.if_on_edge_bounce()
    self.set_rotation_style_none()

sprite1.when_program_starts(when_program_starts_1)

stage.play()
