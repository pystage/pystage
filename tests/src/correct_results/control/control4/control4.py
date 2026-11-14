# control4 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1")
stage.add_sound("pop")
stage.create_variable("my variable", 0)

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.go_to_x_y(-107, -49)
sprite1.add_costume("costume1", center_x=48, center_y=50)
sprite1.add_costume("costume2", center_x=46, center_y=53)
sprite1.add_sound("meow")

# Scratch Blocks for 'sprite1'

def when_i_start_as_a_clone_1(self):
    while not self.key_pressed("space"):
        pass
    self.delete_this_clone()

sprite1.when_i_start_as_a_clone(when_i_start_as_a_clone_1)

def when_program_starts_2(self):
    self.create_clone_of_myself()
    while not self.key_pressed("a"):
        pass
    self.stop_all()

sprite1.when_program_starts(when_program_starts_2)

stage.play()
