from pystage.core.gui import BubbleManager, Bubble
from pystage.core.assets import CostumeManager
from pystage.core._base_sprite import BaseSprite
from pystage.core.values import to_number


class _Looks(BaseSprite):
    def __init__(self):
        super().__init__()

    def looks_switchbackdropto_next(self):
        self.stage.costume_manager.next_costume()
        return self.stage._backdrop_switched()

    looks_switchbackdropto_next.opcode="looks_switchbackdropto"
    looks_switchbackdropto_next.param="BACKDROP"
    looks_switchbackdropto_next.value="next backdrop"

    def looks_switchbackdropto_previous(self):
        self.stage.costume_manager.previous_costume()
        return self.stage._backdrop_switched()

    looks_switchbackdropto_previous.opcode="looks_switchbackdropto"
    looks_switchbackdropto_previous.param="BACKDROP"
    looks_switchbackdropto_previous.value="previous backdrop"

    def looks_switchbackdropto_random(self):
        self.stage.costume_manager.random_costume()
        return self.stage._backdrop_switched()

    looks_switchbackdropto_random.opcode="looks_switchbackdropto"
    looks_switchbackdropto_random.param="BACKDROP"
    looks_switchbackdropto_random.value="random backdrop"

    def looks_switchbackdropto_backdrop(self, backdrop):
        # Backdrops are for the stage.
        # In Scratch, a sprite can change the backdrop.
        special = {
            "next backdrop": self.stage.costume_manager.next_costume,
            "previous backdrop": self.stage.costume_manager.previous_costume,
            "random backdrop": self.stage.costume_manager.random_costume,
        }
        if isinstance(backdrop, str) and backdrop in special and not self.stage.costume_manager.has_costume(backdrop):
            special[backdrop]()
        else:
            self.stage.costume_manager.switch_costume(backdrop)
        return self.stage._backdrop_switched()

    looks_switchbackdropto_backdrop.opcode="looks_switchbackdropto"

    def looks_nextbackdrop(self):
        self.stage.costume_manager.next_costume()
        return self.stage._backdrop_switched()

    def looks_seteffectto_color(self, value):
        value = to_number(value)
        # the color value is from 0 to 200
        # https://scratch.mit.edu/discuss/m/topic/436245/
        self.color = max(0, min(int(value), 200))

    looks_seteffectto_color.opcode="looks_seteffectto"
    looks_seteffectto_color.param="EFFECT"
    looks_seteffectto_color.value="COLOR"
    looks_seteffectto_color.translation="looks_effect_color"


    def looks_seteffectto_fisheye(self, value):
        value = to_number(value)
        self.fisheye = value
    
    looks_seteffectto_fisheye.opcode="looks_seteffectto"
    looks_seteffectto_fisheye.param="EFFECT"
    looks_seteffectto_fisheye.value="FISHEYE"
    looks_seteffectto_fisheye.translation="looks_effect_fisheye"


    def looks_seteffectto_whirl(self, value):
        value = to_number(value)
        self.whirl = value
    
    looks_seteffectto_whirl.opcode="looks_seteffectto"
    looks_seteffectto_whirl.param="EFFECT"
    looks_seteffectto_whirl.value="WHIRL"
    looks_seteffectto_whirl.translation="looks_effect_whirl"


    def looks_seteffectto_pixelate(self, value):
        value = to_number(value)
        self.pixelate = value
    
    looks_seteffectto_pixelate.opcode="looks_seteffectto"
    looks_seteffectto_pixelate.param="EFFECT"
    looks_seteffectto_pixelate.value="PIXELATE"
    looks_seteffectto_pixelate.translation="looks_effect_pixelate"


    def looks_seteffectto_mosaic(self, value):
        value = to_number(value)
        self.mosaic = value
    
    looks_seteffectto_mosaic.opcode="looks_seteffectto"
    looks_seteffectto_mosaic.param="EFFECT"
    looks_seteffectto_mosaic.value="MOSAIC"
    looks_seteffectto_mosaic.translation="looks_effect_mosaic"
    

    def looks_seteffectto_brightness(self, value):
        value = to_number(value)
        self.brightness = value
        self.brightness = max(-100, min(self.brightness, 100))
    
    looks_seteffectto_brightness.opcode="looks_seteffectto"
    looks_seteffectto_brightness.param="EFFECT"
    looks_seteffectto_brightness.value="BRIGHTNESS"
    looks_seteffectto_brightness.translation="looks_effect_brightness"
    

    def looks_seteffectto_ghost(self, value):
        value = to_number(value)
        self.ghost = value
    
    looks_seteffectto_ghost.opcode="looks_seteffectto"
    looks_seteffectto_ghost.param="EFFECT"
    looks_seteffectto_ghost.value="GHOST"
    looks_seteffectto_ghost.translation="looks_effect_ghost"
    

    def looks_changeeffectby_color(self, value):
        value = to_number(value)
        self.color += value
        self.color = self.color % 200

    looks_changeeffectby_color.opcode="looks_changeeffectby"
    looks_changeeffectby_color.param="EFFECT"
    looks_changeeffectby_color.value="COLOR"
    looks_changeeffectby_color.translation="looks_effect_color"


    def looks_changeeffectby_fisheye(self, value):
        value = to_number(value)
        self.fisheye += value
    
    looks_changeeffectby_fisheye.opcode="looks_changeeffectby"
    looks_changeeffectby_fisheye.param="EFFECT"
    looks_changeeffectby_fisheye.value="FISHEYE"
    looks_changeeffectby_fisheye.translation="looks_effect_fisheye"


    def looks_changeeffectby_whirl(self, value):
        value = to_number(value)
        self.whirl += value
    
    looks_changeeffectby_whirl.opcode="looks_changeeffectby"
    looks_changeeffectby_whirl.param="EFFECT"
    looks_changeeffectby_whirl.value="WHIRL"
    looks_changeeffectby_whirl.translation="looks_effect_whirl"


    def looks_changeeffectby_pixelate(self, value):
        value = to_number(value)
        self.pixelate += value
    
    looks_changeeffectby_pixelate.opcode="looks_changeeffectby"
    looks_changeeffectby_pixelate.param="EFFECT"
    looks_changeeffectby_pixelate.value="PIXELATE"
    looks_changeeffectby_pixelate.translation="looks_effect_pixelate"


    def looks_changeeffectby_mosaic(self, value):
        value = to_number(value)
        self.mosaic += value
    
    looks_changeeffectby_mosaic.opcode="looks_changeeffectby"
    looks_changeeffectby_mosaic.param="EFFECT"
    looks_changeeffectby_mosaic.value="MOSAIC"
    looks_changeeffectby_mosaic.translation="looks_effect_mosaic"
    

    def looks_changeeffectby_brightness(self, value):
        value = to_number(value)
        self.brightness += value
        self.brightness = max(-100, min(self.brightness, 100))
    
    looks_changeeffectby_brightness.opcode="looks_changeeffectby"
    looks_changeeffectby_brightness.param="EFFECT"
    looks_changeeffectby_brightness.value="BRIGHTNESS"
    looks_changeeffectby_brightness.translation="looks_effect_brightness"
    

    def looks_changeeffectby_ghost(self, value):
        value = to_number(value)
        self.ghost += value
    
    looks_changeeffectby_ghost.opcode="looks_changeeffectby"
    looks_changeeffectby_ghost.param="EFFECT"
    looks_changeeffectby_ghost.value="GHOST"
    looks_changeeffectby_ghost.translation="looks_effect_ghost"
    

    def looks_cleargraphiceffects(self):
        self.color = 0
        self.fisheye = 0
        self.whirl = 0
        self.pixelate = 0
        self.mosaic = 0
        self.brightness = 0
        self.ghost = 0

    def looks_backdropnumbername_number(self):
        # 1-based
        return self.stage.costume_manager.current_costume + 1

    looks_backdropnumbername_number.opcode="looks_backdropnumbername"
    looks_backdropnumbername_number.param="NUMBER_NAME"
    looks_backdropnumbername_number.value="number"
    looks_backdropnumbername_number.translation="looks_numbername_number"

    looks_backdropnumbername_number.return_type = int


    def looks_backdropnumbername_name(self):
        costume = self.stage.costume_manager.get_costume()
        if not costume:
            return ""
        return costume.name

    looks_backdropnumbername_name.opcode="looks_backdropnumbername"
    looks_backdropnumbername_name.param="NUMBER_NAME"
    looks_backdropnumbername_name.value="name"
    looks_backdropnumbername_name.translation="looks_numbername_name"

    looks_backdropnumbername_name.return_type = str

class _LooksSprite(_Looks):

    def __init__(self):
        super().__init__()
        self.bubble_manager = BubbleManager(self)
        # Make sure to clone all properties in sprite.py that need to be cloned
        self.size = 100
        self.ghost = 0 # 0 - visible / 100 - transparent
        self.visible = True
        self.color = 0  # 0 - 200
        self.fisheye = 0
        self.whirl = 0
        self.pixelate = 0
        self.mosaic = 0
        self.brightness = 0

    def pystage_addcostume(self, name, center_x=None, center_y=None, factor=1):
        self.costume_manager.add_costume(name, center_x, center_y, factor)

    def pystage_replacecostume(self, index, name, center_x=None, center_y=None, factor=1):
        self.costume_manager.replace_costume(index, name, center_x, center_y, factor)

    def pystage_insertcostume(self, index, name, center_x=None, center_y=None, factor=1):
        self.costume_manager.insert_costume(index, name, center_x, center_y, factor)

    def looks_sayforsecs(self, text, secs):
        self.bubble_manager.sayforsecs(text, secs)

    def looks_say(self, text):
        self.bubble_manager.say(text)

    def looks_thinkforsecs(self, text, secs):
        self.bubble_manager.thinkforsecs(text, secs)

    def looks_think(self, text):
        self.bubble_manager.think(text)

    def looks_switchcostumeto(self, costume):
        self.costume_manager.switch_costume(costume)

    def looks_nextcostume(self):
        self.costume_manager.next_costume()


    def looks_changesizeby(self, percent):
        # this is percentage
        self.size += to_number(percent)


    def looks_setsizeto(self, percent):
        self.size = to_number(percent)

    def looks_show(self):
        if self.visible:
            return
        self.visible = True
        self.stage._update_visible()


    def looks_hide(self):
        if not self.visible:
            return
        self.visible = False
        self.stage._update_visible()


    def looks_gotofrontback_front(self):
        self.stage.sprites.to_front(self)

    looks_gotofrontback_front.opcode="looks_gotofrontback"
    looks_gotofrontback_front.param="FRONT_BACK"
    looks_gotofrontback_front.value="front"

    
    def looks_gotofrontback_back(self):
        self.stage.sprites.to_back(self)

    looks_gotofrontback_back.opcode="looks_gotofrontback"
    looks_gotofrontback_back.param="FRONT_BACK"
    looks_gotofrontback_back.value="back"


    def looks_goforwardbackwardlayers_forward(self, value):
        self.stage.sprites.layer_forward(self, int(to_number(value)))

    looks_goforwardbackwardlayers_forward.opcode="looks_goforwardbackwardlayers"
    looks_goforwardbackwardlayers_forward.param="FORWARD_BACKWARD"
    looks_goforwardbackwardlayers_forward.value="forward"

    def looks_goforwardbackwardlayers_backward(self, value):
        self.stage.sprites.layer_backward(self, int(to_number(value)))

    looks_goforwardbackwardlayers_backward.opcode="looks_goforwardbackwardlayers"
    looks_goforwardbackwardlayers_backward.param="FORWARD_BACKWARD"
    looks_goforwardbackwardlayers_backward.value="backward"


    def looks_costumenumbername_number(self):
        # 1-based
        return self.costume_manager.current_costume + 1

    looks_costumenumbername_number.opcode="looks_costumenumbername"
    looks_costumenumbername_number.param="NUMBER_NAME"
    looks_costumenumbername_number.value="number"
    looks_costumenumbername_number.translation="looks_numbername_number"

    looks_costumenumbername_number.return_type = int


    def looks_costumenumbername_name(self):
        costume = self.costume_manager.get_costume()
        if not costume:
            return ""
        return costume.name

    looks_costumenumbername_name.opcode="looks_costumenumbername"
    looks_costumenumbername_name.param="NUMBER_NAME"
    looks_costumenumbername_name.value="name"
    looks_costumenumbername_name.translation="looks_numbername_name"

    looks_costumenumbername_name.return_type = str

    def looks_size(self):
        # percent
        return self.size

    looks_size.return_type = float


class _LooksStage(_Looks):

    def __init__(self):
        super().__init__()
        self.ghost = 0
        self.color = 0  # 0 - 200
        self.fisheye = 0
        self.whirl = 0
        self.pixelate = 0
        self.mosaic = 0
        self.brightness = 0


    def pystage_addbackdrop(self, name, center_x=None, center_y=None, factor=1):
        self.costume_manager.add_costume(name, center_x, center_y, factor)


    def pystage_replacebackdrop(self, index, name, center_x=None, center_y=None, factor=1):
        self.costume_manager.replace_costume(index, name, center_x, center_y, factor)


    def pystage_insertbackdrop(self, index, name, center_x=None, center_y=None, factor=1):
        self.costume_manager.insert_costume(index, name, center_x, center_y, factor)


    def looks_switchbackdroptoandwait(self, backdrop):
        # Wait for any code under a "when backdrop switches to"
        current = self.code_manager.current_block
        started = self.looks_switchbackdropto_backdrop(backdrop)
        current.waiting_for = [block for block in started if block is not current]
