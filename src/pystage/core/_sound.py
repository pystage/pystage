import pygame
from pygame.mixer import music
from pystage.core.assets import SoundManager
from pystage.core._base_sprite import BaseSprite
import time


class _Sound(BaseSprite):

    # Like for costumes and backdrops, we need a class structure here.
    # Plus a global sound manager.
    def __init__(self):
        super().__init__()
        self.sound_manager = SoundManager(self)
        self.mixer = pygame.mixer
        self.mixer.init(channels=2)
        self.current_pan = 0
        self.current_pitch = 0
        self.current_volume = 100


    def pystage_addsound(self, name):
        self.sound_manager.add_sound(name)


    def sound_play(self, name, loop=0):
        channel = self.mixer.find_channel()
        sound = self.sound_manager.get_sound(name)
        if sound is not None:
            channel.play(sound, loop)
        return channel

    def sound_playuntildone(self, name):
        sound = self.sound_manager.get_sound(name)
        if sound is not None:
            self.mixer.find_channel().play(sound, 0)
            # time.sleep(sound.get_length())
            # This need to be done via wait time in code block
            # TODO: Add this function to yield blocks.
            self.code_manager.current_block.add_to_wait_time = sound.get_length()

    def sound_stopallsounds(self):
        self.mixer.stop()

    def sound_changeeffectby_pitch(self, value):
        # TODO: for pitching there is no ready to use code in pygame. To do so
        # we must operate on the audio array itself.
        # -360 to 360, 10 is a half-step, 120 an octave
        # changes only the speed of the sound
        pass

    sound_changeeffectby_pitch.opcode = "sound_changeeffectby"
    sound_changeeffectby_pitch.param = "EFFECT"
    sound_changeeffectby_pitch.value = "PITCH"
    sound_changeeffectby_pitch.translation = "sound_effects_pitch"

    def sound_changeeffectby_pan(self, value):
        # norm pan value from -100/100 to range 0/1
        self.current_pan += value
        self.current_pan = min(100, max(-100, self.current_pan))
        self._apply()

    sound_changeeffectby_pan.opcode = "sound_changeeffectby"
    sound_changeeffectby_pan.param = "EFFECT"
    sound_changeeffectby_pan.value = "PAN"
    sound_changeeffectby_pan.translation = "sound_effects_pan"

    def sound_seteffectto_pitch(self, value):
        # TODO: for pitching there is no ready to use code in pygame. To do so
        # we must operate on the audio array itself.
        pass

    sound_seteffectto_pitch.opcode = "sound_seteffectto"
    sound_seteffectto_pitch.param = "EFFECT"
    sound_seteffectto_pitch.value = "PITCH"
    sound_seteffectto_pitch.translation = "sound_effects_pitch"

    def sound_seteffectto_pan(self, value):
        # Values from -100 (left) to 100 (right)
        self.current_pan = value
        self.current_pan = min(100, max(-100, self.current_pan))
        self._apply()

    sound_seteffectto_pan.opcode = "sound_seteffectto"
    sound_seteffectto_pan.param = "EFFECT"
    sound_seteffectto_pan.value = "PAN"
    sound_seteffectto_pan.translation = "sound_effects_pan"

    def sound_cleareffects(self):
        self.current_pan = 0
        self.current_pitch = 0
        self._apply()

        # apply pitch

    def _apply(self):
        # norm pan value from -100/100 to range 0/1
        pgpan = (self.current_pan + 100) / 200
        pgvolume = self.current_volume / 100
        for channel_id in range(self.mixer.get_num_channels()):
            if pgpan > 0.5:
                self.mixer.Channel(channel_id).set_volume(1, 0)
            else:
                self.mixer.Channel(channel_id).set_volume(0, 1)

        for channel_id in range(self.mixer.get_num_channels()):
            self.mixer.Channel(channel_id).set_volume(pgvolume)

    def sound_changevolumeby(self, value):
        self.current_volume += value
        self.current_volume = min(100, max(0, self.current_volume))
        self._apply()

    def sound_setvolumeto(self, value):
        self.current_volume = value
        self.current_volume = min(100, max(0, self.current_volume))
        self._apply()

    def sound_volume(self):
        # as we hide the channel mechanic, we assume all channels are set to the same volume
        return self.mixer.Channel(0).get_volume() * 100

