# spriteclicked (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1", center_x=240, center_y=180)
stage.add_sound("pop")
stage.create_variable("my variable", 0)

# Create and initialize sprite 'apple'
apple = stage.add_a_sprite(None)
apple.set_name("Apple")
apple.go_to_x_y(-8, -6)
apple.add_costume("apple", center_x=46.301983623248844, center_y=41.25454472833886)
apple.add_costume("apple2", center_x=46.301985, center_y=41.25455425849859)
apple.add_sound("chomp")

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.go_to_x_y(-11, -2)
sprite1.add_costume("costume1", center_x=48, center_y=50)
sprite1.add_costume("costume2", center_x=46, center_y=53)
sprite1.switch_costume_to("costume2")
sprite1.add_sound("meow")

# Scratch Blocks for 'apple'

def when_this_sprite_clicked_1(self):
    self.next_costume()
    self.go_forward(1)

apple.when_this_sprite_clicked(when_this_sprite_clicked_1)

# Scratch Blocks for 'sprite1'

def when_this_sprite_clicked_2(self):
    self.next_costume()
    self.go_forward(1)

sprite1.when_this_sprite_clicked(when_this_sprite_clicked_2)

stage.play()
