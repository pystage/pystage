# username1 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable', 0)
bowl = stage.add_a_sprite(None)
bowl.set_name("Bowl")
bowl.set_x(-3)
bowl.set_y(-11)
bowl.go_to_back_layer()
bowl.go_forward(1)
bowl.add_costume('bowl_a', center_x=30, center_y=15)
bowl.add_sound('pop')

def when_program_starts_1(self):
    if (self.username() == ""):
        self.say_for_seconds("Hello!", 2.0)
    else:
        self.say("".join(["welcome back ", self.username()]))

bowl.when_program_starts(when_program_starts_1)
stage.play()
