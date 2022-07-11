from pystage.en import Stage

stage = Stage()
zombie = stage.add_a_sprite()
zombie.set_ghost_effect_to(20)

def doit():
    for i in range(4):
        zombie.move(10)
        zombie.turn_left(90)
        zombie.wait(1)
        zombie.change_ghost_effect_by(20)
        print(zombie.y_position())

zombie.when_program_starts(doit)

stage.play()
