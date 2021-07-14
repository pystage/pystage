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
        if costume:
            self.pystage_addcostume(costume)
        # The facade is the translated API
        self.facade = None


    def blitRotate(self, surf, image, pos, originPos, angle, zoom):
        # https://stackoverflow.com/questions/54462645/how-to-rotate-an-image-around-its-center-while-its-scale-is-getting-largerin-py

        # calcaulate the axis aligned bounding box of the rotated image
        w, h       = image.get_size()
        box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
        box_rotate = [p.rotate(angle) for p in box]
        min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
        max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

        # calculate the translation of the pivot 
        pivot        = pygame.math.Vector2(originPos[0], -originPos[1])
        pivot_rotate = pivot.rotate(angle)
        pivot_move   = pivot_rotate - pivot

        # calculate the upper left origin of the rotated image
        move   = (-originPos[0] + min_box[0] - pivot_move[0], -originPos[1] - max_box[1] + pivot_move[1])
        origin = (pos[0] + zoom * move[0], pos[1] + zoom * move[1])

        # get a rotated image
        rotozoom_image = pygame.transform.rotozoom(image, angle, zoom)
      
        # rotate and blit the image
        surf.blit(rotozoom_image, origin)

        # draw rectangle around the image
        # pygame.draw.rect (surf, (255, 0, 0), (*origin, *rotozoom_image.get_size()),2)


    def _draw(self, surface: pygame.Surface):
        image = self.costume_manager.get_image()
        if not image:
            return
        # center_x, center_y = self.costume_manager.get_center()
        # transformed = image
        # Rotation
        # Scratch is clockwise with 0 upwards
        # pyGame is counterclockwise with 0 to the right
        # transformed = pygame.transform.rotozoom(transformed, 90-self.direction, self.size/100)
        # keep the center stable when the image size changes
        # TODO: this is only correct when the rotation center is at the center
        # This is currently always the case with Scratch
        # Otherwise, it gets more complicated, the goal would be that the center point
        # remains stable within the image, i.e. if we have it for instance on an eye,
        # it remains on the eye during all transformations.
        # offset_x = (image.get_width() - transformed.get_width()) / 2 - center_x
        # offset_y = (image.get_height() - transformed.get_height()) / 2 - center_y
        # surface.blit(transformed, self._pg_pos((offset_x, offset_y)))
        self.blitRotate(surface, image, self._pg_pos(), self.costume_manager.get_center(), 90-self.direction, self.size/100) 
        self.bubble_manager._draw(surface)


    def _update(self, dt):
        self.code_manager._update(dt)


    def _pg_pos(self, offset=(0,0)):
        return (self.x + self.stage.center_x + offset[0], 
                -self.y + self.stage.center_y + offset[1])
