# collision_and_list_test (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.add_backdrop('canyon')
stage.add_backdrop('hall')
stage.create_variable('my variable', 0)
stage.create_list_variable("l", ['list', 'owl', 'owl', 'owl', 'owl', 'owl', 'owl', 'owl'])
stage.show_list("l", -235, 175)
dinosaur5 = stage.add_a_sprite(None)
dinosaur5.set_name("Dinosaur5")
dinosaur5.set_x(-157.52664184570312)
dinosaur5.set_y(-42)
dinosaur5.go_to_back_layer()
dinosaur5.go_forward(1)
dinosaur5.point_in_direction(168.46572972124042)
dinosaur5.add_costume('dinosaur5_a', center_x=104, center_y=150, factor=2)
dinosaur5.add_costume('dinosaur5_b', center_x=112, center_y=166, factor=2)
dinosaur5.add_costume('dinosaur5_c', center_x=112, center_y=150, factor=2)
dinosaur5.add_costume('dinosaur5_d', center_x=90, center_y=134, factor=2)
dinosaur5.add_costume('dinosaur5_e', center_x=88, center_y=150, factor=2)
dinosaur5.add_costume('dinosaur5_f', center_x=94, center_y=166, factor=2)
dinosaur5.add_costume('dinosaur5_g', center_x=102, center_y=150, factor=2)
dinosaur5.add_costume('dinosaur5_h', center_x=108, center_y=134, factor=2)
dinosaur5.add_sound('dance_funky')
dinosaur5.add_sound('bite')

def when_program_starts_1(self):
    while True:
        self.glide_to_random_position(1.0)
        self.point_towards_mouse_pointer()
        self.if_on_edge_bounce()
        self.wait(1.0)
        if self.list_contains_item("l", "t"):
            self.delete_all_from_list("l")
            self.add_value_to_list("l", "list")

        self.add_value_to_list("l", "owl")

dinosaur5.when_program_starts(when_program_starts_1)
bat = stage.add_a_sprite(None)
bat.set_name("Bat")
bat.set_x(-114)
bat.set_y(-94)
bat.go_to_back_layer()
bat.go_forward(2)
bat.add_costume('bat_a', center_x=80, center_y=60)
bat.add_costume('bat_b', center_x=39, center_y=61)
bat.add_costume('bat_c', center_x=68, center_y=66)
bat.add_costume('bat_d', center_x=29, center_y=62)
bat.add_sound('owl')

def when_program_starts_2(self):
    while True:
        self.go_to_random_position()
        if self.touching_color((102, 202, 204)):
            self.play_sound_until_done("owl")

bat.when_program_starts(when_program_starts_2)
octopus = stage.add_a_sprite(None)
octopus.set_name("Octopus")
octopus.set_x(-94)
octopus.set_y(-20)
octopus.go_to_back_layer()
octopus.go_forward(3)
octopus.point_in_direction(180)
octopus.add_costume('octopus_a', center_x=88, center_y=86)
octopus.add_costume('octopus_b', center_x=88, center_y=86)
octopus.add_costume('octopus_c', center_x=88, center_y=86)
octopus.add_costume('octopus_d', center_x=88, center_y=86)
octopus.add_costume('octopus_e', center_x=88, center_y=86)
octopus.add_sound('splash')
octopus.add_sound('ocean_wave')

def when_program_starts_3(self):
    while True:
        self.set_rotation_style_left_right()
        self.change_x_by(10.0)
        self.turn_right(90.0)
        self.glide_to_sprite(1.0, "NO TRANSLATION: motion_glideto_menu")
        if self.touching_color((100, 100, 90)):
            self.say("Hello!")
            self.wait(10.0)
            self.stop_all()

octopus.when_program_starts(when_program_starts_3)
stage.play()
