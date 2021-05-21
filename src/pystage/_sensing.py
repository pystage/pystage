class _Sensing():
    ##
    # Sensing
    #

    def is_touching_mouse_pointer(self):
        pass

    def is_touching_edge(self):
        pass

    def is_touching_sprite(self, sprite):
        pass

    def is_touching_color(self, color):
        pass

    def is_color_touching_color(self, sprite_color, color):
        pass

    def get_distance_to_mouse_pointer(self):
        pass

    def get_distance_to_sprite(self, sprite):
        pass

    def ask_and_wait(self, question):
        # an input field, answer needs to be available somehow
        pass

    def get_answer(self):
        # Answer of the last question
        pass

    def is_key_pressed(self, key):
        pass

    def is_mouse_down(self):
        pass

    def get_mouse_x(self):
        pass

    def get_mouse_y(self):
        pass

    def set_draggable(self, value):
        pass

    def get_loudness(self):
        # See events area, not sure if we support microphone access
        pass

    def get_timer(self):
        pass

    def reset_timer(self):
        pass

    # the get_something_from_stage seems to be fully redundant
    # the get_something_from_sprite should be done via the methods of the respective sprite.
    # TODO: needs documentation

    def get_current_year(self):
        pass

    def get_current_month(self):
        pass

    def get_current_date(self):
        pass

    def get_current_day_of_week(self):
        pass

    def get_current_hour(self):
        pass

    def get_current_minute(self):
        pass

    def get_current_second(self):
        pass

    def get_days_since_2000(self):
        pass

    def get_username(self):
        # Makes not a lot of sense, maybe for compatibility?
        pass

