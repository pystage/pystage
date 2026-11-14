# delete_from_list (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1", center_x=240, center_y=180)
stage.add_sound("pop")
stage.create_variable("my variable", 0)
stage.create_list("delete_list_plz", ["thing2"])
stage.show_list("delete_list_plz")
stage.set_list_monitor_position("delete_list_plz", -235, 175, 0, 0)

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.add_costume("costume1", center_x=48, center_y=50)
sprite1.add_costume("costume2", center_x=46, center_y=53)
sprite1.add_sound("meow")

# Scratch Blocks for 'sprite1'

def when_program_starts_1(self):
    self.add_to_list("delete_list_plz", "thing")
    self.add_to_list("delete_list_plz", "thing2")
    self.wait(1)
    self.delete_item_of_list("delete_list_plz", 1)

sprite1.when_program_starts(when_program_starts_1)

stage.play()
