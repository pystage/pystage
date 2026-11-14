# lists_monitors (pyStage, converted from Scratch 3)
#
# Not everything of the Scratch project could be converted:
# - [monitor] Sprite1: The slider of variable 'local' is shown as a normal monitor.

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1", center_x=240, center_y=180)
stage.add_backdrop("backdrop2", center_x=240, center_y=180)
stage.add_sound("pop")
stage.create_variable("global", 1)
stage.create_list("fruits", ["apple", "banana", "cherry"])
stage.show_variable("global")
stage.set_monitor_position("global", -235, 175)
stage.show_variable("global")
stage.set_monitor_position("global", -235, 140)
stage.set_monitor_style_large("global")
stage.show_list("fruits")
stage.set_list_monitor_position("fruits", -40, 175, 150, 100)

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.add_costume("costume1", center_x=20, center_y=20)
sprite1.add_costume("costume2", center_x=20, center_y=20)
sprite1.add_sound("meow")
sprite1.create_variable("local", "x", all_sprites=False)
sprite1.create_list("mine", [1, 2, 3], all_sprites=False)
sprite1.show_variable("local")
sprite1.set_monitor_position("local", -235, 100)
sprite1.show_list("mine")
sprite1.set_list_monitor_position("mine", -40, 30, 150, 100)

# Scratch Blocks for 'stage'

def when_program_starts_1(self):
    self.add_to_list("fruits", self.length_of_list("fruits"))
    self.hide_list("fruits")
    self.show_list("fruits")
    self.hide_variable("global")
    self.show_variable("global")

stage.when_program_starts(when_program_starts_1)

# Scratch Blocks for 'sprite1'

def when_program_starts_2(self):
    self.set_variable("global", 5)
    self.change_variable_by("global", 2)
    self.set_variable("local", self.get_variable("global"))
    self.show_variable("local")
    self.hide_variable("local")
    self.show_variable("local")
    self.add_to_list("fruits", "date")
    self.insert_at_list("fruits", "apricot", 1)
    self.insert_at_list("fruits", "zucchini", "last")
    self.replace_item_of_list("fruits", 2, "avocado")
    self.replace_item_of_list("fruits", "random", "mango")
    self.delete_item_of_list("fruits", 1)
    self.delete_item_of_list("fruits", "last")
    self.set_variable("local", self.item_of_list("fruits", 1))
    self.set_variable("local", self.item_of_list("fruits", "random"))
    self.set_variable("local", self.item_number_in_list("fruits", "banana"))
    self.set_variable("local", self.length_of_list("fruits"))
    if self.list_contains("fruits", "banana"):
        self.add_to_list("mine", self.get_list("fruits"))
    self.show_list("mine")
    self.hide_list("mine")
    self.show_list("mine")
    self.delete_all_of_list("mine")
    self.add_to_list("mine", self.get_variable("local"))

sprite1.when_program_starts(when_program_starts_2)

stage.play()
