from pystage import Sprite, Stage

stage = Stage()
stage.add_backdrop("grid")
sprite = stage.create_sprite()

def do_something(self):
    for i in range(4):
        self.move(20)
        self.wait(1)
        self.turn_left(90)
        self.wait(1)

sprite.when_program_is_started(do_something)


def react_to_key(self):
    self.move(10)

sprite.when_key_is_pressed(" ", react_to_key)

stage.play()
