# test (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1")
stage.add_sound("pop")
stage.create_variable("my variable", 0)

# Create and initialize sprite 'cheesy_puffs'
cheesy_puffs = stage.add_a_sprite(None)
cheesy_puffs.set_name("Cheesy Puffs")
cheesy_puffs.go_to_x_y(-13, -15)
cheesy_puffs.add_costume("cheesy_puffs", center_x=87, center_y=72, factor=2)
cheesy_puffs.add_sound("pop")

# Create and initialize sprite 'dog2'
dog2 = stage.add_a_sprite(None)
dog2.set_name("Dog2")
dog2.go_to_x_y(-142, 13)
dog2.add_costume("dog2_a", center_x=75, center_y=75)
dog2.add_costume("dog2_b", center_x=75, center_y=75)
dog2.add_costume("dog2_c", center_x=75, center_y=75)
dog2.switch_costume_to("dog2_c")
dog2.add_sound("dog1")

stage.play()
