# variable5 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1", center_x=240, center_y=180)
stage.add_backdrop("jungle", center_x=480, center_y=360, factor=2)
stage.switch_backdrop_to("jungle")
stage.add_sound("pop")
stage.create_variable("my variable", 44)
stage.create_variable("points", 0)
stage.show_variable("points")
stage.set_monitor_position("points", -235, 175)

# Create and initialize sprite 'donut'
donut = stage.add_a_sprite(None)
donut.set_name("Donut")
donut.go_to_x_y(146, -54)
donut.add_costume("donut", center_x=72.11747235252724, center_y=14.658782444689848)
donut.add_sound("bite")
donut.add_sound("chomp")

# Create and initialize sprite 'dragon'
dragon = stage.add_a_sprite(None)
dragon.set_name("Dragon")
dragon.go_to_x_y(-82, -1)
dragon.add_costume("dragon_a", center_x=124.12215277545062, center_y=106.25815347723332)
dragon.add_costume("dragon_b", center_x=152.5, center_y=99)
dragon.add_costume("dragon_c", center_x=124.4550776985194, center_y=105.92484014389998)
dragon.add_sound("magic_spell")

# Create and initialize sprite 'basketball'
basketball = stage.add_a_sprite(None)
basketball.set_name("Basketball")
basketball.go_to_x_y(142.84310537078323, -82.72394234696634)
basketball.point_in_direction(165)
basketball.add_costume("basketball", center_x=23, center_y=23)
basketball.add_sound("pop")
basketball.add_sound("basketball_bounce")

# Scratch Blocks for 'dragon'

def when_program_starts_1(self):
    if (self.get_variable("points") < 10):
        self.switch_backdrop_to("jungle")
        self.show()
    if (self.get_variable("points") > 10):
        self.hide()
        self.switch_backdrop_to("backdrop1")

dragon.when_program_starts(when_program_starts_1)

def when_program_starts_2(self):
    while True:
        self.change_x_by(10)
        self.wait(1)
        self.change_x_by(-10)
        self.wait(1)
        self.change_y_by(30)
        self.wait(1)
        self.change_y_by(-30)

dragon.when_program_starts(when_program_starts_2)

# Scratch Blocks for 'basketball'

def when_key_pressed_3(self):
    self.show()
    self.move(20)
    self.turn_right(15)

basketball.when_key_pressed("space", when_key_pressed_3)

def when_program_starts_4(self):
    while True:
        if self.color_is_touching((227, 118, 29), (124, 191, 46)):
            self.wait(1)
            self.start_sound("basketball_bounce")
            self.change_variable_by("points", 1)

basketball.when_program_starts(when_program_starts_4)

stage.play()
