from os import environ
# Prevent PyGame support prompt
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
# Do not mess with the compositor
environ['SDL_VIDEO_X11_NET_WM_BYPASS_COMPOSITOR'] = '0'

from .sprite import Sprite
from .stage import Stage


__all__ = ["Sprite", "Stage"]
