from pystage.de import Bühne, Figur

bühne = Bühne()
zombie = bühne.erstelle_figur()

def mach_was(zombie):
    zombie.gehe_zu_x_y(0, 0)
    for i in range(4):
        zombie.gehe(20)
        zombie.warte_sekunden(1)
        zombie.drehe_dich_nach_links_um_grad(90)
        zombie.warte_sekunden(1)

zombie.wenn_grüne_flagge_angeklickt_wird(mach_was)


def reagiere(zombie):
    zombie.gehe(10)

zombie.wenn_taste_gedrückt_wird(" ", reagiere)

bühne.spiele()
