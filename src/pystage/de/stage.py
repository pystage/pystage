
from pystage.core.stage import CoreStage
from pystage.de.sprite import Figur


class Bühne():

    def __init__(self, titel="Welcome to pyStage!"):
        """Erzeugt die Bühne. Der Titel steht in der Titelleiste des Fensters. Meldungen erscheinen auf Deutsch."""
        self._core = CoreStage(titel, language="de")
        self._core.facade = self
        self._core.sprite_facade_class = Figur

    def füge_eine_figur_hinzu(self, costume="default"):
        """Fügt der Bühne eine neue Figur hinzu und gibt sie zurück. Die Figur wird mit dem angegebenen Kostüm gezeigt.

        Der Name der Figur ist "Sprite" beim Standardkostüm, sonst der Name des Kostüms.

        Parameters
        ----------
        costume : str
            Der Name der Bilddatei für das Kostüm der Figur, z. B. "katze.png". "default" ist das Standardkostüm von pystage.

        Returns
        -------
        Figur
            Die neue Figur.
        """
        return self._core.pystage_createsprite(costume=costume)

    def abspielen(self):
        """Startet das Programm. Die Bühne wird gezeigt und alle Skripte laufen, bis das Fenster geschlossen wird.

        Dies wird einmal am Ende des Programms aufgerufen.
        """
        self._core.pystage_play()
        
            
    def erzeuge_klon_von_sprite(self, sprite='_myself_'):
        """Erzeugt einen Klon einer Figur. Ein Klon ist eine Kopie, die an derselben Position mit demselben Kostüm und denselben Variablen startet.

        Es können höchstens 300 Klone gleichzeitig existieren. Weitere Klone werden nicht erzeugt.

        Scratch-Block: erzeuge Klon von (Figur)

        Parameters
        ----------
        sprite : str
            Der Name der Figur, von der ein Klon erzeugt wird. "_myself_" steht für die Figur, in der dieser Block steht.
        """
        return self._core.control_create_clone_of_sprite(sprite)
                
    def stoppe_alles(self):
        """Stoppt alle Skripte aller Figuren und der Bühne, löscht alle Klone und stoppt alle Klänge.

        Scratch-Block: stoppe [alles]
        """
        return self._core.control_stop_all()
                
    def stoppe_andere_skripte_der_bühne(self):
        """Stoppt alle anderen Skripte der Bühne. Das Skript, in dem dieser Block steht, läuft weiter.

        Scratch-Block: stoppe [andere Skripte der Bühne]
        """
        return self._core.control_stop_other()
                
    def stoppe_dieses_skript(self):
        """Stoppt das Skript, in dem dieser Block steht. Die anderen Skripte laufen weiter.

        Scratch-Block: stoppe [dieses Skript]
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
                
    def schalte_grafikeffekte_aus(self):
        """Entfernt alle Grafikeffekte (Farbe, Fischauge, Wirbel, Pixel, Mosaik, Helligkeit und Durchsichtigkeit) der Figur.

        Scratch-Block: schalte Grafikeffekte aus
        """
        return self._core.looks_cleargraphiceffects()
                
    def nächstes_bühnenbild(self):
        """Wechselt zum nächsten Bühnenbild. Nach dem letzten Bühnenbild wird wieder das erste benutzt.

        Scratch-Block: nächstes Bühnenbild
        """
        return self._core.looks_nextbackdrop()
                
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
                
    def wechsle_zu_bühnenbild_und_warte(self, backdrop):
        """Wechselt zu einem anderen Bühnenbild und wartet, bis alle Skripte fertig sind, die mit "Wenn das Bühnenbild wechselt" gestartet wurden.

        Scratch-Block: wechsle zu Bühnenbild (Bühnenbild1) und warte

        Parameters
        ----------
        backdrop : str oder int
            Der Name des Bühnenbilds, seine Nummer (ab 1) oder eines von "nächstes Bühnenbild", "vorheriges Bühnenbild" und "zufälliges Bühnenbild".
        """
        return self._core.looks_switchbackdroptoandwait(backdrop)
                
    def mathematische_funktion(self, operator, number):
        """Berechnet eine mathematische Funktion einer Zahl.

        Scratch-Block: (Betrag) von (-1)

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
                
    def füge_bühnenbild_hinzu(self, name, center_x=None, center_y=None, factor=1):
        """Fügt der Bühne ein Bühnenbild (ein Bild) hinzu. Das Bühnenbild kommt ans Ende der Bühnenbildliste.

        Parameters
        ----------
        name : str
            Der Name der Bilddatei, z. B. "wald.png". Die Datei muss im Projektordner liegen.
        center_x : Zahl
            Die waagerechte Position des Mittelpunkts des Bildes in Pixeln. Ohne Angabe wird die Bildmitte genommen.
        center_y : Zahl
            Die senkrechte Position des Mittelpunkts des Bildes in Pixeln. Ohne Angabe wird die Bildmitte genommen.
        factor : Zahl
            Die Skalierung des Bildes. 1 lässt die Originalgröße.
        """
        return self._core.pystage_addbackdrop(name, center_x, center_y, factor)
                
    def füge_klang_hinzu(self, name):
        """Lädt eine Klangdatei, damit die Figur oder die Bühne sie abspielen kann.

        Klänge werden auch automatisch geladen, wenn sie zum ersten Mal abgespielt werden.

        Parameters
        ----------
        name : str
            Der Name der Klangdatei, z. B. "pop.wav". Die Datei muss im Projektordner liegen.
        """
        return self._core.pystage_addsound(name)
                
    def füge_bühnenbild_ein(self, index, name, center_x=None, center_y=None, factor=1):
        """Fügt ein Bühnenbild (ein Bild) an der angegebenen Stelle in die Bühnenbildliste ein.

        Parameters
        ----------
        index : int
            Die Stelle, an der das Bühnenbild eingefügt wird, ab 1.
        name : str
            Der Name der Bilddatei, z. B. "wald.png".
        center_x : Zahl
            Die waagerechte Position des Mittelpunkts des Bildes in Pixeln. Ohne Angabe wird die Bildmitte genommen.
        center_y : Zahl
            Die senkrechte Position des Mittelpunkts des Bildes in Pixeln. Ohne Angabe wird die Bildmitte genommen.
        factor : Zahl
            Die Skalierung des Bildes. 1 lässt die Originalgröße.
        """
        return self._core.pystage_insertbackdrop(index, name, center_x, center_y, factor)
                
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
                
    def ersetze_bühnenbild(self, index, name, center_x=None, center_y=None, factor=1):
        """Ersetzt ein vorhandenes Bühnenbild durch ein anderes Bild.

        Parameters
        ----------
        index : int
            Die Nummer des Bühnenbilds, das ersetzt wird, ab 1.
        name : str
            Der Name der neuen Bilddatei.
        center_x : Zahl
            Die waagerechte Position des Mittelpunkts des Bildes in Pixeln. Ohne Angabe wird die Bildmitte genommen.
        center_y : Zahl
            Die senkrechte Position des Mittelpunkts des Bildes in Pixeln. Ohne Angabe wird die Bildmitte genommen.
        factor : Zahl
            Die Skalierung des Bildes. 1 lässt die Originalgröße.
        """
        return self._core.pystage_replacebackdrop(index, name, center_x, center_y, factor)
                
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
                
    def datum_im_moment(self):
        """Gibt den aktuellen Tag des Monats zurück, von 1 bis 31.

        Scratch-Block: (Datum im Moment)

        Returns
        -------
        int
            Der aktuelle Tag des Monats.
        """
        return self._core.sensing_current_date()
                
    def wochentag_im_moment(self):
        """Gibt den aktuellen Wochentag als Zahl zurück. 1 ist Sonntag, 2 ist Montag und 7 ist Samstag.

        Scratch-Block: (Wochentag im Moment)

        Returns
        -------
        int
            Der aktuelle Wochentag, von 1 (Sonntag) bis 7 (Samstag).
        """
        return self._core.sensing_current_dayofweek()
                
    def stunde_im_moment(self):
        """Gibt die aktuelle Stunde zurück, von 0 bis 23.

        Scratch-Block: (Stunde im Moment)

        Returns
        -------
        int
            Die aktuelle Stunde.
        """
        return self._core.sensing_current_hour()
                
    def minute_im_moment(self):
        """Gibt die aktuelle Minute zurück, von 0 bis 59.

        Scratch-Block: (Minute im Moment)

        Returns
        -------
        int
            Die aktuelle Minute.
        """
        return self._core.sensing_current_minute()
                
    def monat_im_moment(self):
        """Gibt den aktuellen Monat als Zahl zurück, von 1 (Januar) bis 12 (Dezember).

        Scratch-Block: (Monat im Moment)

        Returns
        -------
        int
            Der aktuelle Monat.
        """
        return self._core.sensing_current_month()
                
    def sekunde_im_moment(self):
        """Gibt die aktuelle Sekunde zurück, von 0 bis 59.

        Scratch-Block: (Sekunde im Moment)

        Returns
        -------
        int
            Die aktuelle Sekunde.
        """
        return self._core.sensing_current_second()
                
    def jahr_im_moment(self):
        """Gibt das aktuelle Jahr zurück.

        Scratch-Block: (Jahr im Moment)

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
                
    def taste_gedrückt(self, key):
        """Prüft, ob im Moment eine Taste gedrückt ist.

        Scratch-Block: Taste (Leertaste) gedrückt?

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

        Scratch-Block: (Lautstärke)

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

        Scratch-Block: (Bühnenbild [Name]) von (Bühne)

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

        Scratch-Block: (Bühnenbild [Nummer]) von (Bühne)

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

        Scratch-Block: (Kostüm [Name]) von (Figur)

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

        Scratch-Block: (Kostüm [Nummer]) von (Figur)

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

        Scratch-Block: (Richtung) von (Figur)

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

        Scratch-Block: (Größe) von (Figur)

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

        Scratch-Block: (Variable) von (Figur)

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

        Scratch-Block: (Lautstärke) von (Figur)

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

        Scratch-Block: (x-Position) von (Figur)

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

        Scratch-Block: (y-Position) von (Figur)

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

        Scratch-Block: setze Ziehbarkeit auf [ziehbar]
        """
        return self._core.sensing_setdragmode_draggable()
                
    def setze_ziehbarkeit_auf_nicht_ziehbar(self):
        """Macht die Figur nicht ziehbar: Der Benutzer kann sie nicht mit der Maus verschieben.

        Scratch-Block: setze Ziehbarkeit auf [nicht ziehbar]
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
        """Prüft, ob der erste Wert größer als der zweite ist. Zahlen werden als Zahlen verglichen, Texte alphabetisch ohne Beachtung von Groß- und Kleinschreibung.

        Scratch-Block: ((a) > (b))

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

        Scratch-Block: ((a) < (b))

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

        Scratch-Block: ((a) = (b))

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
