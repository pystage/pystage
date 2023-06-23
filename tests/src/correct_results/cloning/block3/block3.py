# block3 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable')
stage.show_builtinvariable("data_listcontents")
stage.set_monitor_position("data_listcontents", 138, 180)
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
