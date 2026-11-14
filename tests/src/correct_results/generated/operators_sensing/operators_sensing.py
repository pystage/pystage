# operators_sensing (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1", center_x=240, center_y=180)
stage.add_backdrop("backdrop2", center_x=240, center_y=180)
stage.add_sound("pop")
stage.create_variable("zero", 0)
stage.create_variable("text", "abc")
stage.create_variable("result", 0)

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.add_costume("costume1", center_x=20, center_y=20)
sprite1.add_costume("costume2", center_x=20, center_y=20)
sprite1.add_sound("meow")
sprite1.create_variable("copy", 0, all_sprites=False)

# Create and initialize sprite 'sprite2'
sprite2 = stage.add_a_sprite(None)
sprite2.set_name("Sprite2")
sprite2.add_costume("costume1_2", center_x=20, center_y=20)
sprite2.add_costume("costume2_2", center_x=20, center_y=20)
sprite2.add_sound("meow")
sprite2.create_variable("local", 5, all_sprites=False)

# Scratch Blocks for 'sprite1'

def when_program_starts_1(self):
    self.set_variable("result", (1 + (5 - 2)))
    self.set_variable("result", (3 * 4))
    self.set_variable("result", (10 / 4))
    self.set_variable("result", self.divide(1, 0))
    self.set_variable("result", self.divide(1, self.get_variable("zero")))
    self.set_variable("result", (self.get_variable("text") / 2))
    self.set_variable("result", (10 % 3))
    self.set_variable("result", (-7 % 3))
    self.set_variable("result", self.modulo(5, self.get_variable("zero")))
    self.set_variable("result", self.pick_random(1, 10))
    self.set_variable("result", self.pick_random(0.5, 2.5))
    self.set_variable("result", self.join("apple ", "banana"))
    self.set_variable("result", self.letter_of(2, "apple"))
    self.set_variable("result", self.length_of("apple"))
    self.set_variable("result", self.contains("apple", "PP"))
    self.set_variable("result", self.round(2.5))
    self.set_variable("result", (5 > 3))
    self.set_variable("result", self.less_than("apple", "Banana"))
    self.set_variable("result", self.equals(self.get_variable("text"), "ABC"))
    self.set_variable("result", ((2 > 1) and (1 < 2)))
    self.set_variable("result", ((1 == 2) or self.mouse_down()))
    self.set_variable("result", not (self.key_pressed("space")))
    self.set_variable("result", self.math_function("abs", 30))
    self.set_variable("result", self.math_function("floor", 30))
    self.set_variable("result", self.math_function("ceiling", 30))
    self.set_variable("result", self.math_function("sqrt", 30))
    self.set_variable("result", self.math_function("sin", 30))
    self.set_variable("result", self.math_function("cos", 30))
    self.set_variable("result", self.math_function("tan", 30))
    self.set_variable("result", self.math_function("asin", 30))
    self.set_variable("result", self.math_function("acos", 30))
    self.set_variable("result", self.math_function("atan", 30))
    self.set_variable("result", self.math_function("ln", 30))
    self.set_variable("result", self.math_function("log", 30))
    self.set_variable("result", self.math_function("e ^", 30))
    self.set_variable("result", self.math_function("10 ^", 30))

sprite1.when_program_starts(when_program_starts_1)

def when_key_pressed_2(self):
    if not ((1 == 1)):
        self.say("never")

sprite1.when_key_pressed("any", when_key_pressed_2)

def when_program_starts_3(self):
    self.set_drag_mode_draggable()
    self.set_drag_mode_not_draggable()
    self.set_variable("copy", self.touching_mouse_pointer())
    self.set_variable("copy", self.touching_edge())
    self.set_variable("copy", self.touching(sprite2))
    self.set_variable("copy", self.touching_color((255, 0, 0)))
    self.set_variable("copy", self.color_is_touching((255, 140, 0), (0, 160, 90)))
    self.set_variable("copy", self.distance_to_mouse_pointer())
    self.set_variable("copy", self.distance_to_sprite(sprite2))
    self.set_variable("copy", self.mouse_x())
    self.set_variable("copy", self.mouse_y())
    self.set_variable("copy", self.mouse_down())
    self.set_variable("copy", self.key_pressed("a"))
    self.set_variable("copy", self.key_pressed("space"))
    self.set_variable("copy", self.timer())
    self.reset_timer()
    self.set_variable("copy", self.days_since())
    self.set_variable("copy", self.username())
    self.set_variable("copy", self.loudness())
    self.set_variable("copy", self.current_year())
    self.set_variable("copy", self.current_month())
    self.set_variable("copy", self.current_date())
    self.set_variable("copy", self.current_day_of_week())
    self.set_variable("copy", self.current_hour())
    self.set_variable("copy", self.current_minute())
    self.set_variable("copy", self.current_second())
    self.set_variable("copy", self.x_position_of(sprite2))
    self.set_variable("copy", self.y_position_of(sprite2))
    self.set_variable("copy", self.direction_of(sprite2))
    self.set_variable("copy", self.costume_of(sprite2))
    self.set_variable("copy", self.costume_name_of(sprite2))
    self.set_variable("copy", self.size_of(sprite2))
    self.set_variable("copy", self.volume_of(sprite2))
    self.set_variable("copy", self.get_variable_of("local", sprite2))
    self.set_variable("copy", self.x_position_of(stage))
    self.ask_and_wait("What is your name?")
    self.say(self.answer())
    self.say(self.join("Hello ", self.answer()))

sprite1.when_program_starts(when_program_starts_3)

# Scratch Blocks for 'sprite2'

def when_program_starts_4(self):
    self.go_to_x_y(60, 0)

sprite2.when_program_starts(when_program_starts_4)

stage.play()
