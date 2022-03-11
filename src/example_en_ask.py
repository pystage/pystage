from pystage.en import Stage

stage = Stage()
zombie = stage.add_a_sprite()

def doit():
    zombie.ask_and_wait("Hi, how are you?")
    zombie.say(f"Great, that you are {zombie.answer()}!")
    zombie.wait(2)
    zombie.ask_and_wait("And what else?")
    zombie.ask_and_wait("Just one more question... what is 7+7?")
    zombie.say(f"Your answer: {zombie.answer()}")

zombie.when_program_starts(doit)

stage.play()
