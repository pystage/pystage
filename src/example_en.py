from pystage.en import Sprite, Stage

stage = Stage()
zombie = stage.create_sprite()

def doit(zombie: Sprite):
    for i in range(4):
        zombie.move_steps(10)
        zombie.turn_left_degrees(90)
        zombie.wait_seconds(1)

zombie.when_GREENFLAG_clicked(doit)

stage.play()
