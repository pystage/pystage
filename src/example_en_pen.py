from pystage.en import Stage

stage = Stage()
pen = stage.add_a_sprite("pen")

def doit():
    pen.pen_down()
    for i in range(4):
        pen.move(10)
        pen.turn_left(90)
        pen.wait(1)
        print(pen.y_position())

pen.when_program_starts(doit)

stage.play()
