# spriteclicked (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable', 0)
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(-11)
sprite1.set_y(-2)
sprite1.go_to_back_layer()
sprite1.go_forward(2)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)
sprite1.next_costume()
sprite1.add_sound('meow')

def when_this_sprite_clicked_1(self):
    self.next_costume()
    self.go_forward(1)

sprite1.when_this_sprite_clicked(when_this_sprite_clicked_1)
apple = stage.add_a_sprite(None)
apple.set_name("Apple")
apple.set_x(-8)
apple.set_y(-6)
apple.go_to_back_layer()
apple.go_forward(1)
apple.add_costume('apple', center_x=46.301983623248844, center_y=41.25454472833886)
apple.add_costume('apple2', center_x=46.301985, center_y=41.25455425849859)
apple.add_sound('chomp')

def when_this_sprite_clicked_2(self):
    self.next_costume()
    self.go_forward(1)

apple.when_this_sprite_clicked(when_this_sprite_clicked_2)
stage.play()
