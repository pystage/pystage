# block3 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable', 0)
stage.create_list_variable("car", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54])
stage.show_list("car", 138, 180)
convertible_2 = stage.add_a_sprite(None)
convertible_2.set_name("Convertible 2")
convertible_2.set_x(48)
convertible_2.set_y(120)
convertible_2.go_to_back_layer()
convertible_2.go_forward(1)
convertible_2.add_costume('convertible_3', center_x=75, center_y=75)
convertible_2.add_sound('pop')

def when_program_starts_1(self):
    "NO TRANSLATION: procedures_call"

convertible_2.when_program_starts(when_program_starts_1)

def when_i_start_as_a_clone_2(self):
    self.show()

convertible_2.when_i_start_as_a_clone(when_i_start_as_a_clone_2)
stage.play()
