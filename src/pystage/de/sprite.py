from pystage.core.sprite import CoreSprite

class Figur():
    def __init__(self, core_sprite):
        self._core : CoreSprite = core_sprite
        self._core.facade = self

    ##
    # Events
    #

    def wenn_programm_startet(self, generator, name=""):
        self._core.event_whenflagclicked(generator, name)


    def wenn_taste_gedrueckt_wird(self, key, generator, name=""):
        self._core.event_whenkeypressed(key, generator, name)


    def wenn_nachricht_kommt(self, nachricht, generator, name=""):
        self._core.event_whenbroadcastreceived(nachricht, generator, name)

    def wenn_das_ding_angeklickt_wird(self, generator, name=""):
        self._core.event_whenthisspriteclicked(generator, name)

    ##
    # Motion
    #

    def drehe_links(self, deg):
        self._core.motion_turnleft(deg)


    def drehe_rechts(self, deg):
        self._core.motion_turnright(deg)

    def gehe(self, steps):
        self._core.motion_movesteps(steps)

    def gehe_zu_x_y(self, x, y):
        self._core.motion_gotoxy(x, y)

    def warte(self, secs):
        self._core.control_wait(secs)
