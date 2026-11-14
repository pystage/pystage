# collision_and_list_test (pyStage, converted from Scratch 3)
#
# Not everything of the Scratch project could be converted:
# - [loose_script] Stage: 1 script(s) without a hat block were left out (in Scratch they only run when clicked in the editor).

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1", center_x=240, center_y=180)
stage.add_backdrop("canyon", center_x=480, center_y=360, factor=2)
stage.add_backdrop("hall", center_x=480, center_y=360, factor=2)
stage.switch_backdrop_to("canyon")
stage.add_sound("pop")
stage.create_variable("my variable", 0)
stage.create_list("l", ["list", "owl", "owl", "owl", "owl", "owl", "owl", "owl"])
stage.show_list("l")
stage.set_list_monitor_position("l", -235, 175, 0, 0)

# Create and initialize sprite 'dinosaur5'
dinosaur5 = stage.add_a_sprite(None)
dinosaur5.set_name("Dinosaur5")
dinosaur5.go_to_x_y(-157.52664184570312, -42)
dinosaur5.point_in_direction(168.46572972124042)
dinosaur5.add_costume("dinosaur5_a", center_x=104, center_y=150, factor=2)
dinosaur5.add_costume("dinosaur5_b", center_x=112, center_y=166, factor=2)
dinosaur5.add_costume("dinosaur5_c", center_x=112, center_y=150, factor=2)
dinosaur5.add_costume("dinosaur5_d", center_x=90, center_y=134, factor=2)
dinosaur5.add_costume("dinosaur5_e", center_x=88, center_y=150, factor=2)
dinosaur5.add_costume("dinosaur5_f", center_x=94, center_y=166, factor=2)
dinosaur5.add_costume("dinosaur5_g", center_x=102, center_y=150, factor=2)
dinosaur5.add_costume("dinosaur5_h", center_x=108, center_y=134, factor=2)
dinosaur5.add_sound("dance_funky")
dinosaur5.add_sound("bite")

# Create and initialize sprite 'bat'
bat = stage.add_a_sprite(None)
bat.set_name("Bat")
bat.go_to_x_y(-114, -94)
bat.add_costume("bat_a", center_x=80, center_y=60)
bat.add_costume("bat_b", center_x=39, center_y=61)
bat.add_costume("bat_c", center_x=68, center_y=66)
bat.add_costume("bat_d", center_x=29, center_y=62)
bat.add_sound("owl")

# Create and initialize sprite 'octopus'
octopus = stage.add_a_sprite(None)
octopus.set_name("Octopus")
octopus.go_to_x_y(-94, -20)
octopus.point_in_direction(180)
octopus.set_rotation_style_left_right()
octopus.add_costume("octopus_a", center_x=88, center_y=86)
octopus.add_costume("octopus_b", center_x=88, center_y=86)
octopus.add_costume("octopus_c", center_x=88, center_y=86)
octopus.add_costume("octopus_d", center_x=88, center_y=86)
octopus.add_costume("octopus_e", center_x=88, center_y=86)
octopus.add_sound("splash")
octopus.add_sound("ocean_wave")

# Scratch Blocks for 'dinosaur5'

def when_program_starts_1(self):
    while True:
        self.glide_to_random_position(1)
        self.point_towards_mouse_pointer()
        self.if_on_edge_bounce()
        self.wait(1)
        if self.list_contains("l", "t"):
            self.delete_all_of_list("l")
            self.add_to_list("l", "list")
        self.add_to_list("l", "owl")

dinosaur5.when_program_starts(when_program_starts_1)

# Scratch Blocks for 'bat'

def when_program_starts_2(self):
    while True:
        self.go_to_random_position()
        if self.touching_color((102, 202, 204)):
            self.play_sound_until_done("owl")

bat.when_program_starts(when_program_starts_2)

# Scratch Blocks for 'octopus'

def when_program_starts_3(self):
    while True:
        self.set_rotation_style_left_right()
        self.change_x_by(10)
        self.turn_right(90)
        self.glide_to_sprite(1, dinosaur5)
        if self.touching_color((100, 100, 90)):
            self.say("Hello!")
            self.wait(10)
            self.stop_all()
            return


octopus.when_program_starts(when_program_starts_3)

stage.play()
