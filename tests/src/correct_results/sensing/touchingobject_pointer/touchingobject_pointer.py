# touchingobject_pointer (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable', 0)
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(0)
sprite1.set_y(0)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.add_costume('costume1', center_x=76.67666504588723, center_y=78.67712495013966)
sprite1.add_costume('costume2', center_x=46, center_y=53)
sprite1.add_sound('meow')

def when_key_pressed_1(self):
    if self.touching_mouse_pointer():
        self.say("Hello!")
    else:
        self.think("Hmm...")

sprite1.when_key_pressed("space", when_key_pressed_1)
stage.play()
