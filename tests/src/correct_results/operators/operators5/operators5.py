# operators5 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1", center_x=240, center_y=180)
stage.add_sound("pop")
stage.create_variable("my variable", 0)

# Create and initialize sprite 'cake'
cake = stage.add_a_sprite(None)
cake.set_name("Cake")
cake.go_to_x_y(23, -34)
cake.add_costume("cake_a", center_x=64, center_y=50)
cake.add_costume("cake_b", center_x=64, center_y=42)
cake.add_sound("birthday")

# Scratch Blocks for 'cake'

def when_program_starts_1(self):
    if (self.pick_random(1, 10) > 5):
        self.start_sound("birthday")
    else:
        self.wait((2 % 5))
        self.change_size_by(-10)

cake.when_program_starts(when_program_starts_1)

stage.play()
