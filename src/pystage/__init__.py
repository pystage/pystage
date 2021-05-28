# Prevent PyGame support prompt
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from .sprite import Sprite
from .stage import Stage

__all__ = ["Sprite", "Stage"]
