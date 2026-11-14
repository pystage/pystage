# sound2 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1")
stage.add_sound("pop")
stage.create_variable("my variable", 0)

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.add_costume("costume1", center_x=48, center_y=50)
sprite1.add_costume("costume2", center_x=46, center_y=53)
sprite1.add_sound("meow")

# Create and initialize sprite 'dan'
dan = stage.add_a_sprite(None)
dan.set_name("Dan")
dan.go_to_x_y(-94, -11)
dan.add_costume("dan_a", center_x=72, center_y=196, factor=2)
dan.add_costume("dan_b", center_x=94, center_y=200, factor=2)
dan.add_sound("dance_magic")

# Scratch Blocks for 'sprite1'

def when_program_starts_1(self):
    self.start_sound("meow")
    self.change_pitch_effect_by(100)

sprite1.when_program_starts(when_program_starts_1)

# Scratch Blocks for 'dan'

def when_program_starts_2(self):
    self.start_sound("dance_magic")
    self.clear_sound_effects()

dan.when_program_starts(when_program_starts_2)

stage.play()
