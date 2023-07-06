# add_list_for_sprite_and_stage (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable', 0)
stage.create_list_variable("list_in_Sprite1", [])
stage.create_list_variable("list_for_stage", ['stage'])
stage.show_list("list_for_stage", -85, 175)

def when_GREENFLAG_clicked_1(self):
    self.wait_seconds(1.0)
    self.add_value_to_list("list_for_stage", "stage")

stage.when_GREENFLAG_clicked(when_GREENFLAG_clicked_1)
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(0)
sprite1.set_y(0)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)
sprite1.add_sound('meow')
sprite1.create_list_variable("list_for_sprite", ['sprite'])
sprite1.show_list("list_for_sprite", -235, 175)

def when_program_starts_2(self):
    self.add_value_to_list("list_for_sprite", "sprite")

sprite1.when_program_starts(when_program_starts_2)
stage.play()
