"""Tests for the Lithuanian API (pystage.lt) and its localisation of values and messages."""
import pygame
import pytest

from pystage.core import i18n
from pystage.core.constants import KEY_MAPPINGS
from pystage.lt import Scena
from pystage.en import Stage

FRAME = 1 / 60


@pytest.fixture
def lt():
    stage = Scena()
    yield stage
    i18n.set_language("en")


@pytest.fixture
def core(lt):
    return lt._core


def noop(self):
    pass


# Keys

@pytest.mark.parametrize("name,key", [
    ("tarpą", pygame.K_SPACE), ("Tarpas", pygame.K_SPACE),
    ("⬆️", pygame.K_UP), ("⬇️", pygame.K_DOWN),
    ("<--", pygame.K_LEFT), ("-->", pygame.K_RIGHT),
    ("rodyklė aukštyn", pygame.K_UP), ("RODYKLĖ ŽEMYN", pygame.K_DOWN),
    ("įvesties klavišas", pygame.K_RETURN), ("Enter", pygame.K_RETURN),
    ("space", pygame.K_SPACE), ("A", pygame.K_a),
])
def test_lithuanian_key_names(lt, name, key):
    sprite = lt.pridėk_veikėją()
    sprite.kai_paspaudi_klavišą(name, noop)
    assert key in sprite._core.code_manager.key_pressed_blocks


@pytest.mark.parametrize("name", ["bet kurį", "bet kuris", "bet kuris klavišas", "any"])
def test_any_key(lt, name):
    sprite = lt.pridėk_veikėją()
    sprite.kai_paspaudi_klavišą(name, noop)
    assert len(sprite._core.code_manager.any_key_blocks) == 1


def test_key_pressed_with_lithuanian_name(lt, monkeypatch):
    sprite = lt.pridėk_veikėją()
    pressed = {pygame.K_SPACE: True}

    class Keys:
        def __getitem__(self, k):
            return pressed.get(k, False)

        def __iter__(self):
            return iter(pressed.values())
    monkeypatch.setattr(pygame.key, "get_pressed", lambda: Keys())
    assert sprite.klavišas_paspaustas("tarpą") is True
    assert sprite.klavišas_paspaustas("⬆️") is False
    assert sprite.klavišas_paspaustas("bet kurį") is True


def test_bad_key_message_follows_language(lt):
    sprite = lt.pridėk_veikėją()
    with pytest.raises(ValueError, match="Netinkamas klavišas: foo"):
        sprite.kai_paspaudi_klavišą("foo", noop)
    stage = Stage()
    with pytest.raises(ValueError, match="Bad key: foo"):
        stage.add_a_sprite().when_key_pressed("foo", noop)


# Alias tables

def test_math_functions(core):
    assert core.operator_mathop("teigiama reikšmė", -3) == 3
    assert core.operator_mathop("apvalinimas žemyn", 2.7) == 2
    assert core.operator_mathop("apvalinimas aukštyn", 2.1) == 3
    assert core.operator_mathop("kvadratinė šaknis", 9) == 3
    assert core.operator_mathop("tg", 0) == 0
    assert core.operator_mathop("arctg", 0) == 0
    assert core.operator_mathop("e^", 0) == 1
    assert core.operator_mathop("10^", 2) == 100
    assert core.operator_mathop("sqrt", 16) == 4


def test_list_positions(core):
    core.pystage_makelistvariable("l", ["a", "b", "c"])
    assert core.data_itemoflist("l", "paskutinis") == "c"
    assert core.data_itemoflist("l", "Paskutinis") == "c"
    assert core.data_itemoflist("l", "atsitiktinis") in ("a", "b", "c")
    core.data_deleteoflist("l", "viskas")
    assert core.data_lengthoflist("l") == 0
    core.data_addtolist("l", "x")
    core.data_insertatlist("l", "y", "paskutinis")
    assert list(core.data_listvariable("l")) == ["x", "y"]


def test_backdrop_specials(core):
    core.pystage_addbackdrop("backdrop1")
    core.pystage_addbackdrop("backdrop2")
    assert core.looks_backdropnumbername_number() == 1
    core.looks_switchbackdropto_backdrop("kitas fonas")
    assert core.looks_backdropnumbername_number() == 2
    core.looks_switchbackdropto_backdrop("ankstesnis fonas")
    assert core.looks_backdropnumbername_number() == 1
    core.looks_switchbackdropto_backdrop("kitas  fonas")
    assert core.looks_backdropnumbername_number() == 2
    core.looks_switchbackdropto_backdrop("atsitiktinis fonas")
    assert core.looks_backdropnumbername_number() in (1, 2)


def test_special_sprites(lt, core):
    sprite = lt.pridėk_veikėją()._core
    other = lt.pridėk_veikėją()._core
    other.pystage_setname("Ona")
    sprite.motion_goto_sprite("pelės žymeklis")
    assert (sprite.motion_xposition(), sprite.motion_yposition()) == (core.sensing_mousex(), core.sensing_mousey())
    count = len(core.sprites)
    sprite.control_create_clone_of_sprite("savęs")
    assert len(core.sprites) == count + 1
    assert sprite.sensing_touchingobject_sprite("kraštą") in (True, False)
    assert core._get_sprite("Scena") is core
    # A sprite with such a name is not an alias
    other.pystage_setname("kraštą")
    assert core._special("kraštą") == "kraštą"
    assert core._get_sprite("kraštą") is other


# Every alias maps to a value the core really accepts

def test_all_aliases_are_accepted_by_the_core(core):
    core.pystage_addbackdrop("b1")
    core.pystage_addbackdrop("b2")
    core.pystage_makelistvariable("l", [1, 2, 3])
    sprite = core.pystage_createsprite()._core
    for table, languages in i18n.ALIASES.items():
        assert "lt" in languages
        for value, names in languages["lt"].items():
            for name in names:
                assert i18n.canonical(table, name) == value
                assert i18n.canonical(table, name.upper()) == value
                if table == "keys":
                    key = i18n.canonical_key(name)
                    assert key == "any" or key in KEY_MAPPINGS
                elif table == "math":
                    assert core.operator_mathop(name, 1) is not None
                elif table == "list_positions":
                    core.data_itemoflist("l", name)
                    core.pystage_makelistvariable("tmp" + name, [1, 2], all_sprites=True)
                    core.data_deleteoflist("tmp" + name, name)
                elif table == "backdrops":
                    core.looks_switchbackdropto_backdrop(name)
                elif table == "reporters":
                    from pystage.core._variables import REPORTERS
                    assert value in REPORTERS
                    scope = REPORTERS[value][2]
                    (core if scope == "stage" else sprite).pystage_showmonitor(name)
                elif table == "sprites":
                    assert core._special(name) == value
                    assert value in ("_mouse_", "_random_", "_edge_", "_myself_", "_stage_")


def test_every_reporter_has_a_lithuanian_name():
    from pystage.core._variables import REPORTERS
    names = i18n.ALIASES["reporters"]["lt"]
    assert set(names) == set(REPORTERS)
    assert all(names.values())


# Messages

def test_lithuanian_messages(core):
    with pytest.raises(ValueError, match="Kintamojo x nėra"):
        core.data_variable("x")
    with pytest.raises(ValueError, match="Sąrašo y nėra"):
        core.data_listvariable("y")
    core.pystage_makevariable("v")
    with pytest.raises(ValueError, match="Kintamasis vardu \"v\" jau yra"):
        core.pystage_makevariable("v")
    core.pystage_makelistvariable("l")
    with pytest.raises(ValueError, match="sąrašas pavadintas \"l\""):
        core.pystage_makelistvariable("l")
    with pytest.raises(ValueError, match="nepalaikoma"):
        core.operator_mathop("foo", 1)


def test_lithuanian_warnings(lt, capsys):
    lt._core.pystage_addsound("nėra-tokio")
    assert "ĮSPĖJIMAS: Garso 'nėra-tokio' nerasta." in capsys.readouterr().out


def test_message_catalogue_is_complete():
    assert set(i18n.MESSAGES["lt"]) == set(i18n.MESSAGES["en"])
    i18n.set_language("lt")
    try:
        assert i18n.tr("monitor_empty") == "(tuščia)"
        assert i18n.tr("monitor_length", length=3) == "ilgis 3"
        assert i18n.tr("error_in", file="a.py", line=3) == "Klaida faile a.py, eilutėje 3"
    finally:
        i18n.set_language("en")
    assert i18n.tr("monitor_empty") == "(empty)"


def test_error_overlay_prefix(core, monkeypatch):
    shown = []
    from pystage.core import gui
    monkeypatch.setattr(gui, "wrap_text", lambda text, *a: (shown.append(text), (["x"], 10, 10))[1])
    monkeypatch.setattr(gui, "render_lines", lambda *a: pygame.Surface((10, 10)))
    monkeypatch.setattr(pygame.event, "get", lambda: [pygame.event.Event(pygame.QUIT)])
    try:
        raise ValueError("sugedo")
    except ValueError as error:
        core._show_error(error)
    assert shown[0].startswith("Klaida faile test_lithuanian.py, eilutėje")


def test_title(monkeypatch):
    titles = []
    monkeypatch.setattr(pygame.display, "set_caption", lambda t, *a: titles.append(t))
    Scena(pavadinimas="Mano žaidimas")
    i18n.set_language("en")
    assert titles == ["Mano žaidimas"]


def test_lithuanian_monitor_texts(core):
    core.pystage_makelistvariable("sąrašas")
    core.data_showlist("sąrašas")
    core._frame(FRAME)  # renders "(tuščia)" and "ilgis 0" without error


# The facade

def test_facade_names_and_delegation():
    from pystage.l10n.api import _get_core_names
    from pystage.lt import Veikėjas, sprite_class, stage_class
    assert sprite_class is Veikėjas and stage_class is Scena
    assert Veikėjas.eik_į_x_y and Veikėjas.kai_spusteli_žalią_vėliavėlę and Scena.paleisk
    for cls in (Veikėjas, Scena):
        names = _get_core_names(cls)
        assert names
        for name, core_name in names.items():
            assert hasattr(cls, name) and core_name
    for cls in (Scena, Stage):
        assert not hasattr(cls, "pystage_createsprite") and not hasattr(cls, "pystage_play")


def test_program_in_lithuanian_runs(lt):
    sprite = lt.pridėk_veikėją()
    lt.sukurk_kintamąjį("taškai", 0)

    def pagrindinis(self):
        self.eik_į_x_y(10, 20)
        self.palauk_sek(0.05)
        self.nustatyk_x_į(50)
        self.nustatyk_kintamąjį_į("taškai", 7)

    sprite.kai_spusteli_žalią_vėliavėlę(pagrindinis)
    for _ in range(int(0.5 / FRAME)):
        lt._core._frame(FRAME)
    assert sprite.x_vieta() == 50
    assert sprite.y_vieta() == 20
    assert lt.kintamasis("taškai") == 7
