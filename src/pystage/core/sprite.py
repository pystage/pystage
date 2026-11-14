import pygame


# Mixins
from pystage.core._events import _Events
from pystage.core._motion import _Motion
from pystage.core._sensing import _Sensing, _SensingSprite
from pystage.core._looks import _LooksSprite
from pystage.core._pen import _Pen
from pystage.core._variables import _Variables
from pystage.core._operators import _Operators
from pystage.core._control import _ControlSprite
from pystage.core._sound import _Sound


class CoreSprite(_Motion, _Events, _LooksSprite, _Sound, _Sensing, _SensingSprite, _ControlSprite, _Operators, _Variables, _Pen):

    def __init__(self, stage, costume="default"):
        self.stage = stage
        # Above attributes need to be set first so that mixins can access them properly
        super().__init__()
        # Placeholder until a costume is added
        self.image = pygame.Surface((1, 1), flags=pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        if costume:
            self.pystage_addcostume(costume)
            self.name = "Sprite" if costume=="default" else costume 
        else:
            self.name = "Sprite"
        # The facade is the translated API
        self.facade = None
        # Make sure that the core sprite can always be accessed via _core
        self._core = self


    def pystage_setname(self, name):
        self.name = name


    def update(self, dt):
        self.code_manager._update(dt)
        self.costume_manager.update_sprite_image()

    def __str__(self):
        return self.name
