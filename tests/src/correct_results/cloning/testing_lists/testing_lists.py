# testing_lists (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.add_backdrop('field_at_mit')
stage.create_variable('my variable', 0)
stage.create_list_variable("list_test", ['boy', 'boy', 'bug', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'bug', 'whichacallit', 'thing', 'whichacallit', 'small', 'whichacallit', 'large', 'medium', '', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing', 'thing'])
stage.show_list("list_test", -231, 27)
cassy_dance = stage.add_a_sprite(None)
cassy_dance.set_name("Cassy Dance")
cassy_dance.set_x(-123)
cassy_dance.set_y(54)
cassy_dance.go_to_back_layer()
cassy_dance.go_forward(3)
cassy_dance.add_costume('cassy_a', center_x=104, center_y=192, factor=2)
cassy_dance.add_costume('cassy_b', center_x=140, center_y=192, factor=2)
cassy_dance.add_costume('cassy_c', center_x=74, center_y=188, factor=2)
cassy_dance.add_costume('cassy_d', center_x=94, center_y=180, factor=2)
cassy_dance.add_sound('dance_around')

def when_program_starts_1(self):
    self.add_value_to_list("list_test", "thing")
    self.insert_value_to_list("list_test", "boy", 1)
    self.insert_value_to_list("list_test", "whichacallit", 5)
    self.replace_item_from_list("list_test", 3, "bug")

cassy_dance.when_program_starts(when_program_starts_1)

def when_program_starts_2(self):
    self.create_clone_of("NO TRANSLATION: control_create_clone_of_menu")

cassy_dance.when_program_starts(when_program_starts_2)
champ99 = stage.add_a_sprite(None)
champ99.set_name("Champ99")
champ99.set_x(-5)
champ99.set_y(-12)
champ99.go_to_back_layer()
champ99.go_forward(1)
champ99.add_costume('champ99_a', center_x=248, center_y=306, factor=2)
champ99.add_costume('champ99_b', center_x=164, center_y=290, factor=2)
champ99.add_costume('champ99_c', center_x=152, center_y=270, factor=2)
champ99.add_costume('champ99_d', center_x=188, center_y=260, factor=2)
champ99.add_costume('champ99_e', center_x=190, center_y=248, factor=2)
champ99.add_costume('champ99_f', center_x=114, center_y=250, factor=2)
champ99.add_costume('champ99_g', center_x=132, center_y=258, factor=2)
champ99.add_sound('dance_celebrate')
champ99.create_list_variable("list", ['thing'])
champ99.show_list("list", 127, 168)

def when_program_starts_3(self):
    if (self.item_in_list("list", 1) == 50):
        self.hide_list("list")
        self.wait(3.0)
        self.show_list("list")

    if (self.show_length_of_list("list_test") == 60):
        self.replace_item_from_list("list", 1, "thing")

champ99.when_program_starts(when_program_starts_3)
elephant = stage.add_a_sprite(None)
elephant.set_name("Elephant")
elephant.set_x(174)
elephant.set_y(-151)
elephant.go_to_back_layer()
elephant.go_forward(2)
elephant.add_costume('elephant_a', center_x=107, center_y=33)
elephant.add_costume('elephant_b', center_x=95, center_y=40)
elephant.add_sound('pop')
elephant.create_list_variable("elle", [])
elephant.show_list("elle", -81, 151)

def when_program_starts_4(self):
    while not self.list_contains_item("elle", "bob"):
        pass

    self.delete_value_from_list("elle", 1)
    self.add_value_to_list("elle", "thing")
    self.insert_value_to_list("elle", "thing", 2)

elephant.when_program_starts(when_program_starts_4)

def when_program_starts_5(self):
    self.wait(3.0)
    self.add_value_to_list("elle", "bob")
    if ((5.0 % self.show_length_of_list("elle")) > 4):
        self.delete_all_from_list("elle")
        self.create_clone_of("NO TRANSLATION: control_create_clone_of_menu")
        self.create_clone_of("NO TRANSLATION: control_create_clone_of_menu")

elephant.when_program_starts(when_program_starts_5)
stage.play()
