# cloning_sprites_and_testing_variables_using_lists (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.add_backdrop('field_at_mit')
stage.create_variable('my variable')
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
    "NO TRANSLATION: data_addtolist"
    "NO TRANSLATION: data_insertatlist"
    "NO TRANSLATION: data_insertatlist"
    "NO TRANSLATION: data_replaceitemoflist"

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

def when_program_starts_3(self):
    if ("NO TRANSLATION: data_itemoflist" == 50):
        "NO TRANSLATION: data_hidelist"
        self.wait(3.0)
        "NO TRANSLATION: data_showlist"

    if ("NO TRANSLATION: data_lengthoflist" == 60):
        "NO TRANSLATION: data_replaceitemoflist"

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

def when_program_starts_4(self):
    while not "NO TRANSLATION: data_listcontainsitem":
        pass

    "NO TRANSLATION: data_deleteoflist"
    "NO TRANSLATION: data_addtolist"
    "NO TRANSLATION: data_insertatlist"

elephant.when_program_starts(when_program_starts_4)

def when_program_starts_5(self):
    self.wait(3.0)
    "NO TRANSLATION: data_addtolist"
    if ((5.0 % "NO TRANSLATION: data_lengthoflist") > 4):
        "NO TRANSLATION: data_deletealloflist"
        self.create_clone_of("NO TRANSLATION: control_create_clone_of_menu")
        self.create_clone_of("NO TRANSLATION: control_create_clone_of_menu")

elephant.when_program_starts(when_program_starts_5)

stage.play()
