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


    def pen_changePenColorParamBy_color(self, value):
        pass

    pen_changePenColorParamBy_color.opcode="pen_changePenColorParamBy"
    pen_changePenColorParamBy_color.param="COLOR_PARAM"
    pen_changePenColorParamBy_color.value="color"


    def pen_changePenColorParamBy_saturation(self, value):
        pass

    pen_changePenColorParamBy_saturation.opcode="pen_changePenColorParamBy"
    pen_changePenColorParamBy_saturation.param="COLOR_PARAM"
    pen_changePenColorParamBy_saturation.value="saturation"
    

    def pen_changePenColorParamBy_brightness(self, value):
        pass

    pen_changePenColorParamBy_brightness.opcode="pen_changePenColorParamBy"
    pen_changePenColorParamBy_brightness.param="COLOR_PARAM"
    pen_changePenColorParamBy_brightness.value="brightness"
    

    def pen_changePenColorParamBy_transparency(self, value):
        pass

    pen_changePenColorParamBy_transparency.opcode="pen_changePenColorParamBy"
    pen_changePenColorParamBy_transparency.param="COLOR_PARAM"
    pen_changePenColorParamBy_transparency.value="transparency"


    def pen_setPenColorParamTo_color(self, value):
        pass

    pen_setPenColorParamTo_color.opcode="pen_setPenColorParamTo"
    pen_setPenColorParamTo_color.param="COLOR_PARAM"
    pen_setPenColorParamTo_color.value="color"


    def pen_setPenColorParamTo_saturation(self, value):
        pass

    pen_setPenColorParamTo_saturation.opcode="pen_setPenColorParamTo"
    pen_setPenColorParamTo_saturation.param="COLOR_PARAM"
    pen_setPenColorParamTo_saturation.value="saturation"
    

    def pen_setPenColorParamTo_brightness(self, value):
        pass

    pen_setPenColorParamTo_brightness.opcode="pen_setPenColorParamTo"
    pen_setPenColorParamTo_brightness.param="COLOR_PARAM"
    pen_setPenColorParamTo_brightness.value="brightness"
    

    def pen_setPenColorParamTo_transparency(self, value):
        pass

    pen_setPenColorParamTo_transparency.opcode="pen_setPenColorParamTo"
    pen_setPenColorParamTo_transparency.param="COLOR_PARAM"
    pen_setPenColorParamTo_transparency.value="transparency"


    def pen_changePenSizeBy(self, value):
        pass

    def pen_setPenSizeTo(self, value):
        pass

