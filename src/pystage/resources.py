"""Access to the files that are bundled with pyStage (images, sounds, fonts)."""
import os

_BASE = os.path.dirname(os.path.abspath(__file__))


def resource_filename(path):
    """The absolute path of a bundled file or folder, e.g. "fonts/roboto-bold.ttf".

    A trailing slash is kept.
    """
    filename = os.path.join(_BASE, *path.split("/"))
    return filename
