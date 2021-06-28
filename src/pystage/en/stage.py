from pystage.core.stage import CoreStage
from pystage.en.sprite import Sprite


class Stage():

    def __init__(self):
        self._core = CoreStage()
        self._core.facade = self
        self._core.sprite_facade_class = Sprite

    def create_sprite(self, costume="default"):
        return self._core.pystage_createsprite(costume=costume)

    def play(self):
        self._core.pystage_play()
