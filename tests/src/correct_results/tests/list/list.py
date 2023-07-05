# list (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable', 0)
stage.create_list_variable("fruits", ['pineapple', 'apple', 'peach', 'pear', 'banana'])
stage.show_list("fruits", -235, 175)
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(0)
sprite1.set_y(0)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)
sprite1.add_sound('meow')

def when_program_starts_1(self):
    self.delete_all_from_list("fruits")
    for _ in range(3):
        self.add_value_to_list("fruits", "apple")

    self.wait(1.0)
    self.add_value_to_list("fruits", "pear")
    self.wait(1.0)
    self.add_value_to_list("fruits", "banana")
    self.wait(1.0)
    self.delete_value_from_list("fruits", 1)
    self.wait(1.0)
    self.insert_value_to_list("fruits", "peach", 3)
    self.wait(1.0)
    self.replace_item_from_list("fruits", 1, "pineapple")
    self.wait(1.0)
    self.say_for_seconds(self.item_in_list("fruits", 1), 2.0)
    self.wait(1.0)
    self.say_for_seconds(self.item_number_in_list("fruits", "banana"), 2.0)
    self.wait(1.0)
    self.say_for_seconds(self.show_length_of_list("fruits"), 2.0)
    self.wait(1.0)
    self.say_for_seconds(self.list_contains_item("fruits", "banana"), 2.0)
    self.wait(1.0)
    self.hide_list("fruits")

sprite1.when_program_starts(when_program_starts_1)

def when_this_sprite_clicked_2(self):
    self.show_list("fruits")

sprite1.when_this_sprite_clicked(when_this_sprite_clicked_2)
stage.play()
