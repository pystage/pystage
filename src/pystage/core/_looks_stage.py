from pystage.core.costume import CostumeManager


class _LooksStage():

    def __init__(self):
        super().__init__()
        self.costume_manager = CostumeManager(self)


    def looks_switchbackdropto(self, backdrop):
        # Backdrops are for the stage.
        # In Scratch, a sprite can change the backdrop.
        pass

    def looks_switchbackdroptoandwait(self, backdrop):
        # Wait for any code under a "when backdrop is changed"
        pass

    def looks_nextbackdrop(self):
        pass


    def looks_seteffectto_color(self, value):
        pass

    looks_seteffectto_color.opcode="looks_seteffectto"
    looks_seteffectto_color.param="EFFECT"
    looks_seteffectto_color.value="COLOR"


    def looks_seteffectto_fisheye(self, value):
        pass
    
    looks_seteffectto_fisheye.opcode="looks_seteffectto"
    looks_seteffectto_fisheye.param="EFFECT"
    looks_seteffectto_fisheye.value="FISHEYE"


    def looks_seteffectto_whirl(self, value):
        pass
    
    looks_seteffectto_whirl.opcode="looks_seteffectto"
    looks_seteffectto_whirl.param="EFFECT"
    looks_seteffectto_whirl.value="WHIRL"


    def looks_seteffectto_pixelate(self, value):
        pass
    
    looks_seteffectto_pixelate.opcode="looks_seteffectto"
    looks_seteffectto_pixelate.param="EFFECT"
    looks_seteffectto_pixelate.value="PIXELATE"


    def looks_seteffectto_mosaic(self, value):
        pass
    
    looks_seteffectto_mosaic.opcode="looks_seteffectto"
    looks_seteffectto_mosaic.param="EFFECT"
    looks_seteffectto_mosaic.value="MOSAIC"
    

    def looks_seteffectto_brightness(self, value):
        pass
    
    looks_seteffectto_brightness.opcode="looks_seteffectto"
    looks_seteffectto_brightness.param="EFFECT"
    looks_seteffectto_brightness.value="BRIGHTNESS"
    

    def looks_seteffectto_ghost(self, value):
        pass
    
    looks_seteffectto_ghost.opcode="looks_seteffectto"
    looks_seteffectto_ghost.param="EFFECT"
    looks_seteffectto_ghost.value="GHOST"
    

    def looks_changeeffectby_color(self, value):
        pass

    looks_changeeffectby_color.opcode="looks_changeeffectby"
    looks_changeeffectby_color.param="EFFECT"
    looks_changeeffectby_color.value="COLOR"


    def looks_changeeffectby_fisheye(self, value):
        pass
    
    looks_changeeffectby_fisheye.opcode="looks_changeeffectby"
    looks_changeeffectby_fisheye.param="EFFECT"
    looks_changeeffectby_fisheye.value="FISHEYE"


    def looks_changeeffectby_whirl(self, value):
        pass
    
    looks_changeeffectby_whirl.opcode="looks_changeeffectby"
    looks_changeeffectby_whirl.param="EFFECT"
    looks_changeeffectby_whirl.value="WHIRL"


    def looks_changeeffectby_pixelate(self, value):
        pass
    
    looks_changeeffectby_pixelate.opcode="looks_changeeffectby"
    looks_changeeffectby_pixelate.param="EFFECT"
    looks_changeeffectby_pixelate.value="PIXELATE"


    def looks_changeeffectby_mosaic(self, value):
        pass
    
    looks_changeeffectby_mosaic.opcode="looks_changeeffectby"
    looks_changeeffectby_mosaic.param="EFFECT"
    looks_changeeffectby_mosaic.value="MOSAIC"
    

    def looks_changeeffectby_brightness(self, value):
        pass
    
    looks_changeeffectby_brightness.opcode="looks_changeeffectby"
    looks_changeeffectby_brightness.param="EFFECT"
    looks_changeeffectby_brightness.value="BRIGHTNESS"
    

    def looks_changeeffectby_ghost(self, value):
        pass
    
    looks_changeeffectby_ghost.opcode="looks_changeeffectby"
    looks_changeeffectby_ghost.param="EFFECT"
    looks_changeeffectby_ghost.value="GHOST"
    

    def looks_cleargraphiceffects(self):
        pass

    def looks_backdropnumbername_number(self):
        # 1-based
        pass

    looks_backdropnumbername_number.opcode="looks_backdropnumbername"
    looks_backdropnumbername_number.param="NUMBER_NAME"
    looks_backdropnumbername_number.value="number"


    def looks_backdropnumbername_name(self):
        pass

    looks_backdropnumbername_number.opcode="looks_backdropnumbername"
    looks_backdropnumbername_number.param="NUMBER_NAME"
    looks_backdropnumbername_number.value="name"
