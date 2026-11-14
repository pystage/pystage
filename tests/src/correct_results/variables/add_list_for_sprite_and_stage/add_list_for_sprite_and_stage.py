# add_list_for_sprite_and_stage (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1")
stage.add_sound("pop")
stage.create_variable("my variable", 0)
stage.create_list("list_in_Sprite1", [])
stage.create_list("list_for_stage", ["stage"])
stage.show_list("list_for_stage")
stage.set_list_monitor_position("list_for_stage", -85, 175, 0, 0)

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.add_costume("costume1", center_x=48, center_y=50)
sprite1.add_costume("costume2", center_x=46, center_y=53)
sprite1.add_sound("meow")
sprite1.create_list("list_for_sprite", ["sprite"], all_sprites=False)
sprite1.show_list("list_for_sprite")
sprite1.set_list_monitor_position("list_for_sprite", -235, 175, 0, 0)

# Scratch Blocks for 'stage'

def when_program_starts_1(self):
    self.wait(1)
    self.add_to_list("list_for_stage", "stage")

stage.when_program_starts(when_program_starts_1)

# Scratch Blocks for 'sprite1'

def when_program_starts_2(self):
    self.add_to_list("list_for_sprite", "sprite")

sprite1.when_program_starts(when_program_starts_2)

stage.play()
