from pystage.core.sprite import CoreSprite
from pystage.core.stage import CoreStage
from pystage.core.monitors import Monitor

stage = CoreStage()
stage.pystage_addbackdrop("grid")
sprite = stage.pystage_createsprite()

# This is not yet how it should look like for end users. Either we have a
# generic way to add monitors to a stage or we need to create an API to get the
# monitors for non-variable monitors.

monitor = Monitor(stage, "Zombie: x position", color=Monitor.MOTION_COLOR)
monitor.set_function(sprite.motion_xposition)
monitor.set_position(-100, 130)


def do_something(self: CoreSprite):
    self.pystage_makevariable("test")
    self.data_setvariableto("test", 99999999999)
    self.data_showvariable("test")
    self.pystage_setmonitorposition("test", -100, 100)
    self.pystage_setmonitorstyle_large("test")
    self.motion_glidesecstoxy(5, 100, 0)



sprite.event_whenflagclicked(do_something)



stage.pystage_play()
