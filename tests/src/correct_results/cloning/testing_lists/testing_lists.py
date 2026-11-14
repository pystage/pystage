# testing_lists (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1", center_x=240, center_y=180)
stage.add_backdrop("field_at_mit", center_x=480, center_y=360, factor=2)
stage.add_sound("pop")
stage.create_variable("my variable", 0)
stage.create_list("list_test", ["boy", "boy", "bug", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "bug", "whichacallit", "thing", "whichacallit", "small", "whichacallit", "large", "medium", "", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing", "thing"])
stage.show_list("list_test")
stage.set_list_monitor_position("list_test", -231, 27, 100, 200)

# Create and initialize sprite 'champ99'
champ99 = stage.add_a_sprite(None)
champ99.set_name("Champ99")
champ99.go_to_x_y(-5, -12)
champ99.add_costume("champ99_a", center_x=248, center_y=306, factor=2)
champ99.add_costume("champ99_b", center_x=164, center_y=290, factor=2)
champ99.add_costume("champ99_c", center_x=152, center_y=270, factor=2)
champ99.add_costume("champ99_d", center_x=188, center_y=260, factor=2)
champ99.add_costume("champ99_e", center_x=190, center_y=248, factor=2)
champ99.add_costume("champ99_f", center_x=114, center_y=250, factor=2)
champ99.add_costume("champ99_g", center_x=132, center_y=258, factor=2)
champ99.add_sound("dance_celebrate")
champ99.create_list("list", ["thing"], all_sprites=False)
champ99.show_list("list")
champ99.set_list_monitor_position("list", 127, 168, 0, 0)

# Create and initialize sprite 'elephant'
elephant = stage.add_a_sprite(None)
elephant.set_name("Elephant")
elephant.go_to_x_y(174, -151)
elephant.add_costume("elephant_a", center_x=107, center_y=33)
elephant.add_costume("elephant_b", center_x=95, center_y=40)
elephant.add_sound("pop")
elephant.create_list("elle", [], all_sprites=False)
elephant.show_list("elle")
elephant.set_list_monitor_position("elle", -81, 151, 0, 0)

# Create and initialize sprite 'cassy_dance'
cassy_dance = stage.add_a_sprite(None)
cassy_dance.set_name("Cassy Dance")
cassy_dance.go_to_x_y(-123, 54)
cassy_dance.add_costume("cassy_a", center_x=104, center_y=192, factor=2)
cassy_dance.add_costume("cassy_b", center_x=140, center_y=192, factor=2)
cassy_dance.add_costume("cassy_c", center_x=74, center_y=188, factor=2)
cassy_dance.add_costume("cassy_d", center_x=94, center_y=180, factor=2)
cassy_dance.add_sound("dance_around")

# Scratch Blocks for 'champ99'

def when_program_starts_1(self):
    if (self.item_of_list("list", 1) == 50):
        self.hide_list("list")
        self.wait(3)
        self.show_list("list")
    if (self.length_of_list("list_test") == 60):
        self.replace_item_of_list("list", 1, "thing")

champ99.when_program_starts(when_program_starts_1)

# Scratch Blocks for 'elephant'

def when_program_starts_2(self):
    while not self.list_contains("elle", "bob"):
        pass
    self.delete_item_of_list("elle", 1)
    self.add_to_list("elle", "thing")
    self.insert_at_list("elle", "thing", 2)

elephant.when_program_starts(when_program_starts_2)

def when_program_starts_3(self):
    self.wait(3)
    self.add_to_list("elle", "bob")
    if (self.modulo(5, self.length_of_list("elle")) > 4):
        self.delete_all_of_list("elle")
        self.create_clone_of_myself()
        self.create_clone_of_sprite(champ99)

elephant.when_program_starts(when_program_starts_3)

# Scratch Blocks for 'cassy_dance'

def when_program_starts_4(self):
    self.add_to_list("list_test", "thing")
    self.insert_at_list("list_test", "boy", 1)
    self.insert_at_list("list_test", "whichacallit", 5)
    self.replace_item_of_list("list_test", 3, "bug")

cassy_dance.when_program_starts(when_program_starts_4)

def when_program_starts_5(self):
    self.create_clone_of_myself()

cassy_dance.when_program_starts(when_program_starts_5)

stage.play()
