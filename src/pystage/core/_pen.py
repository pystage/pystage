import pygame
from pystage.core._base_sprite import BaseSprite
from pystage.core.values import to_color, to_number



def int2(vec2):
    x = int(round(vec2[0]))
    y = int(round(vec2[1]))
    return pygame.Vector2(x, y)


class _PenStage(BaseSprite):
    """The only pen block of the stage: erase all."""

    def pen_clear(self):
        self.stage.pen_image.fill((0, 0, 0, 0))


class _Pen(_PenStage):

    def __init__(self):
        super().__init__()

        self.pen = False
        self.pen_color = pygame.Color(0, 0, 255)
        self.pen_size = 1


    def _pen_line(self, start, end):
        """Draw a line on the pen layer, if the pen is down."""
        if not self.pen:
            return
        image = self.stage.pen_image
        size = max(1, int(round(self.pen_size)))
        start, end = int2(start), int2(end)
        if start != end:
            pygame.draw.line(image, self.pen_color, start, end, width=size)
        if size > 2 or start == end:
            # Round ends, this is also the dot when the pen is put down.
            pygame.draw.circle(image, self.pen_color, start, size / 2)
            pygame.draw.circle(image, self.pen_color, end, size / 2)

    def pen_stamp(self):
        self.costume_manager.update_sprite_image()
        self.stage.pen_image.blit(self.image, self.rect)


    def pen_penDown(self):
        if not self.pen:
            self.pen = True
            self._pen_line(self._pos, self._pos)


    def pen_penUp(self):
        self.pen = False


    def pen_setPenColorToColor(self, color):
        # A new object, clones must not share the color with the original
        self.pen_color = to_color(color)

    pen_setPenColorToColor.translation = "pen_setcolor"


    def pen_changePenColorParamBy_color(self, value):
        value = to_number(value)
        hsva = list(self.pen_color.hsva)
        hsva[0] = (hsva[0] + (value * 3.6)) % 360
        self.pen_color.hsva = hsva

    pen_changePenColorParamBy_color.opcode="pen_changePenColorParamBy"
    pen_changePenColorParamBy_color.param="COLOR_PARAM"
    pen_changePenColorParamBy_color.value="color"
    pen_changePenColorParamBy_color.translation="pen_colormenu_color"
    pen_changePenColorParamBy_color.translation_hint="Needs to be distinguished from setPenColorToColor. This is only the hue value."
    pen_changePenColorParamBy_color.outer_translation="pen_changecolorparam"
    pen_changePenColorParamBy_color.position="[COLOR_PARAM]"


    def pen_changePenColorParamBy_saturation(self, value):
        value = to_number(value)
        hsva = list(self.pen_color.hsva)
        hsva[1] = (hsva[1] + (value)) % 100
        self.pen_color.hsva = hsva

    pen_changePenColorParamBy_saturation.opcode="pen_changePenColorParamBy"
    pen_changePenColorParamBy_saturation.param="COLOR_PARAM"
    pen_changePenColorParamBy_saturation.value="saturation"
    pen_changePenColorParamBy_saturation.translation="pen_colormenu_saturation"
    pen_changePenColorParamBy_saturation.outer_translation="pen_changecolorparam"
    pen_changePenColorParamBy_saturation.position="[COLOR_PARAM]"
    

    def pen_changePenColorParamBy_brightness(self, value):
        value = to_number(value)
        hsva = list(self.pen_color.hsva)
        hsva[2] = (hsva[2] + (value)) % 100
        self.pen_color.hsva = hsva

    pen_changePenColorParamBy_brightness.opcode="pen_changePenColorParamBy"
    pen_changePenColorParamBy_brightness.param="COLOR_PARAM"
    pen_changePenColorParamBy_brightness.value="brightness"
    pen_changePenColorParamBy_brightness.translation="pen_colormenu_brightness"
    pen_changePenColorParamBy_brightness.outer_translation="pen_changecolorparam"
    pen_changePenColorParamBy_brightness.position="[COLOR_PARAM]"
    

    def pen_changePenColorParamBy_transparency(self, value):
        value = to_number(value)
        hsva = list(self.pen_color.hsva)
        hsva[3] = 100 - (((100 - hsva[3]) + (value)) % 100)
        self.pen_color.hsva = hsva

    pen_changePenColorParamBy_transparency.opcode="pen_changePenColorParamBy"
    pen_changePenColorParamBy_transparency.param="COLOR_PARAM"
    pen_changePenColorParamBy_transparency.value="transparency"
    pen_changePenColorParamBy_transparency.translation="pen_colormenu_transparency"
    pen_changePenColorParamBy_transparency.outer_translation="pen_changecolorparam"
    pen_changePenColorParamBy_transparency.position="[COLOR_PARAM]"


    def pen_setPenColorParamTo_color(self, value):
        value = to_number(value)
        hsva = list(self.pen_color.hsva)
        hsva[0] = (value * 3.6) % 360 
        self.pen_color.hsva = hsva

    pen_setPenColorParamTo_color.opcode="pen_setPenColorParamTo"
    pen_setPenColorParamTo_color.param="COLOR_PARAM"
    pen_setPenColorParamTo_color.value="color"
    pen_setPenColorParamTo_color.translation="pen_colormenu_color"
    pen_setPenColorParamTo_color.translation_hint="Needs to be distinguished from setPenColorToColor. This is only the hue value."
    pen_setPenColorParamTo_color.outer_translation="pen_setcolorparam"
    pen_setPenColorParamTo_color.position="[COLOR_PARAM]"


    def pen_setPenColorParamTo_saturation(self, value):
        value = to_number(value)
        hsva = list(self.pen_color.hsva)
        hsva[1] = value % 100
        self.pen_color.hsva = hsva

    pen_setPenColorParamTo_saturation.opcode="pen_setPenColorParamTo"
    pen_setPenColorParamTo_saturation.param="COLOR_PARAM"
    pen_setPenColorParamTo_saturation.value="saturation"
    pen_setPenColorParamTo_saturation.translation="pen_colormenu_saturation"
    pen_setPenColorParamTo_saturation.outer_translation="pen_setcolorparam"
    pen_setPenColorParamTo_saturation.position="[COLOR_PARAM]"
    

    def pen_setPenColorParamTo_brightness(self, value):
        value = to_number(value)
        hsva = list(self.pen_color.hsva)
        hsva[2] = value % 100
        self.pen_color.hsva = hsva

    pen_setPenColorParamTo_brightness.opcode="pen_setPenColorParamTo"
    pen_setPenColorParamTo_brightness.param="COLOR_PARAM"
    pen_setPenColorParamTo_brightness.value="brightness"
    pen_setPenColorParamTo_brightness.translation="pen_colormenu_brightness"
    pen_setPenColorParamTo_brightness.outer_translation="pen_setcolorparam"
    pen_setPenColorParamTo_brightness.position="[COLOR_PARAM]"
    

    def pen_setPenColorParamTo_transparency(self, value):
        value = to_number(value)
        hsva = list(self.pen_color.hsva)
        hsva[3] = 100 - (value % 100)
        self.pen_color.hsva = hsva

    pen_setPenColorParamTo_transparency.opcode="pen_setPenColorParamTo"
    pen_setPenColorParamTo_transparency.param="COLOR_PARAM"
    pen_setPenColorParamTo_transparency.value="transparency"
    pen_setPenColorParamTo_transparency.translation="pen_colormenu_transparency"
    pen_setPenColorParamTo_transparency.outer_translation="pen_setcolorparam"
    pen_setPenColorParamTo_transparency.position="[COLOR_PARAM]"


    def pen_changePenSizeBy(self, value):
        self.pen_size = max(1, self.pen_size + to_number(value))

    pen_changePenSizeBy.translation = "pen_changesize"

    def pen_setPenSizeTo(self, value):
        self.pen_size = max(1, to_number(value))

    pen_setPenSizeTo.translation = "pen_setsize"
