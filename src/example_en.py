from pystage.en import Sprite, Stage

stage = Stage()
zombie = stage.create_sprite()

def doit(zombie: Sprite):
    for i in range(4):
        zombie.move(10)
        zombie.turn_left(90)
        zombie.wait(1)

zombie.when_program_is_started(doit)

stage.play()
