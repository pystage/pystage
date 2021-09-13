from pystage.core.sprite import CoreSprite
from pystage.core.stage import CoreStage

stage = CoreStage()
stage.pystage_addbackdrop("grid")
sprite = stage.pystage_createsprite()


def do_something(self: CoreSprite):
    self.pystage_makevariable("test")
    self.data_setvariableto("test", 99999999999)
    self.data_showvariable("test")
    self.pystage_setmonitorposition("test", -100, 100)

sprite.event_whenflagclicked(do_something)



stage.pystage_play()
