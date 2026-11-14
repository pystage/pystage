# looks5 (pyStage, converted from Scratch 3)
#
# Not everything of the Scratch project could be converted:
# - [monitor] Sprite1: The monitor for 'looks_costumenumbername' is not supported and was left out (2 monitors).
# - [monitor] Stage: The monitor for 'looks_backdropnumbername' is not supported and was left out (2 monitors).
# - [monitor] Sprite1: The monitor for 'looks_size' is not supported and was left out.

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1", center_x=240, center_y=180)
stage.add_backdrop("blue_sky_2", center_x=240, center_y=180)
stage.add_backdrop("blue_sky", center_x=240, center_y=180)
stage.switch_backdrop_to("blue_sky")
stage.add_sound("pop")
stage.create_variable("my variable", 0)

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.go_to_x_y(5, -121)
sprite1.add_costume("costume1", center_x=48, center_y=50)
sprite1.add_costume("costume2", center_x=46, center_y=53)
sprite1.add_sound("meow")

# Scratch Blocks for 'sprite1'

def when_program_starts_1(self):
    self.go_to_front_layer()
    self.wait(1)
    self.go_to_back_layer()
    self.wait(1)
    self.go_backward(1)
    self.wait(1)
    self.go_forward(1)

sprite1.when_program_starts(when_program_starts_1)

stage.play()
