# operators3 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1")
stage.add_sound("pop")
stage.create_variable("my variable", 0)

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.add_costume("costume1", center_x=48, center_y=50)
sprite1.add_costume("costume2", center_x=46, center_y=53)
sprite1.add_sound("meow")

# Scratch Blocks for 'sprite1'

def when_program_starts_1(self):
    self.say(self.math_function("abs", -15))
    self.wait(1)
    self.say(self.math_function("floor", 1.9))
    self.wait(1)
    self.say(self.math_function("ceiling", 1.1))
    self.wait(1)
    self.say(self.math_function("sqrt", 15))
    self.wait(1)
    self.say(self.math_function("sin", 90))
    self.wait(1)
    self.say(self.math_function("cos", 90))
    self.wait(1)
    self.say(self.math_function("tan", 45))
    self.wait(1)
    self.say(self.math_function("asin", 1))
    self.wait(1)
    self.say(self.math_function("acos", 0))
    self.wait(1)
    self.say(self.math_function("atan", 1))
    self.wait(1)
    self.say(self.math_function("ln", 1))
    self.wait(1)
    self.say(self.math_function("log", 0.01))
    self.wait(1)
    self.say(self.math_function("e ^", 1))
    self.wait(1)
    self.say(self.math_function("10 ^", 2))
    self.wait(1)

sprite1.when_program_starts(when_program_starts_1)

stage.play()
