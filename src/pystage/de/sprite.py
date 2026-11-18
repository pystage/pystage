
from pystage.core.sprite import CoreSprite


class Figur():
    def __init__(self, core_sprite):
        self._core : CoreSprite = core_sprite
        self._core.facade = self


            
    def erzeuge_klon_von_mir(self):
        """Erzeugt einen Klon dieser Figur. Ein Klon ist eine Kopie, die an derselben Position mit demselben Kostüm und denselben Variablen startet.

        Es können höchstens 300 Klone gleichzeitig existieren. Weitere Klone werden nicht erzeugt.

        Scratch-Block: erzeuge Klon von (mir selbst v)
        """
        return self._core.control_create_clone_of_myself()
                
    def erzeuge_klon_von_sprite(self, sprite):
        """Erzeugt einen Klon einer Figur. Ein Klon ist eine Kopie, die an derselben Position mit demselben Kostüm und denselben Variablen startet.

        Es können höchstens 300 Klone gleichzeitig existieren. Weitere Klone werden nicht erzeugt.

        Scratch-Block: erzeuge Klon von (Figur v)

        Parameters
        ----------
        sprite : str
            Der Name der Figur, von der ein Klon erzeugt wird. "_myself_" steht für die Figur, in der dieser Block steht.
        """
        return self._core.control_create_clone_of_sprite(sprite)

    def lösche_diesen_klon(self):
        """Löscht den Klon, in dem dieser Block steht. Eine Figur, die kein Klon ist, wird nicht gelöscht.

        Scratch-Block: lösche diesen Klon
        """
        return self._core.control_delete_this_clone()
                
    def wenn_ich_als_klon_entstehe(self, generator_function, name='', no_refresh=False):
        """Führt den Code jedes Mal aus, wenn ein Klon dieser Figur entsteht.

        Scratch-Block: Wenn ich als Klon entstehe

        Parameters
        ----------
        generator_function : function
            Die Funktion mit dem Code, der ausgeführt werden soll.
        name : str
            Ein Name, um Skripte zu unterscheiden, die dieselbe Funktion verwenden.
        no_refresh : bool
            Wenn True, wird der Code in einem Durchgang ohne Bildschirmaktualisierung ausgeführt.
        """
        return self._core.control_start_as_clone(generator_function, name, no_refresh)
                
    def stoppe_alles(self):
        """Stoppt alle Skripte aller Figuren und der Bühne, löscht alle Klone und stoppt alle Klänge.

        Scratch-Block: stoppe [alles v]
        """
        return self._core.control_stop_all()
                
    def stoppe_andere_skripte_der_figur(self):
        """Stoppt alle anderen Skripte dieser Figur. Das Skript, in dem dieser Block steht, läuft weiter.

        Scratch-Block: stoppe [andere Skripte der Figur v]
        """
        return self._core.control_stop_other()
                
    def stoppe_dieses_skript(self):
        """Stoppt das Skript, in dem dieser Block steht. Die anderen Skripte laufen weiter.

        Scratch-Block: stoppe [dieses Skript v]
        """
        return self._core.control_stop_this()
                
    def warte_sekunden(self, secs):
        """Wartet die angegebene Anzahl Sekunden, bevor das Skript weitermacht. Andere Skripte laufen währenddessen weiter.

        Scratch-Block: warte (1) Sekunden

        Parameters
        ----------
        secs : Zahl
            Die Anzahl Sekunden, die gewartet wird. Negative Werte zählen als 0.
        """
        return self._core.control_wait(secs)
                
    def ändere_variable_um(self, name, value):
        """Ändert den Wert einer Variable um die angegebene Zahl. Die Variable muss eine Zahl enthalten.

        Scratch-Block: ändere (Variable) um (1)

        Parameters
        ----------
        name : str
            Der Name der Variable.
        value : Zahl
            Die Zahl, die addiert wird. Negative Werte machen die Variable kleiner.
        """
        return self._core.data_changevariableby(name, value)
                
    def verstecke_variable(self, name):
        """Versteckt den Monitor einer Variable auf der Bühne.

        Scratch-Block: verstecke Variable (Variable)

        Parameters
        ----------
        name : str
            Der Name der Variable.
        """
        return self._core.data_hidevariable(name)
                
    def setze_variable(self, name, value):
        """Setzt eine Variable auf einen neuen Wert.

        Scratch-Block: setze (Variable) auf (0)

        Parameters
        ----------
        name : str
            Der Name der Variable.
        value : object
            Der neue Wert, eine Zahl oder ein Text.
        """
        return self._core.data_setvariableto(name, value)
                
    def zeige_variable(self, name):
        """Zeigt den Monitor einer Variable auf der Bühne, damit ihr Wert zu sehen ist.

        Scratch-Block: zeige Variable (Variable)

        Parameters
        ----------
        name : str
            Der Name der Variable.
        """
        return self._core.data_showvariable(name)
                
    def gib_variable(self, name):
        """Gibt den Wert einer Variable zurück.

        Scratch-Block: (Variable)

        Parameters
        ----------
        name : str
            Der Name der Variable.

        Returns
        -------
        object
            Der Wert der Variable.
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

        Scratch-Block: Wenn das Bühnenbild zu [Bühnenbild1 v] wechselt

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

        Scratch-Block: Wenn @greenFlag angeklickt wird

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

        Scratch-Block: Wenn [Lautstärke v] > (10)

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

        Scratch-Block: Wenn [Stoppuhr v] > (10)

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

        Scratch-Block: Wenn Taste [Leertaste v] gedrückt wird

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

        Scratch-Block: (Bühnenbild [Name v])

        Returns
        -------
        str
            Der Name des aktuellen Bühnenbilds, oder ein leerer Text, wenn es kein Bühnenbild gibt.
        """
        return self._core.looks_backdropnumbername_name()
                
    def bühnenbild_nummer(self):
        """Gibt die Nummer des aktuellen Bühnenbilds zurück (ab 1).

        Scratch-Block: (Bühnenbild [Nummer v])

        Returns
        -------
        int
            Die Nummer des aktuellen Bühnenbilds.
        """
        return self._core.looks_backdropnumbername_number()
                
    def ändere_effekt_helligkeit_um(self, value):
        """Ändert den Helligkeit-Effekt der Figur um den angegebenen Wert. Negative Werte machen das Kostüm dunkler.

        Scratch-Block: ändere Effekt [Helligkeit v] um (25)

        Parameters
        ----------
        value : Zahl
            Die Änderung des Effekts. Der Effekt geht von -100 (schwarz) bis 100 (weiß).
        """
        return self._core.looks_changeeffectby_brightness(value)
                
    def ändere_effekt_farbe_um(self, value):
        """Ändert den Farbeffekt der Figur um den angegebenen Wert. Der Farbeffekt verändert die Farben des Kostüms.

        Scratch-Block: ändere Effekt [Farbe v] um (25)

        Parameters
        ----------
        value : Zahl
            Die Änderung des Effekts. Der Effekt geht von 0 bis 200 und beginnt nach 200 wieder bei 0.
        """
        return self._core.looks_changeeffectby_color(value)
                
    def ändere_effekt_fischauge_um(self, value):
        """Ändert den Fischauge-Effekt der Figur um den angegebenen Wert. Das Kostüm wird wie durch eine Fischaugenlinse verzerrt.

        Scratch-Block: ändere Effekt [Fischauge v] um (25)

        Parameters
        ----------
        value : Zahl
            Die Änderung des Effekts. 0 bedeutet kein Effekt.
        """
        return self._core.looks_changeeffectby_fisheye(value)
                
    def ändere_effekt_durchsichtigkeit_um(self, value):
        """Ändert den Durchsichtigkeit-Effekt der Figur um den angegebenen Wert. Je höher der Effekt, desto durchsichtiger wird die Figur.

        Scratch-Block: ändere Effekt [Durchsichtigkeit v] um (25)

        Parameters
        ----------
        value : Zahl
            Die Änderung des Effekts. 0 bedeutet sichtbar, 100 bedeutet unsichtbar.
        """
        return self._core.looks_changeeffectby_ghost(value)
                
    def ändere_effekt_mosaik_um(self, value):
        """Ändert den Mosaik-Effekt der Figur um den angegebenen Wert. Das Kostüm wird als kleine Kacheln wiederholt.

        Scratch-Block: ändere Effekt [Mosaik v] um (25)

        Parameters
        ----------
        value : Zahl
            Die Änderung des Effekts. 0 bedeutet kein Effekt.
        """
        return self._core.looks_changeeffectby_mosaic(value)
                
    def ändere_effekt_pixel_um(self, value):
        """Ändert den Pixel-Effekt der Figur um den angegebenen Wert. Das Kostüm sieht dann klotzig aus.

        Scratch-Block: ändere Effekt [Pixel v] um (25)

        Parameters
        ----------
        value : Zahl
            Die Änderung des Effekts. 0 bedeutet kein Effekt.
        """
        return self._core.looks_changeeffectby_pixelate(value)
                
    def ändere_effekt_wirbel_um(self, value):
        """Ändert den Wirbel-Effekt der Figur um den angegebenen Wert. Das Kostüm wird verdreht.

        Scratch-Block: ändere Effekt [Wirbel v] um (25)

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

        Scratch-Block: (Kostüm [Name v])

        Returns
        -------
        str
            Der Name des aktuellen Kostüms, oder ein leerer Text, wenn die Figur kein Kostüm hat.
        """
        return self._core.looks_costumenumbername_name()
                
    def kostüm_nummer(self):
        """Gibt die Nummer des aktuellen Kostüms der Figur zurück (ab 1).

        Scratch-Block: (Kostüm [Nummer v])

        Returns
        -------
        int
            Die Nummer des aktuellen Kostüms.
        """
        return self._core.looks_costumenumbername_number()
                
    def gehe_ebenen_nach_hinten(self, value):
        """Bringt die Figur um die angegebene Anzahl Ebenen nach hinten, also hinter andere Figuren.

        Scratch-Block: gehe (1) Ebenen [nach hinten v]

        Parameters
        ----------
        value : int
            Die Anzahl Ebenen, um die nach hinten gegangen wird.
        """
        return self._core.looks_goforwardbackwardlayers_backward(value)
                
    def gehe_ebenen_nach_vorne(self, value):
        """Bringt die Figur um die angegebene Anzahl Ebenen nach vorne, also vor andere Figuren.

        Scratch-Block: gehe (1) Ebenen [nach vorne v]

        Parameters
        ----------
        value : int
            Die Anzahl Ebenen, um die nach vorne gegangen wird.
        """
        return self._core.looks_goforwardbackwardlayers_forward(value)
                
    def gehe_zu_hinterster_ebene(self):
        """Bringt die Figur hinter alle anderen Figuren.

        Scratch-Block: gehe zu [hinterster v] Ebene
        """
        return self._core.looks_gotofrontback_back()
                
    def gehe_zu_vorderster_ebene(self):
        """Bringt die Figur vor alle anderen Figuren.

        Scratch-Block: gehe zu [vorderster v] Ebene
        """
        return self._core.looks_gotofrontback_front()
                
    def verstecke_dich(self):
        """Versteckt die Figur. Sie wird erst wieder auf der Bühne gezeigt, wenn sie erneut angezeigt wird.

        Scratch-Block: verstecke dich
        """
        return self._core.looks_hide()
                
    def nächstes_bühnenbild(self):
        """Wechselt zum nächsten Bühnenbild. Nach dem letzten Bühnenbild wird wieder das erste benutzt.

        Scratch-Block: wechsle zum nächsten Bühnenbild
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

        Scratch-Block: setze Effekt [Helligkeit v] auf (0)

        Parameters
        ----------
        value : Zahl
            Der neue Wert des Effekts, von -100 (schwarz) bis 100 (weiß). 0 bedeutet kein Effekt.
        """
        return self._core.looks_seteffectto_brightness(value)
                
    def setze_effekt_farbe_auf(self, value):
        """Setzt den Farbeffekt der Figur. Der Farbeffekt verändert die Farben des Kostüms.

        Scratch-Block: setze Effekt [Farbe v] auf (0)

        Parameters
        ----------
        value : Zahl
            Der neue Wert des Effekts, von 0 bis 200. 0 bedeutet kein Effekt.
        """
        return self._core.looks_seteffectto_color(value)
                
    def setze_effekt_fischauge_auf(self, value):
        """Setzt den Fischauge-Effekt der Figur. Das Kostüm wird wie durch eine Fischaugenlinse verzerrt.

        Scratch-Block: setze Effekt [Fischauge v] auf (0)

        Parameters
        ----------
        value : Zahl
            Der neue Wert des Effekts. 0 bedeutet kein Effekt.
        """
        return self._core.looks_seteffectto_fisheye(value)
                
    def setze_effekt_durchsichtigkeit_auf(self, value):
        """Setzt den Durchsichtigkeit-Effekt der Figur. Je höher der Effekt, desto durchsichtiger wird die Figur.

        Scratch-Block: setze Effekt [Durchsichtigkeit v] auf (0)

        Parameters
        ----------
        value : Zahl
            Der neue Wert des Effekts. 0 bedeutet sichtbar, 100 bedeutet unsichtbar.
        """
        return self._core.looks_seteffectto_ghost(value)
                
    def setze_effekt_mosaik_auf(self, value):
        """Setzt den Mosaik-Effekt der Figur. Das Kostüm wird als kleine Kacheln wiederholt.

        Scratch-Block: setze Effekt [Mosaik v] auf (0)

        Parameters
        ----------
        value : Zahl
            Der neue Wert des Effekts. 0 bedeutet kein Effekt.
        """
        return self._core.looks_seteffectto_mosaic(value)
                
    def setze_effekt_pixel_auf(self, value):
        """Setzt den Pixel-Effekt der Figur. Das Kostüm sieht dann klotzig aus.

        Scratch-Block: setze Effekt [Pixel v] auf (0)

        Parameters
        ----------
        value : Zahl
            Der neue Wert des Effekts. 0 bedeutet kein Effekt.
        """
        return self._core.looks_seteffectto_pixelate(value)
                
    def setze_effekt_wirbel_auf(self, value):
        """Setzt den Wirbel-Effekt der Figur. Das Kostüm wird verdreht.

        Scratch-Block: setze Effekt [Wirbel v] auf (0)

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

        Scratch-Block: wechsle zu Bühnenbild (Bühnenbild1 v)

        Parameters
        ----------
        backdrop : str oder int
            Der Name des Bühnenbilds, seine Nummer (ab 1) oder eines von "nächstes Bühnenbild", "vorheriges Bühnenbild" und "zufälliges Bühnenbild".
        """
        return self._core.looks_switchbackdropto_backdrop(backdrop)
                
    def wechsle_zu_zufälligem_bühnenbild(self):
        """Wechselt zu einem zufälligen Bühnenbild.

        Scratch-Block: wechsle zu Bühnenbild (zufälliges Bühnenbild v)
        """
        return self._core.looks_switchbackdropto_random()

    def wechsle_zum_vorherigen_bühnenbild(self):
        """Wechselt zum vorherigen Bühnenbild. Vor dem ersten Bühnenbild wird das letzte benutzt.

        Scratch-Block: wechsle zu Bühnenbild (vorheriges Bühnenbild v)
        """
        return self._core.looks_switchbackdropto_previous()

    def wechsle_zum_nächsten_bühnenbild(self):
        """Wechselt zum nächsten Bühnenbild. Nach dem letzten Bühnenbild wird wieder das erste benutzt.

        Scratch-Block: wechsle zu Bühnenbild (nächstes Bühnenbild v)
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

        Scratch-Block: gleite in (1) Sek. zu (Mauszeiger v)

        Parameters
        ----------
        secs : Zahl
            Die Dauer des Gleitens in Sekunden. 0 bewegt die Figur sofort.
        """
        return self._core.motion_glideto_pointer(secs)
                
    def gleite_in_sek_zu_zufallsposition(self, secs):
        """Lässt die Figur innerhalb der angegebenen Anzahl Sekunden zu einer zufälligen Position gleiten.

        Das Skript wartet, bis das Gleiten beendet ist.

        Scratch-Block: gleite in (1) Sek. zu (Zufallsposition v)

        Parameters
        ----------
        secs : Zahl
            Die Dauer des Gleitens in Sekunden. 0 bewegt die Figur sofort.
        """
        return self._core.motion_glideto_random(secs)
                
    def gleite_in_sek_zu(self, secs, sprite):
        """Lässt die Figur innerhalb der angegebenen Anzahl Sekunden zur Position einer anderen Figur gleiten.

        Das Skript wartet, bis das Gleiten beendet ist.

        Scratch-Block: gleite in (1) Sek. zu (Figur v)

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

        Scratch-Block: gehe zu (Mauszeiger v)
        """
        return self._core.motion_goto_pointer()
                
    def gehe_zu_zufallsposition(self):
        """Bewegt die Figur an eine zufällige Position auf der Bühne.

        Scratch-Block: gehe zu (Zufallsposition v)
        """
        return self._core.motion_goto_random()
                
    def gehe_zu(self, sprite):
        """Bewegt die Figur an die Position einer anderen Figur.

        Scratch-Block: gehe zu (Figur v)

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

        Scratch-Block: drehe dich zu (Mauszeiger v)
        """
        return self._core.motion_pointtowards_pointer()
                
    def drehe_dich_zu(self, sprite):
        """Dreht die Figur zu einer anderen Figur.

        Scratch-Block: drehe dich zu (Figur v)

        Parameters
        ----------
        sprite : str
            Der Name der Figur, zu der gedreht wird. "_mouse_" steht für den Mauszeiger,
            "_random_" für eine zufällige Richtung.
        """
        return self._core.motion_pointtowards_sprite(sprite)
                
    def drehe_dich_zu_zufallsrichtung(self):
        """Dreht die Figur in eine zufällige Richtung.

        Scratch-Block: drehe dich zu (Zufallsrichtung v)

        Returns
        -------
        None
        """
        return self._core.motion_pointtowards_random()

    def setze_drehtyp_auf_rundherum(self):
        """Setzt den Drehtyp auf "rundherum": Das Kostüm dreht sich mit der Richtung der Figur.

        Scratch-Block: setze Drehtyp auf [rundherum v]
        """
        return self._core.motion_setrotationstyle_allaround()
                
    def setze_drehtyp_auf_nicht_drehen(self):
        """Setzt den Drehtyp auf "nicht drehen": Das Kostüm sieht immer gleich aus, egal in welche Richtung die Figur zeigt.

        Scratch-Block: setze Drehtyp auf [nicht drehen v]
        """
        return self._core.motion_setrotationstyle_dontrotate()
                
    def setze_drehtyp_auf_links_rechts(self):
        """Setzt den Drehtyp auf "links-rechts": Das Kostüm dreht sich nur nach links oder rechts und steht nie auf dem Kopf.

        Scratch-Block: setze Drehtyp auf [links-rechts v]
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
        """Berechnet eine mathematische Funktion einer Zahl.

        Scratch-Block: ([Betrag v] von (-1))

        Parameters
        ----------
        operator : str
            Die Funktion: "abs", "floor", "ceiling", "sqrt", "sin", "cos", "tan", "asin", "acos", "atan", "ln", "log", "e ^" oder "10 ^". Sinus, Kosinus und Tangens rechnen mit Grad.
        number : Zahl
            Die Zahl, von der die Funktion berechnet wird.

        Returns
        -------
        Zahl
            Das Ergebnis. Ist es keine Zahl, ist es "Infinity", "-Infinity" oder "NaN".
        """
        return self._core.operator_mathop(operator, number)
                
    def zufallszahl_von_bis(self, start, end):
        """Gibt eine Zufallszahl zwischen zwei Zahlen zurück, die Grenzen eingeschlossen. Sind beide Zahlen ganze Zahlen, ist das Ergebnis auch eine ganze Zahl.

        Scratch-Block: Zufallszahl von (1) bis (10)

        Parameters
        ----------
        start : Zahl
            Die kleinste mögliche Zahl.
        end : Zahl
            Die größte mögliche Zahl. Ist sie kleiner als start, werden beide vertauscht.

        Returns
        -------
        Zahl
            Eine Zufallszahl zwischen start und end.
        """
        return self._core.operator_random(start, end)
                
    def ändere_stift_helligkeit_um(self, value):
        """Ändert die Helligkeit der Stiftfarbe um den angegebenen Wert. 0 ist schwarz, 100 ist am hellsten.

        Scratch-Block: ändere Stift (Helligkeit v) um (10)

        Parameters
        ----------
        value : Zahl
            Die Änderung der Helligkeit, von 0 bis 100.
        """
        return self._core.pen_changePenColorParamBy_brightness(value)
                
    def ändere_stift_farbe_um(self, value):
        """Ändert die Farbe (den Farbton) des Stifts um den angegebenen Wert. Die Farbe geht von 0 bis 100 und beginnt nach 100 wieder bei 0.

        Scratch-Block: ändere Stift (Farbe v) um (10)

        Parameters
        ----------
        value : Zahl
            Die Änderung der Stiftfarbe.
        """
        return self._core.pen_changePenColorParamBy_color(value)
                
    def ändere_stift_sättigung_um(self, value):
        """Ändert die Sättigung der Stiftfarbe um den angegebenen Wert. Eine höhere Sättigung macht die Farbe kräftiger.

        Scratch-Block: ändere Stift (Sättigung v) um (10)

        Parameters
        ----------
        value : Zahl
            Die Änderung der Sättigung, von 0 bis 100.
        """
        return self._core.pen_changePenColorParamBy_saturation(value)
                
    def ändere_stift_transparenz_um(self, value):
        """Ändert die Transparenz der Stiftfarbe um den angegebenen Wert. 0 ist nicht transparent, höhere Werte machen die Linien durchsichtiger.

        Scratch-Block: ändere Stift (Transparenz v) um (10)

        Parameters
        ----------
        value : Zahl
            Die Änderung der Transparenz, von 0 bis 100.
        """
        return self._core.pen_changePenColorParamBy_transparency(value)
                
    def ändere_stiftdicke_um(self, value):
        """Ändert die Dicke des Stifts um den angegebenen Wert. Der Stift ist mindestens 1 dick.

        Scratch-Block: ändere Stiftdicke um (1)

        Parameters
        ----------
        value : Zahl
            Die Änderung der Stiftdicke. Negative Werte machen den Stift dünner.
        """
        return self._core.pen_changePenSizeBy(value)
                
    def lösche_alles(self):
        """Löscht alles, was die Stifte aller Figuren auf der Bühne gezeichnet haben.

        Scratch-Block: lösche alles
        """
        return self._core.pen_clear()
                
    def schalte_stift_ein(self):
        """Setzt den Stift auf die Bühne. Ab jetzt zeichnet die Figur beim Bewegen eine Linie.

        Scratch-Block: schalte Stift ein
        """
        return self._core.pen_penDown()
                
    def schalte_stift_aus(self):
        """Hebt den Stift ab. Die Figur zeichnet beim Bewegen nicht mehr.

        Scratch-Block: schalte Stift aus
        """
        return self._core.pen_penUp()
                
    def setze_stift_helligkeit_auf(self, value):
        """Setzt die Helligkeit der Stiftfarbe. 0 ist schwarz, 100 ist am hellsten.

        Scratch-Block: setze Stift (Helligkeit v) auf (50)

        Parameters
        ----------
        value : Zahl
            Die neue Helligkeit, von 0 bis 100.
        """
        return self._core.pen_setPenColorParamTo_brightness(value)
                
    def setze_stift_farbe_auf(self, value):
        """Setzt die Farbe (den Farbton) des Stifts. Die Farbe geht von 0 bis 100 und beginnt nach 100 wieder bei 0.

        Scratch-Block: setze Stift (Farbe v) auf (50)

        Parameters
        ----------
        value : Zahl
            Die neue Stiftfarbe, von 0 bis 100.
        """
        return self._core.pen_setPenColorParamTo_color(value)
                
    def setze_stift_sättigung_auf(self, value):
        """Setzt die Sättigung der Stiftfarbe. Eine höhere Sättigung macht die Farbe kräftiger.

        Scratch-Block: setze Stift (Sättigung v) auf (50)

        Parameters
        ----------
        value : Zahl
            Die neue Sättigung, von 0 bis 100.
        """
        return self._core.pen_setPenColorParamTo_saturation(value)
                
    def setze_stift_transparenz_auf(self, value):
        """Setzt die Transparenz der Stiftfarbe. 0 ist nicht transparent, höhere Werte machen die Linien durchsichtiger.

        Scratch-Block: setze Stift (Transparenz v) auf (50)

        Parameters
        ----------
        value : Zahl
            Die neue Transparenz, von 0 bis 100.
        """
        return self._core.pen_setPenColorParamTo_transparency(value)
                
    def setze_stiftfarbe_auf(self, color):
        """Setzt die Farbe des Stifts.

        Scratch-Block: setze Stiftfarbe auf [#ff0000]

        Parameters
        ----------
        color : str oder Tupel
            Die Farbe, z. B. "#ff0000" für Rot, oder ein Tupel aus Rot-, Grün- und Blauwert von 0 bis 255.
        """
        return self._core.pen_setPenColorToColor(color)
                
    def setze_stiftdicke_auf(self, value):
        """Setzt die Dicke des Stifts. Der Stift ist mindestens 1 dick.

        Scratch-Block: setze Stiftdicke auf (1)

        Parameters
        ----------
        value : Zahl
            Die neue Stiftdicke.
        """
        return self._core.pen_setPenSizeTo(value)
                
    def hinterlasse_abdruck(self):
        """Stempelt eine Kopie des Kostüms der Figur auf die Bühne. Die Kopie bleibt dort, auch wenn sich die Figur bewegt.

        Scratch-Block: hinterlasse Abdruck
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
        """Erzeugt eine neue Variable. Die Variable kann mit den Variablen-Blöcken verwendet und als Monitor angezeigt werden.

        Parameters
        ----------
        name : str
            Der Name der Variable. Er darf noch nicht existieren.
        value : object
            Der Anfangswert der Variable. Standardmäßig 0.
        all_sprites : bool
            Wenn True, wird die Variable von der Bühne und allen Figuren gemeinsam genutzt. Wenn False, gehört sie nur dieser Figur.
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
        """Setzt die Position des Monitors einer Variable auf der Bühne.

        Parameters
        ----------
        name : str
            Der Name der Variable.
        x : Zahl
            Die waagerechte Position der oberen linken Ecke des Monitors. Die Mitte der Bühne ist 0.
        y : Zahl
            Die senkrechte Position der oberen linken Ecke des Monitors. Die Mitte der Bühne ist 0.
        """
        return self._core.pystage_setmonitorposition(name, x, y)
                
    def setze_monitor_stil_groß(self, name):
        """Zeigt den Monitor einer Variable im großen Stil, mit einer großen Anzeige ihres Werts.

        Parameters
        ----------
        name : str
            Der Name der Variable.
        """
        return self._core.pystage_setmonitorstyle_large(name)
                
    def setze_monitor_stil_normal(self, name):
        """Zeigt den Monitor einer Variable im normalen Stil, mit einer kleinen Anzeige ihres Werts.

        Parameters
        ----------
        name : str
            Der Name der Variable.
        """
        return self._core.pystage_setmonitorstyle_normal(name)
                
    def setze_monitor_stil_regler(self, name, minimum=0, maximum=100, integer=True):
        """Zeigt die Variable als Regler, den man mit der Maus ziehen kann.

        Parameters
        ----------
        name : str
            Der Name der Variable.
        minimum : Zahl
            Der kleinste Wert des Reglers. Wie in Scratch ist der Standardwert 0.
        maximum : Zahl
            Der größte Wert des Reglers. Wie in Scratch ist der Standardwert 100.
        integer : bool
            Wenn True, stellt der Regler nur ganze Zahlen ein, sonst Zahlen mit zwei Nachkommastellen.
        """
        return self._core.pystage_setmonitorstyle_slider(name, minimum, maximum, integer)
                
    def antwort(self):
        """Gibt die letzte Antwort zurück, die der Benutzer bei einem Frage-Block eingegeben hat.

        Scratch-Block: (Antwort)

        Returns
        -------
        str
            Die letzte Antwort. Vor der ersten Frage ist es ein leerer Text.
        """
        return self._core.sensing_answer()
                
    def frage_und_warte(self, question):
        """Zeigt eine Frage auf der Bühne in einem Textfeld und wartet, bis der Benutzer sie beantwortet hat.

        Die Antwort kann mit dem Block Antwort gelesen werden.

        Scratch-Block: frage (Wie heißt du?) und warte

        Parameters
        ----------
        question : str
            Die Frage, die dem Benutzer gezeigt wird.
        """
        return self._core.sensing_askandwait(question)
                
    def farbe_berührt(self, sprite_color, color):
        """Prüft, ob eine Farbe der Figur eine andere Farbe auf der Bühne berührt.

        Scratch-Block: Farbe (Farbe) berührt (Farbe)?

        Parameters
        ----------
        sprite_color : str oder Tupel
            Die Farbe der Figur, z. B. "#ff0000" für Rot, oder ein Tupel aus Rot-, Grün- und Blauwert von 0 bis 255.
        color : str oder Tupel
            Die Farbe auf der Bühne, nach der gesucht wird, im gleichen Format.

        Returns
        -------
        bool
            True, wenn die Farbe der Figur die Farbe berührt, sonst False.
        """
        return self._core.sensing_coloristouchingcolor(sprite_color, color)
                
    def datum_im_moment(self):
        """Gibt den aktuellen Tag des Monats zurück, von 1 bis 31.

        Scratch-Block: ([Datum v] im Moment)

        Returns
        -------
        int
            Der aktuelle Tag des Monats.
        """
        return self._core.sensing_current_date()
                
    def wochentag_im_moment(self):
        """Gibt den aktuellen Wochentag als Zahl zurück. 1 ist Sonntag, 2 ist Montag und 7 ist Samstag.

        Scratch-Block: ([Wochentag v] im Moment)

        Returns
        -------
        int
            Der aktuelle Wochentag, von 1 (Sonntag) bis 7 (Samstag).
        """
        return self._core.sensing_current_dayofweek()
                
    def stunde_im_moment(self):
        """Gibt die aktuelle Stunde zurück, von 0 bis 23.

        Scratch-Block: ([Stunde v] im Moment)

        Returns
        -------
        int
            Die aktuelle Stunde.
        """
        return self._core.sensing_current_hour()
                
    def minute_im_moment(self):
        """Gibt die aktuelle Minute zurück, von 0 bis 59.

        Scratch-Block: ([Minute v] im Moment)

        Returns
        -------
        int
            Die aktuelle Minute.
        """
        return self._core.sensing_current_minute()
                
    def monat_im_moment(self):
        """Gibt den aktuellen Monat als Zahl zurück, von 1 (Januar) bis 12 (Dezember).

        Scratch-Block: ([Monat v] im Moment)

        Returns
        -------
        int
            Der aktuelle Monat.
        """
        return self._core.sensing_current_month()
                
    def sekunde_im_moment(self):
        """Gibt die aktuelle Sekunde zurück, von 0 bis 59.

        Scratch-Block: ([Sekunde v] im Moment)

        Returns
        -------
        int
            Die aktuelle Sekunde.
        """
        return self._core.sensing_current_second()
                
    def jahr_im_moment(self):
        """Gibt das aktuelle Jahr zurück.

        Scratch-Block: ([Jahr v] im Moment)

        Returns
        -------
        int
            Das aktuelle Jahr, z. B. 2026.
        """
        return self._core.sensing_current_year()
                
    def tage_seit(self):
        """Gibt die Anzahl Tage seit dem 1. Januar 2000 (in UTC) zurück, mit dem Bruchteil des aktuellen Tages.

        Scratch-Block: (Tage seit 2000)

        Returns
        -------
        Zahl
            Die Anzahl Tage seit 2000, z. B. 9500,5.
        """
        return self._core.sensing_dayssince2000()
                
    def entfernung_von_mauszeiger(self):
        """Gibt den Abstand zwischen der Figur und dem Mauszeiger in Pixeln zurück.

        Scratch-Block: (Entfernung von (Mauszeiger v))

        Returns
        -------
        Zahl
            Der Abstand in Pixeln.
        """
        return self._core.sensing_distanceto_pointer()
                
    def entfernung_von(self, sprite):
        """Gibt den Abstand zwischen der Figur und einer anderen Figur in Pixeln zurück.

        Scratch-Block: (Entfernung von (Figur v))

        Parameters
        ----------
        sprite : str
            Der Name der Figur. "_mouse_" steht für den Mauszeiger. Gibt es keine solche Figur, wird 10000 zurückgegeben.

        Returns
        -------
        Zahl
            Der Abstand in Pixeln.
        """
        return self._core.sensing_distanceto_sprite(sprite)
                
    def taste_gedrückt(self, key):
        """Prüft, ob im Moment eine Taste gedrückt ist.

        Scratch-Block: Taste (Leertaste v) gedrückt?

        Parameters
        ----------
        key : str
            Die Taste, z. B. "a", "1", "Leertaste", "Pfeil nach links", "Pfeil nach rechts", "Pfeil nach oben", "Pfeil nach unten" oder "beliebiges" (jede Taste). Groß- und Kleinschreibung spielen keine Rolle.

        Returns
        -------
        bool
            True, wenn die Taste gedrückt ist, sonst False.
        """
        return self._core.sensing_keypressed(key)
                
    def lautstärke_mikrofon(self):
        """Gibt die Lautstärke des Mikrofons zurück.

        Dies ist nur ein Platzhalter: Das Mikrofon wird nicht unterstützt, deshalb ist der Wert immer -1.

        Scratch-Block: (Lautstärke::sensing)

        Returns
        -------
        int
            Immer -1.
        """
        return self._core.sensing_loudness()
                
    def maustaste_gedrückt(self):
        """Prüft, ob im Moment eine Maustaste gedrückt ist.

        Scratch-Block: Maustaste gedrückt?

        Returns
        -------
        bool
            True, wenn eine beliebige Maustaste gedrückt ist, sonst False.
        """
        return self._core.sensing_mousedown()
                
    def maus_x_position(self):
        """Gibt die waagerechte Position des Mauszeigers auf der Bühne zurück. Die Mitte der Bühne ist 0.

        Scratch-Block: (Maus x-Position)

        Returns
        -------
        int
            Die x-Position des Mauszeigers. Sie ist auf die Bühne begrenzt.
        """
        return self._core.sensing_mousex()
                
    def maus_y_position(self):
        """Gibt die senkrechte Position des Mauszeigers auf der Bühne zurück. Die Mitte der Bühne ist 0.

        Scratch-Block: (Maus y-Position)

        Returns
        -------
        int
            Die y-Position des Mauszeigers. Sie ist auf die Bühne begrenzt.
        """
        return self._core.sensing_mousey()
                
    def bühnenbildname_von(self, stage='_stage_'):
        """Gibt den Namen des aktuellen Bühnenbilds zurück. Nur die Bühne hat Bühnenbilder.

        Scratch-Block: ([Bühnenbildname v] von (Bühne v))

        Parameters
        ----------
        stage : str
            Der Name der Bühne, standardmäßig "_stage_". Bei einer Figur wird 0 zurückgegeben.

        Returns
        -------
        str
            Der Name des aktuellen Bühnenbilds.
        """
        return self._core.sensing_of_backdropname(stage)
                
    def bühnenbildnummer_von(self, stage='_stage_'):
        """Gibt die Nummer des aktuellen Bühnenbilds zurück (ab 1). Nur die Bühne hat Bühnenbilder.

        Scratch-Block: ([Bühnenbildnummer v] von (Bühne v))

        Parameters
        ----------
        stage : str
            Der Name der Bühne, standardmäßig "_stage_". Bei einer Figur wird 0 zurückgegeben.

        Returns
        -------
        int
            Die Nummer des aktuellen Bühnenbilds.
        """
        return self._core.sensing_of_backdropnumber(stage)
                
    def kostümname_von(self, sprite):
        """Gibt den Namen des aktuellen Kostüms einer anderen Figur zurück.

        Scratch-Block: ([Kostümname v] von (Figur v))

        Parameters
        ----------
        sprite : str
            Der Name der Figur. Gibt es keine solche Figur, wird 0 zurückgegeben.

        Returns
        -------
        str
            Der Name des aktuellen Kostüms.
        """
        return self._core.sensing_of_costumename(sprite)
                
    def kostümnummer_von(self, sprite):
        """Gibt die Nummer des aktuellen Kostüms einer anderen Figur zurück (ab 1).

        Scratch-Block: ([Kostümnummer v] von (Figur v))

        Parameters
        ----------
        sprite : str
            Der Name der Figur. Gibt es keine solche Figur, wird 0 zurückgegeben.

        Returns
        -------
        int
            Die Nummer des aktuellen Kostüms.
        """
        return self._core.sensing_of_costumenumber(sprite)
                
    def richtung_von(self, sprite):
        """Gibt die Richtung einer anderen Figur in Grad zurück. 90 ist rechts, 0 ist oben.

        Scratch-Block: ([Richtung v] von (Figur v))

        Parameters
        ----------
        sprite : str
            Der Name der Figur. Gibt es keine solche Figur, wird 0 zurückgegeben.

        Returns
        -------
        Zahl
            Die Richtung der Figur, zwischen -180 und 180.
        """
        return self._core.sensing_of_direction(sprite)
                
    def größe_von(self, sprite):
        """Gibt die Größe einer anderen Figur in Prozent zurück. 100 ist die normale Größe.

        Scratch-Block: ([Größe v] von (Figur v))

        Parameters
        ----------
        sprite : str
            Der Name der Figur. Gibt es keine solche Figur, wird 0 zurückgegeben.

        Returns
        -------
        Zahl
            Die Größe der Figur in Prozent.
        """
        return self._core.sensing_of_size(sprite)
                
    def gib_variable_von(self, variable, sprite='_stage_'):
        """Gibt den Wert einer Variable einer Figur oder der Bühne zurück.

        Scratch-Block: ([Variable v] von (Figur v))

        Parameters
        ----------
        variable : str
            Der Name der Variable.
        sprite : str
            Der Name der Figur oder "_stage_" für die Bühne. Standardmäßig wird die Bühne genommen.

        Returns
        -------
        object
            Der Wert der Variable. Gibt es die Variable nicht, wird 0 zurückgegeben.
        """
        return self._core.sensing_of_variable(variable, sprite)
                
    def lautstärke_von(self, sprite='_stage_'):
        """Gibt die Lautstärke der Klänge einer Figur oder der Bühne zurück, von 0 bis 100.

        Scratch-Block: ([Lautstärke v] von (Figur v))

        Parameters
        ----------
        sprite : str
            Der Name der Figur oder "_stage_" für die Bühne. Standardmäßig wird die Bühne genommen.

        Returns
        -------
        Zahl
            Die Lautstärke, von 0 bis 100.
        """
        return self._core.sensing_of_volume(sprite)
                
    def x_position_von(self, sprite):
        """Gibt die x-Position einer anderen Figur zurück.

        Scratch-Block: ([x-Position v] von (Figur v))

        Parameters
        ----------
        sprite : str
            Der Name der Figur. Gibt es keine solche Figur, wird 0 zurückgegeben.

        Returns
        -------
        Zahl
            Die x-Position der Figur.
        """
        return self._core.sensing_of_xposition(sprite)
                
    def y_position_von(self, sprite):
        """Gibt die y-Position einer anderen Figur zurück.

        Scratch-Block: ([y-Position v] von (Figur v))

        Parameters
        ----------
        sprite : str
            Der Name der Figur. Gibt es keine solche Figur, wird 0 zurückgegeben.

        Returns
        -------
        Zahl
            Die y-Position der Figur.
        """
        return self._core.sensing_of_yposition(sprite)
                
    def setze_stoppuhr_zurück(self):
        """Setzt die Stoppuhr auf 0 zurück.

        Scratch-Block: setze Stoppuhr zurück
        """
        return self._core.sensing_resettimer()
                
    def setze_ziehbarkeit_auf_ziehbar(self):
        """Macht die Figur ziehbar: Der Benutzer kann sie während des Programms mit der Maus verschieben.

        Scratch-Block: setze Ziehbarkeit auf [ziehbar v]
        """
        return self._core.sensing_setdragmode_draggable()
                
    def setze_ziehbarkeit_auf_nicht_ziehbar(self):
        """Macht die Figur nicht ziehbar: Der Benutzer kann sie nicht mit der Maus verschieben.

        Scratch-Block: setze Ziehbarkeit auf [nicht ziehbar v]
        """
        return self._core.sensing_setdragmode_notdraggable()
                
    def stoppuhr(self):
        """Gibt die Zeit in Sekunden zurück, die seit dem Start des Programms oder seit dem letzten Zurücksetzen der Stoppuhr vergangen ist.

        Scratch-Block: (Stoppuhr)

        Returns
        -------
        Zahl
            Der Stand der Stoppuhr in Sekunden.
        """
        return self._core.sensing_timer()
                
    def wird_farbe_berührt(self, color):
        """Prüft, ob die Figur eine Farbe auf der Bühne berührt.

        Scratch-Block: wird Farbe (Farbe) berührt?

        Parameters
        ----------
        color : str oder Tupel
            Die Farbe, z. B. "#ff0000" für Rot, oder ein Tupel aus Rot-, Grün- und Blauwert von 0 bis 255.

        Returns
        -------
        bool
            True, wenn die Figur die Farbe berührt, sonst False.
        """
        return self._core.sensing_touchingcolor(color)
                
    def wird_rand_berührt(self):
        """Prüft, ob die Figur den Rand der Bühne berührt.

        Scratch-Block: wird (Rand v) berührt?

        Returns
        -------
        bool
            True, wenn die Figur über den Rand der Bühne hinausragt, sonst False.
        """
        return self._core.sensing_touchingobject_edge()
                
    def wird_mauszeiger_berührt(self):
        """Prüft, ob die Figur den Mauszeiger berührt.

        Scratch-Block: wird (Mauszeiger v) berührt?

        Returns
        -------
        bool
            True, wenn die Figur sichtbar ist und der Mauszeiger auf ihr liegt, sonst False.
        """
        return self._core.sensing_touchingobject_pointer()
                
    def wird_berührt(self, sprite):
        """Prüft, ob die Figur eine andere Figur, den Mauszeiger oder den Rand berührt.

        Scratch-Block: wird (Figur v) berührt?

        Parameters
        ----------
        sprite : str
            Der Name der Figur. "_mouse_" steht für den Mauszeiger, "_edge_" für den Rand der Bühne.

        Returns
        -------
        bool
            True, wenn die Figur das Ziel berührt, sonst False.
        """
        return self._core.sensing_touchingobject_sprite(sprite)
                
    def benutzername(self):
        """Gibt den Benutzernamen zurück. pystage kennt den Benutzernamen nicht, deshalb ist das Ergebnis immer ein leerer Text.

        Scratch-Block: (Benutzername)

        Returns
        -------
        str
            Immer ein leerer Text.
        """
        return self._core.sensing_username()
                
    def ändere_effekt_aussteuern_links_rechts_um(self, value):
        """Ändert den Aussteuern-Effekt des Klangs um den angegebenen Wert. Der Effekt verschiebt den Klang zwischen linkem und rechtem Lautsprecher.

        Scratch-Block: ändere Effekt [Aussteuern links/rechts v] um (10)

        Parameters
        ----------
        value : Zahl
            Die Änderung des Aussteuern-Effekts. -100 ist ganz links, 0 die Mitte und 100 ganz rechts.
        """
        return self._core.sound_changeeffectby_pan(value)
                
    def ändere_effekt_höhe_um(self, value):
        """Ändert den Höhe-Effekt des Klangs um den angegebenen Wert. Positive Werte machen den Klang höher.

        Scratch-Block: ändere Effekt [Höhe v] um (10)

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

        Scratch-Block: spiele Klang (Pop v)

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

        Scratch-Block: spiele Klang (Pop v) ganz

        Parameters
        ----------
        name : str oder int
            Der Name der Klangdatei, z. B. "pop.wav", oder die Nummer des Klangs (ab 1).
        """
        return self._core.sound_playuntildone(name)
                
    def setze_effekt_aussteuern_links_rechts_auf(self, value):
        """Setzt den Aussteuern-Effekt des Klangs. Der Effekt verschiebt den Klang zwischen linkem und rechtem Lautsprecher.

        Scratch-Block: setze Effekt [Aussteuern links/rechts v] auf (0)

        Parameters
        ----------
        value : Zahl
            Der neue Aussteuern-Effekt. -100 ist ganz links, 0 die Mitte und 100 ganz rechts.
        """
        return self._core.sound_seteffectto_pan(value)
                
    def setze_effekt_höhe_auf(self, value):
        """Setzt den Höhe-Effekt des Klangs. Höhere Werte machen den Klang höher.

        Scratch-Block: setze Effekt [Höhe v] auf (0)

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
        """Setzt den Namen der Figur. Andere Blöcke können die Figur über diesen Namen ansprechen.

        Parameters
        ----------
        name : str
            Der neue Name der Figur.
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
        """Fügt ein Element am Ende einer Liste hinzu.

        Scratch-Block: füge [Ding] zu [meine Liste v] hinzu

        Parameters
        ----------
        name : str
            Der Name der Liste.
        item
            Das Element, eine Zahl oder ein Text.
        """
        return self._core.data_addtolist(name, item)

    def lösche_element_aus_liste(self, name, index):
        """Löscht ein Element einer Liste.

        Scratch-Block: lösche (1) aus [meine Liste v]

        Parameters
        ----------
        name : str
            Der Name der Liste.
        index : int or str
            Die Position, beginnend mit 1. Auch möglich: "last" und "random". Mit "all" werden alle Elemente gelöscht.
        """
        return self._core.data_deleteoflist(name, index)

    def lösche_alles_aus_liste(self, name):
        """Löscht alle Elemente einer Liste.

        Scratch-Block: lösche alles aus [meine Liste v]

        Parameters
        ----------
        name : str
            Der Name der Liste.
        """
        return self._core.data_deletealloflist(name)

    def füge_in_liste_ein(self, name, item, index):
        """Fügt ein Element an einer Stelle in eine Liste ein.

        Scratch-Block: füge [Ding] bei (1) in [meine Liste v] ein

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
        """Ersetzt ein Element einer Liste durch ein anderes.

        Scratch-Block: ersetze Element (1) von [meine Liste v] durch [Ding]

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
        """Gibt ein Element einer Liste zurück.

        Scratch-Block: (Element (1) von [meine Liste v])

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
        """Gibt die Stelle eines Elements in einer Liste zurück.

        Scratch-Block: (Nummer von [Ding] in [meine Liste v])

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
        """Gibt die Anzahl der Elemente einer Liste zurück.

        Scratch-Block: (Länge von [meine Liste v])

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
        """Prüft, ob eine Liste ein Element enthält.

        Scratch-Block: <[meine Liste v] enthält [Ding]?>

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
        """Zeigt die Liste auf der Bühne an.

        Scratch-Block: zeige Liste [meine Liste v]

        Parameters
        ----------
        name : str
            Der Name der Liste.
        """
        return self._core.data_showlist(name)

    def verstecke_liste(self, name):
        """Versteckt die Liste auf der Bühne.

        Scratch-Block: verstecke Liste [meine Liste v]

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
        """Verbindet zwei Texte zu einem.

        Scratch-Block: (verbinde [Apfel] und [Birne])

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
        """Gibt einen Buchstaben eines Textes zurück.

        Scratch-Block: (Zeichen (1) von [Welt])

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
        """Gibt die Anzahl der Buchstaben eines Textes zurück.

        Scratch-Block: (Länge von [Welt])

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
        """Prüft, ob ein Text einen anderen Text enthält.

        Scratch-Block: <[Apfel] enthält [A]?>

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
        """Prüft, ob der erste Wert größer als der zweite ist. Zahlen werden als Zahlen verglichen, Texte alphabetisch ohne Beachtung von Groß- und Kleinschreibung.

        Scratch-Block: <(a) > (b)>

        Parameters
        ----------
        operand1 : Zahl oder str
            Der erste Wert.
        operand2 : Zahl oder str
            Der zweite Wert.

        Returns
        -------
        bool
            True, wenn operand1 größer als operand2 ist, sonst False.
        """
        return self._core.operator_gt(operand1, operand2)

    def kleiner_als(self, operand1, operand2):
        """Prüft, ob der erste Wert kleiner als der zweite ist. Zahlen werden als Zahlen verglichen, Texte alphabetisch ohne Beachtung von Groß- und Kleinschreibung.

        Scratch-Block: <(a) < (b)>

        Parameters
        ----------
        operand1 : Zahl oder str
            Der erste Wert.
        operand2 : Zahl oder str
            Der zweite Wert.

        Returns
        -------
        bool
            True, wenn operand1 kleiner als operand2 ist, sonst False.
        """
        return self._core.operator_lt(operand1, operand2)

    def gleich(self, operand1, operand2):
        """Prüft, ob zwei Werte gleich sind. Zahlen werden als Zahlen verglichen, Texte ohne Beachtung von Groß- und Kleinschreibung.

        Scratch-Block: <(a) = (b)>

        Parameters
        ----------
        operand1 : Zahl oder str
            Der erste Wert.
        operand2 : Zahl oder str
            Der zweite Wert.

        Returns
        -------
        bool
            True, wenn die Werte gleich sind, sonst False.
        """
        return self._core.operator_equals(operand1, operand2)

    def runde(self, number):
        """Rundet eine Zahl auf die nächste ganze Zahl.

        Scratch-Block: ((3.5) gerundet)

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
        """Teilt a durch b.

        Scratch-Block: ((10) / (2))

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
        """Gibt den Rest der Division von a durch b zurück.

        Scratch-Block: ((10) mod (3))

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
        """Versteckt den Monitor eines Werts.

        Parameters
        ----------
        reporter : str
            Der Wert, z. B. "x-Position", "Größe", "Stoppuhr" oder "Jahr". Dieselben Werte wie bei zeige_monitor sind erlaubt.
        """
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
