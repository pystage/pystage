# test (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable', 0)
cheesy_puffs = stage.add_a_sprite(None)
cheesy_puffs.set_name("Cheesy Puffs")
cheesy_puffs.set_x(-13)
cheesy_puffs.set_y(-15)
cheesy_puffs.go_to_back_layer()
cheesy_puffs.go_forward(1)
cheesy_puffs.add_costume('cheesy_puffs', center_x=87, center_y=72, factor=2)
cheesy_puffs.add_sound('pop')
dog2 = stage.add_a_sprite(None)
dog2.set_name("Dog2")
dog2.set_x(-142)
dog2.set_y(13)
dog2.go_to_back_layer()
dog2.go_forward(2)
dog2.add_costume('dog2_a', center_x=75, center_y=75)
dog2.add_costume('dog2_b', center_x=75, center_y=75)
dog2.add_costume('dog2_c', center_x=75, center_y=75)
dog2.next_costume()
dog2.next_costume()
dog2.add_sound('dog1')
stage.play()
