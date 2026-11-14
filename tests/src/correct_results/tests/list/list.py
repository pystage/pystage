# list (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1", center_x=240, center_y=180)
stage.add_sound("pop")
stage.create_variable("my variable", 0)
stage.create_list("fruits", ["pineapple", "apple", "peach", "pear", "banana"])
stage.show_list("fruits")
stage.set_list_monitor_position("fruits", -235, 175, 0, 0)

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.add_costume("costume1", center_x=48, center_y=50)
sprite1.add_costume("costume2", center_x=46, center_y=53)
sprite1.add_sound("meow")

# Scratch Blocks for 'sprite1'

def when_program_starts_1(self):
    self.delete_all_of_list("fruits")
    for _ in range(3):
        self.add_to_list("fruits", "apple")
    self.wait(1)
    self.add_to_list("fruits", "pear")
    self.wait(1)
    self.add_to_list("fruits", "banana")
    self.wait(1)
    self.delete_item_of_list("fruits", 1)
    self.wait(1)
    self.insert_at_list("fruits", "peach", 3)
    self.wait(1)
    self.replace_item_of_list("fruits", 1, "pineapple")
    self.wait(1)
    self.say_for_seconds(self.item_of_list("fruits", 1), 2)
    self.wait(1)
    self.say_for_seconds(self.item_number_in_list("fruits", "banana"), 2)
    self.wait(1)
    self.say_for_seconds(self.length_of_list("fruits"), 2)
    self.wait(1)
    self.say_for_seconds(self.list_contains("fruits", "banana"), 2)
    self.wait(1)
    self.hide_list("fruits")

sprite1.when_program_starts(when_program_starts_1)

def when_this_sprite_clicked_2(self):
    self.show_list("fruits")

sprite1.when_this_sprite_clicked(when_this_sprite_clicked_2)

stage.play()
