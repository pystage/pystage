# control5 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.add_backdrop('boardwalk')
stage.create_variable('my variable', 0)
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(64)
sprite1.set_y(-6)
sprite1.go_to_back_layer()
sprite1.go_forward(2)
sprite1.set_size_to(190)
sprite1.add_costume('costume1', center_x=73.76648930018897, center_y=100.95969430024343)
sprite1.add_costume('costume2', center_x=46, center_y=53)
sprite1.add_sound('meow')

def when_program_starts_1(self):
    while not self.touching_edge():
        self.move(10.0)
        self.change_size_by(30.0)

sprite1.when_program_starts(when_program_starts_1)
broom = stage.add_a_sprite(None)
broom.set_name("Broom")
broom.set_x(113)
broom.set_y(-54)
broom.go_to_back_layer()
broom.go_forward(1)
broom.hide()
broom.add_costume('broom', center_x=131.1, center_y=21.100000000000023)
broom.add_sound('pop')

def when_program_starts_2(self):
    while not self.touching_edge():
        self.move(10.0)

    self.hide()

broom.when_program_starts(when_program_starts_2)
stage.play()
