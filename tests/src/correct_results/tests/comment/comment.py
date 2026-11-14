# comment (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1")
stage.add_sound("pop")
stage.create_variable("my variable", 0)

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.add_costume("costume1", center_x=48, center_y=50)
sprite1.add_costume("costume2", center_x=46, center_y=53)
sprite1.add_sound("meow")

# Scratch Blocks for 'sprite1'

def when_program_starts_1(self):
    # comment for say hello
    self.say_for_seconds("Hello!", 2)

sprite1.when_program_starts(when_program_starts_1)

# comment for key pressed
# comment fot when space key pressed
def when_key_pressed_2(self):
    # comment for say Aha
    # multiline
    self.say("Aha")

sprite1.when_key_pressed("space", when_key_pressed_2)

stage.play()
