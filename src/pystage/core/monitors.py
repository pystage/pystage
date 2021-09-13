import pygame
import pkg_resources

class Monitor(pygame.sprite.Sprite):

    bold_font_9 = pygame.font.Font(pkg_resources.resource_filename("pystage", "fonts/roboto-bold.ttf"), 9)
    light_font_9 = pygame.font.Font(pkg_resources.resource_filename("pystage", "fonts/roboto-bold.ttf"), 9)

    variable_color = (255, 140, 26)
    background_color = (230, 240, 255)
    border_color = (196, 204, 217)
    title_font_color = (87, 94, 117)
    value_font_color = (255, 255, 255)

    NORMAL = 1
    LARGE = 2
    SLIDER = 3

    def __init__(self, sprite_or_stage, title, value, mode=1):
        super().__init__()
        self.sprite_or_stage = sprite_or_stage
        self.sprite_or_stage.stage.monitor_group.add(self)
        self.title = title
        self._value = value
        # Pygame coordinates, upper left corner
        self._hidden = False
        self.image = None
        self.rect = None
        self.update_image()


    def update_image(self):
        if self._hidden:
            return
        pos = self.rect.topleft if self.rect else (0,0)
        title_surface = Monitor.bold_font_9.render(self.title, True, Monitor.title_font_color)
        value_surface = Monitor.light_font_9.render(str(self._value), True, Monitor.value_font_color)
        
        padding = 10

        rect_w = max(40, value_surface.get_width() + padding)
        rect_h = value_surface.get_height() + padding/2
        rect_surface = pygame.Surface((rect_w, rect_h), pygame.SRCALPHA)
        pygame.draw.rect(rect_surface, Monitor.variable_color, (0,0, rect_w, rect_h), border_radius=3)
        rect_surface.blit(value_surface, (rect_surface.get_width()/2 - value_surface.get_width()/2, padding/4))
        
        w = padding + title_surface.get_width() + padding + rect_surface.get_width() + padding
        h = rect_surface.get_height() + padding/2
        surface = pygame.Surface((w, h), flags=pygame.SRCALPHA)
        pygame.draw.rect(surface, Monitor.background_color, (0,0,w,h), border_radius=3)
        pygame.draw.rect(surface, Monitor.border_color, (0,0,w,h), width=1, border_radius=3)
        surface.blit(title_surface, (padding, padding/2))
        surface.blit(rect_surface, (padding + title_surface.get_width() + padding, padding/4))
        self.image = surface
        self.rect = surface.get_rect()
        self.rect.topleft = pos


    def set_position(self, x,y):
        if not self.rect:
            return
        self.rect.x = x + self.sprite_or_stage.stage.center_x
        self.rect.y = -y + self.sprite_or_stage.stage.center_y


    def set_value(self, value):
        if self._value == value:
            return
        self._value = value
        self.update_image()


    def show(self):
        self._hidden = False
        self.update_image()


    def hide(self):
        self._hidden = True

    
    def remove(self):
        del self.sprite_or_stage.monitors[self.title]
        self.kill()
