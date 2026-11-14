# pen (pyStage, converted from Scratch 3)

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

# Scratch Blocks for 'stage'

def when_program_starts_1(self):
    self.wait(2)
    self.erase_all()

stage.when_program_starts(when_program_starts_1)

def when_stage_clicked_2(self):
    self.erase_all()

stage.when_stage_clicked(when_stage_clicked_2)

# Scratch Blocks for 'sprite1'

def when_program_starts_3(self):
    self.erase_all()
    self.go_to_x_y(-150, 0)
    self.set_pen_color((255, 0, 0))
    self.set_pen_size_to(5)
    self.pen_down()
    self.move(40)
    self.change_pen_hue_by(10)
    self.change_pen_saturation_by(10)
    self.change_pen_brightness_by(10)
    self.change_pen_transparency_by(10)
    self.move(40)
    self.set_pen_hue_to(50)
    self.set_pen_saturation_to(50)
    self.set_pen_brightness_to(50)
    self.set_pen_transparency_to(50)
    self.change_pen_size_by(3)
    self.move(40)
    self.stamp()
    self.pen_up()
    self.move(40)
    self.set_pen_color(self.pick_random(0, 16777215))
    self.set_pen_color(self.join("#00", "ff00"))
    self.set_pen_size_to(self.math_function("sqrt", -1))
    self.change_pen_size_by(self.join(1, ""))
    self.set_pen_hue_to(self.join(2, 5))
    self.change_pen_brightness_by(self.math_function("sqrt", -1))
    self.set_pen_color((0, 170, 68))
    self.pen_down()
    for _ in range(4):
        self.move(10)
        self.turn_right(90)
    self.pen_up()

sprite1.when_program_starts(when_program_starts_3)

stage.play()
