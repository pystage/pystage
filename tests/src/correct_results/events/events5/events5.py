# events5 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1", center_x=240, center_y=180)
stage.add_sound("pop")
stage.create_variable("my variable", 0)
stage.show_monitor("sensing_loudness")
stage.set_value_monitor_position("sensing_loudness", -224, 137)
stage.show_monitor("sensing_timer")
stage.set_value_monitor_position("sensing_timer", -223, 167)

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.add_costume("costume1", center_x=48, center_y=50)
sprite1.add_costume("costume2", center_x=46, center_y=53)
sprite1.add_sound("meow")

# Scratch Blocks for 'sprite1'

def when_timer_greater_than_1(self):
    self.say("timer greater than 3")

sprite1.when_timer_greater_than(3, when_timer_greater_than_1)

def when_loudness_greater_than_2(self):
    self.say("loudness greater than 1")

sprite1.when_loudness_greater_than(1, when_loudness_greater_than_2)

stage.play()
