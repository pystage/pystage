# timer_events (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1", center_x=240, center_y=180)
stage.add_backdrop("backdrop2", center_x=240, center_y=180)
stage.add_sound("pop")
stage.create_variable("ticks", 0)

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.add_costume("costume1", center_x=20, center_y=20)
sprite1.add_costume("costume2", center_x=20, center_y=20)
sprite1.add_sound("meow")

# Scratch Blocks for 'stage'

def when_timer_greater_than_1(self):
    self.change_variable_by("ticks", 1)
    self.reset_timer()

stage.when_timer_greater_than(2, when_timer_greater_than_1)

def when_program_starts_2(self):
    self.reset_timer()
    self.set_variable("ticks", self.timer())

stage.when_program_starts(when_program_starts_2)

# Scratch Blocks for 'sprite1'

def when_program_starts_3(self):
    self.reset_timer()
    self.say(self.timer())
    self.wait(0.5)
    self.say_for_seconds(self.round(self.timer()), 1)
    self.say(self.loudness())

sprite1.when_program_starts(when_program_starts_3)

def when_timer_greater_than_4(self):
    self.say("The timer is greater than 1")

sprite1.when_timer_greater_than(1, when_timer_greater_than_4)

def when_loudness_greater_than_5(self):
    self.say("Loud!")

sprite1.when_loudness_greater_than(10, when_loudness_greater_than_5)

stage.play()
