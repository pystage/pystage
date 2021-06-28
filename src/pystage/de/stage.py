import pystage
from pystage.de import Figur
from pystage.core.stage import CoreStage

class Buehne():

    def __init__(self):
        self._core = CoreStage()
        self._core.facade = self
        self._core.sprite_facade_class = Figur

    def erstelle_figur(self, costume="default"):
        return self._core.pystage_createsprite(costume=costume)

    def spiele(self):
        self._core.pystage_play()
