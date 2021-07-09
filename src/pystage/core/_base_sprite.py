from pystage.core.code_block import CodeBlock, CodeManager

class BaseSprite():
    """Base Class for Mixin Classes that need access to the stage.
    """
    

    def __init__(self):
        super().__init__()

        self.stage = None
        self.code_manager = CodeManager(self)
