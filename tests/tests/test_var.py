import pytest

from pystage.core._variables import _Variables
from pystage.core.stage import CoreStage


class TestVar:
    _stage = CoreStage()
    sprite1 = _Variables()
    sprite2 = _Variables()
    sprite1.stage = _stage
    sprite2.stage = _stage
    stage = _stage

    def test_make_var(self):
        self.sprite1.pystage_makevariable("a", all_sprites=True)
        assert self.stage.variables == {"a": 0}
        assert self.sprite1.variables == {}
        assert self.sprite1.data_variable("a") == 0
        assert self.sprite2.data_variable("a") == 0
        assert self.stage.data_variable("a") == 0

        with pytest.raises(ValueError):
            # "a" already exists
            self.sprite1.pystage_makevariable("a", all_sprites=False)
            self.sprite1.pystage_makevariable("a", all_sprites=True)
            self.stage.pystage_makevariable("a", all_sprites=True)

        self.sprite1.pystage_makevariable("b", all_sprites=False)
        assert self.stage.variables == {"a": 0}
        assert self.sprite1.variables == {"b": 0}
        assert self.sprite2.variables == {}

        self.sprite2.pystage_makevariable("timer", 10, all_sprites=True)
        assert self.stage.variables == {"a": 0, "timer": 10}

    def test_set_var(self):
        self.stage.data_setvariableto("a", 10)
        assert self.stage.data_variable("a") == 10
        assert self.sprite1.data_variable("a") == 10

        self.sprite1.data_setvariableto("timer", 20)
        assert self.stage.data_variable("timer") == 20

        self.sprite1.data_setvariableto("b", 30)
        assert self.sprite1.data_variable("b") == 30

        with pytest.raises(ValueError):
            self.sprite2.data_setvariableto("b", 40)

    def test_change_var(self):
        self.stage.data_changevariableby("a", 10)
        assert self.stage.data_variable("a") == 20
        assert self.sprite1.data_variable("a") == 20

        self.stage.data_changevariableby("a", -10)
        assert self.stage.data_variable("a") == 10
        assert self.sprite1.data_variable("a") == 10

    def test_var_monitor(self):
        assert len(self.sprite1.var_monitors) == 1
        assert len(self.stage.var_monitors) == 2
        assert len(self.sprite2.var_monitors) == 0


class TestList:
    _stage = CoreStage()
    sprite1 = _Variables()
    sprite2 = _Variables()
    sprite1.stage = _stage
    sprite2.stage = _stage
    stage = _stage

    def test_make_list(self):
        self.sprite1.pystage_makelistvariable("a", all_sprites=True)
        self.sprite1.pystage_makelistvariable(
            "b", ["1", "2"], all_sprites=True)
        assert self.stage.list_variables == {"a": [], "b": ["1", "2"]}
        assert self.sprite1.list_variables == {}
        assert self.sprite1.data_listvariable("a") == []

        with pytest.raises(ValueError):
            # "a" already exists
            self.sprite1.pystage_makelistvariable("a", all_sprites=False)
            self.sprite1.pystage_makelistvariable("a", all_sprites=True)
            self.stage.pystage_makelistvariable("a", all_sprites=True)

        self.sprite1.pystage_makelistvariable("c", all_sprites=False)
        assert self.stage.list_variables == {"a": [], "b": ["1", "2"]}
        assert self.sprite1.list_variables == {"c": []}
        assert self.sprite2.list_variables == {}

    def test_list_method(self):
        self.stage.pystage_makelistvariable("fruits", ["apple"], all_sprites=True)

        self.sprite1.data_addtolist("fruits", "banana")
        assert self.stage.data_listvariable("fruits") == ["apple", "banana"]

        self.sprite1.data_deleteoflist("fruits", 1)
        assert self.stage.data_listvariable("fruits") == ["banana"]
        self.sprite1.data_deleteoflist("fruits", 1)
        assert self.stage.data_listvariable("fruits") == []
        self.sprite1.data_deleteoflist("fruits", 1) # no error
        self.sprite1.data_deleteoflist("fruits", 10) # no error

        self.sprite1.data_addtolist("fruits", "apple")
        self.sprite1.data_addtolist("fruits", "pear")
        self.sprite1.data_deletealloflist("fruits")
        assert self.stage.data_listvariable("fruits") == []

        self.sprite1.data_insertatlist("fruits", "apple", 0) # no error
        self.sprite1.data_insertatlist("fruits", "apple", -10) # no error
        assert self.stage.data_listvariable("fruits") == []

        self.sprite1.data_insertatlist("fruits", "apple", 1)
        assert self.stage.data_listvariable("fruits") == ["apple"]
        self.sprite1.data_insertatlist("fruits", "pear", 1)
        assert self.stage.data_listvariable("fruits") == ["pear", "apple"]

        self.sprite1.data_replaceitemoflist("fruits", 1, "banana")
        assert self.stage.data_listvariable("fruits") == ["banana", "apple"]
        self.sprite1.data_replaceitemoflist("fruits", 2, "banana")
        assert self.stage.data_listvariable("fruits") == ["banana", "banana"]

        assert self.sprite1.data_itemoflist("fruits", 1) == "banana"
        assert self.sprite1.data_itemoflist("fruits", 2) == "banana"
        assert self.sprite1.data_itemoflist("fruits", 3) == ""

        self.sprite2.data_replaceitemoflist("fruits", 1, "apple")
        assert self.sprite1.data_itemnumoflist("fruits", "banana") == 2
        assert self.sprite2.data_itemnumoflist("fruits", "apple") == 1
        assert self.sprite2.data_itemnumoflist("fruits", "peach") == 0

        assert self.sprite1.data_lengthoflist("fruits") == 2

        assert self.sprite1.data_listcontainsitem("fruits", "banana")
        assert not self.sprite1.data_listcontainsitem("fruits", "peach")

