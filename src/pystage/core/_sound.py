import pygame
from pygame.mixer import music
import time


class _Sound:
    ##
    # Sound
    #

    # Like for costumes and backdrops, we need a class structure here.
    # Plus a global sound manager.
    def __init__(self):
        self.mixer = pygame.mixer
        self.mixer.init()

    def start_sound(self, sound, loop=0):
        channel = self.mixer.find_channel()
        channel.play(self.mixer.Sound(sound), loop)
        return channel

    def play_sound_until_done(self, sound):
        sound = self.mixer.Sound(sound)
        self.mixer.find_channel().play(sound, 0)
        time.sleep(sound.get_length())

    def stop_all_sounds(self):
        self.mixer.stop()

    def change_sound_effect_by(self, effect, value):
        # TODO: for pitching an paning there is no readey to use code in pygame. To do so
        # we must operate on the audio array itself.

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
        value *= 0.01
        actual_volume = music.get_volume()
        music.set_volume(actual_volume + value)

    @staticmethod
    def set_volume_to_percent(percent):
        percent *= 0.01
        music.set_volume(percent)

    @staticmethod
    def get_volume():
        return music.get_volume() * 100
