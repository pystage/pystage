from pystage.en import Sprite, Stage

stage = Stage()
zombie1 = stage.add_a_sprite()
zombie2 = stage.add_a_sprite()

def z1(zombie: Sprite):
    zombie.go_to_x_y(-40, 0)
    zombie.broadcast("hello")


def z2(zombie: Sprite):
    zombie.go_to_x_y(40, 0)
    zombie.say("You said hello!")


zombie1.when_program_starts(z1)
zombie2.when_i_receive_message("hello", z2)

stage.play()
