from pygame.mixer import music
import pygame


class _Sound:
    ##
    # Sound
    #

    # Like for costumes and backdrops, we need a class structure here.
    # Plus a global sound manager.
    def __init__(self):
        self.mixer = pygame.mixer
        self.mixer.init()

    def start_sound(self, sound, loop=-1):
        channel = self.mixer.find_channel()
        channel.play(self.mixer.Sound(sound), loop)
        return channel

    def play_sound_until_done(self, sound):
        return self.start_sound(sound, 0)

    def stop_all_sounds(self):
        self.mixer.stop()

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

    @staticmethod
    def change_volume_by(value):
        actual_volume = music.get_volume()
        music.set_volume(actual_volume + value)

    @staticmethod
    def set_volume_to_percent(percent):
        music.set_volume(percent)

    @staticmethod
    def get_volume():
        return music.get_volume()
