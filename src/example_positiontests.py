from pystage.core.sprite import CoreSprite
from pystage.core.stage import CoreStage

stage = CoreStage()
stage.pystage_addbackdrop("grid")
sprite = stage.pystage_createsprite()



def printpos(self):
    print("Pos", self.x, self.y)
    print("PG Pos", self._pg_pos())
    print("Offset", self.costume_manager.get_offset())
    print("Center", self.costume_manager.get_center())
    print("Rect", self.rect)

def turn(self):
    self.motion_turnleft(45)

def move_rect(self):
    self.rect.right += 10
    self._update_pos_from_rect()

sprite.event_whenkeypressed(" ", printpos)
sprite.event_whenkeypressed("t", turn)
sprite.event_whenkeypressed("m", move_rect)

stage.pystage_play()
