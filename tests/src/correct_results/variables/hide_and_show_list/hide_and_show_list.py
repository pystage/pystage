# hide_and_show_list (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable')
stage.create_list_variable("lo")
list = stage.initialize_list("lo", ['thing', 'ghkghjk', 'thing', 'thing'])
stage.create_list_variable("fruits")
stage.initialize_list("fruits", [])
stage.show_builtinvariable("data_listcontents")
stage.set_monitor_position("data_listcontents", -235, 175)
stage.show_builtinvariable("data_listcontents")
stage.set_monitor_position("data_listcontents", -85, 175)
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(0)
sprite1.set_y(0)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)


def when_program_starts_1(self):

    #list = self.create_list_variable("lo")
    #self.add_value_to_list("lo","stuff")
    print(list)
sprite1.when_program_starts(when_program_starts_1)

stage.play()
