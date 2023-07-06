# test2 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable', 0)

"""
# Sprite1

Test for multiple cases
"""
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(0)
sprite1.set_y(0)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)
sprite1.add_sound('meow')

def when_i_receive_message_1(self):
    self.broadcast("message1")
    self.wait(1.0)
    while True:
        pass

sprite1.when_i_receive_message("message1", when_i_receive_message_1)

def when_program_starts_2(self):
    """
    nothing in it
    """
    pass

sprite1.when_program_starts(when_program_starts_2)

def when_backdrop_switches_to_3(self):
    if None:
        pass
    else:
        pass

sprite1.when_backdrop_switches_to("backdrop1", when_backdrop_switches_to_3)
stage.play()
