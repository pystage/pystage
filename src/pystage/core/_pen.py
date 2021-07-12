class _Pen():

    def __init__(self):
        super().__init__()

        self.pen = False
        self.color = (255,0,0)


    def pen_clear(self):
        pass


    def pen_stamp(self):
        pass


    def pen_penDown(self):
        self.pen = True


    def pen_penUp(self):
        self.pen = False


    def pen_setPenColorToColor(self, color):
        self.color = color

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
        pass

    pen_changePenSizeBy.translation = "pen_changesize"

    def pen_setPenSizeTo(self, value):
        pass

    pen_setPenSizeTo.translation = "pen_setsize"
