# sensing1 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.add_backdrop('farm')
stage.create_variable('my variable', 0)
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(-20)
sprite1.set_y(2.4492935982947065e-15)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.point_in_direction(-90)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)
sprite1.add_sound('meow')

def when_program_starts_1(self):
    self.set_drag_mode_draggable()
    if self.touching_color((244, 176, 48)):
        self.ask_and_wait("What's your name?")

sprite1.when_program_starts(when_program_starts_1)

def when_this_sprite_clicked_2(self):
    self.point_in_direction(-90.0)
    self.move(10.0)
    if self.color_is_touching((255, 171, 25), (213, 135, 45)):
        self.ask_and_wait("what are you doing?")

sprite1.when_this_sprite_clicked(when_this_sprite_clicked_2)

def when_program_starts_3(self):
    self.wait(1.0)
    if self.touching_edge():
        self.go_to_x_y(0.0, 0.0)

sprite1.when_program_starts(when_program_starts_3)
stage.play()
