from pystage.core.sprite import Sprite
from pystage.core.stage import Stage

stage = Stage()
stage.add_backdrop("grid")
sprite = stage.create_sprite()


def do_something(self: Sprite):
    self.looks_say("Hello pyStage!")
    for i in range(4):
        self.motion_movesteps(20)
        self.control_wait(1)
        self.looks_think("This is awesome!")
        self.motion_turnleft(90)
        self.control_wait(1)
        self.looks_think("")
    self.looks_say("Move me around with WASD.")

sprite.event_whenflagclicked(do_something)


def right(self: Sprite):
    self.motion_changexby(10)

def left(self: Sprite):
    self.motion_changexby(-10)

def up(self: Sprite):
    self.motion_changeyby(-10)

def down(self: Sprite):
    self.motion_changeyby(10)

def mouse(self: Sprite):
    self.looks_say(f"Mouse pos: {self.sensing_mousex()} / {self.sensing_mousey()}")

def say_space_pressed(self: Sprite):
    while True:
        if self.sensing_keypressed(" "):
            self.looks_say("Space pressed!")

sprite.event_whenkeypressed("d", right)
sprite.event_whenkeypressed("a", left)
sprite.event_whenkeypressed("w", up)
sprite.event_whenkeypressed("s", down)
sprite.event_whenkeypressed("m", mouse)
sprite.event_whenflagclicked(say_space_pressed)

stage.play()
