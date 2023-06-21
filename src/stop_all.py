# stop_all (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable')
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(0)
sprite1.set_y(0)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)


def when_program_starts_1(self):
    self.say_for_seconds("Hello!", 2.0)
    self.stop_all()

sprite1.when_program_starts(when_program_starts_1)
bananas = stage.add_a_sprite(None)
bananas.set_name("Bananas")
bananas.set_x(-135)
bananas.set_y(71)
bananas.go_to_back_layer()
bananas.go_forward(2)
bananas.point_in_direction(-101)
bananas.add_costume('bananas', center_x=39, center_y=38)

def when_program_starts_2(self):
    while True:
        for _ in range(10):
            self.turn_right(359.0)

bananas.when_program_starts(when_program_starts_2)

stage.play()
