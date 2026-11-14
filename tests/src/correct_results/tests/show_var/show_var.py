# show_var (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1", center_x=240, center_y=180)
stage.add_sound("pop")
stage.create_variable("my variable", 29)
stage.create_list("list", ["asdfasdfasdfasdfasdfasfd"])
stage.show_variable("my variable")
stage.set_monitor_position("my variable", -35, 94)
stage.show_list("list")
stage.set_list_monitor_position("list", 82, 64, 100, 200)

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.go_to_x_y(-32, -12)
sprite1.add_costume("costume1", center_x=48, center_y=50)
sprite1.add_costume("costume2", center_x=46, center_y=53)
sprite1.add_sound("meow")
sprite1.create_list("a", [], all_sprites=False)

# Scratch Blocks for 'sprite1'

def when_program_starts_1(self):
    self.set_variable("my variable", 10)

sprite1.when_program_starts(when_program_starts_1)

stage.play()
