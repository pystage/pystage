class _Looks():
    ##
    # Looks
    #
    def say_for_time(self, text, secs):
        pass


    def say(self, text):
        pass


    def think_for_time(self, text, secs):
        pass

    def think(self, text):
        pass

    def switch_costume_to(self, costume):
        # TODO: Data/class structure for costumes
        pass

    def next_costume(self):
        pass

    def switch_backdrop_to(self, backdrop):
        # Backdrops are for the stage.
        # In Scratch, a sprite can change the backdrop.
        pass

    def next_backdrop(self):
        pass

    def change_size_by(self, percent):
        # this is percentage
        pass

    def set_size_to_percent(self, percent):
        pass

    def change_graphic_effect_by(self, effect, value):
        # This is tricky, could be implemented in costumes.
        # Question: would one method per effect better/easier?
        # Effects: 
        # - color (this is hue shifting)
        # - fisheye
        # - whirl
        # - pixelate
        # - mosaic
        # - brightness
        # - ghost (this is transparency)
        pass

    def set_graphic_effect_to(self, effect, value):
        pass

    def clear_graphic_effects(self):
        pass

    def show(self):
        pass

    def hide(self):
        pass

    def go_to_front_layer(self, layer):
        pass

    def go_to_back_layer(self, layer):
        pass

    def go_forward_layers(self, value):
        pass

    def go_backward_layers(self, value):
        pass

    def get_costume_number(self):
        # 1-based
        pass

    def get_backdrop_number(self):
        pass


    def get_costume_name(self):
        pass

    def get_backdrop_name(self):
        pass

    def get_size(self):
        # percent
        pass

