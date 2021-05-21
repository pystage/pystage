from pystage import Sprite, Stage

stage = Stage(500, 500)
sprite = stage.create_sprite()

def do_something(self):
    self.x = 250
    self.y = 250
    yield 1
    for i in range(4):
        self.move(20)
        self.turn_left(90)
        yield 1

sprite.when_program_is_started(do_something)


def react_to_key(self):
    self.move(10)

sprite.when_key_is_pressed(" ", react_to_key)

stage.play()
