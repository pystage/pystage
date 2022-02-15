from pystage.en import Stage

stage = Stage()
zombie = stage.add_a_sprite()

def doit():
    for i in range(4):
        zombie.move(10)
        zombie.turn_left(90)
        zombie.wait(1)
        print(zombie.y_position())

zombie.when_program_starts(doit)

stage.play()
