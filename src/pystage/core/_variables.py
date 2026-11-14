import random

from pystage.core.i18n import canonical, tr

from pystage.core._base_sprite import BaseSprite
from pystage.core.monitors import Monitor
from pystage.core.values import to_number, equals, wrap


class _Variables(BaseSprite):
    # Variables, lists and their monitors.
    #
    # Global variables are stored in the stage (stage variables are global
    # in Scratch), local variables are stored in the sprite. A local name
    # always wins over a global one.
    #
    # Variables and lists have separate namespaces, as in Scratch.

    def __init__(self):
        super().__init__()

        self.variables = {}
        self.list_variables = {}
        self.var_monitors = {}
        self.list_monitors = {}

    ##
    # Lookup helpers
    #

    def _variable_owner(self, name):
        if name in self.variables:
            return self
        if name in self.stage.variables:
            return self.stage
        raise ValueError(tr("variable_missing", name=name))

    def _list(self, name):
        if name in self.list_variables:
            return self.list_variables[name]
        if name in self.stage.list_variables:
            return self.stage.list_variables[name]
        raise ValueError(tr("list_missing", name=name))

    def _get_monitor(self, name):
        if name in self.var_monitors:
            return self.var_monitors[name]
        return self.stage.var_monitors.get(name)

    def _get_list_monitor(self, name):
        if name in self.list_monitors:
            return self.list_monitors[name]
        return self.stage.list_monitors.get(name)

    @staticmethod
    def _list_index(index, lst, insert=False):
        """Translate a Scratch list position to a Python index.

        Scratch positions are 1-based and can also be the texts "last" and
        "random" (or "any"). Returns None if the position does not exist.

        Parameters
        ----------
        index : int or str
            The Scratch position.
        lst : list
            The list the position refers to.
        insert : bool
            If True, the position after the last item is valid as well.
        """
        length = len(lst) + (1 if insert else 0)
        if isinstance(index, str):
            keyword = canonical("list_positions", index).strip().lower()
            if keyword == "last":
                return length - 1 if length > 0 else None
            if keyword in ("random", "any"):
                return random.randrange(length) if length > 0 else None
        index = int(to_number(index))
        if index < 1 or index > length:
            return None
        return index - 1

    ##
    # Variables
    #

    def data_setvariableto(self, name, value):
        self._variable_owner(name).variables[name] = value

    def data_variable(self, name):
        return wrap(self._variable_owner(name).variables[name])

    def data_changevariableby(self, name, value):
        owner = self._variable_owner(name)
        owner.variables[name] = to_number(owner.variables[name]) + to_number(value)

    def data_showvariable(self, name):
        monitor = self._get_monitor(name)
        if monitor:
            monitor.show()

    def data_hidevariable(self, name):
        monitor = self._get_monitor(name)
        if monitor:
            monitor.hide()

    ##
    # Lists
    #

    def data_listvariable(self, name):
        return self._list(name)
    data_listvariable.opcode = "data_listcontents"

    def data_addtolist(self, name, item):
        self._list(name).append(item)

    def data_deleteoflist(self, name, index):
        lst = self._list(name)
        if isinstance(index, str) and canonical("list_positions", index).strip().lower() == "all":
            lst.clear()
            return
        i = self._list_index(index, lst)
        if i is not None:
            del lst[i]

    def data_deletealloflist(self, name):
        self._list(name).clear()

    def data_insertatlist(self, name, item, index):
        lst = self._list(name)
        i = self._list_index(index, lst, insert=True)
        if i is not None:
            lst.insert(i, item)

    def data_replaceitemoflist(self, name, index, item):
        lst = self._list(name)
        i = self._list_index(index, lst)
        if i is not None:
            lst[i] = item

    def data_itemoflist(self, name, index):
        lst = self._list(name)
        i = self._list_index(index, lst)
        if i is None:
            return wrap("")
        return wrap(lst[i])

    def data_itemnumoflist(self, name, item):
        for i, value in enumerate(self._list(name)):
            if equals(value, item):
                return i + 1
        return 0

    def data_lengthoflist(self, name):
        return len(self._list(name))

    def data_listcontainsitem(self, name, item):
        return any(equals(value, item) for value in self._list(name))

    def data_showlist(self, name):
        monitor = self._get_list_monitor(name)
        if monitor:
            monitor.show()

    def data_hidelist(self, name):
        monitor = self._get_list_monitor(name)
        if monitor:
            monitor.hide()

    ##
    # Creation of variables and lists
    #

    def _check_new_name(self, name, attribute, kind, all_sprites):
        if name in getattr(self.stage, attribute) or name in getattr(self, attribute):
            raise ValueError(tr(kind + "_exists", name=name))
        if all_sprites:
            for sprite in self.stage.sprites:
                if name in getattr(sprite, attribute):
                    raise ValueError(tr(kind + "_exists", name=name))

    def pystage_makevariable(self, name, value=0, all_sprites=True):
        # A variable name must be unique for a sprite and globally.
        # The same name for local variables of different sprites is allowed!
        self._check_new_name(name, "variables", "variable", all_sprites)
        owner = self.stage if all_sprites else self
        owner.variables[name] = value
        monitor = Monitor(owner, name)
        monitor.hide()
        monitor.set_function(lambda: owner.variables[name])
        owner.var_monitors[name] = monitor

    def pystage_makelistvariable(self, name, values=None, all_sprites=True):
        self._check_new_name(name, "list_variables", "list", all_sprites)
        owner = self.stage if all_sprites else self
        owner.list_variables[name] = list(values) if values else []
        monitor = Monitor(owner, name, style=Monitor.LIST)
        monitor.hide()
        monitor.set_function(lambda: owner.list_variables[name])
        owner.list_monitors[name] = monitor

    ##
    # Monitors
    #

    def pystage_setmonitorposition(self, name, x, y):
        monitor = self._get_monitor(name)
        if monitor:
            monitor.set_position(x, y)

    def pystage_setlistmonitorposition(self, name, x, y, width=None, height=None):
        monitor = self._get_list_monitor(name)
        if monitor:
            monitor.set_size(width, height)
            monitor.set_position(x, y)

    def pystage_setmonitorstyle_large(self, name):
        monitor = self._get_monitor(name)
        if monitor:
            monitor.set_style(Monitor.LARGE)

    def pystage_setmonitorstyle_normal(self, name):
        monitor = self._get_monitor(name)
        if monitor:
            monitor.set_style(Monitor.NORMAL)

    def pystage_setmonitorstyle_slider(self, name):
        monitor = self._get_monitor(name)
        if monitor:
            monitor.set_style(Monitor.SLIDER)
