# operators5 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable', 0)
cake = stage.add_a_sprite(None)
cake.set_name("Cake")
cake.set_x(23)
cake.set_y(-34)
cake.go_to_back_layer()
cake.go_forward(1)
cake.add_costume('cake_a', center_x=64, center_y=50)
cake.add_costume('cake_b', center_x=64, center_y=42)
cake.add_sound('birthday')

def when_program_starts_1(self):
    if (self.pick_random(1.0, 10.0) > 5):
        self.start_sound("birthday")
    else:
        self.wait((2.0 % 5.0))
        self.change_size_by(-10.0)

cake.when_program_starts(when_program_starts_1)
stage.play()
