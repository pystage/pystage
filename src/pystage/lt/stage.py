
from pystage.core.stage import CoreStage
from pystage.lt.sprite import Veikėjas


class Scena():

    def __init__(self, pavadinimas="Welcome to pyStage!"):
        """Sukuria sceną. Pavadinimas rodomas lango antraštės juostoje. Pranešimai rodomi lietuviškai."""
        self._core = CoreStage(pavadinimas, language="lt")
        self._core.facade = self
        self._core.sprite_facade_class = Veikėjas

    def pridėk_veikėją(self, costume="default"):
        """Prideda scenai naują veikėją ir grąžina jį. Veikėjas rodomas su nurodyta kauke.

        Veikėjo vardas yra "Sprite" su numatytąja kauke, kitu atveju – kaukės vardas.

        Parameters
        ----------
        costume : str
            Kaukės paveikslėlio failo vardas, pvz., "katinas.png". "default" yra numatytoji pystage kaukė.

        Returns
        -------
        Veikėjas
            Naujas veikėjas.
        """
        return self._core.pystage_createsprite(costume=costume)

    def paleisk(self):
        """Paleidžia programą. Scena parodoma ir visi scenarijai veikia, kol langas uždaromas.

        Tai iškviečiama vieną kartą programos pabaigoje.
        """
        self._core.pystage_play()
        
            
    def sukurk_kloną(self, sprite='_myself_'):
        """Sukuria veikėjo kloną. Klonas yra kopija, kuri prasideda toje pačioje vietoje su ta pačia kauke ir tais pačiais kintamaisiais.

        Vienu metu gali egzistuoti ne daugiau kaip 300 klonų. Daugiau klonų nebekuriama.

        Scratch blokas: sukurk (veikėjas v) kloną

        Parameters
        ----------
        sprite : str
            Veikėjo, kurio klonas kuriamas, vardas. "_myself_" reiškia veikėją, kuriame yra šis blokas.
        """
        return self._core.control_create_clone_of_sprite(sprite)
                
    def sustok_visiškai(self):
        """Sustabdo visus visų veikėjų ir scenos scenarijus, ištrina visus klonus ir sustabdo visus garsus.

        Scratch blokas: sustok [visiškai v]
        """
        return self._core.control_stop_all()
                
    def sustok_kitus_scenos_scenarijus(self):
        """Sustabdo visus kitus scenos scenarijus. Scenarijus, kuriame yra šis blokas, veikia toliau.

        Scratch blokas: sustok [kitus scenos scenarijus v]
        """
        return self._core.control_stop_other()
                
    def sustok_šį_scenarijų(self):
        """Sustabdo scenarijų, kuriame yra šis blokas. Kiti scenarijai veikia toliau.

        Scratch blokas: sustok [šį scenarijų v]
        """
        return self._core.control_stop_this()
                
    def palauk_sek(self, secs):
        """Palaukia nurodytą sekundžių skaičių, prieš scenarijui tęsiant darbą. Kiti scenarijai tuo metu veikia toliau.

        Scratch blokas: palauk (1) sek.

        Parameters
        ----------
        secs : skaičius
            Sekundžių, kurias reikia laukti, skaičius. Neigiamos reikšmės laikomos 0.
        """
        return self._core.control_wait(secs)
                
    def padidink_kintamąjį(self, name, value):
        """Pakeičia kintamojo reikšmę nurodytu skaičiumi. Kintamajame turi būti skaičius.

        Scratch blokas: (kintamasis) padidink (1)

        Parameters
        ----------
        name : str
            Kintamojo vardas.
        value : skaičius
            Pridedamas skaičius. Neigiamos reikšmės kintamąjį sumažina.
        """
        return self._core.data_changevariableby(name, value)
                
    def slėpk_kintamąjį(self, name):
        """Paslepia kintamojo monitorių scenoje.

        Scratch blokas: slėpk (kintamasis)

        Parameters
        ----------
        name : str
            Kintamojo vardas.
        """
        return self._core.data_hidevariable(name)
                
    def nustatyk_kintamąjį_į(self, name, value):
        """Nustato naują kintamojo reikšmę.

        Scratch blokas: (kintamasis) = (0)

        Parameters
        ----------
        name : str
            Kintamojo vardas.
        value : object
            Nauja reikšmė, skaičius arba tekstas.
        """
        return self._core.data_setvariableto(name, value)
                
    def rodyk_kintamąjį(self, name):
        """Parodo kintamojo monitorių scenoje, kad matytųsi jo reikšmė.

        Scratch blokas: rodyk (kintamasis)

        Parameters
        ----------
        name : str
            Kintamojo vardas.
        """
        return self._core.data_showvariable(name)
                
    def kintamasis(self, name):
        """Grąžina kintamojo reikšmę.

        Scratch blokas: (kintamasis)

        Parameters
        ----------
        name : str
            Kintamojo vardas.

        Returns
        -------
        object
            Kintamojo reikšmė.
        """
        return self._core.data_variable(name)
                
    def skelbti(self, message):
        """Išsiunčia žinutę visiems veikėjams ir scenai. Kiekvienas blokas "kai gausi žinutę ..." su šia žinute pradeda veikti. Scenarijus jų nelaukia.

        Scratch blokas: skelbti (žinutė1)

        Parameters
        ----------
        message : str
            Žinutės pavadinimas. Didžiosios ir mažosios raidės nesvarbios.
        """
        return self._core.event_broadcast(message)
                
    def skelbti_ir_palaukti(self, message):
        """Išsiunčia žinutę visiems veikėjams ir scenai ir laukia, kol baigs darbą visi ją gaunantys scenarijai.

        Scratch blokas: skelbti (žinutė1) ir palaukti

        Parameters
        ----------
        message : str
            Žinutės pavadinimas. Didžiosios ir mažosios raidės nesvarbios.
        """
        return self._core.event_broadcastandwait(message)
                
    def kai_fonas_perjungiamas_į(self, backdrop, generator_function, name='', no_refresh=False):
        """Vykdo kodą, kai scena persijungia į nurodytą foną.

        Scratch blokas: kai fonas perjungiamas į [fonas1 v]

        Parameters
        ----------
        backdrop : str
            Fono pavadinimas. Didžiosios ir mažosios raidės nesvarbios.
        generator_function : function
            Funkcija su kodu, kuris turi būti vykdomas.
        name : str
            Vardas, kuriuo skiriami scenarijai, naudojantys tą pačią funkciją.
        no_refresh : bool
            Jei True, kodas vykdomas vienu prasukimu be ekrano atnaujinimo.
        """
        return self._core.event_whenbackdropswitchesto(backdrop, generator_function, name, no_refresh)
                
    def kai_gausi_žinutę(self, message, generator_function, name='', no_refresh=False):
        """Vykdo kodą, kai išsiunčiama nurodyta žinutė.

        Scratch blokas: kai gausi žinutę (žinutė1)

        Parameters
        ----------
        message : str
            Žinutės pavadinimas. Didžiosios ir mažosios raidės nesvarbios.
        generator_function : function
            Funkcija su kodu, kuris turi būti vykdomas.
        name : str
            Vardas, kuriuo skiriami scenarijai, naudojantys tą pačią funkciją.
        no_refresh : bool
            Jei True, kodas vykdomas vienu prasukimu be ekrano atnaujinimo.
        """
        return self._core.event_whenbroadcastreceived(message, generator_function, name, no_refresh)
                
    def kai_spusteli_žalią_vėliavėlę(self, generator_function, name='', no_refresh=False):
        """Vykdo kodą, kai spustelėjama žalia vėliavėlė, t. y. kai programa startuoja.

        Scratch blokas: kai spusteli @greenFlag

        Parameters
        ----------
        generator_function : function
            Funkcija su kodu, kuris turi būti vykdomas.
        name : str
            Vardas, kuriuo skiriami scenarijai, naudojantys tą pačią funkciją.
        no_refresh : bool
            Jei True, kodas vykdomas vienu prasukimu be ekrano atnaujinimo.
        """
        return self._core.event_whenflagclicked(generator_function, name, no_refresh)
                
    def kai_garsumas_didesnis_už(self, value, generator_function, name='', no_refresh=False):
        """Vykdo kodą, kai mikrofono garsumas yra didesnis už nurodytą reikšmę.

        Tai tik vietos rezervavimo blokas: mikrofonas nepalaikomas, garsumas visada yra -1, o kodas niekada nevykdomas.

        Scratch blokas: kai [garsumas v] > (10)

        Parameters
        ----------
        value : skaičius
            Garsumo reikšmė, kurią reikia viršyti.
        generator_function : function
            Funkcija su kodu, kuris turi būti vykdomas.
        name : str
            Vardas, kuriuo skiriami scenarijai, naudojantys tą pačią funkciją.
        no_refresh : bool
            Jei True, kodas vykdomas vienu prasukimu be ekrano atnaujinimo.
        """
        return self._core.event_whengreaterthan_loudness(value, generator_function, name, no_refresh)
                
    def kai_laikmatis_didesnis_už(self, value, generator_function, name='', no_refresh=False):
        """Vykdo kodą, kai laikmatis rodo daugiau nei nurodyta reikšmė.

        Kodas vykdomas po vieną kartą, kai laikmatis viršija reikšmę. Jis vėl vykdomas, kai laikmatis nustatomas iš naujo.

        Scratch blokas: kai [laikmatis v] > (10)

        Parameters
        ----------
        value : skaičius
            Sekundžių skaičius, kurį laikmatis turi viršyti.
        generator_function : function
            Funkcija su kodu, kuris turi būti vykdomas.
        name : str
            Vardas, kuriuo skiriami scenarijai, naudojantys tą pačią funkciją.
        no_refresh : bool
            Jei True, kodas vykdomas vienu prasukimu be ekrano atnaujinimo.
        """
        return self._core.event_whengreaterthan_timer(value, generator_function, name, no_refresh)
                
    def kai_paspaudi_klavišą(self, key, generator_function, name='', no_refresh=False):
        """Vykdo kodą, kai paspaudžiamas klavišas.

        Scratch blokas: kai paspaudi [tarpą v]

        Parameters
        ----------
        key : str
            Klavišas, pvz., "a", "1", "tarpas", "rodyklė kairėn", "rodyklė dešinėn", "rodyklė aukštyn", "rodyklė žemyn" arba "bet kuris" (bet kuris klavišas). Didžiosios ir mažosios raidės nesvarbios.
        generator_function : function
            Funkcija su kodu, kuris turi būti vykdomas.
        name : str
            Vardas, kuriuo skiriami scenarijai, naudojantys tą pačią funkciją.
        no_refresh : bool
            Jei True, kodas vykdomas vienu prasukimu be ekrano atnaujinimo.
        """
        return self._core.event_whenkeypressed(key, generator_function, name, no_refresh)
                
    def kai_spusteli_ant_šio_veikėjo(self, generator_function, name='', no_refresh=False):
        """Vykdo kodą, kai pele spustelima ant veikėjo.

        Scratch blokas: kai spusteli ant šio veikėjo

        Parameters
        ----------
        generator_function : function
            Funkcija su kodu, kuris turi būti vykdomas.
        name : str
            Vardas, kuriuo skiriami scenarijai, naudojantys tą pačią funkciją.
        no_refresh : bool
            Jei True, kodas vykdomas vienu prasukimu be ekrano atnaujinimo.
        """
        return self._core.event_whenthisspriteclicked(generator_function, name, no_refresh)
                
    def fonas_vardas(self):
        """Grąžina dabartinio fono pavadinimą.

        Scratch blokas: (fonas [vardas v])

        Returns
        -------
        str
            Dabartinio fono pavadinimas arba tuščias tekstas, jei fono nėra.
        """
        return self._core.looks_backdropnumbername_name()
                
    def fonas_numeris(self):
        """Grąžina dabartinio fono numerį (nuo 1).

        Scratch blokas: (fonas [numeris v])

        Returns
        -------
        int
            Dabartinio fono numeris.
        """
        return self._core.looks_backdropnumbername_number()
                
    def efektą_šviesumas_padidink(self, value):
        """Pakeičia veikėjo šviesumo efektą nurodyta reikšme. Neigiamos reikšmės kaukę padaro tamsesnę.

        Scratch blokas: efektą [šviesumas v] padidink (25)

        Parameters
        ----------
        value : skaičius
            Efekto pokytis. Efektas kinta nuo -100 (juoda) iki 100 (balta).
        """
        return self._core.looks_changeeffectby_brightness(value)
                
    def efektą_spalva_padidink(self, value):
        """Pakeičia veikėjo spalvos efektą nurodyta reikšme. Spalvos efektas keičia kaukės spalvas.

        Scratch blokas: efektą [spalva v] padidink (25)

        Parameters
        ----------
        value : skaičius
            Efekto pokytis. Efektas kinta nuo 0 iki 200, o perkopus 200 vėl prasideda nuo 0.
        """
        return self._core.looks_changeeffectby_color(value)
                
    def efektą_lęšis_padidink(self, value):
        """Pakeičia veikėjo lęšio efektą nurodyta reikšme. Kaukė iškreipiama tarsi per žuvies akies lęšį.

        Scratch blokas: efektą [lęšis v] padidink (25)

        Parameters
        ----------
        value : skaičius
            Efekto pokytis. 0 reiškia, kad efekto nėra.
        """
        return self._core.looks_changeeffectby_fisheye(value)
                
    def efektą_permatomumas_padidink(self, value):
        """Pakeičia veikėjo permatomumo efektą nurodyta reikšme. Kuo didesnis efektas, tuo permatomesnis veikėjas.

        Scratch blokas: efektą [permatomumas v] padidink (25)

        Parameters
        ----------
        value : skaičius
            Efekto pokytis. 0 reiškia matomas, 100 reiškia nematomas.
        """
        return self._core.looks_changeeffectby_ghost(value)
                
    def efektą_mozaika_padidink(self, value):
        """Pakeičia veikėjo mozaikos efektą nurodyta reikšme. Kaukė pakartojama kaip mažos plytelės.

        Scratch blokas: efektą [mozaika v] padidink (25)

        Parameters
        ----------
        value : skaičius
            Efekto pokytis. 0 reiškia, kad efekto nėra.
        """
        return self._core.looks_changeeffectby_mosaic(value)
                
    def efektą_stambinti_taškus_padidink(self, value):
        """Pakeičia veikėjo stambinimo taškais efektą nurodyta reikšme. Kaukė atrodo kampuota.

        Scratch blokas: efektą [stambinti taškus v] padidink (25)

        Parameters
        ----------
        value : skaičius
            Efekto pokytis. 0 reiškia, kad efekto nėra.
        """
        return self._core.looks_changeeffectby_pixelate(value)
                
    def efektą_susukimas_padidink(self, value):
        """Pakeičia veikėjo susukimo efektą nurodyta reikšme. Kaukė susukama.

        Scratch blokas: efektą [susukimas v] padidink (25)

        Parameters
        ----------
        value : skaičius
            Efekto pokytis. 0 reiškia, kad efekto nėra.
        """
        return self._core.looks_changeeffectby_whirl(value)
                
    def panaikink_išvaizdos_efektus(self):
        """Pašalina visus veikėjo išvaizdos efektus (spalvą, lęšį, susukimą, stambinimą taškais, mozaiką, šviesumą ir permatomumą).

        Scratch blokas: panaikink išvaizdos efektus
        """
        return self._core.looks_cleargraphiceffects()
                
    def kitas_fonas(self):
        """Persijungia į kitą foną. Po paskutinio fono vėl naudojamas pirmasis.

        Scratch blokas: kitas fonas
        """
        return self._core.looks_nextbackdrop()
                
    def nustatyk_efektą_šviesumas_į(self, value):
        """Nustato veikėjo šviesumo efektą. Neigiamos reikšmės kaukę padaro tamsesnę.

        Scratch blokas: efektas [šviesumas v] = (0)

        Parameters
        ----------
        value : skaičius
            Nauja efekto reikšmė, nuo -100 (juoda) iki 100 (balta). 0 reiškia, kad efekto nėra.
        """
        return self._core.looks_seteffectto_brightness(value)
                
    def nustatyk_efektą_spalva_į(self, value):
        """Nustato veikėjo spalvos efektą. Spalvos efektas keičia kaukės spalvas.

        Scratch blokas: efektas [spalva v] = (0)

        Parameters
        ----------
        value : skaičius
            Nauja efekto reikšmė, nuo 0 iki 200. 0 reiškia, kad efekto nėra.
        """
        return self._core.looks_seteffectto_color(value)
                
    def nustatyk_efektą_lęšis_į(self, value):
        """Nustato veikėjo lęšio efektą. Kaukė iškreipiama tarsi per žuvies akies lęšį.

        Scratch blokas: efektas [lęšis v] = (0)

        Parameters
        ----------
        value : skaičius
            Nauja efekto reikšmė. 0 reiškia, kad efekto nėra.
        """
        return self._core.looks_seteffectto_fisheye(value)
                
    def nustatyk_efektą_permatomumas_į(self, value):
        """Nustato veikėjo permatomumo efektą. Kuo didesnis efektas, tuo permatomesnis veikėjas.

        Scratch blokas: efektas [permatomumas v] = (0)

        Parameters
        ----------
        value : skaičius
            Nauja efekto reikšmė. 0 reiškia matomas, 100 reiškia nematomas.
        """
        return self._core.looks_seteffectto_ghost(value)
                
    def nustatyk_efektą_mozaika_į(self, value):
        """Nustato veikėjo mozaikos efektą. Kaukė pakartojama kaip mažos plytelės.

        Scratch blokas: efektas [mozaika v] = (0)

        Parameters
        ----------
        value : skaičius
            Nauja efekto reikšmė. 0 reiškia, kad efekto nėra.
        """
        return self._core.looks_seteffectto_mosaic(value)
                
    def nustatyk_efektą_stambinti_taškus_į(self, value):
        """Nustato veikėjo stambinimo taškais efektą. Kaukė atrodo kampuota.

        Scratch blokas: efektas [stambinti taškus v] = (0)

        Parameters
        ----------
        value : skaičius
            Nauja efekto reikšmė. 0 reiškia, kad efekto nėra.
        """
        return self._core.looks_seteffectto_pixelate(value)
                
    def nustatyk_efektą_susukimas_į(self, value):
        """Nustato veikėjo susukimo efektą. Kaukė susukama.

        Scratch blokas: efektas [susukimas v] = (0)

        Parameters
        ----------
        value : skaičius
            Nauja efekto reikšmė. 0 reiškia, kad efekto nėra.
        """
        return self._core.looks_seteffectto_whirl(value)
                
    def nustatyk_foną_į(self, backdrop):
        """Persijungia į kitą foną.

        Scratch blokas: fonas = (fonas1 v)

        Parameters
        ----------
        backdrop : str arba int
            Fono pavadinimas, jo numeris (nuo 1) arba vienas iš "kitas fonas", "ankstesnis fonas" ir "atsitiktinis fonas".
        """
        return self._core.looks_switchbackdropto_backdrop(backdrop)
                
    def nustatyk_atsitiktinį_foną(self):
        """Persijungia į atsitiktinį foną.

        Scratch blokas: fonas = (atsitiktinis fonas v)
        """
        return self._core.looks_switchbackdropto_random()

    def nustatyk_ankstesnį_foną(self):
        """Persijungia į ankstesnį foną. Prieš pirmąjį foną naudojamas paskutinis.

        Scratch blokas: fonas = (ankstesnis fonas v)
        """
        return self._core.looks_switchbackdropto_previous()

    def nustatyk_kitą_foną(self):
        """Persijungia į kitą foną. Po paskutinio fono vėl naudojamas pirmasis.

        Scratch blokas: fonas = (kitas fonas v)
        """
        return self._core.looks_switchbackdropto_next()
                
    def nustatyk_foną_į_ir_palauk(self, backdrop):
        """Persijungia į kitą foną ir laukia, kol baigs darbą visi scenarijai, paleisti bloku "kai fonas perjungiamas".

        Scratch blokas: fonas = (fonas1) \\(palauk, kol pasikeis\\)

        Parameters
        ----------
        backdrop : str arba int
            Fono pavadinimas, jo numeris (nuo 1) arba vienas iš "kitas fonas", "ankstesnis fonas" ir "atsitiktinis fonas".
        """
        return self._core.looks_switchbackdroptoandwait(backdrop)
                
    def matematinė_funkcija(self, operator, number):
        """Apskaičiuoja skaičiaus matematinę funkciją.

        Scratch blokas: ([teigiama reikšmė v] \\( (-1) \\))

        Parameters
        ----------
        operator : str
            Funkcija: "abs", "floor", "ceiling", "sqrt", "sin", "cos", "tan", "asin", "acos", "atan", "ln", "log", "e ^" arba "10 ^". Sinusas, kosinusas ir tangentas skaičiuoja laipsniais.
        number : skaičius
            Skaičius, kurio funkcija skaičiuojama.

        Returns
        -------
        skaičius
            Rezultatas. Jei tai ne skaičius, jis yra "Infinity", "-Infinity" arba "NaN".
        """
        return self._core.operator_mathop(operator, number)
                
    def atsitiktinis_skaičius_tarp(self, start, end):
        """Grąžina atsitiktinį skaičių tarp dviejų skaičių, ribos įskaitytos. Jei abu skaičiai yra sveikieji, rezultatas taip pat yra sveikasis skaičius.

        Scratch blokas: atsitiktinis sk. tarp (1) ir (10)

        Parameters
        ----------
        start : skaičius
            Mažiausias galimas skaičius.
        end : skaičius
            Didžiausias galimas skaičius. Jei jis mažesnis už start, abu sukeičiami vietomis.

        Returns
        -------
        skaičius
            Atsitiktinis skaičius tarp start ir end.
        """
        return self._core.operator_random(start, end)
                
    def pridėk_foną(self, name, center_x=None, center_y=None, factor=1):
        """Prideda scenai foną (paveikslėlį). Fonas atsiduria fonų sąrašo gale.

        Parameters
        ----------
        name : str
            Paveikslėlio failo vardas, pvz., "miškas.png". Failas turi būti projekto aplanke.
        center_x : skaičius
            Paveikslėlio centro horizontali vieta taškais. Jei nenurodyta, imamas paveikslėlio vidurys.
        center_y : skaičius
            Paveikslėlio centro vertikali vieta taškais. Jei nenurodyta, imamas paveikslėlio vidurys.
        factor : skaičius
            Paveikslėlio mastelis. 1 palieka originalų dydį.
        """
        return self._core.pystage_addbackdrop(name, center_x, center_y, factor)
                
    def pridėk_garsą(self, name):
        """Įkelia garso failą, kad veikėjas arba scena galėtų jį groti.

        Garsai taip pat įkeliami automatiškai, kai grojami pirmą kartą.

        Parameters
        ----------
        name : str
            Garso failo vardas, pvz., "pop.wav". Failas turi būti projekto aplanke.
        """
        return self._core.pystage_addsound(name)
                
    def įterpk_foną(self, index, name, center_x=None, center_y=None, factor=1):
        """Įterpia foną (paveikslėlį) nurodytoje vietoje į fonų sąrašą.

        Parameters
        ----------
        index : int
            Vieta, kurioje įterpiamas fonas, nuo 1.
        name : str
            Paveikslėlio failo vardas, pvz., "miškas.png".
        center_x : skaičius
            Paveikslėlio centro horizontali vieta taškais. Jei nenurodyta, imamas paveikslėlio vidurys.
        center_y : skaičius
            Paveikslėlio centro vertikali vieta taškais. Jei nenurodyta, imamas paveikslėlio vidurys.
        factor : skaičius
            Paveikslėlio mastelis. 1 palieka originalų dydį.
        """
        return self._core.pystage_insertbackdrop(index, name, center_x, center_y, factor)
                
    def sukurk_kintamąjį(self, name, value=0, all_sprites=True):
        """Sukuria naują kintamąjį. Kintamąjį galima naudoti su kintamųjų blokais ir rodyti kaip monitorių.

        Parameters
        ----------
        name : str
            Kintamojo vardas. Toks kintamasis dar neturi egzistuoti.
        value : object
            Pradinė kintamojo reikšmė. Pagal numatytąją reikšmę 0.
        all_sprites : bool
            Jei True, kintamąjį bendrai naudoja scena ir visi veikėjai. Jei False, jis priklauso tik šiam veikėjui.
        """
        return self._core.pystage_makevariable(name, value, all_sprites)
                
    def pakeisk_foną(self, index, name, center_x=None, center_y=None, factor=1):
        """Pakeičia esamą foną kitu paveikslėliu.

        Parameters
        ----------
        index : int
            Keičiamo fono numeris, nuo 1.
        name : str
            Naujo paveikslėlio failo vardas.
        center_x : skaičius
            Paveikslėlio centro horizontali vieta taškais. Jei nenurodyta, imamas paveikslėlio vidurys.
        center_y : skaičius
            Paveikslėlio centro vertikali vieta taškais. Jei nenurodyta, imamas paveikslėlio vidurys.
        factor : skaičius
            Paveikslėlio mastelis. 1 palieka originalų dydį.
        """
        return self._core.pystage_replacebackdrop(index, name, center_x, center_y, factor)
                
    def nustatyk_monitoriaus_poziciją(self, name, x, y):
        """Nustato kintamojo monitoriaus vietą scenoje.

        Parameters
        ----------
        name : str
            Kintamojo vardas.
        x : skaičius
            Horizontali viršutinio kairiojo monitoriaus kampo vieta. Scenos vidurys yra 0.
        y : skaičius
            Vertikali viršutinio kairiojo monitoriaus kampo vieta. Scenos vidurys yra 0.
        """
        return self._core.pystage_setmonitorposition(name, x, y)
                
    def nustatyk_monitoriaus_stilių_didesnis(self, name):
        """Rodo kintamojo monitorių dideliu stiliumi, su dideliu reikšmės rodmeniu.

        Parameters
        ----------
        name : str
            Kintamojo vardas.
        """
        return self._core.pystage_setmonitorstyle_large(name)
                
    def nustatyk_monitoriaus_stilių_įprastas(self, name):
        """Rodo kintamojo monitorių įprastu stiliumi, su mažu reikšmės rodmeniu.

        Parameters
        ----------
        name : str
            Kintamojo vardas.
        """
        return self._core.pystage_setmonitorstyle_normal(name)
                
    def nustatyk_monitoriaus_stilių_slinktis(self, name, minimum=0, maximum=100, integer=True):
        """Rodo kintamąjį kaip slinktį, kurią galima tempti pele.

        Parameters
        ----------
        name : str
            Kintamojo vardas.
        minimum : skaičius
            Mažiausia slinkties reikšmė. Kaip Scratch, numatytoji reikšmė yra 0.
        maximum : skaičius
            Didžiausia slinkties reikšmė. Kaip Scratch, numatytoji reikšmė yra 100.
        integer : bool
            Jei True, slinktis nustato tik sveikuosius skaičius, kitaip skaičius su dviem skaitmenimis po kablelio.
        """
        return self._core.pystage_setmonitorstyle_slider(name, minimum, maximum, integer)
                
    def atsakas(self):
        """Grąžina paskutinį atsakymą, kurį naudotojas įvedė klausimo bloke.

        Scratch blokas: (atsakas)

        Returns
        -------
        str
            Paskutinis atsakymas. Prieš pirmąjį klausimą tai yra tuščias tekstas.
        """
        return self._core.sensing_answer()
                
    def paklausk_ir_lauk(self, question):
        """Parodo klausimą scenoje teksto lauke ir laukia, kol naudotojas atsakys.

        Atsakymą galima perskaityti bloku atsakas.

        Scratch blokas: paklausk (Koks tavo vardas?) ir lauk

        Parameters
        ----------
        question : str
            Klausimas, kuris rodomas naudotojui.
        """
        return self._core.sensing_askandwait(question)
                
    def šio_momento_mėn_diena(self):
        """Grąžina dabartinę mėnesio dieną, nuo 1 iki 31.

        Scratch blokas: (šio momento [mėn. diena v])

        Returns
        -------
        int
            Dabartinė mėnesio diena.
        """
        return self._core.sensing_current_date()
                
    def šio_momento_savaitės_diena(self):
        """Grąžina dabartinę savaitės dieną skaičiumi. 1 yra sekmadienis, 2 yra pirmadienis, o 7 yra šeštadienis.

        Scratch blokas: (šio momento [savaitės diena v])

        Returns
        -------
        int
            Dabartinė savaitės diena, nuo 1 (sekmadienis) iki 7 (šeštadienis).
        """
        return self._core.sensing_current_dayofweek()
                
    def šio_momento_valanda(self):
        """Grąžina dabartinę valandą, nuo 0 iki 23.

        Scratch blokas: (šio momento [valanda v])

        Returns
        -------
        int
            Dabartinė valanda.
        """
        return self._core.sensing_current_hour()
                
    def šio_momento_minutė(self):
        """Grąžina dabartinę minutę, nuo 0 iki 59.

        Scratch blokas: (šio momento [minutė v])

        Returns
        -------
        int
            Dabartinė minutė.
        """
        return self._core.sensing_current_minute()
                
    def šio_momento_mėnuo(self):
        """Grąžina dabartinį mėnesį skaičiumi, nuo 1 (sausis) iki 12 (gruodis).

        Scratch blokas: (šio momento [mėnuo v])

        Returns
        -------
        int
            Dabartinis mėnuo.
        """
        return self._core.sensing_current_month()
                
    def šio_momento_sekundė(self):
        """Grąžina dabartinę sekundę, nuo 0 iki 59.

        Scratch blokas: (šio momento [sekundė v])

        Returns
        -------
        int
            Dabartinė sekundė.
        """
        return self._core.sensing_current_second()
                
    def šio_momento_metai(self):
        """Grąžina dabartinius metus.

        Scratch blokas: (šio momento [metai v])

        Returns
        -------
        int
            Dabartiniai metai, pvz., 2026.
        """
        return self._core.sensing_current_year()
                
    def dienų_skaičius_nuo_2000(self):
        """Grąžina dienų skaičių nuo 2000 m. sausio 1 d. (pagal UTC) su dabartinės dienos trupmena.

        Scratch blokas: (dienų skaičius nuo 2000-ųjų)

        Returns
        -------
        skaičius
            Dienų skaičius nuo 2000-ųjų, pvz., 9500,5.
        """
        return self._core.sensing_dayssince2000()
                
    def klavišas_paspaustas(self, key):
        """Patikrina, ar šiuo metu paspaustas klavišas.

        Scratch blokas: (tarpas v) paspausta?

        Parameters
        ----------
        key : str
            Klavišas, pvz., "a", "1", "tarpas", "rodyklė kairėn", "rodyklė dešinėn", "rodyklė aukštyn", "rodyklė žemyn" arba "bet kuris" (bet kuris klavišas). Didžiosios ir mažosios raidės nesvarbios.

        Returns
        -------
        bool
            True, jei klavišas paspaustas, kitaip False.
        """
        return self._core.sensing_keypressed(key)
                
    def mikrofono_garsumas(self):
        """Grąžina mikrofono garsumą.

        Tai tik vietos rezervavimo blokas: mikrofonas nepalaikomas, todėl reikšmė visada yra -1.

        Scratch blokas: (garsumas)

        Returns
        -------
        int
            Visada -1.
        """
        return self._core.sensing_loudness()
                
    def pelė_paspausta(self):
        """Patikrina, ar šiuo metu paspaustas pelės klavišas.

        Scratch blokas: pelė paspausta?

        Returns
        -------
        bool
            True, jei paspaustas bet kuris pelės klavišas, kitaip False.
        """
        return self._core.sensing_mousedown()
                
    def pelės_x(self):
        """Grąžina horizontalią pelės žymeklio vietą scenoje. Scenos vidurys yra 0.

        Scratch blokas: (pelės x)

        Returns
        -------
        int
            Pelės žymeklio x vieta. Ji apribota scena.
        """
        return self._core.sensing_mousex()
                
    def pelės_y(self):
        """Grąžina vertikalią pelės žymeklio vietą scenoje. Scenos vidurys yra 0.

        Scratch blokas: (pelės y)

        Returns
        -------
        int
            Pelės žymeklio y vieta. Ji apribota scena.
        """
        return self._core.sensing_mousey()
                
    def scenos_fono_pavadinimas(self, stage='_stage_'):
        """Grąžina dabartinio fono pavadinimą. Fonus turi tik scena.

        Scratch blokas: ((Scena v) : [fono pavadinimas v])

        Parameters
        ----------
        stage : str
            Scenos vardas, pagal numatytąją reikšmę "_stage_". Veikėjui grąžinama 0.

        Returns
        -------
        str
            Dabartinio fono pavadinimas.
        """
        return self._core.sensing_of_backdropname(stage)
                
    def scenos_fono_nr(self, stage='_stage_'):
        """Grąžina dabartinio fono numerį (nuo 1). Fonus turi tik scena.

        Scratch blokas: ((Scena v) : [fono nr. v])

        Parameters
        ----------
        stage : str
            Scenos vardas, pagal numatytąją reikšmę "_stage_". Veikėjui grąžinama 0.

        Returns
        -------
        int
            Dabartinio fono numeris.
        """
        return self._core.sensing_of_backdropnumber(stage)
                
    def veikėjo_kaukės_pavadinimas(self, sprite):
        """Grąžina dabartinės kito veikėjo kaukės pavadinimą.

        Scratch blokas: ((veikėjas v) : [kaukės pavadinimas v])

        Parameters
        ----------
        sprite : str
            Veikėjo vardas. Jei tokio veikėjo nėra, grąžinama 0.

        Returns
        -------
        str
            Dabartinės kaukės pavadinimas.
        """
        return self._core.sensing_of_costumename(sprite)
                
    def veikėjo_kaukės_nr(self, sprite):
        """Grąžina dabartinės kito veikėjo kaukės numerį (nuo 1).

        Scratch blokas: ((veikėjas v) : [kaukės nr. v])

        Parameters
        ----------
        sprite : str
            Veikėjo vardas. Jei tokio veikėjo nėra, grąžinama 0.

        Returns
        -------
        int
            Dabartinės kaukės numeris.
        """
        return self._core.sensing_of_costumenumber(sprite)
                
    def veikėjo_kryptis(self, sprite):
        """Grąžina kito veikėjo kryptį laipsniais. 90 yra į dešinę, 0 yra aukštyn.

        Scratch blokas: ((veikėjas v) : [kryptis v])

        Parameters
        ----------
        sprite : str
            Veikėjo vardas. Jei tokio veikėjo nėra, grąžinama 0.

        Returns
        -------
        skaičius
            Veikėjo kryptis, tarp -180 ir 180.
        """
        return self._core.sensing_of_direction(sprite)
                
    def veikėjo_dydis(self, sprite):
        """Grąžina kito veikėjo dydį procentais. 100 yra įprastas dydis.

        Scratch blokas: ((veikėjas v) : [dydis v])

        Parameters
        ----------
        sprite : str
            Veikėjo vardas. Jei tokio veikėjo nėra, grąžinama 0.

        Returns
        -------
        skaičius
            Veikėjo dydis procentais.
        """
        return self._core.sensing_of_size(sprite)
                
    def kintamasis_iš(self, variable, sprite='_stage_'):
        """Grąžina veikėjo arba scenos kintamojo reikšmę.

        Scratch blokas: ((veikėjas v) : [kintamasis v])

        Parameters
        ----------
        variable : str
            Kintamojo vardas.
        sprite : str
            Veikėjo vardas arba "_stage_" scenai. Pagal numatytąją reikšmę imama scena.

        Returns
        -------
        object
            Kintamojo reikšmė. Jei tokio kintamojo nėra, grąžinama 0.
        """
        return self._core.sensing_of_variable(variable, sprite)
                
    def garsas_iš(self, sprite='_stage_'):
        """Grąžina veikėjo arba scenos garsų garsumą, nuo 0 iki 100.

        Scratch blokas: ((veikėjas v) : [garsas v])

        Parameters
        ----------
        sprite : str
            Veikėjo vardas arba "_stage_" scenai. Pagal numatytąją reikšmę imama scena.

        Returns
        -------
        skaičius
            Garsumas, nuo 0 iki 100.
        """
        return self._core.sensing_of_volume(sprite)
                
    def veikėjo_x_koordinatė(self, sprite):
        """Grąžina kito veikėjo x vietą.

        Scratch blokas: ((veikėjas v) : [x koordinatė v])

        Parameters
        ----------
        sprite : str
            Veikėjo vardas. Jei tokio veikėjo nėra, grąžinama 0.

        Returns
        -------
        skaičius
            Veikėjo x vieta.
        """
        return self._core.sensing_of_xposition(sprite)
                
    def veikėjo_y_koordinatė(self, sprite):
        """Grąžina kito veikėjo y vietą.

        Scratch blokas: ((veikėjas v) : [y koordinatė v])

        Parameters
        ----------
        sprite : str
            Veikėjo vardas. Jei tokio veikėjo nėra, grąžinama 0.

        Returns
        -------
        skaičius
            Veikėjo y vieta.
        """
        return self._core.sensing_of_yposition(sprite)
                
    def nustatyk_laikmatį_į_0(self):
        """Nustato laikmatį iš naujo į 0.

        Scratch blokas: laikmatis = 0
        """
        return self._core.sensing_resettimer()
                
    def nustatyk_vilkimą_pele_į_velkamas(self):
        """Padaro veikėją velkamą: naudotojas gali jį pele perkelti programos veikimo metu.

        Scratch blokas: vilkimas pele = [velkamas v]
        """
        return self._core.sensing_setdragmode_draggable()
                
    def nustatyk_vilkimą_pele_į_nevelkamas(self):
        """Padaro veikėją nevelkamą: naudotojas negali jo pele perkelti.

        Scratch blokas: vilkimas pele = [nevelkamas v]
        """
        return self._core.sensing_setdragmode_notdraggable()
                
    def laikmatis(self):
        """Grąžina sekundžių skaičių, praėjusį nuo programos starto arba nuo paskutinio laikmačio nustatymo iš naujo.

        Scratch blokas: (laikmatis)

        Returns
        -------
        skaičius
            Laikmačio rodmuo sekundėmis.
        """
        return self._core.sensing_timer()
                
    def vartotojo_vardas(self):
        """Grąžina naudotojo vardą. pystage nežino naudotojo vardo, todėl rezultatas visada yra tuščias tekstas.

        Scratch blokas: (vartotojo vardas)

        Returns
        -------
        str
            Visada tuščias tekstas.
        """
        return self._core.sensing_username()
                
    def efektą_kairiau_dešiniau_padidink(self, value):
        """Pakeičia garso kairiau/dešiniau efektą nurodyta reikšme. Efektas perkelia garsą tarp kairiojo ir dešiniojo garsiakalbio.

        Scratch blokas: efektą [kairiau/dešiniau v] padidink (10)

        Parameters
        ----------
        value : skaičius
            Kairiau/dešiniau efekto pokytis. -100 yra visiškai kairėje, 0 vidurys, 100 visiškai dešinėje.
        """
        return self._core.sound_changeeffectby_pan(value)
                
    def efektą_garso_aukštis_padidink(self, value):
        """Pakeičia garso aukščio efektą nurodyta reikšme. Teigiamos reikšmės garsą padaro aukštesnį.

        Scratch blokas: efektą [garso aukštis v] padidink (10)

        Parameters
        ----------
        value : skaičius
            Garso aukščio efekto pokytis. Efektas kinta nuo -360 iki 360, 0 yra įprastas aukštis.
        """
        return self._core.sound_changeeffectby_pitch(value)
                
    def garsą_padidink(self, value):
        """Pakeičia veikėjo garsų garsumą nurodyta reikšme. Neigiamos reikšmės garsą padaro tylesnį.

        Scratch blokas: garsą padidink (-10)

        Parameters
        ----------
        value : skaičius
            Garsumo pokytis. Garsumas kinta nuo 0 iki 100.
        """
        return self._core.sound_changevolumeby(value)
                
    def pašalink_garso_efektus(self):
        """Pašalina visus veikėjo garso efektus (aukštį ir kairiau/dešiniau).

        Scratch blokas: pašalink garso efektus
        """
        return self._core.sound_cleareffects()
                
    def grok(self, name, loop=0):
        """Pradeda groti garsą. Scenarijus nelaukia, kol garsas baigsis.

        Scratch blokas: grok (Pop v)

        Parameters
        ----------
        name : str arba int
            Garso failo vardas, pvz., "pop.wav", arba garso numeris (nuo 1).
        loop : int
            Kiek kartų garsas kartojamas po pirmojo karto. 0 sugroja vieną kartą, -1 kartoja be galo.
        """
        return self._core.sound_play(name, loop)
                
    def grok_kol_pasibaigs(self, name):
        """Sugroja garsą ir laukia, kol jis baigsis.

        Scratch blokas: grok (Pop v) kol pasibaigs

        Parameters
        ----------
        name : str arba int
            Garso failo vardas, pvz., "pop.wav", arba garso numeris (nuo 1).
        """
        return self._core.sound_playuntildone(name)
                
    def nustatyk_efektą_kairiau_dešiniau_į(self, value):
        """Nustato garso kairiau/dešiniau efektą. Efektas perkelia garsą tarp kairiojo ir dešiniojo garsiakalbio.

        Scratch blokas: efektas [kairiau/dešiniau v] = (0)

        Parameters
        ----------
        value : skaičius
            Naujas kairiau/dešiniau efektas. -100 yra visiškai kairėje, 0 vidurys, 100 visiškai dešinėje.
        """
        return self._core.sound_seteffectto_pan(value)
                
    def nustatyk_efektą_garso_aukštis_į(self, value):
        """Nustato garso aukščio efektą. Didesnės reikšmės garsą padaro aukštesnį.

        Scratch blokas: efektas [garso aukštis v] = (0)

        Parameters
        ----------
        value : skaičius
            Naujas garso aukščio efektas, nuo -360 iki 360. 0 yra įprastas aukštis.
        """
        return self._core.sound_seteffectto_pitch(value)
                
    def nustatyk_garsumą_į(self, value):
        """Nustato veikėjo garsų garsumą. 100 yra pats garsiausias, 0 yra tyla.

        Scratch blokas: garsumas = (100)%

        Parameters
        ----------
        value : skaičius
            Naujas garsumas, nuo 0 iki 100 procentų. Reikšmės už šio intervalo ribų apribojamos jo ribomis.
        """
        return self._core.sound_setvolumeto(value)
                
    def išjunk_garsus(self):
        """Sustabdo visus šiuo metu grojamus garsus, visų veikėjų ir scenos.

        Scratch blokas: išjunk garsus
        """
        return self._core.sound_stopallsounds()
                
    def garsumas(self):
        """Grąžina veikėjo garsų garsumą, nuo 0 iki 100.

        Scratch blokas: (garsumas)

        Returns
        -------
        skaičius
            Dabartinis garsumas, nuo 0 iki 100.
        """
        return self._core.sound_volume()

    def sukurk_sąrašą(self, name, values=None, all_sprites=True):
        """Sukuria sąrašą.

        Parameters
        ----------
        name : str
            Sąrašo vardas.
        values : list
            Pradiniai sąrašo elementai.
        all_sprites : bool
            Jei True, sąrašą gali naudoti scena ir visi veikėjai.
            Jei False, jis priklauso tik šiam veikėjui.
        """
        return self._core.pystage_makelistvariable(name, values, all_sprites)

    def pridėk_į_sąrašą(self, name, item):
        """pridėk %1 į %2

        Parameters
        ----------
        name : str
            Sąrašo vardas.
        item
            Elementas, skaičius arba tekstas.
        """
        return self._core.data_addtolist(name, item)

    def ištrinti_iš_sąrašo(self, name, index):
        """ištrinti %1 iš %2

        Parameters
        ----------
        name : str
            Sąrašo vardas.
        index : int arba str
            Vieta, skaičiuojant nuo 1. Taip pat galima: "last" ir "random". Su "all" ištrinami visi elementai.
        """
        return self._core.data_deleteoflist(name, index)

    def ištrinti_visus_iš_sąrašo(self, name):
        """ištrinti visus iš %1

        Parameters
        ----------
        name : str
            Sąrašo vardas.
        """
        return self._core.data_deletealloflist(name)

    def į_sąrašo_vietą_įterpti(self, name, item, index):
        """į sąrašo %3 %2 vietą įterpti %1

        Parameters
        ----------
        name : str
            Sąrašo vardas.
        item
            Elementas, skaičius arba tekstas.
        index : int arba str
            Vieta, skaičiuojant nuo 1. Taip pat galima: "last" ir "random".
        """
        return self._core.data_insertatlist(name, item, index)

    def sąrašo_vietai_priskirti(self, name, index, item):
        """sąrašo %2 %1 vietai priskirti %3

        Parameters
        ----------
        name : str
            Sąrašo vardas.
        index : int arba str
            Vieta, skaičiuojant nuo 1. Taip pat galima: "last" ir "random".
        item
            Elementas, skaičius arba tekstas.
        """
        return self._core.data_replaceitemoflist(name, index, item)

    def sąrašo_elementas_nr(self, name, index):
        """%2 nr. %1

        Parameters
        ----------
        name : str
            Sąrašo vardas.
        index : int arba str
            Vieta, skaičiuojant nuo 1. Taip pat galima: "last" ir "random".

        Returns
        -------
        Elementas arba tuščias tekstas, jei toje vietoje elemento nėra.
        """
        return self._core.data_itemoflist(name, index)

    def vieta_sąraše(self, name, item):
        """%1 vieta sąraše %2

        Parameters
        ----------
        name : str
            Sąrašo vardas.
        item
            Elementas, skaičius arba tekstas.

        Returns
        -------
        int
            Pirmojo pasitaikymo vieta, 0, jei elemento sąraše nėra.
        """
        return self._core.data_itemnumoflist(name, item)

    def sąrašo_ilgis(self, name):
        """%1 ilgis

        Parameters
        ----------
        name : str
            Sąrašo vardas.

        Returns
        -------
        int
        """
        return self._core.data_lengthoflist(name)

    def sąrašas_turi(self, name, item):
        """%1 turi %2?

        Parameters
        ----------
        name : str
            Sąrašo vardas.
        item
            Elementas, skaičius arba tekstas.

        Returns
        -------
        bool
        """
        return self._core.data_listcontainsitem(name, item)

    def sąrašas(self, name):
        """Pats sąrašas.

        Tai tikras Python sąrašas, jį galima naudoti kaip bet kurį kitą sąrašą.

        Parameters
        ----------
        name : str
            Sąrašo vardas.

        Returns
        -------
        list
        """
        return self._core.data_listvariable(name)

    def rodyti_sąrašą(self, name):
        """rodyti sąrašą %1

        Parameters
        ----------
        name : str
            Sąrašo vardas.
        """
        return self._core.data_showlist(name)

    def slėpti_sąrašą(self, name):
        """slėpti sąrašą %1

        Parameters
        ----------
        name : str
            Sąrašo vardas.
        """
        return self._core.data_hidelist(name)

    def nustatyk_sąrašo_monitoriaus_poziciją(self, name, x, y, width=None, height=None):
        """Nustato scenoje rodomo sąrašo vietą ir dydį.

        Parameters
        ----------
        name : str
            Sąrašo vardas.
        x : int
            Kairysis kraštas.
        y : int
            Viršutinis kraštas.
        width : int
            Plotis taškais, automatinis, jei nenurodytas.
        height : int
            Aukštis taškais, automatinis, jei nenurodytas.
        """
        return self._core.pystage_setlistmonitorposition(name, x, y, width, height)

    def sujunk(self, string1, string2):
        """sujunk %1 ir %2

        Parameters
        ----------
        string1
            Pirmasis tekstas arba pirmasis skaičius.
        string2
            Antrasis tekstas arba antrasis skaičius.

        Returns
        -------
        str
        """
        return self._core.operator_join(string1, string2)

    def raidė_nr(self, letter, string):
        """%2 raidė nr. %1

        Parameters
        ----------
        letter : int
            Simbolio vieta, skaičiuojant nuo 1.
        string : str
            Tekstas.

        Returns
        -------
        str
            Simbolis arba tuščias tekstas, jei toje vietoje simbolio nėra.
        """
        return self._core.operator_letter_of(letter, string)

    def ilgis(self, string):
        """%1 ilgis

        Parameters
        ----------
        string : str
            Tekstas.

        Returns
        -------
        int
        """
        return self._core.operator_length(string)

    def ar_turi(self, string1, string2):
        """ar %1 turi %2?

        Didžiosios ir mažosios raidės ignoruojamos.

        Parameters
        ----------
        string1 : str
            Tekstas, kuriame ieškoma.
        string2 : str
            Tekstas, kurio ieškoma.

        Returns
        -------
        bool
        """
        return self._core.operator_contains(string1, string2)

    def didesnis_už(self, operand1, operand2):
        """Patikrina, ar pirmoji reikšmė didesnė už antrąją. Skaičiai lyginami kaip skaičiai, tekstai pagal abėcėlę be didžiųjų ir mažųjų raidžių skirtumo.

        Scratch blokas: <(a) > (b)>

        Parameters
        ----------
        operand1 : skaičius arba str
            Pirmoji reikšmė.
        operand2 : skaičius arba str
            Antroji reikšmė.

        Returns
        -------
        bool
            True, jei operand1 didesnis už operand2, kitaip False.
        """
        return self._core.operator_gt(operand1, operand2)

    def mažesnis_už(self, operand1, operand2):
        """Patikrina, ar pirmoji reikšmė mažesnė už antrąją. Skaičiai lyginami kaip skaičiai, tekstai pagal abėcėlę be didžiųjų ir mažųjų raidžių skirtumo.

        Scratch blokas: <(a) < (b)>

        Parameters
        ----------
        operand1 : skaičius arba str
            Pirmoji reikšmė.
        operand2 : skaičius arba str
            Antroji reikšmė.

        Returns
        -------
        bool
            True, jei operand1 mažesnis už operand2, kitaip False.
        """
        return self._core.operator_lt(operand1, operand2)

    def lygu(self, operand1, operand2):
        """Patikrina, ar dvi reikšmės lygios. Skaičiai lyginami kaip skaičiai, tekstai be didžiųjų ir mažųjų raidžių skirtumo.

        Scratch blokas: <(a) = (b)>

        Parameters
        ----------
        operand1 : skaičius arba str
            Pirmoji reikšmė.
        operand2 : skaičius arba str
            Antroji reikšmė.

        Returns
        -------
        bool
            True, jei reikšmės lygios, kitaip False.
        """
        return self._core.operator_equals(operand1, operand2)

    def suapvalinta(self, number):
        """suapvalinta %1

        Kaip Scratch, .5 visada apvalinama aukštyn.

        Parameters
        ----------
        number : float

        Returns
        -------
        int
        """
        return self._core.operator_round(number)

    def kai_paspaudi_scenoje(self, generator_function, name="", no_refresh=False):
        """kai paspaudi scenoje

        Parameters
        ----------
        generator_function : function
            Funkcija su kodu, kuris turi būti vykdomas.
        name : str
            Vardas, kuriuo skiriami scenarijai, naudojantys tą pačią funkciją.
        no_refresh : bool
            Jei True, kodas vykdomas vienu prasukimu be ekrano atnaujinimo.
        """
        return self._core.event_whenstageclicked(generator_function, name, no_refresh)

    def padalinta_iš(self, a, b):
        """%1 / %2

        Kaip Scratch, dalyba iš 0 duoda Infinity, -Infinity arba NaN
        vietoj klaidos.

        Parameters
        ----------
        a : float
        b : float

        Returns
        -------
        float
        """
        return self._core.operator_divide(a, b)

    def liekana(self, a, b):
        """%1 / %2 liekana

        Dalybos liekana su daliklio ženklu, kaip
        Scratch. Liekana iš 0 yra NaN.

        Parameters
        ----------
        a : float
        b : float

        Returns
        -------
        float
        """
        return self._core.operator_mod(a, b)

    def ištrinti_viską(self):
        """ištrinti viską

        Ištrina viską, kas buvo nupiešta pieštuku.

        Returns
        -------
        None
        """
        return self._core.pen_clear()

    def rodyk_monitorių(self, reporter):
        """Parodo reikšmės monitorių, kaip langelį šalia bloko Scratch.

        Parameters
        ----------
        reporter : str
            Kas rodoma: "x vieta", "y vieta", "kryptis",
            "kaukė numeris", "kaukė vardas", "dydis", "garsumas" (veikėjai ir
            scena), "fonas numeris", "fonas vardas" (scena), "atsakas",
            "mikrofono garsumas", "laikmatis", "metai", "mėnuo", "mėn. diena",
            "savaitės diena", "valanda", "minutė", "sekundė" arba "vartotojo vardas".
        """
        return self._core.pystage_showmonitor(reporter)

    def slėpk_monitorių(self, reporter):
        """Paslepia reikšmės monitorių.

        Parameters
        ----------
        reporter : str
            Reikšmė, pvz., "x vieta", "dydis", "laikmatis" arba "metai". Leidžiamos tos pačios reikšmės kaip ir rodyk_monitorių.
        """
        return self._core.pystage_hidemonitor(reporter)

    def nustatyk_reikšmės_monitoriaus_poziciją(self, reporter, x, y):
        """Nustato reikšmės monitoriaus vietą.

        Parameters
        ----------
        reporter : str
            Reikšmė, žr. rodyk_monitorių.
        x : int
            Kairysis kraštas (Scratch koordinatės).
        y : int
            Viršutinis kraštas (Scratch koordinatės).
        """
        return self._core.pystage_setreportermonitorposition(reporter, x, y)

    def nustatyk_reikšmės_monitoriaus_stilių(self, reporter, stilius="normal"):
        """Nustato reikšmės monitoriaus stilių.

        Parameters
        ----------
        reporter : str
            Reikšmė, žr. rodyk_monitorių.
        stilius : str
            "normal" arba "large" (taip pat "įprastas" arba "didesnis").
        """
        return self._core.pystage_setreportermonitorstyle(reporter, stilius)
