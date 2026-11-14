# svg_text (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1", center_x=240, center_y=180)
stage.add_backdrop("backdrop2", center_x=240, center_y=180)
stage.add_sound("pop")

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.add_costume("button", center_x=98, center_y=30)
sprite1.add_sound("meow")

# Scratch Blocks for 'sprite1'

def when_program_starts_1(self):
    self.go_to_x_y(0, 0)

sprite1.when_program_starts(when_program_starts_1)

def when_this_sprite_clicked_2(self):
    self.say("clicked")

sprite1.when_this_sprite_clicked(when_this_sprite_clicked_2)

stage.play()
