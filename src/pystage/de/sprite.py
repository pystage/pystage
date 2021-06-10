import pystage

class Figur(pystage.core.sprite.Sprite):

    ##
    # Events
    #

    def wenn_programm_startet(self, generator, name=""):
        self.event_whenflagclicked(generator, name)


    def wenn_taste_gedrueckt_wird(self, key, generator, name=""):
        self.event_whenkeypressed(key, generator, name)


    def wenn_nachricht_kommt(self, nachricht, generator, name=""):
        self.event_whenbroadcastreceived(nachricht, generator, name)

    def wenn_das_ding_angeklickt_wird(self, generator, name=""):
        self.event_whenthisspriteclicked(generator, name)

    ##
    # Motion
    #

    def drehe_links(self, deg):
        self.motion_turnleft(deg)


    def drehe_rechts(self, deg):
        self.motion_turnright(deg)

    def gehe(self, steps):
        self.motion_movesteps(steps)

    def gehe_zu_x_y(self, x, y):
        self.motion_gotoxy(x, y)

    def warte(self, secs):
        self.control_wait(secs)
