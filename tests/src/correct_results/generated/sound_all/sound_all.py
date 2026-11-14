# sound_all (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1", center_x=240, center_y=180)
stage.add_backdrop("backdrop2", center_x=240, center_y=180)
stage.add_sound("pop")
stage.create_variable("loud", 0)

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.add_costume("costume1", center_x=20, center_y=20)
sprite1.add_costume("costume2", center_x=20, center_y=20)
sprite1.add_sound("meow")

# Scratch Blocks for 'stage'

def when_program_starts_1(self):
    self.play_sound_until_done("pop")
    self.set_pan_left_right_effect_to(20)
    self.change_pitch_effect_by(5)
    self.clear_sound_effects()
    self.change_volume_by(-10)
    self.set_volume_to(50)
    self.set_variable("loud", self.volume())
    self.stop_all_sounds()

stage.when_program_starts(when_program_starts_1)

# Scratch Blocks for 'sprite1'

def when_program_starts_2(self):
    self.start_sound("meow")
    self.play_sound_until_done("meow")
    self.set_pitch_effect_to(100)
    self.set_pan_left_right_effect_to(-50)
    self.change_pitch_effect_by(10)
    self.change_pan_left_right_effect_by(10)
    self.clear_sound_effects()
    self.change_volume_by(-10)
    self.set_volume_to(70)
    self.say(self.volume())
    self.start_sound("meow")
    self.stop_all_sounds()

sprite1.when_program_starts(when_program_starts_2)

stage.play()
