class _LooksStage():

    def switch_backdrop_to(self, backdrop):
        pass

    def switch_backdrop_to_and_wait(self, backdrop):
        # Wait for any code under a "when backdrop is changed"
        pass

    def next_backdrop(self):
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

    def get_backdrop_number(self):
        pass

    def get_backdrop_name(self):
        pass
