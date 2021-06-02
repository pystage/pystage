import pygame

from pystage import Sprite

# Mixins
from pystage._events import _Events
from pystage._looks_stage import _LooksStage
from pystage._sound import _Sound
from pystage._sensing import _Sensing
from pystage._variables import _Variables
from pystage._control import _Control
import os

class Stage(_LooksStage, _Sound, _Events, _Control, _Sensing):


    def __init__(self, width=480, height=360):
        pygame.init()
        self.running = False
        self.FPS = 60
        self.dt = 0
        self.sprites = []
        self.background_color = (255, 255, 255)
        self.screen = pygame.display.set_mode([width, height])
        self.clock = pygame.time.Clock()
        self.width = width
        self.height = height
        self.center_x = int(width / 2)
        self.center_y = int(height / 2)
        self.backdrops = []
        self.current_backdrop = -1


    def create_sprite(self, costume="default", constructor=Sprite):
        sprite = constructor(self, costume)
        self.sprites.append(sprite)
        return sprite


    def add_backdrop(self, name, center_x=None, center_y=None):
        if isinstance(name, str):
            backdrop = Backdrop(self, name, center_x, center_y)
            self.backdrops.append(backdrop)
            if self.current_backdrop==-1:
                self.current_backdrop = len(self.backdrops) - 1
        else:
            for n in name:
                self.add_backdrop(n)


    def replace_backdrop(self, index, name, center_x=None, center_y=None):
        backdrop = Costume(self, name, center_x, center_y)
        del self.backdrops[index]
        self.backdrops.insert(index, backdrop)


    def insert_backdrop(self, index, name, center_x=None, center_y=None):
        backdrop = Costume(self, name, center_x, center_y)
        self.backdrops.insert(index, backdrop)


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

            self.screen.fill(self.background_color)

            for sprite in self.sprites:
                sprite._update(dt)
                sprite._draw()

            pygame.display.flip()
            dt = self.clock.tick(self.FPS) / 1000

        pygame.quit()
