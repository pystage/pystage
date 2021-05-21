class _Sound():
    ##
    # Sound
    #

    # Like for costumes and backdrops, we need a class structure here.
    # Plus a global sound manager.

    def play_sound_until_done(self, sound):
        pass

    def start_sound(self, sound):
        pass

    def stop_all_sounds(self):
        pass

    def change_sound_effect_by(self, effect, value):
        # Similar to graphics effects
        # - pitch
        # - pan left/right
        # as volume is separate and we have only two effects,
        # it might be better to just create different methods.
        pass

    def set_sound_effect_to(self, effect, value):
        pass

    def clear_sound_effects(self):
        pass

    def change_volume_by(self, value):
        # percent value
        pass

    def set_volume_to_percent(self, percent):
        pass

    def get_volume(self):
        pass

