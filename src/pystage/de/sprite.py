
from pystage.core.sprite import CoreSprite


class Figur():
    def __init__(self, core_sprite):
        self._core : CoreSprite = core_sprite
        self._core.facade = self


            
    def erzeuge_klon_von_mir(self):
        """erzeuge Klon von mir selbst

        Translation string: erzeuge Klon von %1
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Returns
        -------

        """
        return self._core.control_create_clone_of_myself()
                
    def erzeuge_klon_von_sprite(self, sprite):
        """erzeuge Klon von %1

        Translation string: erzeuge Klon von %1
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite : FILL
        

        Returns
        -------

        """
        return self._core.control_create_clone_of_sprite(sprite)

    def lösche_diesen_klon(self):
        """lösche diesen Klon

        Translation string: lösche diesen Klon
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.control_delete_this_clone()
                
    def wenn_ich_als_klon_entstehe(self, generator_function, name='', no_refresh=False):
        """Wenn ich als Klon entstehe

        Translation string: Wenn ich als Klon entstehe
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        generator_function : FILL
        name : FILL
        no_refresh : FILL
        

        Returns
        -------

        """
        return self._core.control_start_as_clone(generator_function, name, no_refresh)
                
    def stoppe_alles(self):
        """stoppe alles

        Translation string: stoppe alles
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.control_stop_all()
                
    def stoppe_andere_skripte_der_figur(self):
        """stoppe andere Skripte der Figur

        Translation string: stoppe andere Skripte der Figur
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.control_stop_other()
                
    def stoppe_dieses_skript(self):
        """stoppe dieses Skript

        Translation string: stoppe dieses Skript
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.control_stop_this()
                
    def warte_sekunden(self, secs):
        """warte %1 Sekunden

        Translation string: warte %1 Sekunden
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        secs : FILL
        

        Returns
        -------

        """
        return self._core.control_wait(secs)
                
    def ändere_variable_um(self, name, value):
        """ändere %1 um %2

        Translation string: ändere %1 um %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL
        value : FILL
        

        Returns
        -------

        """
        return self._core.data_changevariableby(name, value)
                
    def verstecke_variable(self, name):
        """verstecke Variable %1

        Translation string: verstecke Variable %1
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL
        

        Returns
        -------

        """
        return self._core.data_hidevariable(name)
                
    def setze_variable(self, name, value):
        """setze %1 auf %2

        Translation string: setze %1 auf %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL
        value : FILL
        

        Returns
        -------

        """
        return self._core.data_setvariableto(name, value)
                
    def zeige_variable(self, name):
        """zeige Variable %1

        Translation string: zeige Variable %1
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL
        

        Returns
        -------

        """
        return self._core.data_showvariable(name)
                
    def gib_variable(self, name):
        """

        Translation string: 
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL
        

        Returns
        -------

        """
        return self._core.data_variable(name)
                
    def sende_an_alle(self, message):
        """sende %1 an alle

        Translation string: sende %1 an alle
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        message : FILL
        

        Returns
        -------

        """
        return self._core.event_broadcast(message)
                
    def sende_an_alle_und_warte(self, message):
        """sende %1 an alle und warte

        Translation string: sende %1 an alle und warte
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        message : FILL
        

        Returns
        -------

        """
        return self._core.event_broadcastandwait(message)
                
    def wenn_das_bühnenbild_zu_wechselt(self, backdrop, generator_function, name='', no_refresh=False):
        """Wenn das Bühnenbild zu %1 wechselt

        Translation string: Wenn das Bühnenbild zu %1 wechselt
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        backdrop : FILL
        generator_function : FILL
        name : FILL
        no_refresh : FILL
        

        Returns
        -------

        """
        return self._core.event_whenbackdropswitchesto(backdrop, generator_function, name, no_refresh)
                
    def wenn_ich_empfange(self, message, generator_function, name='', no_refresh=False):
        """Wenn ich %1 empfange

        Translation string: Wenn ich %1 empfange
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        message : FILL
        generator_function : FILL
        name : FILL
        no_refresh : FILL
        

        Returns
        -------

        """
        return self._core.event_whenbroadcastreceived(message, generator_function, name, no_refresh)
                
    def wenn_programm_startet(self, generator_function, name='', no_refresh=False):
        """Wenn <greenflag> angeklickt wird

        Translation string: Wenn <greenflag> angeklickt wird
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        generator_function : FILL
        name : FILL
        no_refresh : FILL
        

        Returns
        -------

        """
        return self._core.event_whenflagclicked(generator_function, name, no_refresh)
                
    def wenn_lautstärke_größer_als(self, value, generator_function, name='', no_refresh=False):
        """Wenn Lautstärke <greater> %2

        Translation string: Wenn Lautstärke <greater> %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        generator_function : FILL
        name : FILL
        no_refresh : FILL
        

        Returns
        -------

        """
        return self._core.event_whengreaterthan_loudness(value, generator_function, name, no_refresh)
                
    def wenn_stoppuhr_größer_als(self, value, generator_function, name='', no_refresh=False):
        """Wenn Stoppuhr <greater> %2

        Translation string: Wenn Stoppuhr <greater> %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        generator_function : FILL
        name : FILL
        no_refresh : FILL
        

        Returns
        -------

        """
        return self._core.event_whengreaterthan_timer(value, generator_function, name, no_refresh)
                
    def wenn_taste_gedrückt_wird(self, key, generator_function, name='', no_refresh=False):
        """Wenn Taste %1 gedrückt wird

        Translation string: Wenn Taste %1 gedrückt wird
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        key : FILL
        generator_function : FILL
        name : FILL
        no_refresh : FILL
        

        Returns
        -------

        """
        return self._core.event_whenkeypressed(key, generator_function, name, no_refresh)
                
    def wenn_diese_figur_angeklickt_wird(self, generator_function, name='', no_refresh=False):
        """Wenn diese Figur angeklickt wird

        Translation string: Wenn diese Figur angeklickt wird
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        generator_function : FILL
        name : FILL
        no_refresh : FILL
        

        Returns
        -------

        """
        return self._core.event_whenthisspriteclicked(generator_function, name, no_refresh)
                
    def bühnenbild_name(self):
        """Bühnenbild Name

        Translation string: Bühnenbild Name
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.looks_backdropnumbername_name()
                
    def bühnenbild_nummer(self):
        """Bühnenbild Nummer

        Translation string: Bühnenbild Nummer
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.looks_backdropnumbername_number()
                
    def ändere_effekt_helligkeit_um(self, value):
        """ändere Effekt Helligkeit um %2

        Translation string: ändere Effekt Helligkeit um %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.looks_changeeffectby_brightness(value)
                
    def ändere_effekt_farbe_um(self, value):
        """ändere Effekt Farbe um %2

        Translation string: ändere Effekt Farbe um %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.looks_changeeffectby_color(value)
                
    def ändere_effekt_fischauge_um(self, value):
        """ändere Effekt Fischauge um %2

        Translation string: ändere Effekt Fischauge um %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.looks_changeeffectby_fisheye(value)
                
    def ändere_effekt_durchsichtigkeit_um(self, value):
        """ändere Effekt Durchsichtigkeit um %2

        Translation string: ändere Effekt Durchsichtigkeit um %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.looks_changeeffectby_ghost(value)
                
    def ändere_effekt_mosaik_um(self, value):
        """ändere Effekt Mosaik um %2

        Translation string: ändere Effekt Mosaik um %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.looks_changeeffectby_mosaic(value)
                
    def ändere_effekt_pixel_um(self, value):
        """ändere Effekt Pixel um %2

        Translation string: ändere Effekt Pixel um %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.looks_changeeffectby_pixelate(value)
                
    def ändere_effekt_wirbel_um(self, value):
        """ändere Effekt Wirbel um %2

        Translation string: ändere Effekt Wirbel um %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.looks_changeeffectby_whirl(value)
                
    def ändere_größe_um(self, percent):
        """ändere Größe um %1

        Translation string: ändere Größe um %1
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        percent : FILL
        

        Returns
        -------

        """
        return self._core.looks_changesizeby(percent)
                
    def schalte_grafikeffekte_aus(self):
        """schalte Grafikeffekte aus

        Translation string: schalte Grafikeffekte aus
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.looks_cleargraphiceffects()
                
    def kostüm_name(self):
        """Kostüm Name

        Translation string: Kostüm Name
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.looks_costumenumbername_name()
                
    def kostüm_nummer(self):
        """Kostüm Nummer

        Translation string: Kostüm Nummer
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.looks_costumenumbername_number()
                
    def gehe_ebenen_nach_hinten(self, value):
        """gehe %2 Ebenen nach hinten

        Translation string: gehe %2 Ebenen nach hinten
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.looks_goforwardbackwardlayers_backward(value)
                
    def gehe_ebenen_nach_vorne(self, value):
        """gehe %2 Ebenen nach vorne

        Translation string: gehe %2 Ebenen nach vorne
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.looks_goforwardbackwardlayers_forward(value)
                
    def gehe_zu_hinterster_ebene(self):
        """gehe zu hinterster Ebene

        Translation string: gehe zu hinterster Ebene
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.looks_gotofrontback_back()
                
    def gehe_zu_vorderster_ebene(self):
        """gehe zu vorderster Ebene

        Translation string: gehe zu vorderster Ebene
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.looks_gotofrontback_front()
                
    def verstecke_dich(self):
        """verstecke dich

        Translation string: verstecke dich
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.looks_hide()
                
    def nächstes_bühnenbild(self):
        """nächstes Bühnenbild

        Translation string: nächstes Bühnenbild
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.looks_nextbackdrop()
                
    def wechsle_zum_nächsten_kostüm(self):
        """wechsle zum nächsten Kostüm

        Translation string: wechsle zum nächsten Kostüm
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.looks_nextcostume()
                
    def sage(self, text):
        """sage %1

        Translation string: sage %1
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        text : FILL
        

        Returns
        -------

        """
        return self._core.looks_say(text)
                
    def sage_für_sekunden(self, text, secs):
        """sage %1 für %2 Sekunden

        Translation string: sage %1 für %2 Sekunden
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        text : FILL
        secs : FILL
        

        Returns
        -------

        """
        return self._core.looks_sayforsecs(text, secs)
                
    def setze_effekt_helligkeit_auf(self, value):
        """setze Effekt Helligkeit auf %2

        Translation string: setze Effekt Helligkeit auf %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.looks_seteffectto_brightness(value)
                
    def setze_effekt_farbe_auf(self, value):
        """setze Effekt Farbe auf %2

        Translation string: setze Effekt Farbe auf %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.looks_seteffectto_color(value)
                
    def setze_effekt_fischauge_auf(self, value):
        """setze Effekt Fischauge auf %2

        Translation string: setze Effekt Fischauge auf %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.looks_seteffectto_fisheye(value)
                
    def setze_effekt_durchsichtigkeit_auf(self, value):
        """setze Effekt Durchsichtigkeit auf %2

        Translation string: setze Effekt Durchsichtigkeit auf %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.looks_seteffectto_ghost(value)
                
    def setze_effekt_mosaik_auf(self, value):
        """setze Effekt Mosaik auf %2

        Translation string: setze Effekt Mosaik auf %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.looks_seteffectto_mosaic(value)
                
    def setze_effekt_pixel_auf(self, value):
        """setze Effekt Pixel auf %2

        Translation string: setze Effekt Pixel auf %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.looks_seteffectto_pixelate(value)
                
    def setze_effekt_wirbel_auf(self, value):
        """setze Effekt Wirbel auf %2

        Translation string: setze Effekt Wirbel auf %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.looks_seteffectto_whirl(value)
                
    def setze_größe_auf(self, percent):
        """setze Größe auf %1

        Translation string: setze Größe auf %1
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        percent : FILL
        

        Returns
        -------

        """
        return self._core.looks_setsizeto(percent)
                
    def zeige_dich(self):
        """zeige dich

        Translation string: zeige dich
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.looks_show()
                
    def größe(self):
        """Größe

        Translation string: Größe
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.looks_size()
                
    def wechsle_zu_bühnenbild(self, backdrop):
        """wechsle zu Bühnenbild %1

        Translation string: wechsle zu Bühnenbild %1
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        backdrop : FILL
        

        Returns
        -------

        """
        return self._core.looks_switchbackdropto_backdrop(backdrop)
                
    def wechsle_zu_zufälligem_bühnenbild(self):
        """wechsle zu zufälligem Bühnenbild

        Translation string: wechsle zu zufäBühnenbild
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Returns
        -------

        """
        return self._core.looks_switchbackdropto_random()

    def wechsle_zum_vorherigen_bühnenbild(self):
        """wechsle zum vorherigen Bühnenbild

        Returns
        -------

        """
        return self._core.looks_switchbackdropto_previous()

    def wechsle_zum_nächsten_bühnenbild(self):
        """wechsle zum nachfolgenden Bühnenbild


        Returns
        -------

        """
        return self._core.looks_switchbackdropto_next()

    def wechsle_zu_kostüm(self, costume):
        """wechsle zu Kostüm %1

        Translation string: wechsle zu Kostüm %1
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        costume : FILL
        

        Returns
        -------

        """
        return self._core.looks_switchcostumeto(costume)
                
    def denke(self, text):
        """denke %1

        Translation string: denke %1
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        text : FILL
        

        Returns
        -------

        """
        return self._core.looks_think(text)
                
    def denke_für_sekunden(self, text, secs):
        """denke %1 für %2 Sekunden

        Translation string: denke %1 für %2 Sekunden
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        text : FILL
        secs : FILL
        

        Returns
        -------

        """
        return self._core.looks_thinkforsecs(text, secs)
                
    def ändere_x_um(self, value):
        """ändere x um %1

        Translation string: ändere x um %1
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.motion_changexby(value)
                
    def ändere_y_um(self, value):
        """ändere y um %1

        Translation string: ändere y um %1
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.motion_changeyby(value)
                
    def richtung(self):
        """Richtung

        Translation string: Richtung
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.motion_direction()
                
    def gleite_in_sek_zu_x_y(self, secs, x, y):
        """gleite in %1 Sek. zu x:%2  y:%3

        Translation string: gleite in %1 Sek. zu x:%2  y:%3
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        secs : FILL
        x : FILL
        y : FILL
        

        Returns
        -------

        """
        return self._core.motion_glidesecstoxy(secs, x, y)
                
    def gleite_in_sek_zu_mauszeiger(self, secs):
        """gleite in %1 Sek. zu Mauszeiger

        Translation string: gleite in %1 Sek. zu Mauszeiger
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        secs : FILL
        

        Returns
        -------

        """
        return self._core.motion_glideto_pointer(secs)
                
    def gleite_in_sek_zu_zufallsposition(self, secs):
        """gleite in %1 Sek. zu Zufallsposition

        Translation string: gleite in %1 Sek. zu Zufallsposition
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        secs : FILL
        

        Returns
        -------

        """
        return self._core.motion_glideto_random(secs)
                
    def gleite_in_sek_zu(self, secs, sprite):
        """gleite in %1 Sek. zu %2

        Translation string: gleite in %1 Sek. zu %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        secs : FILL
        sprite : FILL
        

        Returns
        -------

        """
        return self._core.motion_glideto_sprite(secs, sprite)
                
    def gehe_zu_mauszeiger(self):
        """gehe zu Mauszeiger

        Translation string: gehe zu Mauszeiger
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.motion_goto_pointer()
                
    def gehe_zu_zufallsposition(self):
        """gehe zu Zufallsposition

        Translation string: gehe zu Zufallsposition
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.motion_goto_random()
                
    def gehe_zu(self, sprite):
        """gehe zu %1

        Translation string: gehe zu %1
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite : FILL
        

        Returns
        -------

        """
        return self._core.motion_goto_sprite(sprite)
                
    def gehe_zu_x_y(self, x, y):
        """gehe zu x: %1 y: %2

        Translation string: gehe zu x: %1 y: %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        x : FILL
        y : FILL
        

        Returns
        -------

        """
        return self._core.motion_gotoxy(x, y)
                
    def pralle_vom_rand_ab(self):
        """pralle vom Rand ab

        Translation string: pralle vom Rand ab
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.motion_ifonedgebounce()
                
    def gehe_er_schritt(self, steps):
        """gehe %1 er Schritt

        Translation string: gehe %1 er Schritt
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        steps : FILL
        

        Returns
        -------

        """
        return self._core.motion_movesteps(steps)
                
    def setze_richtung_auf_grad(self, direction):
        """setze Richtung auf %1 Grad

        Translation string: setze Richtung auf %1 Grad
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        direction : FILL
        

        Returns
        -------

        """
        return self._core.motion_pointindirection(direction)
                
    def drehe_dich_zu_mauszeiger(self):
        """drehe dich zu Mauszeiger

        Translation string: drehe dich zu Mauszeiger
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.motion_pointtowards_pointer()
                
    def drehe_dich_zu(self, sprite):
        """drehe dich zu %1

        Translation string: drehe dich zu %1
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite : FILL
        

        Returns
        -------

        """
        return self._core.motion_pointtowards_sprite(sprite)
                
    def setze_drehtyp_auf_rundherum(self):
        """setze Drehtyp auf rundherum

        Translation string: setze Drehtyp auf rundherum
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.motion_setrotationstyle_allaround()
                
    def setze_drehtyp_auf_nicht_drehen(self):
        """setze Drehtyp auf nicht drehen

        Translation string: setze Drehtyp auf nicht drehen
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.motion_setrotationstyle_dontrotate()
                
    def setze_drehtyp_auf_helligkeit(self):
        """setze Drehtyp auf Helligkeit

        Translation string: setze Drehtyp auf Helligkeit
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.motion_setrotationstyle_leftright()
                
    def setze_x_auf(self, value):
        """setze x auf %1

        Translation string: setze x auf %1
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.motion_setx(value)
                
    def setze_y_auf(self, value):
        """setze y auf %1

        Translation string: setze y auf %1
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.motion_sety(value)
                
    def drehe_dich_nach_links_um_grad(self, deg):
        """drehe dich nach links um %2 Grad

        Translation string: drehe dich nach links um %2 Grad
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        deg : FILL
        

        Returns
        -------

        """
        return self._core.motion_turnleft(deg)
                
    def drehe_dich_nach_rechts_um_grad(self, deg):
        """drehe dich nach rechts um %2 Grad

        Translation string: drehe dich nach rechts um %2 Grad
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        deg : FILL
        

        Returns
        -------

        """
        return self._core.motion_turnright(deg)
                
    def x_position(self):
        """x-Position

        Translation string: x-Position
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.motion_xposition()
                
    def y_position(self):
        """y-Position

        Translation string: y-Position
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.motion_yposition()
                
    def mathematische_funktion(self, operator, number):
        """%1 von %2

        Translation string: %1 von %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        operator : FILL
        number : FILL
        

        Returns
        -------

        """
        return self._core.operator_mathop(operator, number)
                
    def zufallszahl_von_bis(self, start, end):
        """Zufallszahl von %1 bis %2

        Translation string: Zufallszahl von %1 bis %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        start : FILL
        end : FILL
        

        Returns
        -------

        """
        return self._core.operator_random(start, end)
                
    def ändere_stift_helligkeit_um(self, value):
        """ändere Stift Helligkeit um [VALUE]

        Translation string: ändere Stift Helligkeit um [VALUE]
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.pen_changePenColorParamBy_brightness(value)
                
    def ändere_stift_farbe_um(self, value):
        """ändere Stift Farbe um [VALUE]
        TODO TRANSLATORS: Needs to be distinguished from setPenColorToColor. This is only the hue value.
        

        Translation string: ändere Stift Farbe um [VALUE]
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.pen_changePenColorParamBy_color(value)
                
    def ändere_stift_sättigung_um(self, value):
        """ändere Stift Sättigung um [VALUE]

        Translation string: ändere Stift Sättigung um [VALUE]
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.pen_changePenColorParamBy_saturation(value)
                
    def ändere_stift_transparenz_um(self, value):
        """ändere Stift Transparenz um [VALUE]

        Translation string: ändere Stift Transparenz um [VALUE]
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.pen_changePenColorParamBy_transparency(value)
                
    def ändere_stiftdicke_um(self, value):
        """ändere Stiftdicke um [SIZE]

        Translation string: ändere Stiftdicke um [SIZE]
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.pen_changePenSizeBy(value)
                
    def lösche_alles(self):
        """lösche alles

        Translation string: lösche alles
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.pen_clear()
                
    def schalte_stift_ein(self):
        """schalte Stift ein

        Translation string: schalte Stift ein
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.pen_penDown()
                
    def schalte_stift_aus(self):
        """schalte Stift aus

        Translation string: schalte Stift aus
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.pen_penUp()
                
    def setze_stift_helligkeit_auf(self, value):
        """setze Stift Helligkeit auf [VALUE]

        Translation string: setze Stift Helligkeit auf [VALUE]
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.pen_setPenColorParamTo_brightness(value)
                
    def setze_stift_farbe_auf(self, value):
        """setze Stift Farbe auf [VALUE]
        TODO TRANSLATORS: Needs to be distinguished from setPenColorToColor. This is only the hue value.
        

        Translation string: setze Stift Farbe auf [VALUE]
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.pen_setPenColorParamTo_color(value)
                
    def setze_stift_sättigung_auf(self, value):
        """setze Stift Sättigung auf [VALUE]

        Translation string: setze Stift Sättigung auf [VALUE]
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.pen_setPenColorParamTo_saturation(value)
                
    def setze_stift_transparenz_auf(self, value):
        """setze Stift Transparenz auf [VALUE]

        Translation string: setze Stift Transparenz auf [VALUE]
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.pen_setPenColorParamTo_transparency(value)
                
    def setze_stiftfarbe_auf(self, color):
        """setze Stiftfarbe auf [COLOR]

        Translation string: setze Stiftfarbe auf [COLOR]
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        color : FILL
        

        Returns
        -------

        """
        return self._core.pen_setPenColorToColor(color)
                
    def setze_stiftdicke_auf(self, value):
        """setze Stiftdicke auf [SIZE]

        Translation string: setze Stiftdicke auf [SIZE]
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.pen_setPenSizeTo(value)
                
    def hinterlasse_abdruck(self):
        """hinterlasse Abdruck

        Translation string: hinterlasse Abdruck
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.pen_stamp()
                
    def füge_kostüm_hinzu(self, name, center_x=None, center_y=None, factor=1):
        """

        Translation string: 
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL
        center_x : FILL
        center_y : FILL
        factor : FILL
        

        Returns
        -------

        """
        return self._core.pystage_addcostume(name, center_x, center_y, factor)
                
    def füge_klang_hinzu(self, name):
        """

        Translation string: 
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL
        

        Returns
        -------

        """
        return self._core.pystage_addsound(name)
                
    def füge_kostüm_ein(self, index, name, center_x=None, center_y=None, factor=1):
        """

        Translation string: 
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        index : FILL
        name : FILL
        center_x : FILL
        center_y : FILL
        factor : FILL
        

        Returns
        -------

        """
        return self._core.pystage_insertcostume(index, name, center_x, center_y, factor)
                
    def erzeuge_variable(self, name, value=0, all_sprites=True):
        """

        Translation string: 
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL
        all_sprites : FILL
        

        Returns
        -------

        """
        return self._core.pystage_makevariable(name, value, all_sprites)
                
    def ersetze_kostüm(self, index, name, center_x=None, center_y=None, factor=1):
        """

        Translation string: 
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        index : FILL
        name : FILL
        center_x : FILL
        center_y : FILL
        factor : FILL
        

        Returns
        -------

        """
        return self._core.pystage_replacecostume(index, name, center_x, center_y, factor)
                
    def setze_monitor_position(self, name, x, y):
        """

        Translation string: 
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL
        x : FILL
        y : FILL
        

        Returns
        -------

        """
        return self._core.pystage_setmonitorposition(name, x, y)
                
    def setze_monitor_stil_groß(self, name):
        """

        Translation string: 
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL
        

        Returns
        -------

        """
        return self._core.pystage_setmonitorstyle_large(name)
                
    def setze_monitor_stil_normal(self, name):
        """

        Translation string: 
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL
        

        Returns
        -------

        """
        return self._core.pystage_setmonitorstyle_normal(name)
                
    def setze_monitor_stil_regler(self, name):
        """

        Translation string: 
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL
        

        Returns
        -------

        """
        return self._core.pystage_setmonitorstyle_slider(name)
                
    def antwort(self):
        """Antwort

        Translation string: Antwort
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_answer()
                
    def frage_und_warte(self, question):
        """frage %1 und warte

        Translation string: frage %1 und warte
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        question : FILL
        

        Returns
        -------

        """
        return self._core.sensing_askandwait(question)
                
    def farbe_berührt(self, sprite_color, color):
        """Farbe %1 berührt %2?

        Translation string: Farbe %1 berührt %2?
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite_color : FILL
        color : FILL
        

        Returns
        -------

        """
        return self._core.sensing_coloristouchingcolor(sprite_color, color)
                
    def datum_im_moment(self):
        """Datum im Moment

        Translation string: Datum im Moment
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_current_date()
                
    def wochentag_im_moment(self):
        """Wochentag im Moment

        Translation string: Wochentag im Moment
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_current_dayofweek()
                
    def stunde_im_moment(self):
        """Stunde im Moment

        Translation string: Stunde im Moment
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_current_hour()
                
    def minute_im_moment(self):
        """Minute im Moment

        Translation string: Minute im Moment
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_current_minute()
                
    def monat_im_moment(self):
        """Monat im Moment

        Translation string: Monat im Moment
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_current_month()
                
    def sekunde_im_moment(self):
        """Sekunde im Moment

        Translation string: Sekunde im Moment
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_current_second()
                
    def jahr_im_moment(self):
        """Jahr im Moment

        Translation string: Jahr im Moment
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_current_year()
                
    def tage_seit(self):
        """Tage seit 2000

        Translation string: Tage seit 2000
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_dayssince2000()
                
    def entfernung_von_mauszeiger(self):
        """Entfernung von Mauszeiger

        Translation string: Entfernung von Mauszeiger
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_distanceto_pointer()
                
    def entfernung_von(self, sprite):
        """Entfernung von %1

        Translation string: Entfernung von %1
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite : FILL
        

        Returns
        -------

        """
        return self._core.sensing_distanceto_sprite(sprite)
                
    def taste_gedrückt(self, key):
        """Taste %1 gedrückt?

        Translation string: Taste %1 gedrückt?
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        key : FILL
        

        Returns
        -------

        """
        return self._core.sensing_keypressed(key)
                
    def lautstärke_mikrofon(self):
        """Lautstärke

        Translation string: Lautstärke
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_loudness()
                
    def maustaste_gedrückt(self):
        """Maustaste gedrückt?

        Translation string: Maustaste gedrückt?
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_mousedown()
                
    def maus_x_position(self):
        """Maus x-Position

        Translation string: Maus x-Position
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_mousex()
                
    def maus_y_position(self):
        """Maus y-Position

        Translation string: Maus y-Position
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_mousey()
                
    def bühnenbildname_von(self, stage='_stage_'):
        """Bühnenbildname von %2

        Translation string: Bühnenbildname von %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        stage : FILL
        

        Returns
        -------

        """
        return self._core.sensing_of_backdropname(stage)
                
    def bühnenbildnummer_von(self, stage='_stage_'):
        """Bühnenbildnummer von %2

        Translation string: Bühnenbildnummer von %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        stage : FILL
        

        Returns
        -------

        """
        return self._core.sensing_of_backdropnumber(stage)
                
    def kostümname_von(self, sprite):
        """Kostümname von %2

        Translation string: Kostümname von %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite : FILL
        

        Returns
        -------

        """
        return self._core.sensing_of_costumename(sprite)
                
    def kostümnummer_von(self, sprite):
        """Kostümnummer von %2

        Translation string: Kostümnummer von %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite : FILL
        

        Returns
        -------

        """
        return self._core.sensing_of_costumenumber(sprite)
                
    def richtung_von(self, sprite):
        """Richtung von %2

        Translation string: Richtung von %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite : FILL
        

        Returns
        -------

        """
        return self._core.sensing_of_direction(sprite)
                
    def größe_von(self, sprite):
        """Größe von %2

        Translation string: Größe von %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite : FILL
        

        Returns
        -------

        """
        return self._core.sensing_of_size(sprite)
                
    def gib_variable_von(self, variable, sprite='_stage_'):
        """%1 von %2

        Translation string: %1 von %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        variable : FILL
        sprite : FILL
        

        Returns
        -------

        """
        return self._core.sensing_of_variable(variable, sprite)
                
    def lautstärke_von(self, sprite='_stage_'):
        """Lautstärke von %2

        Translation string: Lautstärke von %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite : FILL
        

        Returns
        -------

        """
        return self._core.sensing_of_volume(sprite)
                
    def x_position_von(self, sprite):
        """x-Position von %2

        Translation string: x-Position von %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite : FILL
        

        Returns
        -------

        """
        return self._core.sensing_of_xposition(sprite)
                
    def y_position_von(self, sprite):
        """y-Position von %2

        Translation string: y-Position von %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite : FILL
        

        Returns
        -------

        """
        return self._core.sensing_of_yposition(sprite)
                
    def setze_stoppuhr_zurück(self):
        """setze Stoppuhr zurück

        Translation string: setze Stoppuhr zurück
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_resettimer()
                
    def setze_ziehbarkeit_auf_ziehbar(self):
        """setze Ziehbarkeit auf ziehbar

        Translation string: setze Ziehbarkeit auf ziehbar
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_setdragmode_draggable()
                
    def setze_ziehbarkeit_auf_nicht_ziehbar(self):
        """setze Ziehbarkeit auf nicht ziehbar

        Translation string: setze Ziehbarkeit auf nicht ziehbar
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_setdragmode_notdraggable()
                
    def stoppuhr(self):
        """Stoppuhr

        Translation string: Stoppuhr
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_timer()
                
    def wird_farbe_berührt(self, color):
        """wird Farbe %1 berührt?

        Translation string: wird Farbe %1 berührt?
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        color : FILL
        

        Returns
        -------

        """
        return self._core.sensing_touchingcolor(color)
                
    def wird_rand_berührt(self):
        """wird Rand berührt?

        Translation string: wird Rand berührt?
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_touchingobject_edge()
                
    def wird_mauszeiger_berührt(self):
        """wird Mauszeiger berührt?

        Translation string: wird Mauszeiger berührt?
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_touchingobject_pointer()
                
    def wird_berührt(self, sprite):
        """wird %1 berührt?

        Translation string: wird %1 berührt?
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite : FILL
        

        Returns
        -------

        """
        return self._core.sensing_touchingobject_sprite(sprite)
                
    def benutzername(self):
        """Benutzername

        Translation string: Benutzername
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_username()
                
    def ändere_effekt_aussteuern_links_rechts_um(self, value):
        """ändere Effekt Aussteuern links/rechts um %2

        Translation string: ändere Effekt Aussteuern links/rechts um %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.sound_changeeffectby_pan(value)
                
    def ändere_effekt_höhe_um(self, value):
        """ändere Effekt Höhe um %2

        Translation string: ändere Effekt Höhe um %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.sound_changeeffectby_pitch(value)
                
    def ändere_lautstärke_um(self, value):
        """ändere Lautstärke um %1

        Translation string: ändere Lautstärke um %1
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.sound_changevolumeby(value)
                
    def schalte_klangeffekte_aus(self):
        """schalte Klangeffekte aus

        Translation string: schalte Klangeffekte aus
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sound_cleareffects()
                
    def spiele_klang(self, name, loop=0):
        """spiele Klang %1

        Translation string: spiele Klang %1
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL
        loop : FILL
        

        Returns
        -------

        """
        return self._core.sound_play(name, loop)
                
    def spiele_klang_ganz(self, name):
        """spiele Klang %1 ganz

        Translation string: spiele Klang %1 ganz
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL
        

        Returns
        -------

        """
        return self._core.sound_playuntildone(name)
                
    def setze_effekt_aussteuern_links_rechts_auf(self, value):
        """setze Effekt Aussteuern links/rechts auf %2

        Translation string: setze Effekt Aussteuern links/rechts auf %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.sound_seteffectto_pan(value)
                
    def setze_effekt_höhe_auf(self, value):
        """setze Effekt Höhe auf %2

        Translation string: setze Effekt Höhe auf %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.sound_seteffectto_pitch(value)
                
    def setze_lautstärke_auf(self, value):
        """setze Lautstärke auf %1%

        Translation string: setze Lautstärke auf %1%
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.sound_setvolumeto(value)
                
    def stoppe_alle_klänge(self):
        """stoppe alle Klänge

        Translation string: stoppe alle Klänge
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sound_stopallsounds()
                
    def lautstärke(self):
        """Lautstärke

        Translation string: Lautstärke
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sound_volume()
                
    def setze_name(self, name):
        """

        Translation string: 
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL


        Returns
        -------

        """
        return self._core.pystage_setname(name)

    def erzeuge_liste(self, name, values=None, all_sprites=True):
        """Erzeuge eine Liste.

        Parameters
        ----------
        name : str
            Der Name der Liste.
        values : list
            Die anfänglichen Elemente der Liste.
        all_sprites : bool
            Wenn True, kann die Liste von der Bühne und allen Figuren benutzt werden.
            Wenn False, gehört sie nur zu dieser Figur.
        """
        return self._core.pystage_makelistvariable(name, values, all_sprites)

    def füge_zu_liste_hinzu(self, name, item):
        """füge %1 zu Liste %2 hinzu

        Parameters
        ----------
        name : str
            Der Name der Liste.
        item
            Das Element, eine Zahl oder ein Text.
        """
        return self._core.data_addtolist(name, item)

    def lösche_element_aus_liste(self, name, index):
        """lösche %1 aus Liste %2

        Parameters
        ----------
        name : str
            Der Name der Liste.
        index : int or str
            Die Position, beginnend mit 1. Auch möglich: "last" und "random". Mit "all" werden alle Elemente gelöscht.
        """
        return self._core.data_deleteoflist(name, index)

    def lösche_alles_aus_liste(self, name):
        """lösche alles aus Liste %1

        Parameters
        ----------
        name : str
            Der Name der Liste.
        """
        return self._core.data_deletealloflist(name)

    def füge_in_liste_ein(self, name, item, index):
        """füge %1 bei %2 in Liste %3 ein

        Parameters
        ----------
        name : str
            Der Name der Liste.
        item
            Das Element, eine Zahl oder ein Text.
        index : int or str
            Die Position, beginnend mit 1. Auch möglich: "last" und "random".
        """
        return self._core.data_insertatlist(name, item, index)

    def ersetze_element_von_liste(self, name, index, item):
        """ersetze Element %1 von Liste %2 durch %3

        Parameters
        ----------
        name : str
            Der Name der Liste.
        index : int or str
            Die Position, beginnend mit 1. Auch möglich: "last" und "random".
        item
            Das Element, eine Zahl oder ein Text.
        """
        return self._core.data_replaceitemoflist(name, index, item)

    def element_von_liste(self, name, index):
        """Element %1 von Liste %2

        Parameters
        ----------
        name : str
            Der Name der Liste.
        index : int or str
            Die Position, beginnend mit 1. Auch möglich: "last" und "random".

        Returns
        -------
        Das Element oder ein leerer Text, wenn es an dieser Position kein Element gibt.
        """
        return self._core.data_itemoflist(name, index)

    def nummer_in_liste(self, name, item):
        """Nummer von %1 in Liste %2

        Parameters
        ----------
        name : str
            Der Name der Liste.
        item
            Das Element, eine Zahl oder ein Text.

        Returns
        -------
        int
            Die Position des ersten Vorkommens, 0 wenn das Element nicht in der Liste ist.
        """
        return self._core.data_itemnumoflist(name, item)

    def länge_von_liste(self, name):
        """Länge von Liste %1

        Parameters
        ----------
        name : str
            Der Name der Liste.

        Returns
        -------
        int
        """
        return self._core.data_lengthoflist(name)

    def liste_enthält(self, name, item):
        """Liste %1 enthält %2?

        Parameters
        ----------
        name : str
            Der Name der Liste.
        item
            Das Element, eine Zahl oder ein Text.

        Returns
        -------
        bool
        """
        return self._core.data_listcontainsitem(name, item)

    def gib_liste(self, name):
        """Die Liste selbst.

        Das ist die echte Python-Liste, sie kann wie jede andere Liste benutzt werden.

        Parameters
        ----------
        name : str
            Der Name der Liste.

        Returns
        -------
        list
        """
        return self._core.data_listvariable(name)

    def zeige_liste(self, name):
        """zeige Liste %1

        Parameters
        ----------
        name : str
            Der Name der Liste.
        """
        return self._core.data_showlist(name)

    def verstecke_liste(self, name):
        """verstecke Liste %1

        Parameters
        ----------
        name : str
            Der Name der Liste.
        """
        return self._core.data_hidelist(name)

    def setze_listenmonitor_position(self, name, x, y, width=None, height=None):
        """Setze Position und Größe der auf der Bühne angezeigten Liste.

        Parameters
        ----------
        name : str
            Der Name der Liste.
        x : int
            Linker Rand.
        y : int
            Oberer Rand.
        width : int
            Breite in Pixeln, automatisch wenn nicht angegeben.
        height : int
            Höhe in Pixeln, automatisch wenn nicht angegeben.
        """
        return self._core.pystage_setlistmonitorposition(name, x, y, width, height)

    def verbinde(self, string1, string2):
        """verbinde %1 und %2

        Parameters
        ----------
        string1
            Der erste Text oder die erste Zahl.
        string2
            Der zweite Text oder die zweite Zahl.

        Returns
        -------
        str
        """
        return self._core.operator_join(string1, string2)

    def zeichen_von(self, letter, string):
        """Zeichen %1 von %2

        Parameters
        ----------
        letter : int
            Die Position des Zeichens, beginnend mit 1.
        string : str
            Der Text.

        Returns
        -------
        str
            Das Zeichen oder ein leerer Text, wenn es an dieser Position kein Zeichen gibt.
        """
        return self._core.operator_letter_of(letter, string)

    def länge_von(self, string):
        """Länge von %1

        Parameters
        ----------
        string : str
            Der Text.

        Returns
        -------
        int
        """
        return self._core.operator_length(string)

    def enthält(self, string1, string2):
        """%1 enthält %2?

        Groß- und Kleinschreibung wird ignoriert.

        Parameters
        ----------
        string1 : str
            Der Text, in dem gesucht wird.
        string2 : str
            Der Text, nach dem gesucht wird.

        Returns
        -------
        bool
        """
        return self._core.operator_contains(string1, string2)

    def runde(self, number):
        """%1 gerundet

        Wie in Scratch wird .5 immer aufgerundet.

        Parameters
        ----------
        number : float

        Returns
        -------
        int
        """
        return self._core.operator_round(number)
