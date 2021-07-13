
from pystage.core.stage import CoreStage
from pystage.de.sprite import Figur


class Bühne():

    def __init__(self):
        self._core = CoreStage()
        self._core.facade = self
        self._core.sprite_facade_class = Figur

    def füge_eine_figur_hinzu(self, costume="default"):
        return self._core.pystage_createsprite(costume=costume)

    def abspielen(self):
        self._core.pystage_play()
        
            
    def erzeuge_klon_von(self, sprite='_myself_'):
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
        self._core.control_create_clone_of(sprite='_my_')
                
    def stoppe_alles(self):
        """stoppe alles

        Translation string: stoppe alles
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.control_stop_all()
                
    def stoppe_andere_skripte_der_figur(self):
        """stoppe andere Skripte der Figur

        Translation string: stoppe andere Skripte der Figur
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.control_stop_other()
                
    def stoppe_dieses_skript(self):
        """stoppe dieses Skript

        Translation string: stoppe dieses Skript
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.control_stop_this()
                
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
        self._core.control_wait(secs)
                
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
        self._core.event_broadcast(message)
                
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
        self._core.event_broadcastandwait(message)
                
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
        self._core.event_whenbackdropswitchesto(backdrop, generator_function, name='', no_refresh=False)
                
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
        self._core.event_whenbroadcastreceived(message, generator_function, name='', no_refresh=False)
                
    def wenn_GREENFLAG_angeklickt_wird(self, generator_function, name='', no_refresh=False):
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
        self._core.event_whenflagclicked(generator_function, name='', no_refresh=False)
                
    def wenn_lautstärke_GREATERTHAN(self, value, generator_function, name='', no_refresh=False):
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
        self._core.event_whengreaterthan_loudness(value, generator_function, name='', no_refresh=False)
                
    def wenn_stoppuhr_GREATERTHAN(self, value, generator_function, name='', no_refresh=False):
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
        self._core.event_whengreaterthan_timer(value, generator_function, name='', no_refresh=False)
                
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
        self._core.event_whenkeypressed(key, generator_function, name='', no_refresh=False)
                
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
        self._core.event_whenthisspriteclicked(generator_function, name='', no_refresh=False)
                
    def bühnenbild_name(self):
        """Bühnenbild Name

        Translation string: Bühnenbild Name
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.looks_backdropnumbername_name()
                
    def bühnenbild_nummer(self):
        """Bühnenbild Nummer

        Translation string: Bühnenbild Nummer
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.looks_backdropnumbername_number()
                
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
        self._core.looks_changeeffectby_brightness(value)
                
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
        self._core.looks_changeeffectby_color(value)
                
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
        self._core.looks_changeeffectby_fisheye(value)
                
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
        self._core.looks_changeeffectby_ghost(value)
                
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
        self._core.looks_changeeffectby_mosaic(value)
                
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
        self._core.looks_changeeffectby_pixelate(value)
                
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
        self._core.looks_changeeffectby_whirl(value)
                
    def schalte_grafikeffekte_aus(self):
        """schalte Grafikeffekte aus

        Translation string: schalte Grafikeffekte aus
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.looks_cleargraphiceffects()
                
    def nächstes_bühnenbild(self):
        """nächstes Bühnenbild

        Translation string: nächstes Bühnenbild
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.looks_nextbackdrop()
                
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
        self._core.looks_seteffectto_brightness(value)
                
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
        self._core.looks_seteffectto_color(value)
                
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
        self._core.looks_seteffectto_fisheye(value)
                
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
        self._core.looks_seteffectto_ghost(value)
                
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
        self._core.looks_seteffectto_mosaic(value)
                
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
        self._core.looks_seteffectto_pixelate(value)
                
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
        self._core.looks_seteffectto_whirl(value)
                
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
        self._core.looks_switchbackdropto(backdrop)
                
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
        self._core.looks_switchbackdroptoandwait(backdrop)
                
    def von(self, operator, number):
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
        self._core.operator_mathop(operator, number)
                
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
        self._core.operator_random(start, end)
                
    def pystage_addbackdrop(self, name, center_x=None, center_y=None):
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
        self._core.pystage_addbackdrop(name, center_x=None, center_y=None)
                
    def pystage_addsound(self, name):
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
        self._core.pystage_addsound(name)
                
    def pystage_createsprite(self, costume='default'):
        """

        Translation string: 
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        costume : FILL
        

        Returns
        -------

        """
        self._core.pystage_createsprite(costume='default')
                
    def pystage_insertbackdrop(self, index, name, center_x=None, center_y=None):
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
        self._core.pystage_insertbackdrop(index, name, center_x=None, center_y=None)
                
    def pystage_play(self):
        """

        Translation string: 
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.pystage_play()
                
    def pystage_replacebackdrop(self, index, name, center_x=None, center_y=None):
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
        self._core.pystage_replacebackdrop(index, name, center_x=None, center_y=None)
                
    def antwort(self):
        """Antwort

        Translation string: Antwort
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_answer()
                
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
        self._core.sensing_askandwait(question)
                
    def datum_im_moment(self):
        """Datum im Moment

        Translation string: Datum im Moment
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_current_date()
                
    def wochentag_im_moment(self):
        """Wochentag im Moment

        Translation string: Wochentag im Moment
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_current_dayofweek()
                
    def stunde_im_moment(self):
        """Stunde im Moment

        Translation string: Stunde im Moment
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_current_hour()
                
    def minute_im_moment(self):
        """Minute im Moment

        Translation string: Minute im Moment
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_current_minute()
                
    def monat_im_moment(self):
        """Monat im Moment

        Translation string: Monat im Moment
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_current_month()
                
    def sekunde_im_moment(self):
        """Sekunde im Moment

        Translation string: Sekunde im Moment
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_current_second()
                
    def jahr_im_moment(self):
        """Jahr im Moment

        Translation string: Jahr im Moment
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_current_year()
                
    def tage_seit(self):
        """Tage seit 2000

        Translation string: Tage seit 2000
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_dayssince2000()
                
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
        self._core.sensing_keypressed(key)
                
    def lautstärke(self):
        """Lautstärke

        Translation string: Lautstärke
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_loudness()
                
    def maustaste_gedrückt(self):
        """Maustaste gedrückt?

        Translation string: Maustaste gedrückt?
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_mousedown()
                
    def maus_x_position(self):
        """Maus x-Position

        Translation string: Maus x-Position
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_mousex()
                
    def maus_y_position(self):
        """Maus y-Position

        Translation string: Maus y-Position
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_mousey()
                
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
        self._core.sensing_of_backdropname(stage='_stage_')
                
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
        self._core.sensing_of_backdropnumber(stage='_stage_')
                
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
        self._core.sensing_of_costumename(sprite)
                
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
        self._core.sensing_of_costumenumber(sprite)
                
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
        self._core.sensing_of_direction(sprite)
                
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
        self._core.sensing_of_size(sprite)
                
    def von(self, variable, sprite='_stage_'):
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
        self._core.sensing_of_variable(variable, sprite='_stage_')
                
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
        self._core.sensing_of_volume(sprite='_stage_')
                
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
        self._core.sensing_of_xposition(sprite)
                
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
        self._core.sensing_of_yposition(sprite)
                
    def setze_stoppuhr_zurück(self):
        """setze Stoppuhr zurück

        Translation string: setze Stoppuhr zurück
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_resettimer()
                
    def setze_ziehbarkeit_auf_ziehbar(self):
        """setze Ziehbarkeit auf ziehbar

        Translation string: setze Ziehbarkeit auf ziehbar
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_setdragmode_draggable()
                
    def setze_ziehbarkeit_auf_nicht_ziehbar(self):
        """setze Ziehbarkeit auf nicht ziehbar

        Translation string: setze Ziehbarkeit auf nicht ziehbar
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_setdragmode_notdraggable()
                
    def stoppuhr(self):
        """Stoppuhr

        Translation string: Stoppuhr
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_timer()
                
    def benutzername(self):
        """Benutzername

        Translation string: Benutzername
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_username()
                
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
        self._core.sound_changeeffectby_pan(value)
                
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
        self._core.sound_changeeffectby_pitch(value)
                
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
        self._core.sound_changevolumeby(value)
                
    def schalte_klangeffekte_aus(self):
        """schalte Klangeffekte aus

        Translation string: schalte Klangeffekte aus
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sound_cleareffects()
                
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
        self._core.sound_play(name, loop=0)
                
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
        self._core.sound_playuntildone(name)
                
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
        self._core.sound_seteffectto_pan(value)
                
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
        self._core.sound_seteffectto_pitch(value)
                
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
        self._core.sound_setvolumeto(value)
                
    def stoppe_alle_klänge(self):
        """stoppe alle Klänge

        Translation string: stoppe alle Klänge
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sound_stopallsounds()
                
    def lautstärke(self):
        """Lautstärke

        Translation string: Lautstärke
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sound_volume()
                
