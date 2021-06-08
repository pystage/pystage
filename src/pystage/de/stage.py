import pystage
from pystage.de import Figur

class Buehne(pystage.core.stage.Stage):

    def erstelle_figur(self, costume="default"):
        return self.create_sprite(costume=costume, constructor=Figur)

    def spiele(self):
        self.play()