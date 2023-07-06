# looks4 (pyStage, converted from Scratch 3)

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
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)
sprite1.add_sound('meow')
sprite1.show_builtinvariable("size", -235, 148)

def when_key_pressed_1(self):
    self.set_color_effect_to(0.0)

sprite1.when_key_pressed("b", when_key_pressed_1)

def when_key_pressed_2(self):
    self.clear_graphic_effects()

sprite1.when_key_pressed("o", when_key_pressed_2)

def when_key_pressed_3(self):
    self.change_fisheye_effect_by(25.0)

sprite1.when_key_pressed("c", when_key_pressed_3)

def when_key_pressed_4(self):
    self.change_color_effect_by(10.0)

sprite1.when_key_pressed("a", when_key_pressed_4)

def when_program_starts_5(self):
    self.change_size_by(10.0)
    self.wait(1.0)
    self.set_size_to(100.0)
    self.wait(1.0)
    self.hide()
    self.wait(1.0)
    self.show()

sprite1.when_program_starts(when_program_starts_5)

def when_key_pressed_6(self):
    self.set_fisheye_effect_to(0.0)

sprite1.when_key_pressed("d", when_key_pressed_6)

def when_key_pressed_7(self):
    self.change_whirl_effect_by(25.0)

sprite1.when_key_pressed("e", when_key_pressed_7)

def when_key_pressed_8(self):
    self.change_pixelate_effect_by(25.0)

sprite1.when_key_pressed("g", when_key_pressed_8)

def when_key_pressed_9(self):
    self.set_whirl_effect_to(0.0)

sprite1.when_key_pressed("f", when_key_pressed_9)

def when_key_pressed_10(self):
    self.set_pixelate_effect_to(0.0)

sprite1.when_key_pressed("h", when_key_pressed_10)

def when_key_pressed_11(self):
    self.change_mosaic_effect_by(-25.0)

sprite1.when_key_pressed("i", when_key_pressed_11)

def when_key_pressed_12(self):
    self.set_mosaic_effect_to(0.0)

sprite1.when_key_pressed("j", when_key_pressed_12)

def when_key_pressed_13(self):
    self.change_brightness_effect_by(25.0)

sprite1.when_key_pressed("k", when_key_pressed_13)

def when_key_pressed_14(self):
    self.set_brightness_effect_to(0.0)

sprite1.when_key_pressed("l", when_key_pressed_14)

def when_key_pressed_15(self):
    self.change_ghost_effect_by(25.0)

sprite1.when_key_pressed("m", when_key_pressed_15)

def when_key_pressed_16(self):
    self.set_ghost_effect_to(0.0)

sprite1.when_key_pressed("n", when_key_pressed_16)
stage.play()
