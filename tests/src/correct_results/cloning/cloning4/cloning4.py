# cloning4 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable', 0)

def when_i_receive_1(self):
    for _ in range(10):
        self.start_sound("pop")

stage.when_i_receive("message1", when_i_receive_1)

def when_GREENFLAG_clicked_2(self):
    self.broadcast("message1")

stage.when_GREENFLAG_clicked(when_GREENFLAG_clicked_2)
button4 = stage.add_a_sprite(None)
button4.set_name("Button4")
button4.set_x(-165)
button4.set_y(72)
button4.go_to_back_layer()
button4.go_forward(2)
button4.add_costume('button4_a', center_x=35, center_y=34)
button4.add_costume('button4_b', center_x=35, center_y=34)
button4.add_sound('pop')

def when_program_starts_3(self):
    self.broadcast("message1")
    self.set_volume_to(500.0)
    self.broadcast_and_wait("loud_message")
    self.set_pitch_effect_to(100.0)
    for _ in range(3):
        self.wait(1.0)
        self.play_sound_until_done("pop")

button4.when_program_starts(when_program_starts_3)

def when_i_receive_message_4(self):
    for _ in range(10):
        self.say("Hello!")
        self.create_clone_of("NO TRANSLATION: control_create_clone_of_menu")

button4.when_i_receive_message("message1", when_i_receive_message_4)
d_money_dance = stage.add_a_sprite(None)
d_money_dance.set_name("D-Money Dance")
d_money_dance.set_x(41)
d_money_dance.set_y(-5)
d_money_dance.go_to_back_layer()
d_money_dance.go_forward(1)
d_money_dance.add_costume('dm_stance', center_x=106, center_y=238, factor=2)
d_money_dance.add_costume('dm_top_stand', center_x=82, center_y=244, factor=2)
d_money_dance.add_costume('dm_top_r_leg', center_x=218, center_y=232, factor=2)
d_money_dance.add_costume('dm_top_l_leg', center_x=230, center_y=240, factor=2)
d_money_dance.add_costume('dm_freeze', center_x=220, center_y=234, factor=2)
d_money_dance.add_costume('dm_pop_front', center_x=92, center_y=234, factor=2)
d_money_dance.add_costume('dm_pop_down', center_x=64, center_y=74, factor=2)
d_money_dance.add_costume('dm_pop_left', center_x=204, center_y=250, factor=2)
d_money_dance.add_costume('dm_pop_right', center_x=78, center_y=238, factor=2)
d_money_dance.add_costume('dm_pop_l_arm', center_x=90, center_y=238, factor=2)
d_money_dance.add_costume('dm_pop_stand', center_x=100, center_y=244, factor=2)
d_money_dance.add_costume('dm_pop_r_arm', center_x=80, center_y=240, factor=2)
d_money_dance.add_sound('dance_celebrate')

def when_i_receive_message_5(self):
    for _ in range(10):
        self.say("Hello!")
        self.create_clone_of("NO TRANSLATION: control_create_clone_of_menu")

d_money_dance.when_i_receive_message("message1", when_i_receive_message_5)
stage.play()
