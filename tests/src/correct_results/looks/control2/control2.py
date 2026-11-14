# control2 (pyStage, converted from Scratch 3)
#
# Not everything of the Scratch project could be converted:
# - [loose_script] Sprite1: 1 script(s) without a hat block were left out (in Scratch they only run when clicked in the editor).

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1", center_x=240, center_y=180)
stage.add_backdrop("beach_rio", center_x=480, center_y=360, factor=2)
stage.switch_backdrop_to("beach_rio")
stage.add_sound("pop")
stage.create_variable("my variable", 0)

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.go_to_x_y(-15, 1)
sprite1.add_costume("costume1", center_x=48, center_y=50)
sprite1.add_costume("costume2", center_x=46, center_y=53)
sprite1.add_sound("meow")

# Scratch Blocks for 'stage'

def when_program_starts_1(self):
    while True:
        if self.mouse_down():
            self.play_sound_until_done("pop")
        if self.mouse_down():
            self.set_pitch_effect_to(100)
        else:
            self.stop_all_sounds()

stage.when_program_starts(when_program_starts_1)

def when_program_starts_2(self):
    for _ in range(10):
        if self.key_pressed("space"):
            for _ in range(10):
                self.switch_backdrop_to("beach_rio")
        else:
            self.start_sound("pop")

stage.when_program_starts(when_program_starts_2)

stage.play()
