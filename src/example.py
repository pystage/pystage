from pystage import Sprite, Stage

stage = Stage()
stage.add_backdrop("grid")
zombie = stage.create_sprite()


def do_something(zombie: Sprite):
    zombie.say("Hello pyStage!")
    for i in range(4):
        zombie.move(20)
        zombie.wait(1)
        zombie.think("This is awesome!")
        zombie.turn_left(90)
        zombie.wait(1)
        zombie.think("")
    zombie.say("Move me around with WASD.")

zombie.when_program_is_started(do_something)


def right(zombie: Sprite):
    zombie.change_x_by(10)

def left(zombie: Sprite):
    zombie.change_x_by(-10)

def up(zombie: Sprite):
    zombie.change_y_by(-10)

def down(zombie: Sprite):
    zombie.change_y_by(10)

def mouse(zombie: Sprite):
    zombie.say(f"Mouse pos: {zombie.get_mouse_x()} / {zombie.get_mouse_y()}")

def say_space_pressed(zombie):
    while True:
        if zombie.is_key_pressed(" "):
            zombie.say("Space pressed!")

zombie.when_key_is_pressed("d", right)
zombie.when_key_is_pressed("a", left)
zombie.when_key_is_pressed("w", up)
zombie.when_key_is_pressed("s", down)
zombie.when_key_is_pressed("m", mouse)
zombie.when_program_is_started(say_space_pressed)

stage.play()
