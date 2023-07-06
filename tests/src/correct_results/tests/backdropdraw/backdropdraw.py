# backdropdraw (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1', -240, 164)
stage.add_backdrop('backdrop2', 1, 159)
stage.add_backdrop('backdrop3', -233, -49)
stage.add_backdrop('backdrop4', 117, -48)
stage.add_backdrop('backdrop5', -238, 176)
stage.add_backdrop('backdrop6', 176, -115)
stage.add_backdrop('chalkboard')
stage.add_backdrop('theater_2', -403, 277)
stage.add_backdrop('flowers')
stage.add_backdrop('theater')
stage.add_backdrop('beach_malibu')
stage.create_variable('my variable', 0)

def when_key_pressed_1(self):
    self.next_backdrop()

stage.when_key_pressed("space", when_key_pressed_1)
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(-94)
sprite1.set_y(54)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)
sprite1.add_sound('meow')
stage.play()
