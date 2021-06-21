import pystage
from pystage.en import Sprite

class Stage(pystage.core.stage.Stage):

    def erstelle_figur(self, costume="default"):
        return self.pystage_createsprite(costume=costume, constructor=Sprite)

    def spiele(self):
        self.pystage_play()
