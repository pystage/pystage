import math

import pygame
from pystage.resources import resource_filename

from pystage.core.values import to_string
from pystage.core.i18n import tr

pygame.font.init()


class Monitor(pygame.sprite.Sprite):

    BOLD_FONT_9 = pygame.font.Font(resource_filename("fonts/roboto-bold.ttf"), 9)
    LIGHT_FONT_9 = pygame.font.Font(resource_filename("fonts/roboto-light.ttf"), 9)
    LIGHT_FONT_11 = pygame.font.Font(resource_filename("fonts/roboto-light.ttf"), 11)

    VARIABLE_COLOR = (255, 140, 26)
    LIST_COLOR = (252, 102, 44)
    MOTION_COLOR = (76, 151, 255)
    LOOKS_COLOR = (153, 102, 255)
    SOUND_COLOR = (207, 99, 207)
    SENSING_COLOR = (92, 177, 214)
    BACKGROUND_COLOR = (230, 240, 255)
    BORDER_COLOR = (196, 204, 217)
    TITLE_FONT_COLOR = (87, 94, 117)
    VALUE_FONT_COLOR = (255, 255, 255)

    NORMAL = 1
    LARGE = 2
    SLIDER = 3
    LIST = 4

    def __init__(self, sprite_or_stage, title, color=None, style=NORMAL):
        super().__init__()
        self.sprite_or_stage = sprite_or_stage
        # Visible monitors go into this group
        self.sprite_or_stage.stage.monitor_group.add(self)
        self._title = title
        self._value = [] if style == Monitor.LIST else 0
        if color is None:
            color = Monitor.LIST_COLOR if style == Monitor.LIST else Monitor.VARIABLE_COLOR
        self._color = color
        # Pygame coordinates, upper left corner
        self.image = None
        self.rect = None

        # if func is set, it is used to automatically update the monitor
        self._func = None
        self._style = style
        # Only used for lists, None means automatic
        self._width = None
        self._height = None
        # Only used for sliders: the range, whether only whole numbers are
        # allowed, the function that sets the value and the area of the
        # slider in the image (updated when it is rendered).
        self._min = 0
        self._max = 100
        self._discrete = True
        self._setter = None
        self._slider_rect = None
        # If set, the title is computed (e.g. the name of a sprite can change)
        self._title_func = None

        self.update_image()


    def update(self):
        if self._title_func:
            title = self._title_func()
            if title != self._title:
                self._title = title
                self.update_image()
        if not self._func:
            return
        # set_value checks if the value is changed
        self.set_value(self._func())


    def _render_normal(self, border=True):
        title_surface = Monitor.BOLD_FONT_9.render(self._title, True, Monitor.TITLE_FONT_COLOR)
        value_surface = Monitor.LIGHT_FONT_9.render(to_string(self._value), True, Monitor.VALUE_FONT_COLOR)

        padding = 10

        rect_w = max(40, value_surface.get_width() + padding)
        rect_h = value_surface.get_height() + padding/2
        rect_surface = pygame.Surface((rect_w, rect_h), pygame.SRCALPHA)
        pygame.draw.rect(rect_surface, self._color, (0,0, rect_w, rect_h), border_radius=3)
        rect_surface.blit(value_surface, (rect_surface.get_width()/2 - value_surface.get_width()/2, padding/4))

        w = padding + title_surface.get_width() + padding + rect_surface.get_width() + padding
        h = rect_surface.get_height() + padding/2
        surface = pygame.Surface((w, h), flags=pygame.SRCALPHA)
        pygame.draw.rect(surface, Monitor.BACKGROUND_COLOR, (0,0,w,h), border_radius=3)
        if border:
            pygame.draw.rect(surface, Monitor.BORDER_COLOR, (0,0,w,h), width=1, border_radius=3)
        surface.blit(title_surface, (padding, padding/2))
        surface.blit(rect_surface, (padding + title_surface.get_width() + padding, padding/4))
        return surface


    def _slider_fraction(self):
        span = self._max - self._min
        if span == 0:
            return 0
        try:
            value = float(self._value)
        except (TypeError, ValueError):
            value = self._min
        return max(0.0, min(1.0, (value - self._min) / span))


    def _render_slider(self):
        '''Like a normal monitor, with the slider below title and value.'''
        top = self._render_normal(border=False)
        padding = 10
        w = max(top.get_width(), 110)
        track_h = 4
        handle_r = 5
        h = top.get_height() + 2 * handle_r + 6
        surface = pygame.Surface((w, h), flags=pygame.SRCALPHA)
        pygame.draw.rect(surface, Monitor.BACKGROUND_COLOR, (0, 0, w, h), border_radius=3)
        # The top row is centered, the border is drawn last
        surface.blit(top, ((w - top.get_width()) // 2, 0))
        pygame.draw.rect(surface, Monitor.BORDER_COLOR, (0, 0, w, h), width=1, border_radius=3)
        # The handle stays completely inside of the monitor
        left, right = padding, w - padding
        y = top.get_height() + handle_r
        self._slider_rect = pygame.Rect(left, y - handle_r, right - left, 2 * handle_r)
        pygame.draw.rect(surface, Monitor.BORDER_COLOR, (left, y - track_h // 2, right - left, track_h), border_radius=2)
        x = left + round(self._slider_fraction() * (right - left))
        pygame.draw.rect(surface, self._color, (left, y - track_h // 2, x - left, track_h), border_radius=2)
        pygame.draw.circle(surface, (255, 255, 255), (x, y), handle_r)
        pygame.draw.circle(surface, self._color, (x, y), handle_r, width=2)
        return surface


    def configure_slider(self, minimum, maximum, discrete):
        '''Set the range of a slider. The minimum is never above the maximum.'''
        minimum, maximum = float(minimum), float(maximum)
        if minimum > maximum:
            minimum, maximum = maximum, minimum
        if discrete:
            minimum, maximum = round(minimum), round(maximum)
        else:
            minimum, maximum = round(minimum, 2), round(maximum, 2)
        self._min, self._max, self._discrete = minimum, maximum, bool(discrete)
        if self._style == Monitor.SLIDER:
            self.update_image()


    def set_setter(self, setter):
        '''The function that sets the variable when the slider is dragged.'''
        self._setter = setter


    def is_slider(self):
        return self._style == Monitor.SLIDER and self._slider_rect is not None


    def slider_hit(self, pos):
        '''True if pos (stage pixels, pygame coordinates) is on the slider.'''
        if not self.is_slider() or self.rect is None:
            return False
        area = self._slider_rect.move(self.rect.topleft).inflate(6, 6)
        return area.collidepoint(pos)


    def drag_to(self, x):
        '''Move the handle to the stage x position (pygame coordinates)
        and set the variable.'''
        if not self.is_slider() or self._setter is None:
            return
        left = self.rect.x + self._slider_rect.left
        fraction = max(0.0, min(1.0, (x - left) / max(1, self._slider_rect.width)))
        value = self._min + fraction * (self._max - self._min)
        value = round(value) if self._discrete else round(value, 2)
        if self._discrete is False and value == round(value):
            value = round(value)
        self._setter(value)
        self.set_value(value)


    def _render_large(self):
        value_surface = Monitor.LIGHT_FONT_11.render(to_string(self._value), True, Monitor.VALUE_FONT_COLOR)

        padding = 8

        rect_w = value_surface.get_width() + padding * 2
        rect_h = value_surface.get_height() + padding * 2
        surface = pygame.Surface((rect_w, rect_h), pygame.SRCALPHA)
        pygame.draw.rect(surface, self._color, (0,0, rect_w, rect_h), border_radius=3)
        pygame.draw.rect(surface, Monitor.BORDER_COLOR, (0,0,rect_w, rect_h), width=1, border_radius=3)
        surface.blit(value_surface, (surface.get_width()/2 - value_surface.get_width()/2, padding))
        return surface


    def _render_list(self):
        padding = 4
        row_h = Monitor.LIGHT_FONT_9.get_height() + padding
        title_surface = Monitor.BOLD_FONT_9.render(self._title, True, Monitor.TITLE_FONT_COLOR)
        header_h = title_surface.get_height() + 2 * padding
        footer_h = header_h
        items = list(self._value)

        w = int(self._width) if self._width else 100
        if self._height:
            h = int(self._height)
        else:
            h = header_h + footer_h + row_h * min(max(len(items), 1), 10) + padding
        w = max(w, 40)
        h = max(h, header_h + footer_h)

        surface = pygame.Surface((w, h), flags=pygame.SRCALPHA)
        pygame.draw.rect(surface, Monitor.BACKGROUND_COLOR, (0, 0, w, h), border_radius=3)
        pygame.draw.rect(surface, Monitor.BORDER_COLOR, (0, 0, w, h), width=1, border_radius=3)
        surface.blit(title_surface, (w/2 - title_surface.get_width()/2, padding))

        # Rows that fit, the rest is cut off (no scrolling).
        index_w = Monitor.LIGHT_FONT_9.size(str(max(len(items), 1)))[0] + 2 * padding
        y = header_h
        for i, item in enumerate(items):
            if y + row_h > h - footer_h:
                break
            index_surface = Monitor.LIGHT_FONT_9.render(str(i + 1), True, Monitor.TITLE_FONT_COLOR)
            surface.blit(index_surface, (padding, y + padding/2))
            row = pygame.Rect(index_w, y, w - index_w - padding, row_h - 1)
            pygame.draw.rect(surface, self._color, row, border_radius=3)
            value_surface = Monitor.LIGHT_FONT_9.render(to_string(item), True, Monitor.VALUE_FONT_COLOR)
            surface.blit(value_surface, (row.x + padding, y + padding/2), (0, 0, row.w - 2 * padding, row_h))
            y += row_h

        if not items:
            empty = Monitor.LIGHT_FONT_9.render(tr("monitor_empty"), True, Monitor.TITLE_FONT_COLOR)
            surface.blit(empty, (w/2 - empty.get_width()/2, header_h))
        length = Monitor.LIGHT_FONT_9.render(tr("monitor_length", length=len(items)), True, Monitor.TITLE_FONT_COLOR)
        surface.blit(length, (w/2 - length.get_width()/2, h - footer_h + padding))
        return surface


    def update_image(self):
        pos = self.rect.topleft if self.rect else (0,0)

        if self._style == Monitor.LARGE:
            surface = self._render_large()
        elif self._style == Monitor.LIST:
            surface = self._render_list()
        elif self._style == Monitor.SLIDER:
            surface = self._render_slider()
        else:
            surface = self._render_normal()
        if self._style != Monitor.SLIDER:
            self._slider_rect = None

        self.image = surface
        self.rect = surface.get_rect()
        self.rect.topleft = pos


    def set_position(self, x,y):
        if not self.rect:
            return
        self.rect.x = x + self.sprite_or_stage.stage.center_x
        self.rect.y = -y + self.sprite_or_stage.stage.center_y


    def set_size(self, width, height):
        '''Set the size of a list monitor. None or 0 means automatic.'''
        if (width or None) == self._width and (height or None) == self._height:
            return
        self._width = width or None
        self._height = height or None
        self.update_image()


    def set_style(self, style):
        if style != self._style:
            self._style = style
            self.update_image()


    def set_value(self, value):
        '''Only change the value via this method!

        The method takes care of the rerendering, if needed.
        '''
        if isinstance(value, list):
            # Lists are changed in place, we need a copy to detect changes.
            value = list(value)
        elif type(value)==float:
            if math.isfinite(value):
                value = round(value, 2)
                if value == round(value):
                    value = round(value)
        if self._value == value and type(self._value) == type(value):
            return
        self._value = value
        self.update_image()


    def set_title_function(self, func):
        '''The title is computed by the function instead of being fixed.'''
        self._title_func = func
        self._title = func()
        self.update_image()


    def set_function(self, func):
        '''When a function is set, the monitor automatically updates.

        See update(self).
        '''
        self._func = func


    def show(self):
        self.sprite_or_stage.stage.monitor_group.add(self)
        self.update_image()


    def hide(self):
        self.sprite_or_stage.stage.monitor_group.remove(self)


    def remove(self):
        self.kill()
