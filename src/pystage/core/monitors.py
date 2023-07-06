import pygame
import pkg_resources


class Monitor(pygame.sprite.Sprite):

    BOLD_FONT_12 = pygame.font.Font(pkg_resources.resource_filename("pystage", "fonts/roboto-bold.ttf"), 12)
    LIGHT_FONT_12 = pygame.font.Font(pkg_resources.resource_filename("pystage", "fonts/roboto-light.ttf"), 12)
    LIGHT_FONT_14 = pygame.font.Font(pkg_resources.resource_filename("pystage", "fonts/roboto-light.ttf"), 14)

    VARIABLE_COLOR = (255, 140, 26)
    MOTION_COLOR = (76, 151, 255)
    SOUND_COLOR = (207, 99, 207)
    SENSING_COLOR = (92, 177, 214)
    BACKGROUND_COLOR = (230, 240, 255)
    BORDER_COLOR = (196, 204, 217)
    TITLE_FONT_COLOR = (87, 94, 117)
    VALUE_FONT_COLOR = (255, 255, 255)
    LIST_TITLE_BG_COLOR = (255, 255, 255)

    NORMAL = 1
    LARGE = 2
    SLIDER = 3

    def __init__(self, sprite_or_stage, title, color=VARIABLE_COLOR, mode=1, is_list=False):
        super().__init__()
        self.sprite_or_stage = sprite_or_stage
        # Visible sprites go into this group
        self.sprite_or_stage.stage.monitor_group.add(self)
        self._title = title
        self.is_list = is_list
        self._value = [] if is_list else 0
        self._color = color
        # Pygame coordinates, upper left corner
        self.image = None
        self.rect = None
        # Start showing nth item of a list
        self.offset = 0
        # if func is set, it is used to automatically update the monitor
        self._func = None
        self._style = Monitor.NORMAL

        self.update_image()


    def update(self):
        if not self._func:
            return
        # set_value checks if the value is changed
        self.set_value(self._func())


    def update_image(self):
        pos = self.rect.topleft if self.rect else (0,0)

        if self.is_list:
            surface = self.render_list()
        elif self._style == Monitor.LARGE:
            surface = self.render_large()
        elif self._style == Monitor.SLIDER:
            surface = self.render_slider()
        else:
            surface = self.render_normal()
        self.image = surface
        self.rect = surface.get_rect()
        self.rect.topleft = pos


    def scroll_down(self, amount=1):
        self.offset += amount
        self.offset = max(min(len(self._value) - 5, self.offset), 0)
        self.update_image()


    def scroll_up(self):
        self.scroll_down(-1)


    def render_list(self):
        renderTitle = lambda val: Monitor.BOLD_FONT_12.render(val, True, Monitor.TITLE_FONT_COLOR)
        renderValue = lambda val: Monitor.LIGHT_FONT_12.render(val, True, Monitor.VALUE_FONT_COLOR)

        W = 102
        H = 202
        padding = 10

        # frame
        surface = pygame.Surface((W, H), pygame.SRCALPHA)

        # title
        if len(self._title) > 15:
            title_surface = renderTitle(self._title[:15] + "...")
        else:
            title_surface = renderTitle(self._title)

        # values
        value_surfaces = []
        for value in self._value:
            value = str(value)
            if len(value) > 7:
                value_surfaces.append(renderValue(value[:7] + "..."))
            else:
                value_surfaces.append(renderValue(value))

        # length
        length_surface = renderTitle(f"length {len(self._value)}")
        
        # draw background
        top_h = title_surface.get_height() + padding
        bot_h = length_surface.get_height() + padding
        mid_h = H - top_h - bot_h
        pygame.draw.rect(surface, Monitor.LIST_TITLE_BG_COLOR, (0, 0, W, top_h), border_radius=3)
        pygame.draw.rect(surface, Monitor.BACKGROUND_COLOR, (0, top_h, W, mid_h))
        pygame.draw.rect(surface, Monitor.LIST_TITLE_BG_COLOR, (0, top_h+mid_h, W, bot_h), border_radius=3)
        
        # render values
        surface.blit(title_surface, ((W - title_surface.get_width()) / 2, padding/2))

        for i, value_surface in enumerate(value_surfaces[self.offset:self.offset+5]):
            pygame.draw.rect(
                surface,
                (255, 102, 26),
                (25, top_h+3+(i*(value_surface.get_height()+padding*1.5)), W-30, value_surface.get_height()+padding),
                border_radius=3
            )
            surface.blit(value_surface, (25 + (W-30-value_surface.get_width())/2, top_h+3+(i*(value_surface.get_height()+padding*1.5))+padding/2))
            number = renderTitle(str(i+1+self.offset))
            surface.blit(number, ((25-number.get_width())/2, top_h+3+(i*(value_surface.get_height()+padding*1.5))+padding/2))
        surface.blit(length_surface, ((W - length_surface.get_width()) / 2, top_h+mid_h+(padding/2)))

        # border
        pygame.draw.rect(surface, Monitor.BORDER_COLOR, (0,0,W,H), width=1, border_radius=3)
        return surface
    

    def render_normal(self):
        title_surface = Monitor.BOLD_FONT_12.render(self._title, True, Monitor.TITLE_FONT_COLOR)
        value_surface = Monitor.LIGHT_FONT_12.render(str(self._value), True, Monitor.VALUE_FONT_COLOR)
        
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
        pygame.draw.rect(surface, Monitor.BORDER_COLOR, (0,0,w,h), width=1, border_radius=3)
        surface.blit(title_surface, (padding, padding/2))
        surface.blit(rect_surface, (padding + title_surface.get_width() + padding, padding/4))
        return surface


    def render_large(self):
        value_surface = Monitor.LIGHT_FONT_14.render(str(self._value), True, Monitor.VALUE_FONT_COLOR)
        
        padding = 8

        rect_w = value_surface.get_width() + padding * 2
        rect_h = value_surface.get_height() + padding * 2
        surface = pygame.Surface((rect_w, rect_h), pygame.SRCALPHA)
        pygame.draw.rect(surface, self._color, (0,0, rect_w, rect_h), border_radius=3)
        pygame.draw.rect(surface, Monitor.BORDER_COLOR, (0,0,rect_w, rect_h), width=1, border_radius=3)
        surface.blit(value_surface, (surface.get_width()/2 - value_surface.get_width()/2, padding))
        return surface


    def render_slider(self):
        surface = pygame.Surface((10,10), pygame.SRCALPHA)
        return surface


    def set_position(self, x,y):
        if not self.rect:
            return
        self.rect.x = x + self.sprite_or_stage.stage.center_x
        self.rect.y = -y + self.sprite_or_stage.stage.center_y


    def set_style(self, style):
        if style != self._style:
            self._style = style
            self.update_image()


    def set_value(self, value):
        '''Only change the value via this method!

        The method takes care of the rerendering, if needed.
        '''
        if type(value)==float:
            value = round(value, 2)
            if value == round(value):
                value = round(value)
        if self._value == value:
            return
        self._value = value if not self.is_list else list(value)
        self.update_image()


    def set_function(self, func):
        '''When a function is set, the monitor automatically updates.

        See update(self, dt).
        '''
        self._func = func


    def show(self):
        self.sprite_or_stage.stage.monitor_group.add(self)
        self.update_image()


    def hide(self):
        self.sprite_or_stage.stage.monitor_group.remove(self)

    
    def remove(self):
        del self.sprite_or_stage.monitors[self._title]
        self.kill()
