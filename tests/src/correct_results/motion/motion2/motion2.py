# motion2 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable', 0)
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(10)
sprite1.set_y(20)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.point_in_direction(23.08291951430904)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)
sprite1.add_sound('meow')

def when_program_starts_1(self):
    self.point_in_direction(180.0)
    self.glide_to_random_position(2.0)
    self.point_towards_mouse_pointer()
    self.change_x_by(-10.0)
    self.set_x(10.0)
    self.change_y_by(-20.0)
    self.set_y(20.0)

sprite1.when_program_starts(when_program_starts_1)
stage.play()
