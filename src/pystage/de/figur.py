import pystage

class Figur(pystage.Sprite):

    ##
    # Events
    #

    def wenn_programm_startet(self, generator, name=""):
        self.when_program_is_started(generator, name)


    def wenn_taste_gedrueckt_wird(self, key, generator, name=""):
        self.when_key_is_pressed(key, generator, name)



    ##
    # Motion
    #

    def drehe_links(self, deg):
        self.turn_left(deg)


    def drehe_rechts(self, deg):
        self.turn_right(deg)

    def gehe(self, steps):
        self.move(steps)

    def gehe_zu_x_y(self, x, y):
        self.go_to_x_y(x, y)
