from pystage.core.sprite import CoreSprite
from pystage.core.stage import CoreStage

stage = CoreStage()
stage.pystage_addbackdrop("grid")
sprite = stage.pystage_createsprite()



def printpos(self):
    print("Pos", self.motion_xposition(), self.motion_yposition())
    print("PG Pos", self._pos)
    print("Center", self.costume_manager.get_center())
    print("Rect", self.rect)

def turn(self):
    self.motion_turnleft(45)

def move_rect(self):
    self.motion_changexby(10)

sprite.event_whenkeypressed(" ", printpos)
sprite.event_whenkeypressed("t", turn)
sprite.event_whenkeypressed("m", move_rect)

stage.pystage_play()
