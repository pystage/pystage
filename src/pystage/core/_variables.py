from pystage.core._base_sprite import BaseSprite
from pystage.core.monitors import Monitor

BUILTIN_VAR_MAP = {
    # Stage
    "timer": "sensing_timer",
    "backdrop_number": "looks_backdropnumbername_number",
    "backdrop_name": "looks_backdropnumbername_name",
    "answer": "sensing_answer",
    "loudness": "sensing_loudness",
    "username": "sensing_username",
    "volume": "sound_volume",
    "current_year": "sensing_current_year",
    "current_month": "sensing_current_month",
    "current_date": "sensing_current_date",
    "current_dayofweek": "sensing_current_dayofweek",
    "current_hour": "sensing_current_hour",
    "current_minute": "sensing_current_minute",
    "current_second": "sensing_current_second",
    # Sprite
    "x_position": "motion_xposition",
    "y_position": "motion_yposition",
    "direction": "motion_direction",
    "size": "looks_size",
    "costume_number": "looks_costumenumbername_number",
    "costume_name": "looks_costumenumbername_name",
}


class _Variables(BaseSprite):
    # Also monitors

    # Implementation needs to be aware of naming conflicts and raise Exceptions if a name
    # is used both globally and locally.

    # global variables are stored in stage (stage variables are global in Scratch)
    # local variables are stored in the sprite
    # dictionaries are used to store the variables

    # if a var was created in a stage(for all sprites),
    # then sprites can access it, but can't create a var with the same name
    # if a var was created in a sprite(for single sprite),
    # then the stage can't access it, but other sprites can create a var with the same name

    def __init__(self):
        super().__init__()
        self.variables = {}
        self.list_variables: dict[str, list] = {}
        self.var_monitors = {}
        self.list_monitors = {}
        self.builtin_monitors = {}
        self.is_stage = (type(self) == type(self.stage))

    def pystage_makevariable(self, name, value=0, all_sprites=True):
        # Make sure a variable name is unique for a sprite or globally.
        # Same name for local variables is allowed!
        self._raise_if_var_exists(name)
        if all_sprites:
            for sprite in self.stage.sprites:
                if name in sprite.variables:
                    raise ValueError(f"The variable {name} already exists!")

        monitor = Monitor(self, name)
        monitor.hide()
        monitor.set_function(lambda: self.data_variable(name))

        if not all_sprites:
            self.variables[name] = value
            self.var_monitors[name] = monitor
        else:
            self.stage.variables[name] = value
            self.stage.var_monitors[name] = monitor

    def pystage_makelistvariable(self, name, value=[], all_sprites=True):
        self._raise_if_list_exists(name)
        if all_sprites:
            for sprite in self.stage.sprites:
                if name in sprite.list_variables:
                    raise ValueError(
                        f"The list variable {name} already exists!")

        monitor = Monitor(self, name, is_list=True)
        monitor.hide()
        monitor.set_function(lambda: self.data_listvariable(name))

        if not all_sprites:
            self.list_variables[name] = value
            self.list_monitors[name] = monitor
        else:
            self.stage.list_variables[name] = value
            self.stage.list_monitors[name] = monitor

    def data_variable(self, name):
        self._raise_if_var_not_exists(name)
        if name in self.variables:
            return self.variables[name]
        else:
            return self.stage.variables[name]

    def data_listvariable(self, name):
        self._raise_if_list_not_exists(name)
        if name in self.list_variables:
            return self.list_variables[name]
        else:
            return self.stage.list_variables[name]

    def data_showbuiltinvariable(self, name, x=None, y=None, style=None):
        monitor = self._get_builtin_monitor(name)
        if not monitor:
            monitor_title = name if self.is_stage else f"{self.name}: {name}"
            sprite_or_stage = self.stage if self.is_stage else self

            monitor = Monitor(self, monitor_title, Monitor.SENSING_COLOR)
            sprite_or_stage.builtin_monitors[name] = monitor

            # callback might be an attribute in the future
            def callback():
                try:
                    return func() if callable((func := getattr(self, BUILTIN_VAR_MAP[name]))) else func
                except (AttributeError, KeyError):
                    sprite_or_stage = "Stage" if self.is_stage else "Sprite"
                    raise ValueError(
                        f"\"{name}\" is not a built-in variable for {sprite_or_stage}."
                    )

            monitor.set_function(callback)
        else:
            monitor.show()
        if x and y:
            monitor.set_position(x, y)
        if style:
            monitor.set_style(style)

    def data_hidebuiltinvariable(self, name):
        monitor = self._get_builtin_monitor(name)
        if not monitor:
            return
        monitor.hide()

    def data_showvariable(self, name, x=None, y=None, style=None):
        # Use smart positioning or old position, if we have one.
        monitor = self._get_var_monitor(name)
        if not monitor:
            return
        if x and y:
            monitor.set_position(x, y)
        if style:
            monitor.set_style(style)
        monitor.show()

    def data_hidevariable(self, name):
        monitor = self._get_var_monitor(name)
        if not monitor:
            return
        monitor.hide()

    def data_showlist(self, list_variable, x=None, y=None):
        monitor = self._get_list_monitor(list_variable)
        if not monitor:
            return
        if x and y:
            monitor.set_position(x, y)
        monitor.show()

    def data_hidelist(self, list_variable):
        monitor = self._get_list_monitor(list_variable)
        if not monitor:
            return
        monitor.hide()

    def data_setvariableto(self, name, value):
        self._raise_if_var_not_exists(name)
        if name in self.variables:
            self.variables[name] = value
        else:
            self.stage.variables[name] = value

    def data_changevariableby(self, name, value):
        self._raise_if_var_not_exists(name)
        if name in self.variables:
            self.variables[name] += value
        else:
            self.stage.variables[name] += value

    def data_addtolist(self, list_variable, value):
        self._raise_if_list_not_exists(list_variable)
        if list_variable in self.list_variables:
            self.list_variables[list_variable].append(value)
        else:
            self.stage.list_variables[list_variable].append(value)

    def data_deleteoflist(self, list_variable, position):
        self._raise_if_list_not_exists(list_variable)
        if list_variable in self.list_variables and (1 <= position <= len(self.list_variables[list_variable])):
            del self.list_variables[list_variable][position-1]
        elif 1 <= position <= len(self.stage.list_variables[list_variable]):
            del self.stage.list_variables[list_variable][position-1]

    def data_deletealloflist(self, list_variable):
        self._raise_if_list_not_exists(list_variable)
        if list_variable in self.list_variables:
            self.list_variables[list_variable].clear()
        else:
            self.stage.list_variables[list_variable].clear()

    def data_insertatlist(self, list_variable, value, position):
        self._raise_if_list_not_exists(list_variable)
        if list_variable in self.list_variables and (1 <= position <= len(self.list_variables[list_variable])+1):
            self.list_variables[list_variable].insert(position-1, value)
        elif 1 <= position <= len(self.stage.list_variables[list_variable])+1:
            self.stage.list_variables[list_variable].insert(position-1, value)

    def data_replaceitemoflist(self, list_variable, position, value):
        self._raise_if_list_not_exists(list_variable)
        if list_variable in self.list_variables and (1 <= position <= len(self.list_variables[list_variable])):
            self.list_variables[list_variable][position-1] = value
        elif 1 <= position <= len(self.stage.list_variables[list_variable]):
            self.stage.list_variables[list_variable][position-1] = value

    def data_itemoflist(self, list_variable, position):
        self._raise_if_list_not_exists(list_variable)
        if list_variable in self.list_variables:
            if 1 <= position <= len(self.list_variables[list_variable]):
                return self.list_variables[list_variable][position-1]
        elif 1 <= position <= len(self.stage.list_variables[list_variable]):
            return self.stage.list_variables[list_variable][position-1]
        # Return empty string because Scratch returns empty string
        return ""

    def data_itemnumoflist(self, list_variable, value):
        self._raise_if_list_not_exists(list_variable)
        if list_variable in self.list_variables:
            if value in self.list_variables[list_variable]:
                return self.list_variables[list_variable].index(value)+1
        elif value in self.stage.list_variables[list_variable]:
            return self.stage.list_variables[list_variable].index(value)+1
        return 0

    def data_lengthoflist(self, list_variable):
        self._raise_if_list_not_exists(list_variable)
        if list_variable in self.list_variables:
            return len(self.list_variables[list_variable])
        return len(self.stage.list_variables[list_variable])

    def data_listcontainsitem(self, list_variable, value):
        self._raise_if_list_not_exists(list_variable)
        if list_variable in self.list_variables:
            return value in self.list_variables[list_variable]
        return value in self.stage.list_variables[list_variable]

    def pystage_setmonitorposition(self, name, x, y):
        monitor = self._get_monitor(name)
        if not monitor:
            return
        monitor.set_position(x, y)

    def pystage_setmonitorstyle_large(self, name):
        monitor = self._get_monitor(name)
        if not monitor:
            return
        monitor.set_style(Monitor.LARGE)

    def pystage_setmonitorstyle_normal(self, name):
        monitor = self._get_monitor(name)
        if not monitor:
            return
        monitor.set_style(Monitor.NORMAL)

    def pystage_setmonitorstyle_slider(self, name):
        monitor = self._get_monitor(name)
        if not monitor:
            return
        monitor.set_style(Monitor.SLIDER)

    def _get_var_monitor(self, name):
        return self.stage.var_monitors.get(name) or self.var_monitors.get(name)

    def _get_list_monitor(self, name):
        return self.stage.list_monitors.get(name) or self.list_monitors.get(name)

    def _get_builtin_monitor(self, name):
        return self.stage.builtin_monitors.get(name) or self.builtin_monitors.get(name)

    def _raise_if_var_not_exists(self, name):
        if name not in self.variables and name not in self.stage.variables:
            raise ValueError(f"The variable \"{name}\" does not exist.")

    def _raise_if_var_exists(self, name):
        if name in self.variables or name in self.stage.variables:
            raise ValueError(f"The variable \"{name}\" already exists.")

    def _raise_if_list_not_exists(self, name):
        if name not in self.list_variables and name not in self.stage.list_variables:
            raise ValueError(f"The list variable \"{name}\" does not exist.")

    def _raise_if_list_exists(self, name):
        if name in self.list_variables or name in self.stage.list_variables:
            raise ValueError(f"The list variable \"{name}\" already exists.")
