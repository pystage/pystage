from .sprite import Sprite
from .stage import Stage
from pystage.core.code_block import no_refresh

sprite_class = Sprite
stage_class = Stage

__all__ = ["Sprite", "Stage", "no_refresh"]
