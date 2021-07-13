from pystage.de import Bühne, Figur

bühne = Bühne()
zombie = bühne.füge_eine_figur_hinzu()

def mach_was(zombie : Figur):
    zombie.gehe_zu_x_y(0, 0)
    for i in range(4):
        zombie.gehe_er_schritt(20)
        zombie.warte_sekunden(1)
        zombie.drehe_dich_nach_links_um_grad(90)
        zombie.warte_sekunden(1)

zombie.wenn_GREENFLAG_angeklickt_wird(mach_was)


def reagiere(zombie):
    zombie.gehe_er_schritt(10)

zombie.wenn_taste_gedrückt_wird(" ", reagiere)

bühne.abspielen()
