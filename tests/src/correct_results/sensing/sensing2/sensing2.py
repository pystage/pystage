# sensing2 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1", center_x=240, center_y=180)
stage.add_sound("pop")
stage.create_variable("my variable", 0)

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.go_to_x_y(8, 28)
sprite1.set_drag_mode_draggable()
sprite1.add_costume("costume1", center_x=48, center_y=50)
sprite1.add_costume("costume2", center_x=46, center_y=53)
sprite1.add_sound("meow")

# Scratch Blocks for 'sprite1'

def when_program_starts_1(self):
    if self.key_pressed("n"):
        while not self.mouse_down():
            pass
        while True:
            self.set_pitch_effect_to(100)
            self.start_sound("meow")
            self.stop_all()
            return


sprite1.when_program_starts(when_program_starts_1)

def when_program_starts_2(self):
    self.set_drag_mode_draggable()
    if ((self.distance_to_mouse_pointer() + 10) > 100):
        self.play_sound_until_done("meow")
    else:
        self.go_to_x_y(0, 0)

sprite1.when_program_starts(when_program_starts_2)

stage.play()
