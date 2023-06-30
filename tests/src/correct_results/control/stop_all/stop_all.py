# stop_all (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable')

def when_GREENFLAG_clicked_1(self):
    self.ask_and_wait("What's your name?")

stage.when_GREENFLAG_clicked(when_GREENFLAG_clicked_1)
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(0)
sprite1.set_y(0)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.point_in_direction(150)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)


def when_program_starts_2(self):
    self.say("Hello!")

sprite1.when_program_starts(when_program_starts_2)

def when_program_starts_3(self):
    while True:
        self.turn_right(15.0)
        self.wait(1.0)
        self.stop_all()

sprite1.when_program_starts(when_program_starts_3)

stage.play()
