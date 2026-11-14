"""Tests for the localisation of values and messages (pystage.core.i18n)."""
import pygame
import pytest

from pystage.core import i18n
from pystage.core.constants import KEY_MAPPINGS
from pystage.de import Bühne
from pystage.en import Stage


@pytest.fixture
def de():
    stage = Bühne()
    yield stage
    i18n.set_language("en")


@pytest.fixture
def core(de):
    return de._core


def noop(self):
    pass


# Keys

@pytest.mark.parametrize("name,key", [
    ("Leertaste", pygame.K_SPACE), ("leertaste", pygame.K_SPACE),
    ("Pfeil nach oben", pygame.K_UP), ("Pfeil nach unten", pygame.K_DOWN),
    ("Pfeil nach links", pygame.K_LEFT), ("PFEIL NACH RECHTS", pygame.K_RIGHT),
    ("Eingabetaste", pygame.K_RETURN), ("Enter", pygame.K_RETURN),
    ("space", pygame.K_SPACE), ("A", pygame.K_a),
])
def test_german_key_names(de, name, key):
    sprite = de.füge_eine_figur_hinzu()
    sprite.wenn_taste_gedrückt_wird(name, noop)
    assert key in sprite._core.code_manager.key_pressed_blocks


@pytest.mark.parametrize("name", ["beliebiges", "beliebige Taste", "any"])
def test_any_key(de, name):
    sprite = de.füge_eine_figur_hinzu()
    sprite.wenn_taste_gedrückt_wird(name, noop)
    assert len(sprite._core.code_manager.any_key_blocks) == 1


def test_key_pressed_with_german_name(de, monkeypatch):
    sprite = de.füge_eine_figur_hinzu()
    pressed = {pygame.K_SPACE: True}

    class Keys:
        def __getitem__(self, k):
            return pressed.get(k, False)

        def __iter__(self):
            return iter(pressed.values())
    monkeypatch.setattr(pygame.key, "get_pressed", lambda: Keys())
    assert sprite.taste_gedrückt("Leertaste") is True
    assert sprite.taste_gedrückt("Pfeil nach oben") is False
    assert sprite.taste_gedrückt("beliebiges") is True


def test_bad_key_message_follows_language(de):
    sprite = de.füge_eine_figur_hinzu()
    with pytest.raises(ValueError, match="Ungültige Taste: foo"):
        sprite.wenn_taste_gedrückt_wird("foo", noop)
    stage = Stage()
    with pytest.raises(ValueError, match="Bad key: foo"):
        stage.add_a_sprite().when_key_pressed("foo", noop)


# Alias tables

def test_math_functions(core):
    assert core.operator_mathop("Betrag", -3) == 3
    assert core.operator_mathop("abrunden", 2.7) == 2
    assert core.operator_mathop("aufrunden", 2.1) == 3
    assert core.operator_mathop("Wurzel", 9) == 3
    assert core.operator_mathop("e^", 0) == 1
    assert core.operator_mathop("10^", 2) == 100
    assert core.operator_mathop("sqrt", 16) == 4


def test_list_positions(core):
    core.pystage_makelistvariable("l", ["a", "b", "c"])
    assert core.data_itemoflist("l", "letztes") == "c"
    assert core.data_itemoflist("l", "Letztes") == "c"
    assert core.data_itemoflist("l", "zufälliges") in ("a", "b", "c")
    core.data_deleteoflist("l", "alles")
    assert core.data_lengthoflist("l") == 0
    core.data_addtolist("l", "x")
    core.data_insertatlist("l", "y", "letztes")
    assert list(core.data_listvariable("l")) == ["x", "y"]


def test_backdrop_specials(core):
    core.pystage_addbackdrop("backdrop1")
    core.pystage_addbackdrop("backdrop2")
    assert core.looks_backdropnumbername_number() == 1
    core.looks_switchbackdropto_backdrop("nächstes Bühnenbild")
    assert core.looks_backdropnumbername_number() == 2
    core.looks_switchbackdropto_backdrop("vorheriges Bühnenbild")
    assert core.looks_backdropnumbername_number() == 1
    core.looks_switchbackdropto_backdrop("zufälliges Bühnenbild")
    assert core.looks_backdropnumbername_number() in (1, 2)


def test_special_sprites(de, core):
    sprite = de.füge_eine_figur_hinzu()._core
    other = de.füge_eine_figur_hinzu()._core
    other.pystage_setname("Anna")
    sprite.motion_goto_sprite("Mauszeiger")
    assert (sprite.motion_xposition(), sprite.motion_yposition()) == (core.sensing_mousex(), core.sensing_mousey())
    count = len(core.sprites)
    sprite.control_create_clone_of_sprite("mir selbst")
    assert len(core.sprites) == count + 1
    assert sprite.sensing_touchingobject_sprite("Rand") in (True, False)
    assert core._get_sprite("Bühne") is core
    # A sprite with such a name is not an alias
    other.pystage_setname("Rand")
    assert core._special("Rand") == "Rand"
    assert core._get_sprite("Rand") is other


# Every alias maps to a value the core really accepts

def test_all_aliases_are_accepted_by_the_core(core):
    core.pystage_addbackdrop("b1")
    core.pystage_addbackdrop("b2")
    core.pystage_makelistvariable("l", [1, 2, 3])
    sprite = core.pystage_createsprite()._core
    for table, languages in i18n.ALIASES.items():
        for aliases in languages.values():
            for value, names in aliases.items():
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
                    elif table == "sprites":
                        assert core._special(name) == value
                        assert value in ("_mouse_", "_random_", "_edge_", "_myself_", "_stage_")


def test_canonical_values_stay_unchanged():
    assert i18n.canonical("keys", "space") == "space"
    assert i18n.canonical("keys", 5) == 5
    assert i18n.canonical("math", "sin") == "sin"


# Messages

def test_german_messages(core):
    with pytest.raises(ValueError, match="Die Variable x gibt es nicht"):
        core.data_variable("x")
    with pytest.raises(ValueError, match="Die Liste y gibt es nicht"):
        core.data_listvariable("y")
    core.pystage_makevariable("v")
    with pytest.raises(ValueError, match="Die Variable v gibt es schon"):
        core.pystage_makevariable("v")
    core.pystage_makelistvariable("l")
    with pytest.raises(ValueError, match="Die Liste l gibt es schon"):
        core.pystage_makelistvariable("l")
    with pytest.raises(ValueError, match="nicht unterstützt"):
        core.operator_mathop("foo", 1)


def test_english_messages_are_default():
    stage = Stage()
    with pytest.raises(ValueError, match="The variable x does not exist"):
        stage._core.data_variable("x")


def test_german_warnings(de, capsys):
    de._core.pystage_addsound("gibt-es-nicht")
    assert "WARNUNG: Der Klang 'gibt-es-nicht' wurde nicht gefunden." in capsys.readouterr().out


def test_message_catalogue_is_complete():
    assert set(i18n.MESSAGES["de"]) == set(i18n.MESSAGES["en"])
    assert i18n.tr("monitor_empty") == "(empty)"
    i18n.set_language("de")
    try:
        assert i18n.tr("monitor_empty") == "(leer)"
        assert i18n.tr("monitor_length", length=3) == "Länge 3"
        assert i18n.tr("error_in", file="a.py", line=3) == "Fehler in a.py, Zeile 3"
    finally:
        i18n.set_language("en")
    with pytest.raises(ValueError):
        i18n.set_language("xx")


def test_error_overlay_prefix(core, monkeypatch):
    shown = []
    from pystage.core import gui
    monkeypatch.setattr(gui, "wrap_text", lambda text, *a: (shown.append(text), (["x"], 10, 10))[1])
    monkeypatch.setattr(gui, "render_lines", lambda *a: pygame.Surface((10, 10)))
    monkeypatch.setattr(pygame.event, "get", lambda: [pygame.event.Event(pygame.QUIT)])
    try:
        raise ValueError("kaputt")
    except ValueError as error:
        core._show_error(error)
    assert shown[0].startswith("Fehler in test_german.py, Zeile")


def test_title(monkeypatch):
    titles = []
    monkeypatch.setattr(pygame.display, "set_caption", lambda t, *a: titles.append(t))
    Bühne(titel="Mein Spiel")
    Stage(title="My game")
    Stage()
    i18n.set_language("en")
    assert titles == ["Mein Spiel", "My game", "Welcome to pyStage!"]


def test_german_monitor_texts(core):
    from pystage.core.monitors import Monitor
    core.pystage_makelistvariable("liste")
    core.data_showlist("liste")
    core._frame(1 / 60)  # renders "(leer)" and "Länge 0" without error
