# looks3 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1", center_x=140.89789386542452, center_y=142.7356775946011)
stage.add_backdrop("blue_sky", center_x=240, center_y=180)
stage.add_backdrop("random_one", center_x=165.39802840013851, center_y=139.91927969531463)
stage.add_backdrop("next_backdrop", center_x=139, center_y=80.55260901728201)
stage.switch_backdrop_to("next_backdrop")
stage.add_sound("pop")
stage.create_variable("my variable", 0)

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.add_costume("costume1", center_x=48, center_y=50)
sprite1.add_costume("costume2", center_x=46, center_y=53)
sprite1.switch_costume_to("costume2")
sprite1.add_sound("meow")

# Scratch Blocks for 'sprite1'

def when_program_starts_1(self):
    self.switch_backdrop_to("backdrop1")
    self.wait(1)
    self.switch_backdrop_to("blue_sky")
    self.wait(1)
    self.switch_to_next_backdrop()
    self.wait(1)
    self.switch_to_previous_backdrop()
    self.wait(1)
    self.switch_to_random_backdrop()
    self.wait(1)
    self.next_backdrop()

sprite1.when_program_starts(when_program_starts_1)

stage.play()
