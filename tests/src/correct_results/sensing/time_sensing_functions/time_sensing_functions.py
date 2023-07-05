# time_sensing_functions (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable', 0)
anina_dance = stage.add_a_sprite(None)
anina_dance.set_name("Anina Dance")
anina_dance.set_x(28)
anina_dance.set_y(-28)
anina_dance.go_to_back_layer()
anina_dance.go_forward(1)
anina_dance.add_costume('anina_stance', center_x=76, center_y=252, factor=2)
anina_dance.add_costume('anina_top_stand', center_x=74, center_y=280, factor=2)
anina_dance.add_costume('anina_top_r_step', center_x=248, center_y=272, factor=2)
anina_dance.add_costume('anina_top_l_step', center_x=228, center_y=274, factor=2)
anina_dance.add_costume('anina_top_freeze', center_x=110, center_y=268, factor=2)
anina_dance.add_costume('anina_r_cross', center_x=126, center_y=268, factor=2)
anina_dance.add_costume('anina_pop_front', center_x=68, center_y=270, factor=2)
anina_dance.add_costume('anina_pop_down', center_x=74, center_y=156, factor=2)
anina_dance.add_costume('anina_pop_left', center_x=238, center_y=266, factor=2)
anina_dance.add_costume('anina_pop_right', center_x=66, center_y=268, factor=2)
anina_dance.add_costume('anina_pop_l_arm', center_x=68, center_y=274, factor=2)
anina_dance.add_costume('anina_pop_stand', center_x=76, center_y=276, factor=2)
anina_dance.add_costume('anina_pop_r_arm', center_x=88, center_y=272, factor=2)
anina_dance.next_costume()
anina_dance.next_costume()
anina_dance.add_sound('dance_celebrate')
anina_dance.add_sound('dance_magic')

def when_program_starts_1(self):
    self.think(self.current_year())

anina_dance.when_program_starts(when_program_starts_1)

def when_key_pressed_2(self):
    self.say(self.current_month())

anina_dance.when_key_pressed("space", when_key_pressed_2)

def when_key_pressed_3(self):
    self.say(self.current_date())

anina_dance.when_key_pressed("u", when_key_pressed_3)

def when_key_pressed_4(self):
    self.say(self.current_hour())

anina_dance.when_key_pressed("j", when_key_pressed_4)

def when_key_pressed_5(self):
    self.say(self.current_day_of_week())

anina_dance.when_key_pressed("h", when_key_pressed_5)

def when_key_pressed_6(self):
    self.say(self.current_minute())

anina_dance.when_key_pressed("k", when_key_pressed_6)

def when_key_pressed_7(self):
    self.say(self.current_second())

anina_dance.when_key_pressed("a", when_key_pressed_7)

def when_key_pressed_8(self):
    self.say(self.days_since())

anina_dance.when_key_pressed("z", when_key_pressed_8)
stage.play()
