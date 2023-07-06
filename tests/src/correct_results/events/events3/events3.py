# events3 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable', 0)
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(0)
sprite1.set_y(0)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)
sprite1.add_sound('meow')

def when_this_sprite_clicked_1(self):
    self.say("Sprite clicked")

sprite1.when_this_sprite_clicked(when_this_sprite_clicked_1)

def when_program_starts_2(self):
    self.say("Runned")

sprite1.when_program_starts(when_program_starts_2)

def when_key_pressed_3(self):
    self.say("Space pressed")

sprite1.when_key_pressed("space", when_key_pressed_3)
stage.play()
