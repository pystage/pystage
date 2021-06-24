from pystage.core.stage import Stage
from pystage.en import Sprite


class Stage(Stage):

    def erstelle_figur(self, costume="default"):
        return self.pystage_createsprite(costume=costume, constructor=Sprite)

    def spiele(self):
        self.pystage_play()
