# test2 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1", center_x=240, center_y=180)
stage.add_sound("pop")
stage.create_variable("my variable", 0)

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.add_costume("costume1", center_x=48, center_y=50)
sprite1.add_costume("costume2", center_x=46, center_y=53)
sprite1.add_sound("meow")

# Scratch Blocks for 'sprite1'

def when_i_receive_message_1(self):
    self.broadcast("message1")
    self.wait(1)
    # nothing in it
    while True:
        pass

sprite1.when_i_receive_message("message1", when_i_receive_message_1)

# nothing in it
def when_program_starts_2(self):
    pass

sprite1.when_program_starts(when_program_starts_2)

def when_backdrop_switches_to_3(self):
    if False:
        pass
    else:
        pass

sprite1.when_backdrop_switches_to("backdrop1", when_backdrop_switches_to_3)

stage.play()
