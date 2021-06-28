import pygame
import pkg_resources


# Mixins
from pystage.core._events import _Events
from pystage.core._motion import _Motion
from pystage.core._sensing import _Sensing, _SensingSprite
from pystage.core._looks_sprite import _LooksSprite
from pystage.core._pen import _Pen
from pystage.core._variables import _Variables
from pystage.core._operators import _Operators
from pystage.core._control import _Control
from pystage.core._control_sprite import _ControlSprite
from pystage.core._sound import _Sound


class CoreSprite(_Motion, _Events, _LooksSprite, _Sound, _Sensing, _SensingSprite, _Control, _ControlSprite, _Operators, _Variables, _Pen):

    def __init__(self, stage, costume="default"):
        super().__init__()
        self.stage = stage
        self.pystage_addcostume(costume)
        # The facade is the translated API
        self.facade = None




    def _draw(self, surface: pygame.Surface):
        image = self.costume_manager.get_image()
        if not image:
            return
        center_x, center_y = self.costume_manager.get_center()
        # Rotation
        # Scratch is clockwise with 0 upwards
        # pyGame is counterclockwise with 0 to the right
        transformed = pygame.transform.rotate(image, 90-self.direction)
        # keep the center stable when the image size changes
        # TODO: this is only correct when the rotation center is at the center
        # This is currently always the case with Scratch
        # Otherwise, it gets more complicated, the goal would be that the center point
        # remains stable within the image, i.e. if we have it for instance on an eye,
        # it remains on the eye during all transformations.
        offset_x = (image.get_width() - transformed.get_width()) / 2 - center_x
        offset_y = (image.get_height() - transformed.get_height()) / 2 - center_y
        surface.blit(transformed, self._pg_pos((offset_x, offset_y)))
        self.bubble_manager._draw(surface)


    def _update(self, dt):
        self.code_manager._update(dt)


    def _pg_pos(self, offset=(0,0)):
        return (self.x + self.stage.center_x + offset[0], 
                self.y + self.stage.center_y + offset[1])
