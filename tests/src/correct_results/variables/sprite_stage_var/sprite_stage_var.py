# sprite_stage_var (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('stage_var')
stage.show_variable("stage_var")
stage.set_monitor_position("stage_var", -235, 148)

def when_GREENFLAG_clicked_1(self):
    self.set_variable("stage_var", 0)

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
sprite1.create_variable('sprite_var')
sprite1.show_variable("sprite_var")
sprite1.set_monitor_position("sprite_var", -235, 175)

def when_program_starts_2(self):
    self.set_variable("sprite_var", 5)

sprite1.when_program_starts(when_program_starts_2)

stage.play()
