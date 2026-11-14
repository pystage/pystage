# custom_blocks (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage, no_refresh

stage = Stage()
stage.add_backdrop("backdrop1", center_x=240, center_y=180)
stage.add_backdrop("backdrop2", center_x=240, center_y=180)
stage.add_sound("pop")
stage.create_variable("count", 0)

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.add_costume("costume1", center_x=20, center_y=20)
sprite1.add_costume("costume2", center_x=20, center_y=20)
sprite1.add_sound("meow")
sprite1.create_variable("sum", 0, all_sprites=False)

# Scratch Blocks for 'stage'

@no_refresh
def stage_count_up(self, by):
    self.change_variable_by("count", by)


def when_program_starts_1(self):
    stage_count_up(self, 2)
    stage_count_up(self, 3)

stage.when_program_starts(when_program_starts_1)

# Scratch Blocks for 'sprite1'

def sprite1_jump_times(self, count):
    for _ in range(int(count)):
        self.change_y_by(10)
        self.wait(0.05)
    self.change_y_by(-50)


@no_refresh
def sprite1_square(self, size, steps):
    for _ in range(int(steps)):
        self.move(size)
        self.turn_right(90)


def sprite1_say_if(self, flag):
    if flag:
        self.say("yes")
    else:
        self.say("no")


def sprite1_add_up(self, n):
    if (n > 0):
        self.change_variable_by("sum", n)
        sprite1_add_up(self, (n - 1))
    return

    self.say("never")


def sprite1_no_arguments(self):
    self.turn_left(1)


def when_program_starts_2(self):
    sprite1_jump_times(self, 3)
    sprite1_square(self, 20, 4)
    sprite1_say_if(self, (2 > 1))
    sprite1_say_if(self, "")
    sprite1_add_up(self, 4)
    sprite1_no_arguments(self)
    sprite1_jump_times(self, self.get_variable("sum"))
    self.say(self.get_variable("sum"))

sprite1.when_program_starts(when_program_starts_2)

stage.play()
