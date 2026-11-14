# list_contains_item (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1")
stage.add_sound("pop")
stage.create_variable("my variable", 0)
stage.create_list("a_list_man", ["thing"])
stage.show_list("a_list_man")
stage.set_list_monitor_position("a_list_man", -235, 175, 0, 0)

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.add_costume("costume1", center_x=48, center_y=50)
sprite1.add_costume("costume2", center_x=46, center_y=53)
sprite1.add_sound("meow")

# Scratch Blocks for 'sprite1'

def when_program_starts_1(self):
    if self.list_contains("a_list_man", "thing"):
        self.say("Hello!")

sprite1.when_program_starts(when_program_starts_1)

def when_key_pressed_2(self):
    self.add_to_list("a_list_man", "thing")

sprite1.when_key_pressed("space", when_key_pressed_2)

stage.play()
