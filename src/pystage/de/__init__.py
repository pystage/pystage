from .sprite import Figur
from .stage import Bühne
from pystage.core.code_block import no_refresh as ohne_bildschirmaktualisierung

sprite_class = Figur
stage_class = Bühne

__all__ = ["Figur", "Bühne", "ohne_bildschirmaktualisierung"]
