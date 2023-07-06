# comment (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage


"""
# Stage

comment for backdrop1
"""
stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable', 0)

"""
# Sprite1

comment for sprite1
multiline
comment2 for sprite1
"""
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
    self.say_for_seconds("Hello!", 2.0)  # comment for say hello 

sprite1.when_program_starts(when_program_starts_1)

def when_key_pressed_2(self):
    """
    comment fot when space key pressed
    """
    self.say("Aha")  # comment for say Aha | multiline

sprite1.when_key_pressed("space", when_key_pressed_2)
stage.play()
