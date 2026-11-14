
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
        """Sendet eine Nachricht an alle Figuren und die Bühne. Jeder Block "Wenn ich ... empfange" mit dieser Nachricht startet. Das Skript wartet nicht auf sie.

        Scratch-Block: sende (Nachricht1) an alle

        Parameters
        ----------
        message : str
            Der Name der Nachricht. Groß- und Kleinschreibung spielen keine Rolle.
        """
        return self._core.event_broadcast(message)
                
    def sende_an_alle_und_warte(self, message):
        """Sendet eine Nachricht an alle Figuren und die Bühne und wartet, bis alle Skripte fertig sind, die sie empfangen.

        Scratch-Block: sende (Nachricht1) an alle und warte

        Parameters
        ----------
        message : str
            Der Name der Nachricht. Groß- und Kleinschreibung spielen keine Rolle.
        """
        return self._core.event_broadcastandwait(message)
                
    def wenn_das_bühnenbild_wechselt_zu(self, backdrop, generator_function, name='', no_refresh=False):
        """Führt den Code aus, wenn die Bühne zu dem angegebenen Bühnenbild wechselt.

        Scratch-Block: Wenn das Bühnenbild zu (Bühnenbild1) wechselt

        Parameters
        ----------
        backdrop : str
            Der Name des Bühnenbilds. Groß- und Kleinschreibung spielen keine Rolle.
        generator_function : function
            Die Funktion mit dem Code, der ausgeführt werden soll.
        name : str
            Ein Name, um Skripte zu unterscheiden, die dieselbe Funktion verwenden.
        no_refresh : bool
            Wenn True, wird der Code in einem Durchgang ohne Bildschirmaktualisierung ausgeführt.
        """
        return self._core.event_whenbackdropswitchesto(backdrop, generator_function, name, no_refresh)
                
    def wenn_ich_empfange(self, message, generator_function, name='', no_refresh=False):
        """Führt den Code aus, wenn die angegebene Nachricht gesendet wird.

        Scratch-Block: Wenn ich (Nachricht1) empfange

        Parameters
        ----------
        message : str
            Der Name der Nachricht. Groß- und Kleinschreibung spielen keine Rolle.
        generator_function : function
            Die Funktion mit dem Code, der ausgeführt werden soll.
        name : str
            Ein Name, um Skripte zu unterscheiden, die dieselbe Funktion verwenden.
        no_refresh : bool
            Wenn True, wird der Code in einem Durchgang ohne Bildschirmaktualisierung ausgeführt.
        """
        return self._core.event_whenbroadcastreceived(message, generator_function, name, no_refresh)
                
    def wenn_programm_startet(self, generator_function, name='', no_refresh=False):
        """Führt den Code aus, wenn die grüne Flagge angeklickt wird, also wenn das Programm startet.

        Scratch-Block: Wenn [grüne Flagge] angeklickt wird

        Parameters
        ----------
        generator_function : function
            Die Funktion mit dem Code, der ausgeführt werden soll.
        name : str
            Ein Name, um Skripte zu unterscheiden, die dieselbe Funktion verwenden.
        no_refresh : bool
            Wenn True, wird der Code in einem Durchgang ohne Bildschirmaktualisierung ausgeführt.
        """
        return self._core.event_whenflagclicked(generator_function, name, no_refresh)
                
    def wenn_lautstärke_größer_als(self, value, generator_function, name='', no_refresh=False):
        """Führt den Code aus, wenn die Lautstärke des Mikrofons größer als der angegebene Wert ist.

        Dies ist nur ein Platzhalter: Das Mikrofon wird nicht unterstützt, die Lautstärke ist immer -1 und der Code wird nie ausgeführt.

        Scratch-Block: Wenn [Lautstärke] > (10)

        Parameters
        ----------
        value : Zahl
            Der Lautstärkewert, der überschritten werden muss.
        generator_function : function
            Die Funktion mit dem Code, der ausgeführt werden soll.
        name : str
            Ein Name, um Skripte zu unterscheiden, die dieselbe Funktion verwenden.
        no_refresh : bool
            Wenn True, wird der Code in einem Durchgang ohne Bildschirmaktualisierung ausgeführt.
        """
        return self._core.event_whengreaterthan_loudness(value, generator_function, name, no_refresh)
                
    def wenn_stoppuhr_größer_als(self, value, generator_function, name='', no_refresh=False):
        """Führt den Code aus, wenn die Stoppuhr größer als der angegebene Wert ist.

        Der Code wird jedes Mal einmal ausgeführt, wenn die Stoppuhr den Wert überschreitet. Er wird erneut ausgeführt, nachdem die Stoppuhr zurückgesetzt wurde.

        Scratch-Block: Wenn [Stoppuhr] > (10)

        Parameters
        ----------
        value : Zahl
            Die Anzahl Sekunden, die die Stoppuhr überschreiten muss.
        generator_function : function
            Die Funktion mit dem Code, der ausgeführt werden soll.
        name : str
            Ein Name, um Skripte zu unterscheiden, die dieselbe Funktion verwenden.
        no_refresh : bool
            Wenn True, wird der Code in einem Durchgang ohne Bildschirmaktualisierung ausgeführt.
        """
        return self._core.event_whengreaterthan_timer(value, generator_function, name, no_refresh)
                
    def wenn_taste_gedrückt_wird(self, key, generator_function, name='', no_refresh=False):
        """Führt den Code aus, wenn eine Taste gedrückt wird.

        Scratch-Block: Wenn Taste (Leertaste) gedrückt wird

        Parameters
        ----------
        key : str
            Die Taste, z. B. "a", "1", "Leertaste", "Pfeil nach links", "Pfeil nach rechts", "Pfeil nach oben", "Pfeil nach unten" oder "beliebiges" (jede Taste). Groß- und Kleinschreibung spielen keine Rolle.
        generator_function : function
            Die Funktion mit dem Code, der ausgeführt werden soll.
        name : str
            Ein Name, um Skripte zu unterscheiden, die dieselbe Funktion verwenden.
        no_refresh : bool
            Wenn True, wird der Code in einem Durchgang ohne Bildschirmaktualisierung ausgeführt.
        """
        return self._core.event_whenkeypressed(key, generator_function, name, no_refresh)
                
    def wenn_diese_figur_angeklickt_wird(self, generator_function, name='', no_refresh=False):
        """Führt den Code aus, wenn die Figur mit der Maus angeklickt wird.

        Scratch-Block: Wenn diese Figur angeklickt wird

        Parameters
        ----------
        generator_function : function
            Die Funktion mit dem Code, der ausgeführt werden soll.
        name : str
            Ein Name, um Skripte zu unterscheiden, die dieselbe Funktion verwenden.
        no_refresh : bool
            Wenn True, wird der Code in einem Durchgang ohne Bildschirmaktualisierung ausgeführt.
        """
        return self._core.event_whenthisspriteclicked(generator_function, name, no_refresh)
                
    def bühnenbild_name(self):
        """Gibt den Namen des aktuellen Bühnenbilds zurück.

        Scratch-Block: (Bühnenbild [Name])

        Returns
        -------
        str
            Der Name des aktuellen Bühnenbilds, oder ein leerer Text, wenn es kein Bühnenbild gibt.
        """
        return self._core.looks_backdropnumbername_name()
                
    def bühnenbild_nummer(self):
        """Gibt die Nummer des aktuellen Bühnenbilds zurück (ab 1).

        Scratch-Block: (Bühnenbild [Nummer])

        Returns
        -------
        int
            Die Nummer des aktuellen Bühnenbilds.
        """
        return self._core.looks_backdropnumbername_number()
                
    def ändere_effekt_helligkeit_um(self, value):
        """Ändert den Helligkeit-Effekt der Figur um den angegebenen Wert. Negative Werte machen das Kostüm dunkler.

        Scratch-Block: ändere Effekt Helligkeit um (25)

        Parameters
        ----------
        value : Zahl
            Die Änderung des Effekts. Der Effekt geht von -100 (schwarz) bis 100 (weiß).
        """
        return self._core.looks_changeeffectby_brightness(value)
                
    def ändere_effekt_farbe_um(self, value):
        """Ändert den Farbeffekt der Figur um den angegebenen Wert. Der Farbeffekt verändert die Farben des Kostüms.

        Scratch-Block: ändere Effekt Farbe um (25)

        Parameters
        ----------
        value : Zahl
            Die Änderung des Effekts. Der Effekt geht von 0 bis 200 und beginnt nach 200 wieder bei 0.
        """
        return self._core.looks_changeeffectby_color(value)
                
    def ändere_effekt_fischauge_um(self, value):
        """Ändert den Fischauge-Effekt der Figur um den angegebenen Wert. Das Kostüm wird wie durch eine Fischaugenlinse verzerrt.

        Scratch-Block: ändere Effekt Fischauge um (25)

        Parameters
        ----------
        value : Zahl
            Die Änderung des Effekts. 0 bedeutet kein Effekt.
        """
        return self._core.looks_changeeffectby_fisheye(value)
                
    def ändere_effekt_durchsichtigkeit_um(self, value):
        """Ändert den Durchsichtigkeit-Effekt der Figur um den angegebenen Wert. Je höher der Effekt, desto durchsichtiger wird die Figur.

        Scratch-Block: ändere Effekt Durchsichtigkeit um (25)

        Parameters
        ----------
        value : Zahl
            Die Änderung des Effekts. 0 bedeutet sichtbar, 100 bedeutet unsichtbar.
        """
        return self._core.looks_changeeffectby_ghost(value)
                
    def ändere_effekt_mosaik_um(self, value):
        """Ändert den Mosaik-Effekt der Figur um den angegebenen Wert. Das Kostüm wird als kleine Kacheln wiederholt.

        Scratch-Block: ändere Effekt Mosaik um (25)

        Parameters
        ----------
        value : Zahl
            Die Änderung des Effekts. 0 bedeutet kein Effekt.
        """
        return self._core.looks_changeeffectby_mosaic(value)
                
    def ändere_effekt_pixel_um(self, value):
        """Ändert den Pixel-Effekt der Figur um den angegebenen Wert. Das Kostüm sieht dann klotzig aus.

        Scratch-Block: ändere Effekt Pixel um (25)

        Parameters
        ----------
        value : Zahl
            Die Änderung des Effekts. 0 bedeutet kein Effekt.
        """
        return self._core.looks_changeeffectby_pixelate(value)
                
    def ändere_effekt_wirbel_um(self, value):
        """Ändert den Wirbel-Effekt der Figur um den angegebenen Wert. Das Kostüm wird verdreht.

        Scratch-Block: ändere Effekt Wirbel um (25)

        Parameters
        ----------
        value : Zahl
            Die Änderung des Effekts. 0 bedeutet kein Effekt.
        """
        return self._core.looks_changeeffectby_whirl(value)
                
    def ändere_größe_um(self, percent):
        """Ändert die Größe der Figur um den angegebenen Prozentwert. Negative Werte machen sie kleiner.

        Scratch-Block: ändere Größe um (10)

        Parameters
        ----------
        percent : Zahl
            Die Änderung in Prozent. Mit 10 wird die Figur 10 Prozent größer.
        """
        return self._core.looks_changesizeby(percent)
                
    def schalte_grafikeffekte_aus(self):
        """Entfernt alle Grafikeffekte (Farbe, Fischauge, Wirbel, Pixel, Mosaik, Helligkeit und Durchsichtigkeit) der Figur.

        Scratch-Block: schalte Grafikeffekte aus
        """
        return self._core.looks_cleargraphiceffects()
                
    def kostüm_name(self):
        """Gibt den Namen des aktuellen Kostüms der Figur zurück.

        Scratch-Block: (Kostüm [Name])

        Returns
        -------
        str
            Der Name des aktuellen Kostüms, oder ein leerer Text, wenn die Figur kein Kostüm hat.
        """
        return self._core.looks_costumenumbername_name()
                
    def kostüm_nummer(self):
        """Gibt die Nummer des aktuellen Kostüms der Figur zurück (ab 1).

        Scratch-Block: (Kostüm [Nummer])

        Returns
        -------
        int
            Die Nummer des aktuellen Kostüms.
        """
        return self._core.looks_costumenumbername_number()
                
    def gehe_ebenen_nach_hinten(self, value):
        """Bringt die Figur um die angegebene Anzahl Ebenen nach hinten, also hinter andere Figuren.

        Scratch-Block: gehe (1) Ebenen nach hinten

        Parameters
        ----------
        value : int
            Die Anzahl Ebenen, um die nach hinten gegangen wird.
        """
        return self._core.looks_goforwardbackwardlayers_backward(value)
                
    def gehe_ebenen_nach_vorne(self, value):
        """Bringt die Figur um die angegebene Anzahl Ebenen nach vorne, also vor andere Figuren.

        Scratch-Block: gehe (1) Ebenen nach vorne

        Parameters
        ----------
        value : int
            Die Anzahl Ebenen, um die nach vorne gegangen wird.
        """
        return self._core.looks_goforwardbackwardlayers_forward(value)
                
    def gehe_zu_hinterster_ebene(self):
        """Bringt die Figur hinter alle anderen Figuren.

        Scratch-Block: gehe zu hinterster Ebene
        """
        return self._core.looks_gotofrontback_back()
                
    def gehe_zu_vorderster_ebene(self):
        """Bringt die Figur vor alle anderen Figuren.

        Scratch-Block: gehe zu vorderster Ebene
        """
        return self._core.looks_gotofrontback_front()
                
    def verstecke_dich(self):
        """Versteckt die Figur. Sie wird erst wieder auf der Bühne gezeigt, wenn sie erneut angezeigt wird.

        Scratch-Block: verstecke dich
        """
        return self._core.looks_hide()
                
    def nächstes_bühnenbild(self):
        """Wechselt zum nächsten Bühnenbild. Nach dem letzten Bühnenbild wird wieder das erste benutzt.

        Scratch-Block: nächstes Bühnenbild
        """
        return self._core.looks_nextbackdrop()
                
    def wechsle_zum_nächsten_kostüm(self):
        """Wechselt zum nächsten Kostüm der Figur. Nach dem letzten Kostüm wird wieder das erste benutzt.

        Scratch-Block: wechsle zum nächsten Kostüm
        """
        return self._core.looks_nextcostume()
                
    def sage(self, text):
        """Zeigt eine Sprechblase mit dem angegebenen Text neben der Figur.

        Scratch-Block: sage (Hallo!)

        Parameters
        ----------
        text : str
            Der Text, der in der Sprechblase steht.
        """
        return self._core.looks_say(text)
                
    def sage_für_sekunden(self, text, secs):
        """Zeigt eine Sprechblase mit dem angegebenen Text neben der Figur für eine bestimmte Anzahl Sekunden.

        Das Skript wartet, bis die Zeit vorbei ist.

        Scratch-Block: sage (Hallo!) für (2) Sekunden

        Parameters
        ----------
        text : str
            Der Text, der in der Sprechblase steht.
        secs : Zahl
            Die Anzahl Sekunden, für die die Sprechblase angezeigt wird.
        """
        return self._core.looks_sayforsecs(text, secs)
                
    def setze_effekt_helligkeit_auf(self, value):
        """Setzt den Helligkeit-Effekt der Figur. Negative Werte machen das Kostüm dunkler.

        Scratch-Block: setze Effekt Helligkeit auf (0)

        Parameters
        ----------
        value : Zahl
            Der neue Wert des Effekts, von -100 (schwarz) bis 100 (weiß). 0 bedeutet kein Effekt.
        """
        return self._core.looks_seteffectto_brightness(value)
                
    def setze_effekt_farbe_auf(self, value):
        """Setzt den Farbeffekt der Figur. Der Farbeffekt verändert die Farben des Kostüms.

        Scratch-Block: setze Effekt Farbe auf (0)

        Parameters
        ----------
        value : Zahl
            Der neue Wert des Effekts, von 0 bis 200. 0 bedeutet kein Effekt.
        """
        return self._core.looks_seteffectto_color(value)
                
    def setze_effekt_fischauge_auf(self, value):
        """Setzt den Fischauge-Effekt der Figur. Das Kostüm wird wie durch eine Fischaugenlinse verzerrt.

        Scratch-Block: setze Effekt Fischauge auf (0)

        Parameters
        ----------
        value : Zahl
            Der neue Wert des Effekts. 0 bedeutet kein Effekt.
        """
        return self._core.looks_seteffectto_fisheye(value)
                
    def setze_effekt_durchsichtigkeit_auf(self, value):
        """Setzt den Durchsichtigkeit-Effekt der Figur. Je höher der Effekt, desto durchsichtiger wird die Figur.

        Scratch-Block: setze Effekt Durchsichtigkeit auf (0)

        Parameters
        ----------
        value : Zahl
            Der neue Wert des Effekts. 0 bedeutet sichtbar, 100 bedeutet unsichtbar.
        """
        return self._core.looks_seteffectto_ghost(value)
                
    def setze_effekt_mosaik_auf(self, value):
        """Setzt den Mosaik-Effekt der Figur. Das Kostüm wird als kleine Kacheln wiederholt.

        Scratch-Block: setze Effekt Mosaik auf (0)

        Parameters
        ----------
        value : Zahl
            Der neue Wert des Effekts. 0 bedeutet kein Effekt.
        """
        return self._core.looks_seteffectto_mosaic(value)
                
    def setze_effekt_pixel_auf(self, value):
        """Setzt den Pixel-Effekt der Figur. Das Kostüm sieht dann klotzig aus.

        Scratch-Block: setze Effekt Pixel auf (0)

        Parameters
        ----------
        value : Zahl
            Der neue Wert des Effekts. 0 bedeutet kein Effekt.
        """
        return self._core.looks_seteffectto_pixelate(value)
                
    def setze_effekt_wirbel_auf(self, value):
        """Setzt den Wirbel-Effekt der Figur. Das Kostüm wird verdreht.

        Scratch-Block: setze Effekt Wirbel auf (0)

        Parameters
        ----------
        value : Zahl
            Der neue Wert des Effekts. 0 bedeutet kein Effekt.
        """
        return self._core.looks_seteffectto_whirl(value)
                
    def setze_größe_auf(self, percent):
        """Setzt die Größe der Figur in Prozent. 100 ist die normale Größe.

        Scratch-Block: setze Größe auf (100) %

        Parameters
        ----------
        percent : Zahl
            Die neue Größe in Prozent. 100 ist die normale Größe, 50 ist halb so groß.
        """
        return self._core.looks_setsizeto(percent)
                
    def zeige_dich(self):
        """Zeigt die Figur auf der Bühne.

        Scratch-Block: zeige dich
        """
        return self._core.looks_show()
                
    def größe(self):
        """Gibt die Größe der Figur in Prozent zurück. 100 ist die normale Größe.

        Scratch-Block: (Größe)

        Returns
        -------
        Zahl
            Die Größe der Figur in Prozent.
        """
        return self._core.looks_size()
                
    def wechsle_zu_bühnenbild(self, backdrop):
        """Wechselt zu einem anderen Bühnenbild.

        Scratch-Block: wechsle zu Bühnenbild (Bühnenbild1)

        Parameters
        ----------
        backdrop : str oder int
            Der Name des Bühnenbilds, seine Nummer (ab 1) oder eines von "nächstes Bühnenbild", "vorheriges Bühnenbild" und "zufälliges Bühnenbild".
        """
        return self._core.looks_switchbackdropto_backdrop(backdrop)
                
    def wechsle_zu_zufälligem_bühnenbild(self):
        """Wechselt zu einem zufälligen Bühnenbild.

        Scratch-Block: wechsle zu [zufälliges Bühnenbild]
        """
        return self._core.looks_switchbackdropto_random()

    def wechsle_zum_vorherigen_bühnenbild(self):
        """Wechselt zum vorherigen Bühnenbild. Vor dem ersten Bühnenbild wird das letzte benutzt.

        Scratch-Block: wechsle zu [vorheriges Bühnenbild]
        """
        return self._core.looks_switchbackdropto_previous()

    def wechsle_zum_nächsten_bühnenbild(self):
        """Wechselt zum nächsten Bühnenbild. Nach dem letzten Bühnenbild wird wieder das erste benutzt.

        Scratch-Block: wechsle zu [nächstes Bühnenbild]
        """
        return self._core.looks_switchbackdropto_next()

    def wechsle_zu_kostüm(self, costume):
        """Wechselt zu einem anderen Kostüm der Figur.

        Scratch-Block: wechsle zu Kostüm (Kostüm2)

        Parameters
        ----------
        costume : str oder int
            Der Name des Kostüms oder seine Nummer (ab 1).
        """
        return self._core.looks_switchcostumeto(costume)
                
    def denke(self, text):
        """Zeigt eine Denkblase mit dem angegebenen Text neben der Figur.

        Scratch-Block: denke (Hmm...)

        Parameters
        ----------
        text : str
            Der Text, der in der Denkblase steht.
        """
        return self._core.looks_think(text)
                
    def denke_für_sekunden(self, text, secs):
        """Zeigt eine Denkblase mit dem angegebenen Text neben der Figur für eine bestimmte Anzahl Sekunden.

        Das Skript wartet, bis die Zeit vorbei ist.

        Scratch-Block: denke (Hmm...) für (2) Sekunden

        Parameters
        ----------
        text : str
            Der Text, der in der Denkblase steht.
        secs : Zahl
            Die Anzahl Sekunden, für die die Denkblase angezeigt wird.
        """
        return self._core.looks_thinkforsecs(text, secs)
                
    def ändere_x_um(self, value):
        """Bewegt die Figur waagerecht um den angegebenen Wert. Positive Werte bewegen sie nach rechts.

        Scratch-Block: ändere x um (10)

        Parameters
        ----------
        value : Zahl
            Die Anzahl Schritte, um die waagerecht bewegt wird.
        """
        return self._core.motion_changexby(value)
                
    def ändere_y_um(self, value):
        """Bewegt die Figur senkrecht um den angegebenen Wert. Positive Werte bewegen sie nach oben.

        Scratch-Block: ändere y um (10)

        Parameters
        ----------
        value : Zahl
            Die Anzahl Schritte, um die senkrecht bewegt wird.
        """
        return self._core.motion_changeyby(value)
                
    def richtung(self):
        """Gibt die Richtung der Figur in Grad zurück. 90 ist rechts, 0 ist oben, 180 ist unten und -90 ist links.

        Scratch-Block: (Richtung)

        Returns
        -------
        Zahl
            Die Richtung der Figur, zwischen -180 und 180.
        """
        return self._core.motion_direction()
                
    def gleite_in_sek_zu_x_y(self, secs, x, y):
        """Lässt die Figur innerhalb der angegebenen Anzahl Sekunden zur angegebenen x- und y-Position gleiten.

        Das Skript wartet, bis das Gleiten beendet ist.

        Scratch-Block: gleite in (1) Sek. zu x: (0) y: (0)

        Parameters
        ----------
        secs : Zahl
            Die Dauer des Gleitens in Sekunden. 0 bewegt die Figur sofort.
        x : Zahl
            Die waagerechte Zielposition.
        y : Zahl
            Die senkrechte Zielposition.
        """
        return self._core.motion_glidesecstoxy(secs, x, y)
                
    def gleite_in_sek_zu_mauszeiger(self, secs):
        """Lässt die Figur innerhalb der angegebenen Anzahl Sekunden zur Position des Mauszeigers gleiten.

        Das Skript wartet, bis das Gleiten beendet ist.

        Scratch-Block: gleite in (1) Sek. zu [Mauszeiger]

        Parameters
        ----------
        secs : Zahl
            Die Dauer des Gleitens in Sekunden. 0 bewegt die Figur sofort.
        """
        return self._core.motion_glideto_pointer(secs)
                
    def gleite_in_sek_zu_zufallsposition(self, secs):
        """Lässt die Figur innerhalb der angegebenen Anzahl Sekunden zu einer zufälligen Position gleiten.

        Das Skript wartet, bis das Gleiten beendet ist.

        Scratch-Block: gleite in (1) Sek. zu [Zufallsposition]

        Parameters
        ----------
        secs : Zahl
            Die Dauer des Gleitens in Sekunden. 0 bewegt die Figur sofort.
        """
        return self._core.motion_glideto_random(secs)
                
    def gleite_in_sek_zu(self, secs, sprite):
        """Lässt die Figur innerhalb der angegebenen Anzahl Sekunden zur Position einer anderen Figur gleiten.

        Das Skript wartet, bis das Gleiten beendet ist.

        Scratch-Block: gleite in (1) Sek. zu [Figur]

        Parameters
        ----------
        secs : Zahl
            Die Dauer des Gleitens in Sekunden. 0 bewegt die Figur sofort.
        sprite : str
            Der Name der Figur, zu der die Figur gleitet. "_mouse_" steht für den Mauszeiger,
            "_random_" für eine zufällige Position.
        """
        return self._core.motion_glideto_sprite(secs, sprite)
                
    def gehe_zu_mauszeiger(self):
        """Bewegt die Figur an die Position des Mauszeigers.

        Scratch-Block: gehe zu [Mauszeiger]
        """
        return self._core.motion_goto_pointer()
                
    def gehe_zu_zufallsposition(self):
        """Bewegt die Figur an eine zufällige Position auf der Bühne.

        Scratch-Block: gehe zu [Zufallsposition]
        """
        return self._core.motion_goto_random()
                
    def gehe_zu(self, sprite):
        """Bewegt die Figur an die Position einer anderen Figur.

        Scratch-Block: gehe zu [Figur]

        Parameters
        ----------
        sprite : str
            Der Name der Figur, zu der gegangen wird. "_mouse_" steht für den Mauszeiger,
            "_random_" für eine zufällige Position.
        """
        return self._core.motion_goto_sprite(sprite)
                
    def gehe_zu_x_y(self, x, y):
        """Bewegt die Figur an die angegebene x- und y-Position. Die Mitte der Bühne ist x = 0, y = 0.

        Scratch-Block: gehe zu x: (0) y: (0)

        Parameters
        ----------
        x : Zahl
            Die waagerechte Position. Auf der Standardbühne mit 480 mal 360 Pixeln reicht x von -240 (links) bis 240 (rechts).
        y : Zahl
            Die senkrechte Position. Auf der Standardbühne reicht y von -180 (unten) bis 180 (oben).
        """
        return self._core.motion_gotoxy(x, y)
                
    def pralle_vom_rand_ab(self):
        """Wenn die Figur den Rand der Bühne berührt, prallt sie ab und bleibt auf der Bühne.

        Scratch-Block: pralle vom Rand ab
        """
        return self._core.motion_ifonedgebounce()
                
    def gehe_schritte(self, steps):
        """Bewegt die Figur um die angegebene Anzahl Schritte in die Richtung, in die sie zeigt.

        Scratch-Block: gehe (10) er Schritt

        Parameters
        ----------
        steps : Zahl
            Die Anzahl Schritte. Negative Werte bewegen die Figur rückwärts.
        """
        return self._core.motion_movesteps(steps)
                
    def setze_richtung_auf_grad(self, direction):
        """Dreht die Figur in die angegebene Richtung.

        Scratch-Block: setze Richtung auf (90) Grad

        Parameters
        ----------
        direction : Zahl
            Die Richtung in Grad. 0 ist oben, 90 ist rechts, 180 ist unten und -90 ist links.
        """
        return self._core.motion_pointindirection(direction)
                
    def drehe_dich_zu_mauszeiger(self):
        """Dreht die Figur zum Mauszeiger.

        Scratch-Block: drehe dich zu [Mauszeiger]
        """
        return self._core.motion_pointtowards_pointer()
                
    def drehe_dich_zu(self, sprite):
        """Dreht die Figur zu einer anderen Figur.

        Scratch-Block: drehe dich zu [Figur]

        Parameters
        ----------
        sprite : str
            Der Name der Figur, zu der gedreht wird. "_mouse_" steht für den Mauszeiger,
            "_random_" für eine zufällige Richtung.
        """
        return self._core.motion_pointtowards_sprite(sprite)
                
    def drehe_dich_zu_zufallsrichtung(self):
        """drehe dich zu (Zufallsrichtung)

        Returns
        -------
        None
        """
        return self._core.motion_pointtowards_random()

    def setze_drehtyp_auf_rundherum(self):
        """Setzt den Drehtyp auf "rundherum": Das Kostüm dreht sich mit der Richtung der Figur.

        Scratch-Block: setze Drehtyp auf [rundherum]
        """
        return self._core.motion_setrotationstyle_allaround()
                
    def setze_drehtyp_auf_nicht_drehen(self):
        """Setzt den Drehtyp auf "nicht drehen": Das Kostüm sieht immer gleich aus, egal in welche Richtung die Figur zeigt.

        Scratch-Block: setze Drehtyp auf [nicht drehen]
        """
        return self._core.motion_setrotationstyle_dontrotate()
                
    def setze_drehtyp_auf_links_rechts(self):
        """Setzt den Drehtyp auf "links-rechts": Das Kostüm dreht sich nur nach links oder rechts und steht nie auf dem Kopf.

        Scratch-Block: setze Drehtyp auf [links-rechts]
        """
        return self._core.motion_setrotationstyle_leftright()
                
    def setze_x_auf(self, value):
        """Setzt die waagerechte Position der Figur. Die Mitte der Bühne ist x = 0.

        Scratch-Block: setze x auf (0)

        Parameters
        ----------
        value : Zahl
            Die neue x-Position.
        """
        return self._core.motion_setx(value)
                
    def setze_y_auf(self, value):
        """Setzt die senkrechte Position der Figur. Die Mitte der Bühne ist y = 0.

        Scratch-Block: setze y auf (0)

        Parameters
        ----------
        value : Zahl
            Die neue y-Position.
        """
        return self._core.motion_sety(value)
                
    def drehe_dich_nach_links_um_grad(self, deg):
        """Dreht die Figur um die angegebene Anzahl Grad nach links (gegen den Uhrzeigersinn).

        Scratch-Block: drehe dich ↺ um (15) Grad

        Parameters
        ----------
        deg : Zahl
            Die Anzahl Grad, um die gedreht wird. 90 ist eine Vierteldrehung.
        """
        return self._core.motion_turnleft(deg)
                
    def drehe_dich_nach_rechts_um_grad(self, deg):
        """Dreht die Figur um die angegebene Anzahl Grad nach rechts (im Uhrzeigersinn).

        Scratch-Block: drehe dich ↻ um (15) Grad

        Parameters
        ----------
        deg : Zahl
            Die Anzahl Grad, um die gedreht wird. 90 ist eine Vierteldrehung.
        """
        return self._core.motion_turnright(deg)
                
    def x_position(self):
        """Gibt die waagerechte Position der Figur zurück. Die Mitte der Bühne ist 0.

        Scratch-Block: (x-Position)

        Returns
        -------
        Zahl
            Die x-Position der Figur.
        """
        return self._core.motion_xposition()
                
    def y_position(self):
        """Gibt die senkrechte Position der Figur zurück. Die Mitte der Bühne ist 0.

        Scratch-Block: (y-Position)

        Returns
        -------
        Zahl
            Die y-Position der Figur.
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
        """Fügt der Figur ein Kostüm (ein Bild) hinzu. Das Kostüm kommt ans Ende der Kostümliste.

        Parameters
        ----------
        name : str
            Der Name der Bilddatei, z. B. "katze.png". Die Datei muss im Projektordner liegen.
        center_x : Zahl
            Die waagerechte Position des Mittelpunkts des Kostüms im Bild in Pixeln. Ohne Angabe wird die Bildmitte genommen.
        center_y : Zahl
            Die senkrechte Position des Mittelpunkts des Kostüms im Bild in Pixeln. Ohne Angabe wird die Bildmitte genommen.
        factor : Zahl
            Die Skalierung des Bildes. 1 lässt die Originalgröße, 2 zeigt das Bild doppelt so groß.
        """
        return self._core.pystage_addcostume(name, center_x, center_y, factor)
                
    def füge_klang_hinzu(self, name):
        """Lädt eine Klangdatei, damit die Figur oder die Bühne sie abspielen kann.

        Klänge werden auch automatisch geladen, wenn sie zum ersten Mal abgespielt werden.

        Parameters
        ----------
        name : str
            Der Name der Klangdatei, z. B. "pop.wav". Die Datei muss im Projektordner liegen.
        """
        return self._core.pystage_addsound(name)
                
    def füge_kostüm_ein(self, index, name, center_x=None, center_y=None, factor=1):
        """Fügt ein Kostüm (ein Bild) an der angegebenen Stelle in die Kostümliste der Figur ein.

        Parameters
        ----------
        index : int
            Die Stelle, an der das Kostüm eingefügt wird, ab 1.
        name : str
            Der Name der Bilddatei, z. B. "katze.png".
        center_x : Zahl
            Die waagerechte Position des Mittelpunkts des Kostüms im Bild in Pixeln. Ohne Angabe wird die Bildmitte genommen.
        center_y : Zahl
            Die senkrechte Position des Mittelpunkts des Kostüms im Bild in Pixeln. Ohne Angabe wird die Bildmitte genommen.
        factor : Zahl
            Die Skalierung des Bildes. 1 lässt die Originalgröße.
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
        """Ersetzt ein vorhandenes Kostüm der Figur durch ein anderes Bild.

        Parameters
        ----------
        index : int
            Die Nummer des Kostüms, das ersetzt wird, ab 1.
        name : str
            Der Name der neuen Bilddatei.
        center_x : Zahl
            Die waagerechte Position des Mittelpunkts des Kostüms im Bild in Pixeln. Ohne Angabe wird die Bildmitte genommen.
        center_y : Zahl
            Die senkrechte Position des Mittelpunkts des Kostüms im Bild in Pixeln. Ohne Angabe wird die Bildmitte genommen.
        factor : Zahl
            Die Skalierung des Bildes. 1 lässt die Originalgröße.
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
        """Ändert den Aussteuern-Effekt des Klangs um den angegebenen Wert. Der Effekt verschiebt den Klang zwischen linkem und rechtem Lautsprecher.

        Scratch-Block: ändere Effekt Aussteuern links/rechts um (10)

        Parameters
        ----------
        value : Zahl
            Die Änderung des Aussteuern-Effekts. -100 ist ganz links, 0 die Mitte und 100 ganz rechts.
        """
        return self._core.sound_changeeffectby_pan(value)
                
    def ändere_effekt_höhe_um(self, value):
        """Ändert den Höhe-Effekt des Klangs um den angegebenen Wert. Positive Werte machen den Klang höher.

        Scratch-Block: ändere Effekt Höhe um (10)

        Parameters
        ----------
        value : Zahl
            Die Änderung des Höhe-Effekts. Der Effekt geht von -360 bis 360, 0 ist die normale Höhe.
        """
        return self._core.sound_changeeffectby_pitch(value)
                
    def ändere_lautstärke_um(self, value):
        """Ändert die Lautstärke der Klänge der Figur um den angegebenen Wert. Negative Werte machen den Klang leiser.

        Scratch-Block: ändere Lautstärke um (-10)

        Parameters
        ----------
        value : Zahl
            Die Änderung der Lautstärke. Die Lautstärke geht von 0 bis 100.
        """
        return self._core.sound_changevolumeby(value)
                
    def schalte_klangeffekte_aus(self):
        """Entfernt alle Klangeffekte (Höhe und Aussteuern) der Figur.

        Scratch-Block: schalte Klangeffekte aus
        """
        return self._core.sound_cleareffects()
                
    def spiele_klang(self, name, loop=0):
        """Startet das Abspielen eines Klangs. Das Skript wartet nicht, bis der Klang zu Ende ist.

        Scratch-Block: spiele Klang (Pop)

        Parameters
        ----------
        name : str oder int
            Der Name der Klangdatei, z. B. "pop.wav", oder die Nummer des Klangs (ab 1).
        loop : int
            Wie oft der Klang nach dem ersten Mal wiederholt wird. 0 spielt ihn einmal, -1 wiederholt ihn immer.
        """
        return self._core.sound_play(name, loop)
                
    def spiele_klang_ganz(self, name):
        """Spielt einen Klang ab und wartet, bis er zu Ende ist.

        Scratch-Block: spiele Klang (Pop) ganz

        Parameters
        ----------
        name : str oder int
            Der Name der Klangdatei, z. B. "pop.wav", oder die Nummer des Klangs (ab 1).
        """
        return self._core.sound_playuntildone(name)
                
    def setze_effekt_aussteuern_links_rechts_auf(self, value):
        """Setzt den Aussteuern-Effekt des Klangs. Der Effekt verschiebt den Klang zwischen linkem und rechtem Lautsprecher.

        Scratch-Block: setze Effekt Aussteuern links/rechts auf (0)

        Parameters
        ----------
        value : Zahl
            Der neue Aussteuern-Effekt. -100 ist ganz links, 0 die Mitte und 100 ganz rechts.
        """
        return self._core.sound_seteffectto_pan(value)
                
    def setze_effekt_höhe_auf(self, value):
        """Setzt den Höhe-Effekt des Klangs. Höhere Werte machen den Klang höher.

        Scratch-Block: setze Effekt Höhe auf (0)

        Parameters
        ----------
        value : Zahl
            Der neue Höhe-Effekt, von -360 bis 360. 0 ist die normale Höhe.
        """
        return self._core.sound_seteffectto_pitch(value)
                
    def setze_lautstärke_auf(self, value):
        """Setzt die Lautstärke der Klänge der Figur. 100 ist am lautesten, 0 ist still.

        Scratch-Block: setze Lautstärke auf (100)%

        Parameters
        ----------
        value : Zahl
            Die neue Lautstärke, von 0 bis 100 Prozent. Werte außerhalb dieses Bereichs werden auf ihn begrenzt.
        """
        return self._core.sound_setvolumeto(value)
                
    def stoppe_alle_klänge(self):
        """Stoppt alle gerade spielenden Klänge, von allen Figuren und der Bühne.

        Scratch-Block: stoppe alle Klänge
        """
        return self._core.sound_stopallsounds()
                
    def lautstärke(self):
        """Gibt die Lautstärke der Klänge der Figur zurück, von 0 bis 100.

        Scratch-Block: (Lautstärke)

        Returns
        -------
        Zahl
            Die aktuelle Lautstärke, von 0 bis 100.
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
