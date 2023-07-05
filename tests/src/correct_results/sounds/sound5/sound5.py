# sound5 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.add_backdrop('witch_house')
stage.create_variable('my variable', 0)
saxophone = stage.add_a_sprite(None)
saxophone.set_name("Saxophone")
saxophone.set_x(-2)
saxophone.set_y(-28)
saxophone.go_to_back_layer()
saxophone.go_forward(2)
saxophone.point_in_direction(180)
saxophone.add_costume('saxophone_a', center_x=47, center_y=80)
saxophone.add_costume('saxophone_b', center_x=47, center_y=80)
saxophone.add_sound('c_sax')
saxophone.add_sound('d_sax')
saxophone.add_sound('e_sax')
saxophone.add_sound('f_sax')
saxophone.add_sound('g_sax')
saxophone.add_sound('a_sax')
saxophone.add_sound('b_sax')
saxophone.add_sound('c2_sax')

def when_this_sprite_clicked_1(self):
    self.switch_backdrop_to("witch_house")
    self.set_pitch_effect_to(100.0)
    for _ in range(10):
        self.change_volume_by(self.volume())
        self.play_sound_until_done("c2_sax")
        self.change_volume_by(-10.0)

    self.point_in_direction(180.0)

saxophone.when_this_sprite_clicked(when_this_sprite_clicked_1)
guitar_electric1 = stage.add_a_sprite(None)
guitar_electric1.set_name("Guitar-electric1")
guitar_electric1.set_x(187)
guitar_electric1.set_y(-31)
guitar_electric1.go_to_back_layer()
guitar_electric1.go_forward(1)
guitar_electric1.add_costume('guitar_electric1_a', center_x=42, center_y=85)
guitar_electric1.add_costume('guitar_electric1_b', center_x=42, center_y=85)
guitar_electric1.add_sound('c_elec_guitar')
guitar_electric1.add_sound('d_elec_guitar')
guitar_electric1.add_sound('e_elec_guitar')
guitar_electric1.add_sound('f_elec_guitar')
guitar_electric1.add_sound('g_elec_guitar')
guitar_electric1.add_sound('a_elec_guitar')
guitar_electric1.add_sound('b_elec_guitar')
guitar_electric1.add_sound('c2_elec_guitar')
guitar_electric1.show_builtinvariable("volume", -235, 175)

def when_this_sprite_clicked_2(self):
    self.change_pitch_effect_by(1000000.0)
    for _ in range(10):
        self.change_volume_by(self.volume())
        self.play_sound_until_done("c2_elec_guitar")
        self.set_volume_to(200.0)

guitar_electric1.when_this_sprite_clicked(when_this_sprite_clicked_2)
drum_kit = stage.add_a_sprite(None)
drum_kit.set_name("Drum Kit")
drum_kit.set_x(-154)
drum_kit.set_y(-38)
drum_kit.go_to_back_layer()
drum_kit.go_forward(3)
drum_kit.add_costume('drum_kit', center_x=58, center_y=78)
drum_kit.add_costume('drum_kit_b', center_x=58, center_y=78)
drum_kit.add_sound('drum_bass1')
drum_kit.add_sound('drum_bass2')
drum_kit.add_sound('drum_bass3')
drum_kit.add_sound('high_tom')
drum_kit.add_sound('low_tom')

def when_this_sprite_clicked_3(self):
    for _ in range(10):
        self.change_volume_by(self.volume())
        self.play_sound_until_done("low_tom")

drum_kit.when_this_sprite_clicked(when_this_sprite_clicked_3)
stage.play()
