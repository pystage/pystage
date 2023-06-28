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
        self.list_variables = {}
        self.monitors = {}


    def _get_monitor(self, name):
        if name in self.monitors:
            return self.monitors[name]
        elif name in self.stage.monitors:
            return self.stage.monitors[name]
        return None


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

    def data_listvariable(self, name):
        if name in self.list_variables:
            return self.list_variables[name]
        elif name in self.stage.list_variables:
            return self.stage.list_variables[name]
        else:
            raise ValueError(f"The list variable {name} does not exist.")

    def data_changevariableby(self, name, value):
        if name in self.variables:
            self.variables[name] += value
        elif name in self.stage.variables:
            self.stage.variables[name] += value
        else:
            raise ValueError(f"The variable {name} does not exist.")

    def data_showvariable(self, name):
        # Use smart positioning or old position, if we have one.
        monitor = self._get_monitor(name)
        if not monitor:
            return
        monitor.show()


    def data_hidevariable(self, name):
        monitor = self._get_monitor(name)
        if not monitor:
            return
        monitor.hide()
    # This function is used for variables in scratch that are built in like timer, answer and xposition
    def data_showbuiltinvariable(self, name):
        pass
   
    def data_initializelist(self, list_variable, list_of_values, value):
        # This function is used to display the entire list
        # Lists are used in scratch for sprites and stages
        if list_variable not in self.list_variables:
            self.list_variables[list_variable] = []
        self.list_variables[list_variable].extend(list_of_values)
        return self.list_variables[list_variable]
   
    def data_addtolist(self, list_variable, value):
        if list_variable not in self.list_variables:
            self.list_variables[list_variable] = []
        self.list_variables[list_variable].append(value)
        if list_variable not in self.stage.list_variables:
            self.stage.list_variables[list_variable] = []
        self.stage.list_variables[list_variable].append(value)
        
    def data_deleteoflist(self, list_variable, position):
        if list_variable in self.list_variables:
            del self.list_variables[list_variable][position]
        elif list_variable in self.stage.list_variables:
            del self.stage.list_variables[list_variable][position]
            
    def data_deletealloflist(self, list_variable):
        if list_variable in self.list_variables:
            self.list_variables[list_variable].clear()
        if list_variable in self.stage.list_variables:
            self.stage.list_variables[list_variable].clear()
        
    def data_insertatlist(self, list_variable, value, position):
        if list_variable in self.list_variables:
            self.list_variables[list_variable].insert(position, value)
        elif list_variable in self.stage.list_variables:
            self.stage.list_variables[list_variable].insert(position, value) 
            
    def data_replaceitemoflist(self, list_variable, value, position):
        if list_variable in self.list_variables:
            self.list_variables[list_variable][position] = value
        elif list_variable in self.stage.list_variables:
            self.stage.list_variables[list_variable][position] = value
            
    def data_itemoflist(self, list_variable, position):
        if list_variable in self.list_variables:
            return self.list_variables[list_variable][position]
        if list_variable in self.stage.list_variables:
            return self.stage.list_variables[list_variable][position] 
    
    def data_itemnumoflist(self, list_variable, value):
        if list_variable in self.list_variables:
            if value in self.list_variables[list_variable]:
                return self.list_variables[list_variable].index(value) 
        if list_variable in self.stage.list_variables:
            if value in self.stage.list_variables[list_variable]:
                return self.stage.list_variables[list_variable].index(value)       
    
    def data_lengthoflist(self, list_variable):
        if list_variable in self.list_variables:
            return len(self.list_variables[list_variable])
        elif list_variable in self.stage.list_variables:
            return len(self.stage.list_variables[list_variable])
        
    def data_listcontainsitem(self, list_variable, value):
        if list_variable in self.list_variables:
            if value in self.list_variables[list_variable]:
                return True
        if list_variable in self.stage.list_variables:
            if value in self.stage.list_variables[list_variable]:
                return True
        
    
    def data_showlist(self, list_variable):
        pass
    
    def data_hidelist(self, list_variable):
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

        monitor = Monitor(self, name)
        monitor.hide()
        monitor.set_function(lambda: self.data_variable(name))

        if not all_sprites:
            self.variables[name]=0
            self.monitors[name] = monitor
        else:
            self.stage.variables[name] = 0
            self.stage.monitors[name] = monitor

    def pystage_makelistvariable(self, name, all_sprites=True):
        # Make sure a list variable name is unique for a sprite or globally.
        # Same name for local variables is allowed!

        # We can have a variable and list variable with the same name, but
        # we use Monitors for both, and access them via the name/title.
        # So, we need to uniquify the list variables' names. Thus, we add '[]'
        # to the name.
        name = name + '[]'

        if name in self.stage.list_variables:
            raise ValueError(f"The list variable {name} already exists!")
        if name in self.variables:
            raise ValueError(f"The list variable {name} already exists!")
        if all_sprites:
            for sprite in self.stage.sprites:
                if name in sprite.list_variables:
                    raise ValueError(f"The list variable {name} already exists!")

        monitor = Monitor(self, name)
        monitor.hide()
        monitor.set_function(lambda: self.data_listvariable(name))

        if not all_sprites:
            self.list_variables[name] = []
            self.monitors[name] = monitor
        else:
            self.stage.list_variables[name] = 0
            self.stage.monitors[name] = monitor


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
