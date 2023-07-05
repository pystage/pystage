# stage1 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('blue_sky')
stage.add_backdrop('canyon')
stage.create_variable('my variable', 0)

def when_key_pressed_1(self):
    self.change_color_effect_by(25.0)

stage.when_key_pressed("a", when_key_pressed_1)

def when_key_pressed_2(self):
    self.change_fisheye_effect_by(25.0)

stage.when_key_pressed("b", when_key_pressed_2)

def when_key_pressed_3(self):
    self.change_whirl_effect_by(25.0)

stage.when_key_pressed("c", when_key_pressed_3)

def when_key_pressed_4(self):
    self.change_pixelate_effect_by(25.0)

stage.when_key_pressed("d", when_key_pressed_4)

def when_key_pressed_5(self):
    self.change_mosaic_effect_by(25.0)

stage.when_key_pressed("e", when_key_pressed_5)

def when_key_pressed_6(self):
    self.change_brightness_effect_by(25.0)

stage.when_key_pressed("f", when_key_pressed_6)

def when_key_pressed_7(self):
    self.change_ghost_effect_by(25.0)

stage.when_key_pressed("g", when_key_pressed_7)
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(11)
sprite1.set_y(-52)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)
sprite1.add_sound('meow')
stage.play()
