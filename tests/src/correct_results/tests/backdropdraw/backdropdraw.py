# backdropdraw (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1", center_x=239.57979208269109, center_y=163.7754501423998)
stage.add_backdrop("backdrop2", center_x=-0.9589751705999277, center_y=159.33277924427264)
stage.add_backdrop("backdrop3", center_x=233.2400985227273, center_y=-49.258614090909106)
stage.add_backdrop("backdrop4", center_x=-234, center_y=-95, factor=2)
stage.add_backdrop("backdrop5", center_x=475, center_y=352, factor=2)
stage.add_backdrop("backdrop6", center_x=-175.7599014772727, center_y=-115.25861409090908)
stage.add_backdrop("chalkboard", center_x=480, center_y=360, factor=2)
stage.add_backdrop("theater_2", center_x=403, center_y=277)
stage.add_backdrop("flowers", center_x=480, center_y=360, factor=2)
stage.add_backdrop("theater", center_x=480, center_y=360, factor=2)
stage.add_backdrop("beach_malibu", center_x=480, center_y=360, factor=2)
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
