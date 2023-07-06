# motion1 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable', 0)
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(-185.162)
sprite1.set_y(58.461999999999996)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.point_in_direction(-90.35745470593531)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)
sprite1.add_sound('meow')

def when_program_starts_1(self):
    self.move(80.0)
    self.turn_left(180.0)
    self.turn_right(90.0)
    self.go_to_random_position()
    self.go_to_x_y(15.0, -111.0)
    self.glide_to_random_position(1.0)
    self.go_to_mouse_pointer()
    self.glide_to_x_y(1.0, -188.0, 14.0)
    self.glide_to_mouse_pointer(1.0)

sprite1.when_program_starts(when_program_starts_1)
stage.play()
