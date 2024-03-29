# show_var (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable', 29)
stage.create_list_variable("list", ['asdfasdfasdfasdfasdfasfd'])
stage.show_builtinvariable("timer", -235, 175)
stage.show_builtinvariable("backdrop_number", -235, 7)
stage.show_builtinvariable("backdrop_name", -235, -20)
stage.show_builtinvariable("answer", -85, 175)
stage.show_builtinvariable("loudness", -85, -47)
stage.show_builtinvariable("current_year", -35, 148)
stage.show_builtinvariable("username", -35, 121)
stage.show_variable("my variable", -35, 94)
stage.show_list("list", 82, 64)
stage.show_builtinvariable("current_month", -35, 7)
stage.show_builtinvariable("current_date", -35, -20)
stage.show_builtinvariable("current_dayofweek", 65, 175)
stage.show_builtinvariable("current_hour", -35, -74)
stage.show_builtinvariable("current_minute", 65, 148)
stage.show_builtinvariable("current_second", 115, 121)
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(-32)
sprite1.set_y(-12)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)
sprite1.add_sound('meow')
sprite1.create_list_variable("a", [])
sprite1.show_builtinvariable("x_position", -235, 148)
sprite1.show_builtinvariable("y_position", -240, 88)
sprite1.show_builtinvariable("direction", -237, 118)
sprite1.show_builtinvariable("costume_number", -235, 61)
sprite1.show_builtinvariable("costume_name", -235, 34)
sprite1.show_builtinvariable("size", -235, -47)
sprite1.show_builtinvariable("volume", -235, -74)

def when_program_starts_1(self):
    self.set_variable("my variable", 10)

sprite1.when_program_starts(when_program_starts_1)
stage.play()
