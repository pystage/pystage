from pystage.core.assets import CostumeManager


class _LooksStage():

    def __init__(self):
        super().__init__()
        self.costume_manager = CostumeManager(self)


    def pystage_addbackdrop(self, name, center_x=None, center_y=None):
        self.costume_manager.add_costume(name, center_x, center_y)


    def pystage_replacebackdrop(self, index, name, center_x=None, center_y=None):
        self.costume_manager.replace_costume(index, name, center_x, center_y)


    def pystage_insertbackdrop(self, index, name, center_x=None, center_y=None):
        self.costume_manager.insert_costume(index, name, center_x, center_y)


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
    looks_seteffectto_color.translation="looks_effect_color"


    def looks_seteffectto_fisheye(self, value):
        pass
    
    looks_seteffectto_fisheye.opcode="looks_seteffectto"
    looks_seteffectto_fisheye.param="EFFECT"
    looks_seteffectto_fisheye.value="FISHEYE"
    looks_seteffectto_fisheye.translation="looks_effect_fisheye"


    def looks_seteffectto_whirl(self, value):
        pass
    
    looks_seteffectto_whirl.opcode="looks_seteffectto"
    looks_seteffectto_whirl.param="EFFECT"
    looks_seteffectto_whirl.value="WHIRL"
    looks_seteffectto_whirl.translation="looks_effect_whirl"


    def looks_seteffectto_pixelate(self, value):
        pass
    
    looks_seteffectto_pixelate.opcode="looks_seteffectto"
    looks_seteffectto_pixelate.param="EFFECT"
    looks_seteffectto_pixelate.value="PIXELATE"
    looks_seteffectto_pixelate.translation="looks_effect_pixelate"


    def looks_seteffectto_mosaic(self, value):
        pass
    
    looks_seteffectto_mosaic.opcode="looks_seteffectto"
    looks_seteffectto_mosaic.param="EFFECT"
    looks_seteffectto_mosaic.value="MOSAIC"
    looks_seteffectto_mosaic.translation="looks_effect_mosaic"
    

    def looks_seteffectto_brightness(self, value):
        pass
    
    looks_seteffectto_brightness.opcode="looks_seteffectto"
    looks_seteffectto_brightness.param="EFFECT"
    looks_seteffectto_brightness.value="BRIGHTNESS"
    looks_seteffectto_brightness.translation="looks_effect_brightness"
    

    def looks_seteffectto_ghost(self, value):
        pass
    
    looks_seteffectto_ghost.opcode="looks_seteffectto"
    looks_seteffectto_ghost.param="EFFECT"
    looks_seteffectto_ghost.value="GHOST"
    looks_seteffectto_ghost.translation="looks_effect_ghost"
    

    def looks_changeeffectby_color(self, value):
        pass

    looks_changeeffectby_color.opcode="looks_changeeffectby"
    looks_changeeffectby_color.param="EFFECT"
    looks_changeeffectby_color.value="COLOR"
    looks_changeeffectby_color.translation="looks_effect_color"


    def looks_changeeffectby_fisheye(self, value):
        pass
    
    looks_changeeffectby_fisheye.opcode="looks_changeeffectby"
    looks_changeeffectby_fisheye.param="EFFECT"
    looks_changeeffectby_fisheye.value="FISHEYE"
    looks_changeeffectby_fisheye.translation="looks_effect_fisheye"


    def looks_changeeffectby_whirl(self, value):
        pass
    
    looks_changeeffectby_whirl.opcode="looks_changeeffectby"
    looks_changeeffectby_whirl.param="EFFECT"
    looks_changeeffectby_whirl.value="WHIRL"
    looks_changeeffectby_whirl.translation="looks_effect_whirl"


    def looks_changeeffectby_pixelate(self, value):
        pass
    
    looks_changeeffectby_pixelate.opcode="looks_changeeffectby"
    looks_changeeffectby_pixelate.param="EFFECT"
    looks_changeeffectby_pixelate.value="PIXELATE"
    looks_changeeffectby_pixelate.translation="looks_effect_pixelate"


    def looks_changeeffectby_mosaic(self, value):
        pass
    
    looks_changeeffectby_mosaic.opcode="looks_changeeffectby"
    looks_changeeffectby_mosaic.param="EFFECT"
    looks_changeeffectby_mosaic.value="MOSAIC"
    looks_changeeffectby_mosaic.translation="looks_effect_mosaic"
    

    def looks_changeeffectby_brightness(self, value):
        pass
    
    looks_changeeffectby_brightness.opcode="looks_changeeffectby"
    looks_changeeffectby_brightness.param="EFFECT"
    looks_changeeffectby_brightness.value="BRIGHTNESS"
    looks_changeeffectby_brightness.translation="looks_effect_brightness"
    

    def looks_changeeffectby_ghost(self, value):
        pass
    
    looks_changeeffectby_ghost.opcode="looks_changeeffectby"
    looks_changeeffectby_ghost.param="EFFECT"
    looks_changeeffectby_ghost.value="GHOST"
    looks_changeeffectby_ghost.translation="looks_effect_ghost"
    

    def looks_cleargraphiceffects(self):
        pass

    def looks_backdropnumbername_number(self):
        # 1-based
        pass

    looks_backdropnumbername_number.opcode="looks_backdropnumbername"
    looks_backdropnumbername_number.param="NUMBER_NAME"
    looks_backdropnumbername_number.value="number"
    looks_backdropnumbername_number.translation="looks_numbername_number"


    def looks_backdropnumbername_name(self):
        pass

    looks_backdropnumbername_name.opcode="looks_backdropnumbername"
    looks_backdropnumbername_name.param="NUMBER_NAME"
    looks_backdropnumbername_name.value="name"
    looks_backdropnumbername_name.translation="looks_numbername_name"
