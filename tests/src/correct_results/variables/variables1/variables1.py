# variables1 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable', 0)
stage.create_variable('a', 11)
stage.show_variable("my variable", -235, 175)
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(0)
sprite1.set_y(0)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)
sprite1.add_sound('meow')

def when_program_starts_1(self):
    self.show_variable("a")
    self.set_variable("a", 10)
    self.wait(1.0)
    self.change_variable_by("a", 1.0)
    self.wait(1.0)
    self.hide_variable("a")

sprite1.when_program_starts(when_program_starts_1)
stage.play()
