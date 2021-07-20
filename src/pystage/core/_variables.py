from pystage.core._base_sprite import BaseSprite

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

    def data_setvariableto(self, name, value):
        if name in self.variables:
            self.variables[name] = value
        elif name in self.stage.variables:
            self.stage.variables[name] = value
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
        elif name in self.stage.variables:
            self.stage.variables[name] += value
        else:
            raise ValueError(f"The variable {name} does not exist.")

    def data_showvariable(self, name):
        # Use smart positioning or old position, if we have one.
        pass

    def data_hidevariable(self, name):
        pass

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

        if not all_sprites:
            self.variables[name]=None
        else:
            self.stage.variables[name]=None

    def pystage_setmonitorposition(self, name, x, y):
        pass
