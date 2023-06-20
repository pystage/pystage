# motion3 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable')
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(216.2211115722656)
sprite1.set_y(-156.0312922363281)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.point_in_direction(-82.71618147372726)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)
sprite1.add_sound('meow')

def when_program_starts_1(self):
    self.glide_to_x_y(1.0, -1000.0, -1000.0)
    self.if_on_edge_bounce()
    self.set_rotation_style_around()
    self.wait(1.0)
    self.glide_to_x_y(1.0, 1000.0, -1000.0)
    self.if_on_edge_bounce()
    self.set_rotation_style_left_right()
    self.wait(1.0)
    self.glide_to_x_y(1.0, 1000.0, -1000.0)
    self.if_on_edge_bounce()
    self.set_rotation_style_none()

sprite1.when_program_starts(when_program_starts_1)

stage.play()
