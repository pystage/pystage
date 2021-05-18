from pystage import Sprite, Stage

stage = Stage(500, 500)
sprite = stage.create_sprite()

def do_something():
    sprite.x = 250
    sprite.y = 250
    yield 0
    for i in range(4):
        sprite.move(20)
        sprite.turn_left(90)
        yield 1

sprite.do(do_something)

stage.play()
