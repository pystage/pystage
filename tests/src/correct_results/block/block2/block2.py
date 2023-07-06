# block2 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable', 0)
bear = stage.add_a_sprite(None)
bear.set_name("Bear")
bear.set_x(-114)
bear.set_y(-5)
bear.go_to_back_layer()
bear.go_forward(1)
bear.add_costume('bear_a', center_x=100, center_y=90)
bear.add_costume('bear_b', center_x=94, center_y=190.66666666666666)
bear.add_sound('pop')

def when_program_starts_1(self):
    while True:
        "NO TRANSLATION: procedures_call"
        self.wait(3.0)
        "NO TRANSLATION: procedures_call"

bear.when_program_starts(when_program_starts_1)
stage.play()
