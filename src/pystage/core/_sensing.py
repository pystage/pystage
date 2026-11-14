import pygame
from pystage.core.constants import KEY_MAPPINGS
from pystage.core._base_sprite import BaseSprite
import datetime


class _Nothing:
    """Stands for a sprite that does not exist, all blocks return 0."""

    def __getattr__(self, name):
        return lambda *args: 0


class _Sensing(BaseSprite):

    def __init__(self):
        super().__init__()


    def sensing_askandwait(self, question):
        self.code_manager.current_block.ask(question)

    def sensing_answer(self):
        return self.stage.input_manager.answer

    def sensing_keypressed(self, key):
        pressed = pygame.key.get_pressed()
        key = str(key).lower()
        if key == "any":
            return any(pressed)
        if key not in KEY_MAPPINGS:
            return False
        return bool(pressed[KEY_MAPPINGS[key]])

    def sensing_mousedown(self):
        return any(pygame.mouse.get_pressed())

    def sensing_mousex(self):
        x = self.stage._mouse_pos().x - self.stage.center_x
        return max(-self.stage.center_x, min(self.stage.center_x, round(x)))

    def sensing_mousey(self):
        y = -self.stage._mouse_pos().y + self.stage.center_y
        return max(-self.stage.center_y, min(self.stage.center_y, round(y)))

    def sensing_loudness(self):
        # There is no microphone access, Scratch returns -1 in this case.
        # See https://github.com/pystage/pystage/issues/116
        return -1

    def sensing_timer(self):
        return self.stage.timer

    def sensing_resettimer(self):
        self.stage.timer = 0


    def sensing_setdragmode_draggable(self):
        self.draggable = True
    sensing_setdragmode_draggable.opcode="sensing_setdragmode"
    sensing_setdragmode_draggable.param="DRAG_MODE"
    sensing_setdragmode_draggable.value="draggable"


    def sensing_setdragmode_notdraggable(self):
        self.draggable = False
    sensing_setdragmode_notdraggable.opcode="sensing_setdragmode"
    sensing_setdragmode_notdraggable.param="DRAG_MODE"
    sensing_setdragmode_notdraggable.value="not draggable"

    # Here follows the mess of our favorite block, where a lot of stuff 
    # from other sprites and the stage can be retrieved.
    # This is all redundant, as in Python you would simply do something like
    # self.stage.get_backdrop_name(). Along these lines, we need good
    # explanations and examples in the documentation that show why these functions
    # should not be used.

    def _of(self, sprite):
        # Unknown sprites have 0 for all properties in Scratch
        return self.stage._get_sprite(sprite) or _Nothing()

    def sensing_of_xposition(self, sprite):
        return self._of(sprite).motion_xposition()
    sensing_of_xposition.opcode="sensing_of"
    sensing_of_xposition.param="PROPERTY"
    sensing_of_xposition.value="x position"


    def sensing_of_yposition(self, sprite):
        return self._of(sprite).motion_yposition()
    sensing_of_yposition.opcode="sensing_of"
    sensing_of_yposition.param="PROPERTY"
    sensing_of_yposition.value="y position"


    def sensing_of_direction(self, sprite):
        return self._of(sprite).motion_direction()
    sensing_of_direction.opcode="sensing_of"
    sensing_of_direction.param="PROPERTY"
    sensing_of_direction.value="direction"


    def sensing_of_costumenumber(self, sprite):
        return self._of(sprite).looks_costumenumbername_number()
    sensing_of_costumenumber.opcode="sensing_of"
    sensing_of_costumenumber.param="PROPERTY"
    sensing_of_costumenumber.value="costume #"


    def sensing_of_costumename(self, sprite):
        return self._of(sprite).looks_costumenumbername_name()
    sensing_of_costumename.opcode="sensing_of"
    sensing_of_costumename.param="PROPERTY"
    sensing_of_costumename.value="costume name"


    def sensing_of_size(self, sprite):
        return self._of(sprite).looks_size()
    sensing_of_size.opcode="sensing_of"
    sensing_of_size.param="PROPERTY"
    sensing_of_size.value="size"


    def sensing_of_volume(self, sprite="_stage_"):
        return self._of(sprite).sound_volume()
    sensing_of_volume.opcode="sensing_of"
    sensing_of_volume.param="PROPERTY"
    sensing_of_volume.value="volume"


    def sensing_of_variable(self, variable, sprite="_stage_"):
        target = self.stage._get_sprite(sprite)
        if target is not None and variable in target.variables:
            return target.variables[variable]
        return 0
    sensing_of_variable.opcode="sensing_of"


    def sensing_of_backdropnumber(self, stage="_stage_"):
        return self.stage.looks_backdropnumbername_number()
    sensing_of_backdropnumber.opcode="sensing_of"
    sensing_of_backdropnumber.param="PROPERTY"
    sensing_of_backdropnumber.value="backdrop #"


    def sensing_of_backdropname(self, stage="_stage_"):
        return self.stage.looks_backdropnumbername_name()
    sensing_of_backdropname.opcode="sensing_of"
    sensing_of_backdropname.param="PROPERTY"
    sensing_of_backdropname.value="backdrop name"


    def sensing_current_year(self):
        return datetime.datetime.now().year
    sensing_current_year.opcode="sensing_current"
    sensing_current_year.param="CURRENTMENU"
    sensing_current_year.value="YEAR"


    def sensing_current_month(self):
        return datetime.datetime.now().month
    sensing_current_month.opcode="sensing_current"
    sensing_current_month.param="CURRENTMENU"
    sensing_current_month.value="MONTH"


    def sensing_current_date(self):
        return datetime.datetime.now().day
    sensing_current_date.opcode="sensing_current"
    sensing_current_date.param="CURRENTMENU"
    sensing_current_date.value="DATE"


    def sensing_current_dayofweek(self):
        current_datetime = datetime.datetime.now().date()
        #This leads to a Sunday=1 based counting
        day_of_week = (current_datetime.isoweekday() % 7) + 1
        return day_of_week
    sensing_current_dayofweek.opcode="sensing_current"
    sensing_current_dayofweek.param="CURRENTMENU"
    sensing_current_dayofweek.value="DAYOFWEEK"


    def sensing_current_hour(self):
        return datetime.datetime.now().hour
    sensing_current_hour.opcode="sensing_current"
    sensing_current_hour.param="CURRENTMENU"
    sensing_current_hour.value="HOUR"


    def sensing_current_minute(self):
        return datetime.datetime.now().minute
    sensing_current_minute.opcode="sensing_current"
    sensing_current_minute.param="CURRENTMENU"
    sensing_current_minute.value="MINUTE"


    def sensing_current_second(self):
        return datetime.datetime.now().second
    sensing_current_second.opcode="sensing_current"
    sensing_current_second.param="CURRENTMENU"
    sensing_current_second.value="SECOND"


    def sensing_dayssince2000(self):
        # use datetime to find days since 2000 in timezone
        start_date = datetime.datetime(2000, 1, 1, tzinfo=datetime.timezone.utc)
        current_datetime = datetime.datetime.now(datetime.timezone.utc)
        time_difference = current_datetime - start_date
        days = time_difference.days
        # find fraction of current day like in Scratch
        decimal_in_day_string = (current_datetime.hour * 3600 + current_datetime.minute * 60 + current_datetime.second) / (24 * 3600)
        # put full days and part of day together
        since_2000 = days + decimal_in_day_string
        return since_2000

    def sensing_username(self):
        # Nobody is logged in, like in the offline editor of Scratch.
        return ""

class _SensingSprite(BaseSprite):
    def __init__(self):
        super().__init__()

    def sensing_touchingobject_pointer(self):
        if not self.visible:
            return False
        return self.stage._sprite_at(self.stage._mouse_pos(), [self]) is not None

    sensing_touchingobject_pointer.opcode="sensing_touchingobject"
    sensing_touchingobject_pointer.param="TOUCHINGOBJECTMENU"
    sensing_touchingobject_pointer.value="_mouse_"

    def sensing_touchingobject_edge(self):
        self.costume_manager.update_sprite_image()
        return not self.stage.rect.contains(self.rect)

    sensing_touchingobject_edge.opcode="sensing_touchingobject"
    sensing_touchingobject_edge.param="TOUCHINGOBJECTMENU"
    sensing_touchingobject_edge.value="_edge_"

    def _touches(self, other):
        if other is self or not other.visible:
            return False
        if not other.rect.colliderect(self.rect):
            return False
        offset = (other.rect.left - self.rect.left, other.rect.top - self.rect.top)
        return self.mask.overlap(other.mask, offset) is not None

    def sensing_touchingobject_sprite(self, sprite):
        if sprite == "_mouse_":
            return self.sensing_touchingobject_pointer()
        if sprite == "_edge_":
            return self.sensing_touchingobject_edge()
        if not self.visible:
            return False
        sprite = self.stage._get_sprite(sprite)
        if sprite is None or sprite is self.stage:
            return False
        self.costume_manager.update_sprite_image()
        # Clones of the sprite count as well
        for other in self.stage.sprites:
            if other is sprite or (other.is_clone and other.name == sprite.name):
                other.costume_manager.update_sprite_image()
                if self._touches(other):
                    return True
        return False

    sensing_touchingobject_sprite.opcode="sensing_touchingobject"

    def _color_mask(self, surface, color):
        # Scratch is tolerant with colors, so are we.
        return pygame.mask.from_threshold(surface, pygame.Color(color), (12, 12, 12, 255))

    def _touching_color(self, color, own_mask):
        """True, if own_mask (in the rect of the sprite) touches the color."""
        area = self.rect.clip(self.stage.rect)
        if area.width == 0 or area.height == 0:
            return False
        # Everything but this sprite as it is seen on the stage
        background = pygame.Surface(area.size, flags=pygame.SRCALPHA)
        background.fill((255, 255, 255))
        offset = (-area.left, -area.top)
        self.stage._draw(background, offset)
        background.blit(self.stage.pen_image, offset)
        for other in self.stage.visible_sprites:
            if other is not self:
                background.blit(other.image, other.rect.move(offset))
        color_mask = self._color_mask(background, color)
        return own_mask.overlap(color_mask, (area.left - self.rect.left, area.top - self.rect.top)) is not None

    def sensing_touchingcolor(self, color):
        if not self.visible:
            return False
        self.costume_manager.update_sprite_image()
        return self._touching_color(color, self.mask)

    def sensing_coloristouchingcolor(self, sprite_color, color):
        if not self.visible:
            return False
        self.costume_manager.update_sprite_image()
        own_mask = self._color_mask(self.image, sprite_color)
        own_mask = own_mask.overlap_mask(self.mask, (0, 0))
        return self._touching_color(color, own_mask)

    def sensing_distanceto_pointer(self):
        return self._pos.distance_to(self.stage._mouse_pos())

    sensing_distanceto_pointer.opcode="sensing_distanceto"
    sensing_distanceto_pointer.param="DISTANCETOMENU"
    sensing_distanceto_pointer.value="_mouse_"

    def sensing_distanceto_sprite(self, sprite):
        if sprite == "_mouse_":
            return self.sensing_distanceto_pointer()
        sprite = self.stage._get_sprite(sprite)
        if sprite is None or sprite is self.stage:
            # Like in Scratch
            return 10000
        return self._pos.distance_to(sprite._pos)
    sensing_distanceto_sprite.opcode="sensing_distanceto"
