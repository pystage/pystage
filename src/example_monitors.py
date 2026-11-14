from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop("grid")
sprite = stage.add_a_sprite()

# Monitors of values, like the checkboxes next to the blocks in Scratch
sprite.show_monitor("x position")
sprite.set_value_monitor_position("x position", -100, 130)
stage.show_monitor("timer")
stage.set_value_monitor_position("timer", -100, 100)


def do_something(self: Sprite):
    self.create_variable("test")
    self.set_variable("test", 99999999999)
    self.show_variable("test")
    self.set_monitor_position("test", -100, 70)
    self.set_monitor_style_large("test")
    self.create_variable("speed", 50)
    self.show_variable("speed")
    self.set_monitor_position("speed", -100, 20)
    # A slider can be dragged with the mouse
    self.set_monitor_style_slider("speed", 0, 100)
    self.glide_to_x_y(5, 100, 0)


sprite.when_program_starts(do_something)

stage.play()
