# backdrop_switches (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.add_backdrop('blue_sky')
stage.add_backdrop('chalkboard')
stage.add_backdrop('colorful_city')
stage.create_variable('my variable', 0)

def when_GREENFLAG_clicked_1(self):
    self.wait_seconds(2.0)
    self.switch_backdrop_to("colorful_city")

stage.when_GREENFLAG_clicked(when_GREENFLAG_clicked_1)

def when_backdrop_switches_to_2(self):
    self.wait_seconds(1.0)
    self.change_color_effect_by(25.0)

stage.when_backdrop_switches_to("colorful_city", when_backdrop_switches_to_2)
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(0)
sprite1.set_y(0)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)
sprite1.add_sound('meow')

def when_program_starts_3(self):
    self.switch_backdrop_to("chalkboard")
    self.wait(1.0)
    self.switch_backdrop_to("blue_sky")

sprite1.when_program_starts(when_program_starts_3)

def when_backdrop_switches_to_4(self):
    self.say_for_seconds("Backdrop changed to Chalkboard", 0.5)

sprite1.when_backdrop_switches_to("chalkboard", when_backdrop_switches_to_4)
sprite2 = stage.add_a_sprite(None)
sprite2.set_name("Sprite2")
sprite2.set_x(-130.95103779895632)
sprite2.set_y(8.150999853107244)
sprite2.go_to_back_layer()
sprite2.go_forward(2)
sprite2.add_costume('costume1_2', center_x=47.67898252524472, center_y=49.49923017660271)
sprite2.add_costume('costume2', center_x=46, center_y=53)
sprite2.add_sound('meow')

def when_program_starts_5(self):
    self.wait(1.0)
    self.switch_backdrop_to("blue_sky")
    self.wait(1.0)

sprite2.when_program_starts(when_program_starts_5)

def when_backdrop_switches_to_6(self):
    self.say_for_seconds("Sprite2 backdrop changed to Blue Sky", 0.5)

sprite2.when_backdrop_switches_to("blue_sky", when_backdrop_switches_to_6)
stage.play()
