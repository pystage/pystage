
from pystage.core.stage import CoreStage
from pystage.de.sprite import Figur


class Bühne():

    def __init__(self, titel="Welcome to pyStage!"):
        """Erzeugt die Bühne. Der Titel steht in der Titelleiste des Fensters. Meldungen erscheinen auf Deutsch."""
        self._core = CoreStage(titel, language="de")
        self._core.facade = self
        self._core.sprite_facade_class = Figur

    def füge_eine_figur_hinzu(self, costume="default"):
        return self._core.pystage_createsprite(costume=costume)

    def abspielen(self):
        self._core.pystage_play()
        
            
    def erzeuge_klon_von_sprite(self, sprite='_myself_'):
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
                
    def stoppe_alles(self):
        """stoppe alles

        Translation string: stoppe alles
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.control_stop_all()
                
    def stoppe_andere_skripte_der_bühne(self):
        """stoppe andere Skripte der Bühne

        Translation string: stoppe andere Skripte der Bühne
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
                
    def wenn_das_bühnenbild_wechselt_zu(self, backdrop, generator_function, name='', no_refresh=False):
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
                
    def schalte_grafikeffekte_aus(self):
        """schalte Grafikeffekte aus

        Translation string: schalte Grafikeffekte aus
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.looks_cleargraphiceffects()
                
    def nächstes_bühnenbild(self):
        """nächstes Bühnenbild

        Translation string: nächstes Bühnenbild
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.looks_nextbackdrop()
                
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
                
    def wechsle_zu_bühnenbild_und_warte(self, backdrop):
        """wechsle zu Bühnenbild %1 und warte

        Translation string: wechsle zu Bühnenbild %1 und warte
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        backdrop : FILL
        

        Returns
        -------

        """
        return self._core.looks_switchbackdroptoandwait(backdrop)
                
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
                
    def füge_bühnenbild_hinzu(self, name, center_x=None, center_y=None, factor=1):
        """

        Translation string: 
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL
        center_x : FILL
        center_y : FILL
        

        Returns
        -------

        """
        return self._core.pystage_addbackdrop(name, center_x, center_y, factor)
                
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
                
    def füge_bühnenbild_ein(self, index, name, center_x=None, center_y=None, factor=1):
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
        

        Returns
        -------

        """
        return self._core.pystage_insertbackdrop(index, name, center_x, center_y, factor)
                
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
                
    def ersetze_bühnenbild(self, index, name, center_x=None, center_y=None, factor=1):
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
        

        Returns
        -------

        """
        return self._core.pystage_replacebackdrop(index, name, center_x, center_y, factor)
                
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
                
    def setze_monitor_stil_regler(self, name, minimum=0, maximum=100, integer=True):
        """Zeigt die Variable als Regler, den man mit der Maus ziehen kann.

        Parameters
        ----------
        name : str
            Der Name der Variablen.
        minimum, maximum : number
            Der Bereich des Reglers (wie in Scratch standardmäßig 0 bis 100).
        integer : bool
            Bei True setzt der Regler nur ganze Zahlen, sonst Zahlen mit zwei Nachkommastellen.
        """
        return self._core.pystage_setmonitorstyle_slider(name, minimum, maximum, integer)
                
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

    def größer_als(self, operand1, operand2):
        """%1 > %2

        Größer als; compares like Scratch (numbers numerically, otherwise text without case).

        Returns
        -------
        bool
        """
        return self._core.operator_gt(operand1, operand2)

    def kleiner_als(self, operand1, operand2):
        """%1 < %2

        Kleiner als; compares like Scratch (numbers numerically, otherwise text without case).

        Returns
        -------
        bool
        """
        return self._core.operator_lt(operand1, operand2)

    def gleich(self, operand1, operand2):
        """%1 = %2

        Gleich; compares like Scratch (numbers numerically, otherwise text without case).

        Returns
        -------
        bool
        """
        return self._core.operator_equals(operand1, operand2)

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

    def wenn_bühne_angeklickt_wird(self, generator_function, name="", no_refresh=False):
        """Wenn Bühne angeklickt wird

        Parameters
        ----------
        generator_function : function
            Die Funktion mit dem Code, der ausgeführt werden soll.
        name : str
            Ein Name, um Skripte zu unterscheiden, die dieselbe Funktion verwenden.
        no_refresh : bool
            Wenn True, wird der Code in einem Durchgang ohne Bildschirmaktualisierung ausgeführt.
        """
        return self._core.event_whenstageclicked(generator_function, name, no_refresh)

    def geteilt_durch(self, a, b):
        """%1 / %2

        Wie in Scratch ergibt die Division durch 0 Infinity, -Infinity oder NaN
        statt eines Fehlers.

        Parameters
        ----------
        a : float
        b : float

        Returns
        -------
        float
        """
        return self._core.operator_divide(a, b)

    def modulo(self, a, b):
        """%1 modulo %2

        Der Rest einer Division, mit dem Vorzeichen des Teilers wie in
        Scratch. Modulo 0 ergibt NaN.

        Parameters
        ----------
        a : float
        b : float

        Returns
        -------
        float
        """
        return self._core.operator_mod(a, b)

    def lösche_alles(self):
        """lösche alles

        Löscht alles, was mit dem Stift gemalt wurde.

        Returns
        -------
        None
        """
        return self._core.pen_clear()

    def zeige_monitor(self, reporter):
        """Zeigt den Monitor eines Werts, wie das Kästchen neben einem Block in Scratch.

        Parameters
        ----------
        reporter : str
            Was gezeigt wird: "x-Position", "y-Position", "Richtung",
            "Kostümnummer", "Kostümname", "Größe", "Lautstärke" (Figuren und
            Bühne), "Bühnenbildnummer", "Bühnenbildname" (Bühne), "Antwort",
            "Mikrofon-Lautstärke", "Stoppuhr", "Jahr", "Monat", "Datum",
            "Wochentag", "Stunde", "Minute", "Sekunde" oder "Benutzername".
        """
        return self._core.pystage_showmonitor(reporter)

    def verstecke_monitor(self, reporter):
        """Versteckt den Monitor eines Werts. Die Werte stehen bei zeige_monitor."""
        return self._core.pystage_hidemonitor(reporter)

    def setze_wertemonitor_position(self, reporter, x, y):
        """Setzt die Position des Monitors eines Werts.

        Parameters
        ----------
        reporter : str
            Der Wert, siehe zeige_monitor.
        x : int
            Linker Rand (Scratch-Koordinaten).
        y : int
            Oberer Rand (Scratch-Koordinaten).
        """
        return self._core.pystage_setreportermonitorposition(reporter, x, y)

    def setze_wertemonitor_stil(self, reporter, stil="normal"):
        """Setzt den Stil des Monitors eines Werts.

        Parameters
        ----------
        reporter : str
            Der Wert, siehe zeige_monitor.
        stil : str
            "normal" oder "groß" (auch "large").
        """
        return self._core.pystage_setreportermonitorstyle(reporter, stil)
