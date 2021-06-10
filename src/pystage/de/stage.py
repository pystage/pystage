import pystage
from pystage.de import Figur
from pystage.core.stage import Stage

class Buehne(Stage):

    def erstelle_figur(self, costume="default"):
        return self.pystage_createsprite(costume=costume, constructor=Figur)

    def spiele(self):
        self.play()
