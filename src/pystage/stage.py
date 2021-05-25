import pygame

from pystage import Sprite

class Stage():
    running = False
    FPS = 60
    dt = 0
    sprites = []
    background_color = (255, 255, 255)

    def __init__(self, width=480, height=360):
        pygame.init()
        self.screen = pygame.display.set_mode([width, height])
        self.clock = pygame.time.Clock()
        self.width = width
        self.height = height


    def create_sprite(self, constructor=Sprite):
        sprite = constructor(self)
        self.sprites.append(sprite)
        return sprite

    # TODO: Implement the API for stage blocks

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
                        sprite._process_key_pressed(event.key)

            self.screen.fill(self.background_color)

            for sprite in self.sprites:
                sprite._update(dt)
                sprite._draw()

            pygame.display.flip()
            dt = self.clock.tick(self.FPS) / 1000

        pygame.quit()

