from pystage import Sprite, Stage

stage = Stage()
stage.add_backdrop("grid")
sprite = stage.create_sprite()


def do_something(self):
    self.say("Hello pyStage!")
    for i in range(4):
        self.move(20)
        self.wait(1)
        self.think("This is awesome!")
        self.turn_left(90)
        self.wait(1)
        self.think("")
    self.say("Move me around with WASD.")

sprite.when_program_is_started(do_something)


def right(self: Sprite):
    self.change_x_by(10)

def left(self: Sprite):
    self.change_x_by(-10)

def up(self: Sprite):
    self.change_y_by(-10)

def down(self: Sprite):
    self.change_y_by(10)

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
