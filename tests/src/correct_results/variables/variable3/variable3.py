# variable3 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("backdrop1")
stage.add_sound("pop")
stage.create_variable("Num2", "3")
stage.create_variable("Num1", "3")
stage.create_variable("Sum", 6)
stage.create_variable("Year", 8556.637145104167)
stage.show_variable("Num1")
stage.set_monitor_position("Num1", -235, 175)
stage.show_variable("Sum")
stage.set_monitor_position("Sum", -235, 148)
stage.show_variable("Num2")
stage.set_monitor_position("Num2", -235, 121)
stage.show_variable("Year")
stage.set_monitor_position("Year", -235, 94)

# Create and initialize sprite 'jouvi_dance'
jouvi_dance = stage.add_a_sprite(None)
jouvi_dance.set_name("Jouvi Dance")
jouvi_dance.go_to_x_y(-47, 38)
jouvi_dance.add_costume("jo_stance", center_x=94, center_y=240, factor=2)
jouvi_dance.add_costume("jo_top_stand", center_x=68, center_y=260, factor=2)
jouvi_dance.add_costume("jo_top_r_leg", center_x=218, center_y=262, factor=2)
jouvi_dance.add_costume("jo_top_l_leg", center_x=208, center_y=268, factor=2)
jouvi_dance.add_costume("jo_top_r_cross", center_x=144, center_y=270, factor=2)
jouvi_dance.add_costume("jo_top_l_cross", center_x=84, center_y=268, factor=2)
jouvi_dance.add_costume("jo_pop_front", center_x=70, center_y=228, factor=2)
jouvi_dance.add_costume("jo_pop_down", center_x=68, center_y=74, factor=2)
jouvi_dance.add_costume("jo_pop_left", center_x=196, center_y=226, factor=2)
jouvi_dance.add_costume("jo_pop_right", center_x=66, center_y=242, factor=2)
jouvi_dance.add_costume("jo_pop_l_arm", center_x=108, center_y=258, factor=2)
jouvi_dance.add_costume("jo_pop_stand", center_x=78, center_y=262, factor=2)
jouvi_dance.add_costume("jo_pop_r_arm", center_x=108, center_y=260, factor=2)
jouvi_dance.add_sound("dance_celebrate")

# Scratch Blocks for 'jouvi_dance'

def when_program_starts_1(self):
    self.ask_and_wait("enter your number")
    self.set_variable("Num1", self.answer())
    self.ask_and_wait("enter your number")
    self.set_variable("Num2", self.answer())
    self.set_variable("Sum", (self.get_variable("Num1") + self.get_variable("Num2")))
    self.set_variable("Year", self.days_since())
    self.say_for_seconds(self.join("the answer is ", self.get_variable("Sum")), 2)

jouvi_dance.when_program_starts(when_program_starts_1)

stage.play()
