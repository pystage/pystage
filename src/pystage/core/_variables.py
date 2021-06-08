class _Variables():
    ##
    # Variables
    #

    # Of course usual variables can be used. This 
    # is for a direct translation of Scratch code.
    # To learn dictionaries and lists, we only provide
    # dictionaries for storage, value can be arbitrary, including lists
    # global variables are stored in the stage.
    # Not sure if we document sprite.variables["name"]/stage.variables["name"]
    # Or just implement the following blocks:

    def set_local_variable(self, name, value):
        # Managed in a sprite dictionary
        pass

    def set_global_variable(self, name, value):
        # Managed in a global dictionary
        pass

    def get_local_variable(self, name):
        # Managed in a sprite dictionary
        pass

    def get_global_variable(self, name):
        # Managed in a global dictionary
        pass

    # Showing of variables is tricky.
    # Scratch provides drag and drop for the position. Do we?
    def show_local_variable(self, name):
        # Use smart positioning or old position, if we have one.
        pass

    def show_global_variable(self, name):
        pass

    def show_local_variable_at(self, name, x, y):
        pass

    def show_global_variable_at(self, name, x, y):
        pass

    def hide_local_variable(self, name):
        pass

    def hide_global_variable(self, name):
        pass

