# motion3 (pyStage, converted from Scratch 3)

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
sprite1.show_monitor("motion_xposition")
sprite1.set_value_monitor_position("motion_xposition", -235, 175)
sprite1.show_monitor("motion_yposition")
sprite1.set_value_monitor_position("motion_yposition", -235, 148)
sprite1.show_monitor("motion_direction")
sprite1.set_value_monitor_position("motion_direction", -235, 121)

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
