# variables1 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1")
stage.add_sound("pop")
stage.create_variable("my variable", 0)
stage.create_variable("a", 11)
stage.show_variable("my variable")
stage.set_monitor_position("my variable", -235, 175)

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.add_costume("costume1", center_x=48, center_y=50)
sprite1.add_costume("costume2", center_x=46, center_y=53)
sprite1.add_sound("meow")

# Scratch Blocks for 'sprite1'

def when_program_starts_1(self):
    self.show_variable("a")
    self.set_variable("a", 10)
    self.wait(1)
    self.change_variable_by("a", 1)
    self.wait(1)
    self.hide_variable("a")

sprite1.when_program_starts(when_program_starts_1)

stage.play()
