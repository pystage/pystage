# motion_all (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1", center_x=240, center_y=180)
stage.add_backdrop("backdrop2", center_x=240, center_y=180)
stage.add_sound("pop")

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.add_costume("costume1", center_x=20, center_y=20)
sprite1.add_costume("costume2", center_x=20, center_y=20)
sprite1.add_sound("meow")
sprite1.create_variable("here", 0, all_sprites=False)

# Create and initialize sprite 'sprite2'
sprite2 = stage.add_a_sprite(None)
sprite2.set_name("Sprite2")
sprite2.add_costume("costume1_2", center_x=20, center_y=20)
sprite2.add_costume("costume2_2", center_x=20, center_y=20)
sprite2.add_sound("meow")

# Scratch Blocks for 'sprite1'

def when_program_starts_1(self):
    self.go_to_x_y(-50, 20)
    self.go_to_random_position()
    self.go_to_sprite(sprite2)
    self.go_to_mouse_pointer()
    self.glide_to_x_y(0.5, 20, -20)
    self.glide_to_random_position(0.5)
    self.glide_to_sprite(0.5, sprite2)
    self.glide_to_mouse_pointer(0.5)
    self.point_in_direction(45)
    self.point_towards_mouse_pointer()
    self.point_towards_random_direction()
    self.point_towards_sprite(sprite2)
    self.turn_right(15)
    self.turn_left(15)
    self.move(10)
    self.change_x_by(10)
    self.set_x(-20)
    self.change_y_by(10)
    self.set_y(30)
    self.if_on_edge_bounce()
    self.set_rotation_style_around()
    self.set_rotation_style_none()
    self.set_rotation_style_left_right()
    self.set_variable("here", self.join(self.x_position(), self.y_position()))
    self.say(self.direction())
    for _ in range(30):
        self.move(15)
        self.if_on_edge_bounce()

sprite1.when_program_starts(when_program_starts_1)

# Scratch Blocks for 'sprite2'

def when_program_starts_2(self):
    self.go_to_x_y(100, 60)
    self.set_rotation_style_left_right()
    self.turn_left(15)

sprite2.when_program_starts(when_program_starts_2)

stage.play()
