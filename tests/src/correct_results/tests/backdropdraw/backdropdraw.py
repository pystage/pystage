# backdropdraw (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1")
stage.add_backdrop("backdrop2")
stage.add_backdrop("backdrop3")
stage.add_backdrop("backdrop4")
stage.add_backdrop("backdrop5")
stage.add_backdrop("backdrop6")
stage.add_backdrop("chalkboard")
stage.add_backdrop("theater_2")
stage.add_backdrop("flowers")
stage.add_backdrop("theater")
stage.add_backdrop("beach_malibu")
stage.add_sound("pop")
stage.create_variable("my variable", 0)

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.go_to_x_y(-94, 54)
sprite1.add_costume("costume1", center_x=48, center_y=50)
sprite1.add_costume("costume2", center_x=46, center_y=53)
sprite1.add_sound("meow")

# Scratch Blocks for 'stage'

def when_key_pressed_1(self):
    self.next_backdrop()

stage.when_key_pressed("space", when_key_pressed_1)

stage.play()
