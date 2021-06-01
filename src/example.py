from pystage import Sprite, Stage

stage = Stage()
sprite = stage.create_sprite()

def do_something(self):
    self.x = 250
    self.y = 250
    for i in range(4):
        self.move(20)
        self.turn_left(90)

sprite.when_program_is_started(do_something)


def react_to_key(self):
    self.move(10)

sprite.when_key_is_pressed(" ", react_to_key, no_refresh=True)

stage.play()
