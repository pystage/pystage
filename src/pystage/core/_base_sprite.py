import pygame

from pystage.core.code_block import CodeBlock, CodeManager
from pystage.core.assets import CostumeManager

class BaseSprite(pygame.sprite.Sprite):
    """Base Class for Mixin Classes that need access to the stage.
    """
    

    def __init__(self):
        super().__init__()
        self.stage = self.stage if hasattr(self, "stage") else None
        self.code_manager = CodeManager(self)
        self.costume_manager = CostumeManager(self)
