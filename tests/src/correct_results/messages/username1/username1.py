# username1 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1", center_x=240, center_y=180)
stage.add_sound("pop")
stage.create_variable("my variable", 0)

# Create and initialize sprite 'bowl'
bowl = stage.add_a_sprite(None)
bowl.set_name("Bowl")
bowl.go_to_x_y(-3, -11)
bowl.add_costume("bowl_a", center_x=30, center_y=15)
bowl.add_sound("pop")

# Scratch Blocks for 'bowl'

def when_program_starts_1(self):
    if self.equals(self.username(), ""):
        self.say_for_seconds("Hello!", 2)
    else:
        self.say(self.join("welcome back ", self.username()))

bowl.when_program_starts(when_program_starts_1)

stage.play()
