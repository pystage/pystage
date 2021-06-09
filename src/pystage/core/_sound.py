import pygame
from pygame.mixer import music
import time


class _Sound:

    # Like for costumes and backdrops, we need a class structure here.
    # Plus a global sound manager.
    def __init__(self):
        self.mixer = pygame.mixer
        self.mixer.init(channels=2)
        self.actual_pan = 0
        self.actual_pitch = 0

    def sound_play(self, sound, loop=0):
        channel = self.mixer.find_channel()
        channel.play(self.mixer.Sound(sound), loop)
        return channel

    def sound_playuntildone(self, sound):
        sound = self.mixer.Sound(sound)
        self.mixer.find_channel().play(sound, 0)
        time.sleep(sound.get_length())

    def sound_stopallsounds(self):
        self.mixer.stop()

    def sound_changeeffectby_pitch(self, value):
        # TODO: for pitching there is no ready to use code in pygame. To do so
        # we must operate on the audio array itself.

        # Similar to graphics effects
        # - pitch
        # - pan left/right
        # as volume is separate and we have only two effects,
        # it might be better to just create different methods.
        pass

    sound_changeeffectby_pitch.opcode = "sound_changeeffectby"
    sound_changeeffectby_pitch.param = "EFFECT"
    sound_changeeffectby_pitch.value = "PITCH"

    def sound_changeeffectby_pan(self, value):
        # norm pan value from -100/100 to range 0/1
        self.actual_pan = (value + 100) / 200
        self._apply_pan()

    sound_changeeffectby_pitch.opcode = "sound_changeeffectby"
    sound_changeeffectby_pitch.param = "EFFECT"
    sound_changeeffectby_pitch.value = "PAN"

    def sound_seteffectto(self, effect, value):
        pass

    def sound_cleareffects(self):
        self.actual_pan = 0
        self._apply_pan()

        self.actual_pitch = 0
        # apply pitch

    def _apply_pan(self):
        for channel_id in range(self.mixer.get_num_channels()):
            if self.actual_pan > 0.5:
                self.mixer.Channel(channel_id).set_volume(1, 0)
            else:
                self.mixer.Channel(channel_id).set_volume(0, 1)

    def sound_changevolumeby(self, value):
        value /= 100
        for channel_id in range(self.mixer.get_num_channels()):
            actual_volume = self.mixer.Channel(channel_id).get_volume()
            self.mixer.Channel(channel_id).set_volume(actual_volume + value)

    def sound_setvolumeto(self, value):
        value /= 100
        for channel_id in range(self.mixer.get_num_channels()):
            self.mixer.Channel(channel_id).set_volume(value)

    def sound_volume(self):
        # as we hide the channel mechanic, we assume all channels are set to the same volume
        return self.mixer.Channel(0).get_volume() * 100

    def sound_sounds_menu(self):
        """
        Toggle sound menu.

        Returns
        -------
        None
        """
        pass
