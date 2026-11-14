# control5 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1")
stage.add_backdrop("boardwalk")
stage.switch_backdrop_to("boardwalk")
stage.add_sound("pop")
stage.create_variable("my variable", 0)

# Create and initialize sprite 'broom'
broom = stage.add_a_sprite(None)
broom.set_name("Broom")
broom.go_to_x_y(113, -54)
broom.hide()
broom.add_costume("broom", center_x=131.1, center_y=21.100000000000023)
broom.add_sound("pop")

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.go_to_x_y(64, -6)
sprite1.set_size_to(190)
sprite1.add_costume("costume1", center_x=73.76648930018897, center_y=100.95969430024343)
sprite1.add_costume("costume2", center_x=46, center_y=53)
sprite1.add_sound("meow")

# Scratch Blocks for 'broom'

def when_program_starts_1(self):
    while not self.touching_edge():
        self.move(10)
    self.hide()

broom.when_program_starts(when_program_starts_1)

# Scratch Blocks for 'sprite1'

def when_program_starts_2(self):
    while not self.touching_edge():
        self.move(10)
        self.change_size_by(30)

sprite1.when_program_starts(when_program_starts_2)

stage.play()
