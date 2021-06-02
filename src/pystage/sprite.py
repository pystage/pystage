import pygame

from pystage.code_block import CodeBlock, CodeManager
from pystage.costume import Costume, CostumeManager

# Mixins
from pystage._events import _Events
from pystage._motion import _Motion
from pystage._sensing import _Sensing, _SensingSprite
from pystage._looks_sprite import _LooksSprite
from pystage._pen import _Pen
from pystage._variables import _Variables
from pystage._control import _Control
from pystage._control_sprite import _ControlSprite
from pystage._sound import _Sound


class Sprite(_Motion, _Events, _LooksSprite, _Sound, _Sensing, _SensingSprite, _Control, _ControlSprite, _Variables, _Pen):

    def __init__(self, stage, costume="default"):
        self.x = 0.0
        self.y = 0.0
        self.direction = 90
        self.pen = False
        self.color = (255,0,0)
        self.stage = stage

        self.costume_manager = CostumeManager(self)
        self.code_manager = CodeManager(self)

        self.add_costume(costume)


    def add_costume(self, name, center_x=None, center_y=None):
        self.costume_manager.add_costume(name, center_x, center_y)


    def replace_costume(self, index, name, center_x=None, center_y=None):
        self.costume_manager.replace_costume(index, name, center_x, center_y)


    def insert_costume(self, index, name, center_x=None, center_y=None):
        self.costume_manager.insert(index, name, center_x, center_y)


    def _draw(self):
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
        offset_x = (image.get_width() - transformed.get_width()) / 2
        offset_y = (image.get_height() - transformed.get_height()) / 2
        self.stage.screen.blit(transformed, (self.x + self.stage.center_x - center_x + offset_x, self.y + self.stage.center_y - center_y + offset_y))


    def _update(self, dt):
        self.code_manager._update(dt)


