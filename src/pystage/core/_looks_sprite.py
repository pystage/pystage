from pystage.core.gui import BubbleManager
from pystage.core.assets import CostumeManager
from pystage.core._base_sprite import BaseSprite


class _LooksSprite(BaseSprite):

    def __init__(self):
        super().__init__()
        self.bubble_manager = BubbleManager(self)
        self.costume_manager = CostumeManager(self)


    def pystage_addcostume(self, name, center_x=None, center_y=None):
        self.costume_manager.add_costume(name, center_x, center_y)


    def pystage_replacecostume(self, index, name, center_x=None, center_y=None):
        self.costume_manager.replace_costume(index, name, center_x, center_y)


    def pystage_insertcostume(self, index, name, center_x=None, center_y=None):
        self.costume_manager.insert_costume(index, name, center_x, center_y)


    def looks_sayforsecs(self, text, secs):
        pass


    def looks_say(self, text):
        self.bubble_manager.say(text)


    def looks_thinkforsecs(self, text, secs):
        pass

    def looks_think(self, text):
        self.bubble_manager.say(text, BubbleManager.THINK)

    def looks_switchcostumeto(self, costume):
        # TODO: Data/class structure for costumes
        pass

    def looks_nextcostume(self):
        pass

    def looks_switchbackdropto(self, backdrop):
        # Backdrops are for the stage.
        # In Scratch, a sprite can change the backdrop.
        pass

    def looks_nextbackdrop(self):
        pass

    def looks_changesizeby(self, percent):
        # this is percentage
        pass

    def looks_setsizeto(self, percent):
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

    def looks_show(self):
        pass

    def looks_hide(self):
        pass

    def looks_gotofrontback_front(self):
        pass

    looks_gotofrontback_front.opcode="looks_gotofrontback"
    looks_gotofrontback_front.param="FRONT_BACK"
    looks_gotofrontback_front.value="front"

    
    def looks_gotofrontback_back(self):
        pass

    looks_gotofrontback_back.opcode="looks_gotofrontback"
    looks_gotofrontback_back.param="FRONT_BACK"
    looks_gotofrontback_back.value="back"


    def looks_goforwardbackwardlayers_forward(self, value):
        pass

    looks_goforwardbackwardlayers_forward.opcode="looks_goforwardbackwardlayers"
    looks_goforwardbackwardlayers_forward.param="FORWARD_BACKWARD"
    looks_goforwardbackwardlayers_forward.value="forward"

    def looks_goforwardbackwardlayers_backward(self, value):
        pass

    looks_goforwardbackwardlayers_backward.opcode="looks_goforwardbackwardlayers"
    looks_goforwardbackwardlayers_backward.param="FORWARD_BACKWARD"
    looks_goforwardbackwardlayers_backward.value="backward"


    def looks_backdropnumbername_number(self):
        # 1-based
        pass

    looks_backdropnumbername_number.opcode="looks_backdropnumbername"
    looks_backdropnumbername_number.param="NUMBER_NAME"
    looks_backdropnumbername_number.value="number"
    looks_backdropnumbername_number.translation="looks_numbername_number"

    looks_backdropnumbername_number.return_type = int


    def looks_backdropnumbername_name(self):
        pass

    looks_backdropnumbername_name.opcode="looks_backdropnumbername"
    looks_backdropnumbername_name.param="NUMBER_NAME"
    looks_backdropnumbername_name.value="name"
    looks_backdropnumbername_name.translation="looks_numbername_name"

    looks_backdropnumbername_name.return_type = str

    def looks_costumenumbername_number(self):
        # 1-based
        pass

    looks_costumenumbername_number.opcode="looks_costumenumbername"
    looks_costumenumbername_number.param="NUMBER_NAME"
    looks_costumenumbername_number.value="number"
    looks_costumenumbername_number.translation="looks_numbername_number"

    looks_costumenumbername_number.return_type = int


    def looks_costumenumbername_name(self):
        pass

    looks_costumenumbername_name.opcode="looks_costumenumbername"
    looks_costumenumbername_name.param="NUMBER_NAME"
    looks_costumenumbername_name.value="name"
    looks_costumenumbername_name.translation="looks_numbername_name"

    looks_costumenumbername_name.return_type = str

    def looks_size(self):
        # percent
        pass

    looks_size.return_type = float
