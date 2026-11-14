# cloning2 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1")
stage.add_sound("pop")
stage.create_variable("my variable", 0)

# Create and initialize sprite 'dinosaur1'
dinosaur1 = stage.add_a_sprite(None)
dinosaur1.set_name("Dinosaur1")
dinosaur1.go_to_x_y(49, -5)
dinosaur1.add_costume("dinosaur1_a", center_x=98, center_y=92)
dinosaur1.add_costume("dinosaur1_b", center_x=98, center_y=47)
dinosaur1.add_costume("dinosaur1_c", center_x=81, center_y=91)
dinosaur1.add_costume("dinosaur1_d", center_x=99, center_y=91)
dinosaur1.add_sound("pop")

# Create and initialize sprite 'cheesy_puffs'
cheesy_puffs = stage.add_a_sprite(None)
cheesy_puffs.set_name("Cheesy Puffs")
cheesy_puffs.go_to_x_y(147, -82)
cheesy_puffs.add_costume("cheesy_puffs", center_x=87, center_y=72, factor=2)
cheesy_puffs.add_sound("pop")

# Scratch Blocks for 'dinosaur1'

def when_program_starts_1(self):
    self.create_clone_of_myself()

dinosaur1.when_program_starts(when_program_starts_1)

def when_i_start_as_a_clone_2(self):
    while True:
        self.create_clone_of_myself()
        self.go_to_random_position()
        self.turn_right(15)

dinosaur1.when_i_start_as_a_clone(when_i_start_as_a_clone_2)

# Scratch Blocks for 'cheesy_puffs'

def when_key_pressed_3(self):
    while True:
        self.go_to_random_position()

cheesy_puffs.when_key_pressed("space", when_key_pressed_3)

def when_program_starts_4(self):
    while True:
        self.wait(1)
        self.create_clone_of_myself()
        self.go_to_random_position()

cheesy_puffs.when_program_starts(when_program_starts_4)

stage.play()
