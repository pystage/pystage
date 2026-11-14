# looks_all (pyStage, converted from Scratch 3)

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
sprite1.create_variable("info", "", all_sprites=False)

# Create and initialize sprite 'sprite2'
sprite2 = stage.add_a_sprite(None)
sprite2.set_name("Sprite2")
sprite2.add_costume("costume1_2", center_x=20, center_y=20)
sprite2.add_costume("costume2_2", center_x=20, center_y=20)
sprite2.add_sound("meow")

# Scratch Blocks for 'sprite1'

def when_program_starts_1(self):
    self.say_for_seconds("Hello!", 0.2)
    self.say("Hmm")
    self.think_for_seconds("Thinking", 0.2)
    self.think("Hmm...")
    self.switch_costume_to("costume2")
    self.next_costume()
    self.switch_backdrop_to("backdrop2")
    self.next_backdrop()
    self.change_size_by(10)
    self.set_size_to(120)
    self.hide()
    self.show()
    self.set_color_effect_to(20)
    self.set_fisheye_effect_to(20)
    self.set_whirl_effect_to(20)
    self.set_pixelate_effect_to(20)
    self.set_mosaic_effect_to(20)
    self.set_brightness_effect_to(20)
    self.set_ghost_effect_to(20)
    self.change_color_effect_by(5)
    self.change_fisheye_effect_by(5)
    self.change_whirl_effect_by(5)
    self.change_pixelate_effect_by(5)
    self.change_mosaic_effect_by(5)
    self.change_brightness_effect_by(5)
    self.change_ghost_effect_by(5)
    self.clear_graphic_effects()
    self.go_to_front_layer()
    self.go_to_back_layer()
    self.go_forward(1)
    self.go_backward(1)
    self.set_variable("info", self.join(self.costume_name(), self.costume_number()))
    self.set_variable("info", self.join(self.backdrop_name(), self.backdrop_number()))
    self.say(self.size())
    self.switch_costume_to(self.join("costume", 1))

sprite1.when_program_starts(when_program_starts_1)

# Scratch Blocks for 'sprite2'

def when_program_starts_2(self):
    self.go_to_x_y(-120, -80)
    self.say("I am behind")

sprite2.when_program_starts(when_program_starts_2)

stage.play()
