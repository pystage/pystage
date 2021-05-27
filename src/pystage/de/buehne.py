import pystage
from pystage.de import Figur

class Buehne(pystage.Stage):

    def erstelle_figur(self):
        return self.create_sprite(Figur)

    def spiele(self):
        self.play()
