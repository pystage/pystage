from pystage.de import Buehne, Figur

buehne = Buehne()
zombie = buehne.erstelle_figur()

def mach_was(zombie):
    zombie.gehe_zu_x_y(0, 0)
    for i in range(4):
        zombie.gehe(20)
        zombie.warte(1)
        zombie.drehe_links(90)
        zombie.warte(1)

zombie.wenn_programm_startet(mach_was)


def reagiere(zombie):
    zombie.gehe(10)

zombie.wenn_taste_gedrueckt_wird(" ", reagiere)

buehne.spiele()
