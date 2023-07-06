# events5 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable', 0)
stage.show_builtinvariable("loudness", -224, 137)
stage.show_builtinvariable("timer", -223, 167)
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(0)
sprite1.set_y(0)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)
sprite1.add_sound('meow')

def when_timer_greater_than_1(self):
    self.say("timer greater than 3")

sprite1.when_timer_greater_than(3.0, when_timer_greater_than_1)

def when_loudness_greater_than_2(self):
    self.say("loudness greater than 1")

sprite1.when_loudness_greater_than(1.0, when_loudness_greater_than_2)
stage.play()
