class _Pen():
    ##
    # Pen Extension
    #

    def erase_all(self):
        pass

    def stamp(self):
        pass

    def pen_down(self):
        self.pen = True

    def pen_up(self):
        self.pen = False

    def set_pen_color_to(self, color):
        self.color = color

    def change_pen_effect_by(self, effect, value):
        # Similar to graphics effect, again: separate methods?
        # - color
        # - saturation
        # - brightness
        # - transparency
        pass

    def set_pen_effect_to(self, effect, value):
        pass

    def change_pen_size_by(self, value):
        pass

    def set_pen_size_to(self, value):
        pass

