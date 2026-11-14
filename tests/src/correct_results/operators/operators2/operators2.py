# operators2 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1", center_x=240, center_y=180)
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
    self.say(self.join("apple ", "banana"))
    self.wait(1)
    self.say(self.letter_of(2, "apple"))
    self.wait(1)
    self.say(self.length_of("apple"))
    self.wait(1)
    self.say(self.contains("apple", "a"))
    self.wait(1)
    self.say((10 % 3))
    self.wait(1)
    self.say(self.round(1.1))
    self.wait(1)
    self.say(self.round(1.5))

sprite1.when_program_starts(when_program_starts_1)

stage.play()
