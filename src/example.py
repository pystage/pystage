from pystage.core.sprite import CoreSprite
from pystage.core.stage import CoreStage

stage = CoreStage()
stage.pystage_addbackdrop("grid")
sprite = stage.pystage_createsprite()
sprite.pystage_addsound("dancehead2")



def do_something(self: CoreSprite):
    self.looks_say("Hello pyStage!")
    for i in range(4):
        self.looks_changesizeby(20)
        self.motion_movesteps(20)
        self.control_wait(1)
        # self.looks_think("This is awesome!")
        self.motion_turnleft(90)
        self.control_wait(1)
        # self.looks_think("")
    self.looks_say("Move me around with WASD.")

sprite.event_whenflagclicked(do_something)


def soundcheck(self: CoreSprite):
    self.sound_playuntildone("dancehead2")
    self.looks_say("Sound finished!")

sprite.event_whenflagclicked(soundcheck)

def right(self: CoreSprite):
    self.motion_changexby(10)

def left(self: CoreSprite):
    self.motion_changexby(-10)

def up(self: CoreSprite):
    self.motion_changeyby(10)

def down(self: CoreSprite):
    self.motion_changeyby(-10)

def mouse(self: CoreSprite):
    self.motion_pointtowards_pointer()
    self.looks_say(f"Mouse pos: {self.sensing_mousex()} / {self.sensing_mousey()}")

def say_space_pressed(self: CoreSprite):
    while True:
        if self.sensing_keypressed(" "):
            self.looks_say("Space pressed!")

def pen_toggle(self: CoreSprite):
    if self.pen:
        self.pen_penUp()
    else:
        self.pen_penDown()

def pen_clear(self: CoreSprite):
    self.pen_clear()

sprite.event_whenkeypressed("d", right)
sprite.event_whenkeypressed("a", left)
sprite.event_whenkeypressed("w", up)
sprite.event_whenkeypressed("s", down)
sprite.event_whenkeypressed("m", mouse)
sprite.event_whenkeypressed("p", pen_toggle)
sprite.event_whenkeypressed("c", pen_clear)
sprite.event_whenflagclicked(say_space_pressed)

stage.pystage_play()
