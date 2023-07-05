# motion5 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.add_backdrop('forest')
stage.add_backdrop('blue_sky_2')
stage.create_variable('your_score', 5)
stage.show_builtinvariable("timer", -235, 175)
stage.show_variable("your_score", -233, 146)
bread = stage.add_a_sprite(None)
bread.set_name("Bread")
bread.set_x(-38.32409760250535)
bread.set_y(-12.564624023471827)
bread.go_to_back_layer()
bread.go_forward(3)
bread.point_in_direction(-101.5369590328155)
bread.hide()
bread.add_costume('bread', center_x=37, center_y=12)
bread.add_sound('pop')

def when_program_starts_1(self):
    self.show()
    while True:
        self.wait(1.0)
        while not self.touching("NO TRANSLATION: sensing_touchingobjectmenu"):
            pass

        self.change_variable_by("your_score", 1.0)
        self.hide()

bread.when_program_starts(when_program_starts_1)

def when_program_starts_2(self):
    self.go_to_x_y(-100.0, 200.0)
    while True:
        self.if_on_edge_bounce()
        self.move(2.0)

bread.when_program_starts(when_program_starts_2)
dot = stage.add_a_sprite(None)
dot.set_name("Dot")
dot.set_x(57)
dot.set_y(0)
dot.go_to_back_layer()
dot.go_forward(1)
dot.add_costume('dot_a', center_x=52, center_y=67)
dot.add_costume('dot_b', center_x=65, center_y=67)
dot.add_costume('dot_c', center_x=50.53907324990831, center_y=68.96764494984302)
dot.add_costume('dot_d', center_x=56.58074394930321, center_y=66.76919584395038)
dot.add_sound('bark')

def when_key_pressed_3(self):
    self.change_x_by(10.0)

dot.when_key_pressed("d", when_key_pressed_3)

def when_key_pressed_4(self):
    self.change_x_by(-10.0)

dot.when_key_pressed("a", when_key_pressed_4)

def when_key_pressed_5(self):
    self.change_y_by(10.0)

dot.when_key_pressed("w", when_key_pressed_5)

def when_key_pressed_6(self):
    self.change_y_by(-10.0)

dot.when_key_pressed("s", when_key_pressed_6)

def when_program_starts_7(self):
    self.switch_backdrop_to("forest")
    self.reset_timer()
    self.set_variable("your_score", 0)

dot.when_program_starts(when_program_starts_7)

def when_timer_greater_than_8(self):
    if (self.get_variable("your_score") > 4):
        self.switch_backdrop_to("blue_sky_2")
        self.say_for_seconds("You win!", 10.0)
    else:
        self.think_for_seconds("".join([" You Lose ", self.username()]), 10.0)

dot.when_timer_greater_than(10.0, when_timer_greater_than_8)

def when_loudness_greater_than_9(self):
    pass

dot.when_loudness_greater_than(10.0, when_loudness_greater_than_9)
bread2 = stage.add_a_sprite(None)
bread2.set_name("Bread2")
bread2.set_x(36.641465728846036)
bread2.set_y(-7.363814353977223)
bread2.go_to_back_layer()
bread2.go_forward(5)
bread2.point_in_direction(101.53695903281549)
bread2.hide()
bread2.add_costume('bread', center_x=37, center_y=12)
bread2.add_sound('pop')

def when_program_starts_10(self):
    self.show()
    while not self.touching("NO TRANSLATION: sensing_touchingobjectmenu"):
        pass

    self.change_variable_by("your_score", 1.0)
    self.hide()

bread2.when_program_starts(when_program_starts_10)

def when_program_starts_11(self):
    self.go_to_x_y(100.0, 200.0)
    while True:
        self.if_on_edge_bounce()
        self.move(2.0)

bread2.when_program_starts(when_program_starts_11)
bread3 = stage.add_a_sprite(None)
bread3.set_name("Bread3")
bread3.set_x(-7.027960616554102)
bread3.set_y(140.61516742703085)
bread3.go_to_back_layer()
bread3.go_forward(4)
bread3.point_in_direction(101.53695903281549)
bread3.hide()
bread3.add_costume('bread', center_x=37, center_y=12)
bread3.add_sound('pop')

def when_program_starts_12(self):
    self.show()
    while not self.touching("NO TRANSLATION: sensing_touchingobjectmenu"):
        pass

    self.change_variable_by("your_score", 1.0)
    self.hide()

bread3.when_program_starts(when_program_starts_12)

def when_program_starts_13(self):
    self.go_to_x_y(50.0, 10.0)
    while True:
        self.if_on_edge_bounce()
        self.move(2.0)

bread3.when_program_starts(when_program_starts_13)
bread4 = stage.add_a_sprite(None)
bread4.set_name("Bread4")
bread4.set_x(62.47610381351032)
bread4.set_y(-12.936527442966451)
bread4.go_to_back_layer()
bread4.go_forward(6)
bread4.point_in_direction(-101.5369590328155)
bread4.hide()
bread4.add_costume('bread', center_x=37, center_y=12)
bread4.add_sound('pop')

def when_program_starts_14(self):
    self.show()
    while not self.touching("NO TRANSLATION: sensing_touchingobjectmenu"):
        pass

    self.change_variable_by("your_score", 1.0)
    self.hide()

bread4.when_program_starts(when_program_starts_14)

def when_program_starts_15(self):
    self.go_to_x_y(0.0, 300.0)
    while True:
        self.if_on_edge_bounce()
        self.move(2.0)

bread4.when_program_starts(when_program_starts_15)
bread5 = stage.add_a_sprite(None)
bread5.set_name("Bread5")
bread5.set_x(-146.04253870781898)
bread5.set_y(10.577908515898349)
bread5.go_to_back_layer()
bread5.go_forward(2)
bread5.point_in_direction(-78.46304096718453)
bread5.hide()
bread5.add_costume('bread', center_x=37, center_y=12)
bread5.add_sound('pop')

def when_program_starts_16(self):
    self.show()
    while not self.touching("NO TRANSLATION: sensing_touchingobjectmenu"):
        pass

    self.change_variable_by("your_score", 1.0)
    self.hide()

bread5.when_program_starts(when_program_starts_16)

def when_program_starts_17(self):
    self.go_to_x_y(-300.0, -200.0)
    while True:
        self.if_on_edge_bounce()
        self.move(2.0)

bread5.when_program_starts(when_program_starts_17)
stage.play()
