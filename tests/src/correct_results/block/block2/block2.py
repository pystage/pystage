# block2 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1")
stage.add_sound("pop")
stage.create_variable("my variable", 0)

# Create and initialize sprite 'bear'
bear = stage.add_a_sprite(None)
bear.set_name("Bear")
bear.go_to_x_y(-114, -5)
bear.add_costume("bear_a", center_x=100, center_y=90)
bear.add_costume("bear_b", center_x=94, center_y=190.66666666666666)
bear.add_sound("pop")

# Scratch Blocks for 'bear'

def bear_fade_in(self):
    bear_fade_number_of_times_change_amount(self, 10, -10, "")


def bear_fade_out(self):
    bear_fade_number_of_times_change_amount(self, 10, 10, "")


def bear_fade_number_of_times_change_amount(self, repeat_times, change_amount, in_):
    for _ in range(int(repeat_times)):
        self.change_ghost_effect_by(change_amount)


def when_program_starts_1(self):
    while True:
        bear_fade_out(self)
        self.wait(3)
        bear_fade_in(self)

bear.when_program_starts(when_program_starts_1)

stage.play()
