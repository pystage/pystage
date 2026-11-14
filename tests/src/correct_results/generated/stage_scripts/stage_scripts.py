# stage_scripts (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1", center_x=240, center_y=180)
stage.add_backdrop("backdrop2", center_x=240, center_y=180)
stage.add_sound("pop")
stage.create_variable("score", 7)
stage.create_list("log", ["start"])
stage.show_variable("score")
stage.set_monitor_position("score", -235, 175)
stage.show_list("log")
stage.set_list_monitor_position("log", -235, 140, 150, 100)

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.add_costume("costume1", center_x=20, center_y=20)
sprite1.add_costume("costume2", center_x=20, center_y=20)
sprite1.add_sound("meow")

# Scratch Blocks for 'stage'

def when_stage_clicked_1(self):
    self.next_backdrop()
    self.change_variable_by("score", 1)
    self.start_sound("pop")

stage.when_stage_clicked(when_stage_clicked_1)

def when_backdrop_switches_to_2(self):
    self.add_to_list("log", "backdrop2")
    self.broadcast("backdrop changed")

stage.when_backdrop_switches_to("backdrop2", when_backdrop_switches_to_2)

def when_program_starts_3(self):
    self.switch_backdrop_to("backdrop2")
    self.switch_to_next_backdrop()
    self.switch_to_previous_backdrop()
    self.switch_to_random_backdrop()
    self.switch_backdrop_to_and_wait("backdrop2")
    self.switch_backdrop_to_and_wait("backdrop1")
    self.next_backdrop()
    self.set_color_effect_to(25)
    self.change_brightness_effect_by(10)
    self.clear_graphic_effects()
    self.set_volume_to(80)
    self.set_variable("score", self.get_variable_of("score", stage))
    self.add_to_list("log", self.backdrop_name())
    self.add_to_list("log", self.backdrop_number())
    self.add_to_list("log", self.backdrop_of(stage))
    self.add_to_list("log", self.backdrop_name_of(stage))
    self.add_to_list("log", self.volume_of(stage))
    self.broadcast_and_wait("done")
    self.stop_other_scripts_in_stage()

    self.add_to_list("log", "end")

stage.when_program_starts(when_program_starts_3)

def when_program_starts_4(self):
    while True:
        self.change_variable_by("score", 1)
        self.wait(0.1)

stage.when_program_starts(when_program_starts_4)

def when_key_pressed_5(self):
    self.broadcast_and_wait("done")

stage.when_key_pressed("space", when_key_pressed_5)

def when_i_receive_message_6(self):
    self.add_to_list("log", "done")

stage.when_i_receive_message("done", when_i_receive_message_6)

def when_program_starts_7(self):
    self.create_clone_of_sprite(sprite1)
    self.ask_and_wait("Name?")
    self.add_to_list("log", self.answer())

stage.when_program_starts(when_program_starts_7)

# Scratch Blocks for 'sprite1'

def when_i_receive_message_8(self):
    self.say(self.backdrop_name())
    self.say(self.backdrop_number())

sprite1.when_i_receive_message("backdrop changed", when_i_receive_message_8)

def when_key_pressed_9(self):
    self.say("enter")

sprite1.when_key_pressed("enter", when_key_pressed_9)

stage.play()
