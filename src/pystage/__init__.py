from os import environ

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("pystage")
except PackageNotFoundError:
    # package is not installed
    __version__ = "Pre 0.1"

# Prevent PyGame support prompt
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
# Do not mess with the compositor
environ['SDL_VIDEO_X11_NET_WM_BYPASS_COMPOSITOR'] = '0'

