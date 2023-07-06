# sensing3 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.add_backdrop('castle_3')
stage.create_variable('my variable', 0)
stage.show_builtinvariable("timer", -235, 148)
stage.show_builtinvariable("current_year", -235, 175)
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(293)
sprite1.set_y(13)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.point_in_direction(-126)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)
sprite1.add_sound('meow')

def when_program_starts_1(self):
    self.set_drag_mode_draggable()

sprite1.when_program_starts(when_program_starts_1)

def when_program_starts_2(self):
    self.go_to_sprite(self.backdrop_of("NO TRANSLATION: sensing_of_object_menu"))
    self.reset_timer()

sprite1.when_program_starts(when_program_starts_2)

def when_key_pressed_3(self):
    self.point_in_direction(self.mouse_x())

sprite1.when_key_pressed("space", when_key_pressed_3)

def when_key_pressed_4(self):
    self.point_in_direction(self.mouse_y())

sprite1.when_key_pressed("y", when_key_pressed_4)

def when_program_starts_5(self):
    self.change_x_by(self.days_since())

sprite1.when_program_starts(when_program_starts_5)
cat = stage.add_a_sprite(None)
cat.set_name("Cat")
cat.set_x(-69)
cat.set_y(-75)
cat.go_to_back_layer()
cat.go_forward(2)
cat.add_costume('costume1', center_x=48, center_y=50)
cat.add_costume('costume2', center_x=46, center_y=53)
cat.add_sound('meow')

def when_key_pressed_6(self):
    self.point_in_direction(self.mouse_x())

cat.when_key_pressed("space", when_key_pressed_6)

def when_key_pressed_7(self):
    self.point_in_direction(self.mouse_y())

cat.when_key_pressed("y", when_key_pressed_7)

def when_program_starts_8(self):
    self.go_to_sprite(self.backdrop_of("NO TRANSLATION: sensing_of_object_menu"))
    self.reset_timer()

cat.when_program_starts(when_program_starts_8)

def when_program_starts_9(self):
    self.set_drag_mode_draggable()

cat.when_program_starts(when_program_starts_9)

def when_program_starts_10(self):
    self.change_x_by(self.days_since())

cat.when_program_starts(when_program_starts_10)
stage.play()
