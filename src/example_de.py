from pystage.de import Buehne, Figur

buehne = Buehne(500, 500)
figur = buehne.erstelle_figur()

def mach_was(self):
    self.gehe_zu_x_y(250, 250)
    yield 0
    for i in range(4):
        self.gehe(20)
        self.drehe_links(90)
        yield 1

figur.wenn_programm_started(mach_was)


def reagiere(self):
    self.gehe(10)
    yield

figur.wenn_taste_gedrueckt_wird(" ", reagiere)

buehne.spiele()
