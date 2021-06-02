import pygame

from pystage.code_block import CodeBlock
from pystage.costume import Costume

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
        self.costumes = []
        self.current_costume = -1
        self.x = 0.0
        self.y = 0.0
        self.direction = 90
        self.pen = False
        self.color = (255,0,0)
        # name: code_block
        self.code_blocks = {}
        # pygame.K_?: [name, ...]
        self.key_pressed_blocks = {}
        self.stage = stage
        # Name of the code block currently executed.
        # This way, state about the current execustion
        # can be stored safely where it belongs
        self.current_block : CodeBlock = None
        self.add_costume(costume)


    def add_costume(self, name, center_x=None, center_y=None):
        if isinstance(name, str):
            costume = Costume(self, name, center_x, center_y)
            self.costumes.append(costume)
            if self.current_costume==-1:
                self.current_costume = len(self.costumes) - 1
        else:
            for n in name:
                self.add_costume(n)


    def replace_costume(self, index, name, center_x=None, center_y=None):
        costume = Costume(self, name, center_x, center_y)
        del self.costumes[index]
        self.costumes.insert(index, costume)


    def insert_costume(self, index, name, center_x=None, center_y=None):
        costume = Costume(self, name, center_x, center_y)
        self.costumes.insert(index, costume)


    def _draw(self):
        if self.current_costume > -1:
            self.costumes[self.current_costume]._draw()


    def _update(self, dt):
        for name in self.code_blocks:
            self.current_block = self.code_blocks[name]
            self.code_blocks[name].update(dt)


    def _process_key_pressed(self, key):
        # key is a pygame constant, e.g. pygame.K_a
        # This hat block is special as it only fires again when the code block has ended. 
        # All other hat block methods stop the current execution and restart the block.
        if key in self.key_pressed_blocks:
            for name in self.key_pressed_blocks[key]:
                self.code_blocks[name].start_if_not_running()


    def _register_code_block(self, generator_function, name="", no_refresh=False):
        new_block = CodeBlock(self, generator_function, name, no_refresh=no_refresh)
        self.code_blocks[new_block.name] = new_block
        print(f"New code block registered: {new_block.name}")
        return new_block
