# item_of_list (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1")
stage.add_sound("pop")
stage.create_variable("my variable", 0)
stage.create_list("second list", ["branden", "branden", "branden", "thing", "branden", "thing"])
stage.show_list("second list")
stage.set_list_monitor_position("second list", 84, 170, 0, 0)

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.go_to_x_y(-39, -39)
sprite1.add_costume("costume1", center_x=48, center_y=50)
sprite1.add_costume("costume2", center_x=46, center_y=53)
sprite1.add_sound("meow")

# Scratch Blocks for 'sprite1'

def when_program_starts_1(self):
    self.say(self.item_of_list("second list", 1))
    self.wait(1)
    self.say(self.item_of_list("second list", 4))

sprite1.when_program_starts(when_program_starts_1)

def when_program_starts_2(self):
    self.add_to_list("second list", "branden")
    self.add_to_list("second list", "thing")

sprite1.when_program_starts(when_program_starts_2)

stage.play()
