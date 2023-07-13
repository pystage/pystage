# draggable (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.add_backdrop('farm')
stage.create_variable('my variable')

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(18.07692307692306)
sprite1.set_y(-43.02797202797203)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)
sprite1.add_sound('meow')

# Create and initialize sprite 'bear'
bear = stage.add_a_sprite(None)
bear.set_name("Bear")
bear.set_x(-117)
bear.set_y(66)
bear.go_to_back_layer()
bear.go_forward(2)
bear.add_costume('bear_a', center_x=100, center_y=90)
bear.add_costume('bear_b', center_x=94, center_y=190.66666666666666)
bear.add_sound('pop')

# Create and initialize sprite 'cat_2'
cat_2 = stage.add_a_sprite(None)
cat_2.set_name("Cat 2")
cat_2.set_x(170)
cat_2.set_y(74)
cat_2.go_to_back_layer()
cat_2.go_forward(3)
cat_2.add_costume('cat_2', center_x=87, center_y=39)
cat_2.add_sound('meow2')

# Scratch Blocks for 'sprite1'

def when_program_starts_1(self):
    self.set_drag_mode_draggable()

sprite1.when_program_starts(when_program_starts_1)

def when_key_pressed_2(self):
    self.set_drag_mode_not_draggable()

sprite1.when_key_pressed("space", when_key_pressed_2)

# Scratch Blocks for 'bear'

def when_program_starts_3(self):
    self.set_drag_mode_draggable()

bear.when_program_starts(when_program_starts_3)

def when_key_pressed_4(self):
    self.set_drag_mode_not_draggable()

bear.when_key_pressed("space", when_key_pressed_4)

# Scratch Blocks for 'cat_2'

def when_program_starts_5(self):
    self.set_drag_mode_draggable()

cat_2.when_program_starts(when_program_starts_5)

def when_key_pressed_6(self):
    self.set_drag_mode_not_draggable()

cat_2.when_key_pressed("space", when_key_pressed_6)

stage.play()
