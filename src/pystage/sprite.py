import pygame
import pkg_resources

from pystage.code_block import CodeBlock

# Mixins
from pystage._events import _Events
from pystage._motion import _Motion
from pystage._sensing import _Sensing
from pystage._looks import _Looks
from pystage._pen import _Pen
from pystage._variables import _Variables
from pystage._control import _Control
from pystage._sound import _Sound


class Sprite(_Motion, _Events, _Looks, _Sound, _Sensing, _Control, _Variables, _Pen):
    image = pygame.image.load(pkg_resources.resource_filename(__name__, "images/zombie_idle.png"))
    x = 0.0
    y = 0.0
    direction = 0
    pen = False
    color = (255,0,0)
    # name: code_block
    code_blocks = {}
    # pygame.K_?: [name, ...]
    key_pressed_blocks = {}


    def __init__(self, stage):
        self.stage = stage


    def _draw(self):
        self.stage.screen.blit(self.image, (self.x, self.y))


    def _update(self, dt):
        for name in self.code_blocks:
            self.code_blocks[name].update(dt)


    def _process_key_pressed(self, key):
        # key is a pygame constant, e.g. pygame.K_a
        # This hat block is special as it only fires again when the code block has ended. 
        # All other hat block methods stop the current execution and restart the block.
        if key in self.key_pressed_blocks:
            for name in self.key_pressed_blocks[key]:
                self.code_blocks[name].start_if_not_running()


    def _register_code_block(self, generator_function, name=""):
        new_block = CodeBlock(self, generator_function, name)
        self.code_blocks[new_block.name] = new_block
        print(f"New code block registered: {new_block.name}")
        return new_block



    ##
    # Operators
    #

    # Operators are all available in python.
    # TODO: Needs documentation

    # - +-*/
    # - pick random from range (inclusive)
    # - < > =
    # and / or / not
    # join
    # letter 1 of string
    # length of string
    # string contains a
    # mod
    # round
    # abs/floor/ceiling/sqrt/sin/cos/tan/asin/acos/atan/ln/log/e^/10^


    ##
    # My Blocks (custom blocks)
    #

    # a custom block is simply a generator or a function (we need to distinguish here!)
    # generators (long running blocks that need yields) are invoked with yield from 
    # functions as usual (they block the thread).
    # Scratch does not support custom reporters, actually, unlike Snap.
    # Reporters would be functions, as only this way we can work with the return value
    #
    # TODO: document this

