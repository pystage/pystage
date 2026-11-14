# control_clones (pyStage, converted from Scratch 3)

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
sprite1.create_variable("n", 0, all_sprites=False)

# Create and initialize sprite 'sprite2'
sprite2 = stage.add_a_sprite(None)
sprite2.set_name("Sprite2")
sprite2.add_costume("costume1_2", center_x=20, center_y=20)
sprite2.add_costume("costume2_2", center_x=20, center_y=20)
sprite2.add_sound("meow")

# Scratch Blocks for 'sprite1'

def when_program_starts_1(self):
    for _ in range(3):
        self.change_x_by(5)
    if (self.get_variable("n") == 0):
        self.set_variable("n", 1)
    else:
        self.set_variable("n", 2)
    while not (self.get_variable("n") > 4):
        self.change_variable_by("n", 1)
    while not (self.timer() > 0.2):
        pass
    self.wait(0.1)
    self.create_clone_of_myself()
    self.create_clone_of_sprite(sprite2)
    self.broadcast("go")
    self.stop_other_scripts_in_sprite()

    return


sprite1.when_program_starts(when_program_starts_1)

def when_program_starts_2(self):
    while True:
        self.turn_right(1)
        if (self.get_variable("n") > 100):
            self.stop_all()
            return


sprite1.when_program_starts(when_program_starts_2)

def when_i_start_as_a_clone_3(self):
    self.change_y_by(30)
    self.wait(0.2)
    self.delete_this_clone()

sprite1.when_i_start_as_a_clone(when_i_start_as_a_clone_3)

def when_this_sprite_clicked_4(self):
    self.say("Clicked")

sprite1.when_this_sprite_clicked(when_this_sprite_clicked_4)

def when_key_pressed_5(self):
    self.stop_all()
    return


sprite1.when_key_pressed("space", when_key_pressed_5)

# Scratch Blocks for 'sprite2'

def when_i_receive_message_6(self):
    self.broadcast_and_wait("go2")
    self.stop_all()
    return


sprite2.when_i_receive_message("go", when_i_receive_message_6)

def when_i_receive_message_7(self):
    self.wait(0.1)

sprite2.when_i_receive_message("go2", when_i_receive_message_7)

def when_key_pressed_8(self):
    self.change_y_by(10)

sprite2.when_key_pressed("up arrow", when_key_pressed_8)

def when_key_pressed_9(self):
    self.change_y_by(-10)

sprite2.when_key_pressed("0", when_key_pressed_9)

stage.play()
