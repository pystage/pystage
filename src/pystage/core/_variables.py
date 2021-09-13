from pystage.core._base_sprite import BaseSprite
from pystage.core.monitors import Monitor

class _Variables(BaseSprite):
    # Also monitors

    # Implementation needs to be aware of naming conflicts and raise Exceptions if a name
    # is used both globally and locally.

    # global variables are stored in stage (stage variables are global in Scratch)
    # local variables are stored in the sprite
    # dictionaries are used to store the variables

    def __init__(self):
        super().__init__()

        self.variables = {}
        self.monitors = {}


    def data_setvariableto(self, name, value):
        if name in self.variables:
            self.variables[name] = value
            self.monitors[name].set_value(value)
        elif name in self.stage.variables:
            self.stage.variables[name] = value
            self.stage.monitors[name].set_value(value)
        else:
            raise ValueError(f"The variable {name} does not exist.")


    def data_variable(self, name):
        if name in self.variables:
            return self.variables[name]
        elif name in self.stage.variables:
            return self.stage.variables[name]
        else:
            raise ValueError(f"The variable {name} does not exist.")


    def data_changevariableby(self, name, value):
        if name in self.variables:
            self.variables[name] += value
            self.monitors[name].set_value(self.variables[name])
        elif name in self.stage.variables:
            self.stage.variables[name] += value
            self.stage.monitors[name].set_value(self.stage.variables[name])
        else:
            raise ValueError(f"The variable {name} does not exist.")

    def data_showvariable(self, name):
        # Use smart positioning or old position, if we have one.
        monitor = None
        if name in self.monitors:
            monitor = self.monitors[name]
        elif name in self.stage.monitors:
            monitor = self.stage.monitors[name]
        if not monitor:
            return
        monitor.show()


    def data_hidevariable(self, name):
        monitor = None
        if name in self.monitors:
            monitor = self.monitors[name]
        elif name in self.stage.monitors:
            monitor = self.stage.monitors[name]
        if not monitor:
            return
        monitor.hide()


    def pystage_makevariable(self, name, all_sprites=True):
        # Make sure a variable name is unique for a sprite or globally. 
        # Same name for local variables is allowed!
        if name in self.stage.variables:
            raise ValueError(f"The variable {name} already exists!")
        if name in self.variables:
            raise ValueError(f"The variable {name} already exists!")
        if all_sprites:
            for sprite in self.stage.sprites:
                if name in sprite.variables:
                    raise ValueError(f"The variable {name} already exists!")

        monitor = Monitor(self, name, 0)
        monitor.hide()

        if not all_sprites:
            self.variables[name]=0
            self.monitors[name] = monitor
        else:
            self.stage.variables[name]=0
            self.stage.monitors[name] = monitor


    def pystage_setmonitorposition(self, name, x, y):
        monitor = None
        if name in self.monitors:
            monitor = self.monitors[name]
        elif name in self.stage.monitors:
            monitor = self.stage.monitors[name]
        if not monitor:
            return
        monitor.set_position(x, y)
