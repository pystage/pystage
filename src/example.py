from pystage.core.sprite import Sprite
from pystage.core.stage import Stage

stage = Stage()
stage.add_backdrop("grid")
sprite = stage.create_sprite()


def do_something(self: Sprite):
    self.say("Hello pyStage!")
    for i in range(4):
        self.motion_movesteps(20)
        self.wait(1)
        self.think("This is awesome!")
        self.motion_turnleft(90)
        self.wait(1)
        self.think("")
    self.say("Move me around with WASD.")

sprite.when_program_is_started(do_something)


def right(self: Sprite):
    self.motion_changexby(10)

def left(self: Sprite):
    self.motion_changexby(-10)

def up(self: Sprite):
    self.motion_changeyby(-10)

def down(self: Sprite):
    self.motion_changeyby(10)

def mouse(self: Sprite):
    self.say("Mouse pos: " + str(self.get_mouse_x()) + " / " + str(self.get_mouse_y()))

def say_space_pressed(self):
    while True:
        if self.is_key_pressed(" "):
            self.say("Space pressed!")

sprite.when_key_is_pressed("d", right)
sprite.when_key_is_pressed("a", left)
sprite.when_key_is_pressed("w", up)
sprite.when_key_is_pressed("s", down)
sprite.when_key_is_pressed("m", mouse)
sprite.when_program_is_started(say_space_pressed)

stage.play()
