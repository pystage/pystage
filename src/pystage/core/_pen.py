import pygame
from pystage.core._base_sprite import BaseSprite


class _Pen(BaseSprite):

    def __init__(self):
        super().__init__()

        self.pen = False
        self.pen_color = (255,0,0)
        self.pen_size = 3
        self.old_position = (0,0)
        self.pen_up_at = (0,0)


    def _get_image(self):
        if not self in self.stage.pen_images:
            image = pygame.Surface((self.stage.width, self.stage.height), flags=pygame.SRCALPHA)
            self.stage.pen_images[self] = image
        return self.stage.pen_images[self]

    def _update_pen(self):
        if self.pen:
            position = self._pg_pos()
            if position == self.old_position:
                return
            pygame.draw.line(self._get_image(), self.pen_color, self.old_position, position, width=self.pen_size)
            self.old_position = position
        else:
            if self.pen_up_at != self.old_position:
                pygame.draw.line(self._get_image(), self.pen_color, self.old_position, self.pen_up_at, width=self.pen_size)
                self.pen_up_at = self.old_position

    def pen_clear(self):
        if self in self.stage.pen_images:
            del self.stage.pen_images[self]


    def pen_stamp(self):
        pass


    def pen_penDown(self):
        if not self.pen:
            self.old_position = self._pg_pos()
        self.pen = True


    def pen_penUp(self):
        self.pen_up_at = self._pg_pos()
        self.pen = False


    def pen_setPenColorToColor(self, color):
        self.pen_color = color

    pen_setPenColorToColor.translation = "pen_setcolor"


    def pen_changePenColorParamBy_color(self, value):
        pass

    pen_changePenColorParamBy_color.opcode="pen_changePenColorParamBy"
    pen_changePenColorParamBy_color.param="COLOR_PARAM"
    pen_changePenColorParamBy_color.value="color"
    pen_changePenColorParamBy_color.translation="pen_colormenu_color"
    pen_changePenColorParamBy_color.translation_hint="Needs to be distinguished from setPenColorToColor. This is only the hue value."
    pen_changePenColorParamBy_color.outer_translation="pen_changecolorparam"
    pen_changePenColorParamBy_color.position="[COLOR_PARAM]"


    def pen_changePenColorParamBy_saturation(self, value):
        pass

    pen_changePenColorParamBy_saturation.opcode="pen_changePenColorParamBy"
    pen_changePenColorParamBy_saturation.param="COLOR_PARAM"
    pen_changePenColorParamBy_saturation.value="saturation"
    pen_changePenColorParamBy_saturation.translation="pen_colormenu_saturation"
    pen_changePenColorParamBy_saturation.outer_translation="pen_changecolorparam"
    pen_changePenColorParamBy_saturation.position="[COLOR_PARAM]"
    

    def pen_changePenColorParamBy_brightness(self, value):
        pass

    pen_changePenColorParamBy_brightness.opcode="pen_changePenColorParamBy"
    pen_changePenColorParamBy_brightness.param="COLOR_PARAM"
    pen_changePenColorParamBy_brightness.value="brightness"
    pen_changePenColorParamBy_brightness.translation="pen_colormenu_brightness"
    pen_changePenColorParamBy_brightness.outer_translation="pen_changecolorparam"
    pen_changePenColorParamBy_brightness.position="[COLOR_PARAM]"
    

    def pen_changePenColorParamBy_transparency(self, value):
        pass

    pen_changePenColorParamBy_transparency.opcode="pen_changePenColorParamBy"
    pen_changePenColorParamBy_transparency.param="COLOR_PARAM"
    pen_changePenColorParamBy_transparency.value="transparency"
    pen_changePenColorParamBy_transparency.translation="pen_colormenu_transparency"
    pen_changePenColorParamBy_transparency.outer_translation="pen_changecolorparam"
    pen_changePenColorParamBy_transparency.position="[COLOR_PARAM]"


    def pen_setPenColorParamTo_color(self, value):
        pass

    pen_setPenColorParamTo_color.opcode="pen_setPenColorParamTo"
    pen_setPenColorParamTo_color.param="COLOR_PARAM"
    pen_setPenColorParamTo_color.value="color"
    pen_setPenColorParamTo_color.translation="pen_colormenu_color"
    pen_setPenColorParamTo_color.translation_hint="Needs to be distinguished from setPenColorToColor. This is only the hue value."
    pen_setPenColorParamTo_color.outer_translation="pen_setcolorparam"
    pen_setPenColorParamTo_color.position="[COLOR_PARAM]"


    def pen_setPenColorParamTo_saturation(self, value):
        pass

    pen_setPenColorParamTo_saturation.opcode="pen_setPenColorParamTo"
    pen_setPenColorParamTo_saturation.param="COLOR_PARAM"
    pen_setPenColorParamTo_saturation.value="saturation"
    pen_setPenColorParamTo_saturation.translation="pen_colormenu_saturation"
    pen_setPenColorParamTo_saturation.outer_translation="pen_setcolorparam"
    pen_setPenColorParamTo_saturation.position="[COLOR_PARAM]"
    

    def pen_setPenColorParamTo_brightness(self, value):
        pass

    pen_setPenColorParamTo_brightness.opcode="pen_setPenColorParamTo"
    pen_setPenColorParamTo_brightness.param="COLOR_PARAM"
    pen_setPenColorParamTo_brightness.value="brightness"
    pen_setPenColorParamTo_brightness.translation="pen_colormenu_brightness"
    pen_setPenColorParamTo_brightness.outer_translation="pen_setcolorparam"
    pen_setPenColorParamTo_brightness.position="[COLOR_PARAM]"
    

    def pen_setPenColorParamTo_transparency(self, value):
        pass

    pen_setPenColorParamTo_transparency.opcode="pen_setPenColorParamTo"
    pen_setPenColorParamTo_transparency.param="COLOR_PARAM"
    pen_setPenColorParamTo_transparency.value="transparency"
    pen_setPenColorParamTo_transparency.translation="pen_colormenu_transparency"
    pen_setPenColorParamTo_transparency.outer_translation="pen_setcolorparam"
    pen_setPenColorParamTo_transparency.position="[COLOR_PARAM]"


    def pen_changePenSizeBy(self, value):
        self.pen_size += value

    pen_changePenSizeBy.translation = "pen_changesize"

    def pen_setPenSizeTo(self, value):
        self.pen_size = value

    pen_setPenSizeTo.translation = "pen_setsize"
