# testing_big_list (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable')
stage.create_list_variable("big_list")
stage.initialize_list("big_list", ['thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing'])
stage.show_builtinvariable("data_listcontents")
stage.set_monitor_position("data_listcontents", -235, 175)
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(0)
sprite1.set_y(0)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)
sprite1.initialize_list("groceries", [])
assert sprite1.length_of_list("groceries") == 0
sprite1.add_value_to_list("groceries", "apple")
assert sprite1.item_number_in_list("groceries", "apple") == 1

sprite1.create_list_variable("a")
sprite1.initialize_list("a", [1,2,3,4])
assert sprite1.length_of_list("a") == 4
assert sprite1.item_number_in_list("a", 1) == 1
assert sprite1.item_number_in_list("a", 2) == 2
assert sprite1.item_number_in_list("a", 3) == 3
assert sprite1.list_contains_item("a", 1)
assert not sprite1.list_contains_item("a", 10)
sprite1.add_value_to_list("a", "llll")
assert sprite1.length_of_list("a") == 5
assert sprite1.list_contains_item("a", "llll")


sprite1.delete_value_from_list("a", 0)
assert sprite1.length_of_list("a") == 4
assert not sprite1.list_contains_item("a", 1)

sprite1.delete_all_from_list("a")
assert sprite1.length_of_list("a") == 0

sprite1.initialize_list("b", ["hi", "hello", "hey"])
assert not sprite1.item_in_list("b", 1) == "hello"
assert sprite1.item_in_list("b", 1) == "hi"
assert sprite1.item_in_list("b", 3) == "hey"

sprite1.create_list_variable("c")
sprite1.initialize_list("c", ["a", "b", "c", "d"])
assert sprite1.item_number_in_list("c", "a") == 1
assert sprite1.item_number_in_list("c", "b") == 2
assert sprite1.item_number_in_list("c", "ab") == None
sprite1.replace_item_from_list("c", "z", 0)
assert sprite1.item_number_in_list("c", "z") == 1
assert sprite1.item_number_in_list("c", "b") == 2
sprite1.insert_value_to_list("c", "yes", 5)
assert sprite1.item_number_in_list("c", "yes") == 5
sprite1.insert_value_to_list("c", "insert", 3)
assert sprite1.item_number_in_list("c", "insert") == 3
sprite1.insert_value_to_list("c", "i", 4)
assert sprite1.item_number_in_list("c", "i") == 4

def when_program_starts_1(self):
    for _ in range(10):
        self.add_value_to_list("big_list", "thing")

sprite1.when_program_starts(when_program_starts_1)

stage.play()
