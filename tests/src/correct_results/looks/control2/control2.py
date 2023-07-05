# control2 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.add_backdrop('beach_rio')
stage.create_variable('my variable', 0)

def when_GREENFLAG_clicked_1(self):
    while True:
        if self.mouse_down():
            self.play_sound_until_done("pop")

        if self.mouse_down():
            self.set_pitch_effect_to(100.0)
        else:
            self.stop_all_sounds()

stage.when_GREENFLAG_clicked(when_GREENFLAG_clicked_1)

def when_GREENFLAG_clicked_2(self):
    for _ in range(10):
        if self.key_pressed("space"):
            for _ in range(10):
                self.switch_backdrop_to("beach_rio")
        else:
            self.start_sound("pop")

stage.when_GREENFLAG_clicked(when_GREENFLAG_clicked_2)
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(-15)
sprite1.set_y(1)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)
sprite1.add_sound('meow')
stage.play()
