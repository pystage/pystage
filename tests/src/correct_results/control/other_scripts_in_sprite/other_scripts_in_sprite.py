# other_scripts_in_sprite (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable')
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(0)
sprite1.set_y(0)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)


def when_program_starts_1(self):
    self.stop_other_scripts_in_sprite()
    self.go_to_random_position()
    self.glide_to_x_y(1.0, 0.0, 0.0)

sprite1.when_program_starts(when_program_starts_1)

def when_program_starts_2(self):
    self.wait(1.0)
    self.say("Hello!")

sprite1.when_program_starts(when_program_starts_2)

def when_program_starts_3(self):
    self.wait(1.0)
    self.move(100.0)

sprite1.when_program_starts(when_program_starts_3)

stage.play()
