import pygame
from pystage.core.assets import SoundManager
from pystage.core._base_sprite import BaseSprite
from pystage.core.values import to_number


class _Sound(BaseSprite):

    def __init__(self):
        super().__init__()
        self.sound_manager = SoundManager(self)
        if not pygame.mixer.get_init():
            try:
                pygame.mixer.init()
                pygame.mixer.set_num_channels(32)
            except pygame.error as e:
                print(f"WARNING: No sound available. ({e})")
        # Each sprite and the stage has its own volume and effects.
        self.current_pan = 0
        self.current_pitch = 0
        self.current_volume = 100
        # The channels this sprite is currently playing on.
        self._channels = []
        # sound name: channel
        self._playing = {}


    def pystage_addsound(self, name):
        self.sound_manager.add_sound(name)


    def _play(self, name, loop=0):
        """Start a sound and return it, None if it can't be played."""
        if not pygame.mixer.get_init():
            return None
        sound = self.sound_manager.get_sound(name, self.current_pitch)
        if sound is None:
            return None
        # Like in Scratch, a sound that is still playing is started again.
        channel = self._playing.get(name)
        if channel is not None and channel in self._channels and channel.get_busy():
            channel.stop()
        else:
            channel = pygame.mixer.find_channel()
        if channel is None:
            print(f"WARNING: No more free sound channels. Can't play '{name}'.")
            return None
        self._channels = [c for c in self._channels if c.get_busy() and c is not channel]
        self._channels.append(channel)
        self._playing[name] = channel
        self._apply(channel)
        channel.play(sound, loop)
        return sound

    def sound_play(self, name, loop=0):
        self._play(name, loop)

    def sound_playuntildone(self, name):
        sound = self._play(name)
        if sound is not None:
            self.code_manager.current_block.add_to_wait_time = sound.get_length()

    def sound_stopallsounds(self):
        if pygame.mixer.get_init():
            pygame.mixer.stop()

    def sound_changeeffectby_pitch(self, value):
        self.sound_seteffectto_pitch(self.current_pitch + to_number(value))

    sound_changeeffectby_pitch.opcode = "sound_changeeffectby"
    sound_changeeffectby_pitch.param = "EFFECT"
    sound_changeeffectby_pitch.value = "PITCH"
    sound_changeeffectby_pitch.translation = "sound_effects_pitch"

    def sound_changeeffectby_pan(self, value):
        self.sound_seteffectto_pan(self.current_pan + to_number(value))

    sound_changeeffectby_pan.opcode = "sound_changeeffectby"
    sound_changeeffectby_pan.param = "EFFECT"
    sound_changeeffectby_pan.value = "PAN"
    sound_changeeffectby_pan.translation = "sound_effects_pan"

    def sound_seteffectto_pitch(self, value):
        # -360 to 360, 10 is a half-step, 120 an octave.
        # The pitch is used for sounds that are started from now on.
        self.current_pitch = min(360, max(-360, to_number(value)))

    sound_seteffectto_pitch.opcode = "sound_seteffectto"
    sound_seteffectto_pitch.param = "EFFECT"
    sound_seteffectto_pitch.value = "PITCH"
    sound_seteffectto_pitch.translation = "sound_effects_pitch"

    def sound_seteffectto_pan(self, value):
        # Values from -100 (left) to 100 (right)
        self.current_pan = min(100, max(-100, to_number(value)))
        self._apply()

    sound_seteffectto_pan.opcode = "sound_seteffectto"
    sound_seteffectto_pan.param = "EFFECT"
    sound_seteffectto_pan.value = "PAN"
    sound_seteffectto_pan.translation = "sound_effects_pan"

    def sound_cleareffects(self):
        self.current_pan = 0
        self.current_pitch = 0
        self._apply()

    def _apply(self, channel=None):
        """Apply volume and pan to one or all channels of this sprite."""
        volume = self.current_volume / 100
        left = volume * min(1, (100 - self.current_pan) / 100)
        right = volume * min(1, (100 + self.current_pan) / 100)
        self._channels = [c for c in self._channels if c.get_busy() or c is channel]
        for c in ([channel] if channel else self._channels):
            c.set_volume(left, right)

    def sound_changevolumeby(self, value):
        self.sound_setvolumeto(self.current_volume + to_number(value))

    def sound_setvolumeto(self, value):
        self.current_volume = min(100, max(0, to_number(value)))
        self._apply()

    def sound_volume(self):
        return self.current_volume
