import pygame
import pystage
from pystage.core.constants import KEY_MAPPINGS
from pystage.core._base_sprite import BaseSprite



class _Sensing(BaseSprite):

    def __init__(self):
        super().__init__()


    def sensing_askandwait(self, question):
        # an input field, answer needs to be available somehow
        pass

    def sensing_answer(self):
        # Answer of the last question
        pass

    def sensing_keypressed(self, key):
        return pygame.key.get_pressed()[KEY_MAPPINGS[key]]   

    def sensing_mousedown(self):
        return any(pygame.mouse.get_pressed())

    def sensing_mousex(self):
        x = pygame.mouse.get_pos()[0]
        return ((x - self.stage.offset_x) / self.stage.scale_factor) - self.stage.width / 2

    def sensing_mousey(self):
        y = pygame.mouse.get_pos()[1]
        return -(y - self.stage.offset_y) / self.stage.scale_factor + self.stage.height / 2

    def sensing_loudness(self):
        # See events area, not sure if we support microphone access
        pass

    def sensing_timer(self):
        pass

    def sensing_resettimer(self):
        pass


    def sensing_setdragmode_draggable(self, value):
        pass
    sensing_setdragmode_draggable.opcode="sensing_setdragmode"
    sensing_setdragmode_draggable.param="DRAG_MODE"
    sensing_setdragmode_draggable.value="draggable"


    def sensing_setdragmode_not_draggable(self, value):
        pass
    sensing_setdragmode_draggable.opcode="sensing_setdragmode"
    sensing_setdragmode_draggable.param="DRAG_MODE"
    sensing_setdragmode_draggable.value="not draggable"

    # Here follows the mess of our favorite block, where a lot of stuff 
    # from other sprites and the stage can be retrieved.
    # This is all redundant, as in Python you would simply do something like
    # self.stage.get_backdrop_name(). Along these lines, we need good
    # explanations and examples in the documentation that show why these functions
    # should not be used.

    def sensing_of_x_position(self, sprite):
        pass
    sensing_of_x_position.opcode="sensing_of"
    sensing_of_x_position.param="PROPERTY"
    sensing_of_x_position.value="x position"


    def sensing_of_y_position(self, sprite):
        pass
    sensing_of_y_position.opcode="sensing_of"
    sensing_of_y_position.param="PROPERTY"
    sensing_of_y_position.value="y position"


    def sensing_of_direction(self, sprite):
        pass
    sensing_of_direction.opcode="sensing_of"
    sensing_of_direction.param="PROPERTY"
    sensing_of_direction.value="direction"


    def sensing_of_costume_no(self, sprite):
        pass
    sensing_of_costume_no.opcode="sensing_of"
    sensing_of_costume_no.param="PROPERTY"
    sensing_of_costume_no.value="costume #"


    def sensing_of_costume_name(self, sprite):
        pass
    sensing_of_costume_name.opcode="sensing_of"
    sensing_of_costume_name.param="PROPERTY"
    sensing_of_costume_name.value="costume name"


    def sensing_of_size(self, sprite):
        pass
    sensing_of_size.opcode="sensing_of"
    sensing_of_size.param="PROPERTY"
    sensing_of_size.value="size"


    def sensing_of_volume(self, sprite="_stage_"):
        pass
    sensing_of_volume.opcode="sensing_of"
    sensing_of_volume.param="PROPERTY"
    sensing_of_volume.value="volume"


    def sensing_of_variable(self, sprite="_stage_"):
        pass
    sensing_of_variable.opcode="sensing_of"


    def sensing_of_backdrop_no(self, stage="_stage_"):
        pass
    sensing_of_backdrop_no.opcode="sensing_of"
    sensing_of_backdrop_no.param="PROPERTY"
    sensing_of_backdrop_no.value="backdrop #"


    def sensing_of_backdrop_name(self, stage="_stage_"):
        pass
    sensing_of_backdrop_name.opcode="sensing_of"
    sensing_of_backdrop_name.param="PROPERTY"
    sensing_of_backdrop_name.value="backdrop name"

    def sensing_current_year(self):
        pass
    sensing_current_year.opcode="sensing_current"
    sensing_current_year.param="CURRENTMENU"
    sensing_current_year.value="YEAR"


    def sensing_current_month(self):
        pass
    sensing_current_month.opcode="sensing_current"
    sensing_current_month.param="CURRENTMENU"
    sensing_current_month.value="MONTH"


    def sensing_current_date(self):
        pass
    sensing_current_date.opcode="sensing_current"
    sensing_current_date.param="CURRENTMENU"
    sensing_current_date.value="DATE"


    def sensing_current_dayofweek(self):
        pass
    sensing_current_dayofweek.opcode="sensing_current"
    sensing_current_dayofweek.param="CURRENTMENU"
    sensing_current_dayofweek.value="DAYOFWEEK"


    def sensing_current_hour(self):
        pass
    sensing_current_hour.opcode="sensing_current"
    sensing_current_hour.param="CURRENTMENU"
    sensing_current_hour.value="HOUR"


    def sensing_current_minute(self):
        pass
    sensing_current_minute.opcode="sensing_current"
    sensing_current_minute.param="CURRENTMENU"
    sensing_current_minute.value="MINUTE"


    def sensing_current_second(self):
        pass
    sensing_current_second.opcode="sensing_current"
    sensing_current_second.param="CURRENTMENU"
    sensing_current_second.value="SECOND"


    def sensing_dayssince2000(self):
        pass

    def sensing_username(self):
        # Makes not a lot of sense, maybe for compatibility?
        pass

class _SensingSprite(BaseSprite):
    def __init__(self):
        super().__init__()

    def sensing_touchingobject_mouse(self):
        pass
    sensing_touchingobject_mouse.opcode="sensing_touchingobject"
    sensing_touchingobject_mouse.param="TOUCHINGOBJECTMENU"
    sensing_touchingobject_mouse.value="_mouse_"

    def sensing_touchingobject_edge(self):
        pass
    sensing_touchingobject_edge.opcode="sensing_touchingobject"
    sensing_touchingobject_edge.param="TOUCHINGOBJECTMENU"
    sensing_touchingobject_edge.value="_edge_"

    def sensing_touchingobject_sprite(self):
        pass
    sensing_touchingobject_sprite.opcode="sensing_touchingobject"

    def sensing_touchingcolor(self, color):
        pass

    def sensing_coloristouchingcolor(self, sprite_color, color):
        pass

    def sensing_distanceto_mouse(self):
        pass
    sensing_distanceto_mouse.opcode="sensing_distanceto"
    sensing_distanceto_mouse.param="DISTANCETOMENU"
    sensing_distanceto_mouse.value="_mouse_"

    def sensing_distanceto_sprite(self):
        pass
    sensing_distanceto_sprite.opcode="sensing_distanceto"


