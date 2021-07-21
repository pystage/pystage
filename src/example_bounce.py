from pystage.en import Sprite, Stage

stage = Stage()
zombie = stage.add_a_sprite()


def doit(zombie: Sprite):
    zombie.set_rotation_style_left_right()
    while True:
        zombie.move(1)
        zombie.if_on_edge_bounce()

def gotomouse(zombie: Sprite):
    zombie.point_towards_mouse_pointer()
    print(zombie.direction())

zombie.when_program_starts(doit)
zombie.when_key_pressed(" ", gotomouse)

stage.play()
