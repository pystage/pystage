# variable6 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1")
stage.add_sound("pop")
stage.create_variable("my variable", 2)
stage.create_variable("var", 0)
stage.show_variable("var")
stage.set_monitor_position("var", -235, 175)

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.go_to_x_y(19, 100)
sprite1.add_costume("costume1", center_x=48, center_y=50)
sprite1.add_costume("costume2", center_x=46, center_y=53)
sprite1.add_sound("meow")

# Create and initialize sprite 'buildings'
buildings = stage.add_a_sprite(None)
buildings.set_name("Buildings")
buildings.go_to_x_y(100, -11)
buildings.add_costume("building_a", center_x=40, center_y=30)
buildings.add_costume("building_b", center_x=46, center_y=-11)
buildings.add_costume("building_c", center_x=25, center_y=17)
buildings.add_costume("building_d", center_x=59, center_y=-10)
buildings.add_costume("building_e", center_x=36, center_y=55)
buildings.add_costume("building_f", center_x=41, center_y=27)
buildings.add_costume("building_g", center_x=64, center_y=-65)
buildings.add_costume("building_h", center_x=33, center_y=136)
buildings.add_costume("building_i", center_x=31, center_y=-12)
buildings.add_costume("building_j", center_x=29, center_y=33)
buildings.add_sound("pop")

# Scratch Blocks for 'sprite1'

def when_program_starts_1(self):
    self.set_variable("my variable", self.costume_number())
    self.wait(1)
    self.change_variable_by("my variable", self.backdrop_number())
    self.wait(1)
    self.set_y(self.size())

sprite1.when_program_starts(when_program_starts_1)

# Scratch Blocks for 'buildings'

def when_program_starts_2(self):
    self.set_x(self.size())

buildings.when_program_starts(when_program_starts_2)

stage.play()
