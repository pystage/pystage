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
        pass

    def data_variable(self, name):
        pass

    def data_changevariableby(self, name, value):
        pass

    def data_showvariable(self, name):
        # Use smart positioning or old position, if we have one.
        pass

    def data_hidevariable(self, name):
        pass

    def pystage_makevariable(self, name, all_sprites=True):
        pass

    def pystage_setmonitorposition(self, name, x, y):
        pass
