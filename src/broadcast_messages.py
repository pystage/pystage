# broadcast_messages (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable')
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(-151)
sprite1.set_y(103)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.point_in_direction(-150)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)


def when_program_starts_1(self):
    self.broadcast("go!")

sprite1.when_program_starts(when_program_starts_1)

def when_i_receive_message_2(self):
    self.say_for_seconds("h", 2.0)
    self.say("e")
    self.say_for_seconds("l", 2.0)
    self.say("heaven")

sprite1.when_i_receive_message("go!", when_i_receive_message_2)

def when_i_receive_message_3(self):
    self.go_to_x_y(-151.0, 103.0)
    self.broadcast("o")

sprite1.when_i_receive_message("message1", when_i_receive_message_3)

def when_program_starts_4(self):
    self.ask_and_wait("What's your name?")
    self.broadcast_and_wait("message1")

sprite1.when_program_starts(when_program_starts_4)

def when_i_receive_message_5(self):
    self.wait(1.0)
    self.think_for_seconds("Hmm...", 2.0)

sprite1.when_i_receive_message("o", when_i_receive_message_5)

stage.play()
