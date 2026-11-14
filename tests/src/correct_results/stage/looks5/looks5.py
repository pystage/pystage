# looks5 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1", center_x=240, center_y=180)
stage.add_backdrop("blue_sky_2", center_x=240, center_y=180)
stage.add_backdrop("blue_sky", center_x=240, center_y=180)
stage.switch_backdrop_to("blue_sky")
stage.add_sound("pop")
stage.create_variable("my variable", 0)
stage.show_monitor("looks_backdropnumbername:number")
stage.set_value_monitor_position("looks_backdropnumbername:number", -235, 148)
stage.show_monitor("looks_backdropnumbername:name")
stage.set_value_monitor_position("looks_backdropnumbername:name", -235, 40)

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.go_to_x_y(5, -121)
sprite1.add_costume("costume1", center_x=48, center_y=50)
sprite1.add_costume("costume2", center_x=46, center_y=53)
sprite1.add_sound("meow")
sprite1.show_monitor("looks_costumenumbername:number")
sprite1.set_value_monitor_position("looks_costumenumbername:number", -235, 175)
sprite1.show_monitor("looks_size")
sprite1.set_value_monitor_position("looks_size", -235, 121)
sprite1.show_monitor("looks_costumenumbername:name")
sprite1.set_value_monitor_position("looks_costumenumbername:name", -235, 94)

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
