from .sprite import Veikėjas
from .stage import Scena
from pystage.core.code_block import no_refresh as be_ekrano_atnaujinimo

sprite_class = Veikėjas
stage_class = Scena

__all__ = ["Veikėjas", "Scena", "be_ekrano_atnaujinimo"]
