import pygame

from pystage.core.sprite import Sprite

# Mixins
from pystage.core._events import _Events
from pystage.core._looks_stage import _LooksStage
from pystage.core._sound import _Sound
from pystage.core._sensing import _Sensing
from pystage.core._variables import _Variables
from pystage.core._operators import _Operators
from pystage.core._control import _Control
import os

class Stage(_LooksStage, _Sound, _Events, _Control, _Operators, _Sensing):


    def __init__(self, name="Welcome to pyStage!", width=480, height=360):
        super().__init__()
        # This way, code blocks can consistently refer to the stage with self.stage:
        self.stage = self

        pygame.init()
        pygame.display.set_caption(name)
        self.running = False
        self.FPS = 60
        self.dt = 0
        self.sprites = []
        self.background_color = (255, 255, 255)
        # surface is where the whole stage is rendered to
        # it defines the in-game resolution
        self.surface = pygame.Surface([width, height], flags=pygame.SRCALPHA)
        # screen is the actual screen, the surface gets scaled
        self.screen = pygame.display.set_mode([width, height], pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.width = width
        self.height = height
        self.center_x = int(width / 2)
        self.center_y = int(height / 2)
        # current scale factor of the stage if the window is resized
        self.scale_factor = 1
        # current offset of the top left corner if the window is resized 
        self.offset_x = 0
        self.offset_y = 0


    def create_sprite(self, costume="default", constructor=Sprite):
        sprite = constructor(self, costume)
        self.sprites.append(sprite)
        return sprite


    def add_backdrop(self, name, center_x=None, center_y=None):
        self.costume_manager.add_costume(name, center_x, center_y)


    def replace_backdrop(self, index, name, center_x=None, center_y=None):
        self.costume_manager.replace_costume(index, name, center_x, center_y)


    def insert_backdrop(self, index, name, center_x=None, center_y=None):
        self.costume_manager.insert_costume(index, name, center_x, center_y)


    def _draw(self, surface: pygame.Surface):
        surface.fill(self.background_color)
        image = self.costume_manager.get_image()
        if not image:
            return
        center_x, center_y = self.costume_manager.get_center()
        surface.blit(image, (self.center_x - center_x, self.center_y - center_y))


    def play(self):
        self.running = True
        '''
        This runs the game loop
        '''
        dt = 0
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    for sprite in self.sprites:
                        sprite.code_manager.process_key_pressed(event.key)

            self._draw(self.surface)

            for sprite in self.sprites:
                sprite._update(dt)
                sprite._draw(self.surface)

            factor_x = self.screen.get_width() / self.surface.get_width()
            factor_y = self.screen.get_height() / self.surface.get_height()
            self.scale_factor = min(factor_x, factor_y)
            scaled = pygame.transform.smoothscale(self.surface, (
                int(self.surface.get_width() * self.scale_factor), 
                int(self.surface.get_height() * self.scale_factor)))
            self.offset_x = int((self.screen.get_width() - scaled.get_width())/2)
            self.offset_y = int((self.screen.get_height() - scaled.get_height())/2)
            self.screen.blit(scaled, (
                self.offset_x,
                self.offset_y,
                ))
            pygame.display.flip()

            dt = self.clock.tick(self.FPS) / 1000

        pygame.quit()
