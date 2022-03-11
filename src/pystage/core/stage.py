import pygame

from pystage.core.sprite import CoreSprite

# Mixins
from pystage.core._events import _Events
from pystage.core._looks import _LooksStage
from pystage.core._sound import _Sound
from pystage.core._sensing import _Sensing
from pystage.core._variables import _Variables
from pystage.core._operators import _Operators
from pystage.core._control import _Control
from pystage.core.messages import MessageBroker
from pystage.core.asking import InputManager

import os
import sys


class SpriteGroup(pygame.sprite.OrderedUpdates):

    def __init__(self):
        super().__init__()
    

    def get_layer(self, sprite):
        try:
            return self.sprites().index(sprite)
        except ValueError:
            return -1


    def to_front(self, sprite):
        if not sprite in self._spritelist:
            raise ValueError(f"Sprite {sprite} unknown.")
        self._spritelist.remove(sprite)
        self._spritelist.append(sprite)
        print(self._spritelist)


    def to_back(self, sprite):
        if not sprite in self._spritelist:
            raise ValueError(f"Sprite {sprite} unknown.")
        self._spritelist.remove(sprite)
        self._spritelist.insert(0, sprite)
        print(self._spritelist)


    def layer_forward(self, sprite, value=1):
        if not sprite in self._spritelist:
            raise ValueError(f"Sprite {sprite} unknown.")
        index = self._spritelist.index(sprite)
        self._spritelist.remove(sprite)
        new_index = index + value
        if new_index < 0:
            new_index = 0
        if new_index > len(self._spritelist) - 1:
            new_index = len(self._spritelist) - 1
        self._spritelist.insert(new_index, sprite)
        print(self._spritelist)


    def layer_backward(self, sprite, value=1):
        self.forwards(-value)


    def insert(self, i, sprite):
        self._spritelist.insert(i, sprite)


class CoreStage(_LooksStage, _Sound, _Events, _Control, _Operators, _Sensing, _Variables):


    def __init__(self, name="Welcome to pyStage!", width=480, height=360):
        # This way, code blocks can consistently refer to the stage with self.stage:
        self.stage = self
        # Above attributes need to be set first so that mixins can access them properly
        super().__init__()
        # The facade is the translated API
        self.facade = None
        self.sprite_facade_class : type = None

        self.message_broker = MessageBroker(self)
        self.input_manager = InputManager(self)

        pygame.init()
        pygame.display.set_caption(name)
        self.running = False
        self.FPS = 60
        self.dt = 0
        # The stage is added to the sprites as it also contains code.
        self.sprites = SpriteGroup()
        self.visible_sprites = SpriteGroup()
        self.bubbles = pygame.sprite.Group()
        self.visible_bubbles = pygame.sprite.Group()
        self.monitor_group = pygame.sprite.Group()
        self.pen_images = {}
        self.background_color = (255, 255, 255)
        # surface is where the whole stage is rendered to
        # it defines the in-game resolution
        self.surface = pygame.Surface([width, height], flags=pygame.SRCALPHA)
        # screen is the actual screen, the surface gets scaled
        self.screen = pygame.display.set_mode([width, height], pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.width = width
        self.height = height
        self.rect = pygame.rect.Rect(0,0,width, height)
        self.center_x = int(width / 2)
        self.center_y = int(height / 2)
        # current scale factor of the stage if the window is resized
        self.scale_factor = 1
        # current offset of the top left corner if the window is resized 
        self.offset_x = 0
        self.offset_y = 0

        self.timer = 0
        self.show_sprite_boundaries = "--show-sprite-boundaries" in sys.argv


    def pystage_createsprite(self, costume="default"):
        sprite = CoreSprite(self, costume)
        self.sprites.add(sprite)
        self._update_visible()
        if self.sprite_facade_class:
            return self.sprite_facade_class(sprite) # pylint: disable=E1102
            # pylint produces a false positive here
            # https://github.com/PyCQA/pylint/issues/1493
        else:
            return sprite


    def _update_visible(self):
        self.visible_sprites.empty()
        self.visible_bubbles.empty()
        for sprite in self.sprites:
            if sprite.visible:
                self.visible_sprites.add(sprite)
                if sprite.bubble_manager.bubble:
                    self.visible_bubbles.add(sprite.bubble_manager.bubble)


    def _update(self, dt):
        self.code_manager._update(dt)


    def _draw(self, surface: pygame.Surface):
        surface.fill(self.background_color)
        image = self.costume_manager.get_image()
        if not image:
            return
        center_x, center_y = self.costume_manager.get_center()
        surface.blit(image, (0,0))


    def pystage_play(self):
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
                    if self.input_manager.is_active():
                        self.input_manager.process_key(event)
                    else:
                        for sprite in self.sprites:
                            sprite.code_manager.process_key_pressed(event.key)
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.Vector2(pygame.mouse.get_pos())
                    for sprite in self.visible_sprites.sprites()[-1:0:-1]:
                        if sprite.rect.collidepoint(pos):
                            internal_pos = pos - sprite.rect.topleft
                            x = int(internal_pos.x)
                            y = int(internal_pos.y)
                            color = sprite.image.get_at((x, y))
                            if color.a == 0:
                                continue
                            sprite.code_manager.process_click()
                            break

            # Handle broadcast messages
            for message in self.message_broker.get_messages():
                for sprite in self.sprites:
                    sprite.code_manager.process_broadcast(message)
            self.message_broker.mark_completed()

            self._update(dt)
            self.sprites.update(dt)
            self.bubbles.update()
            self.input_manager.update(dt)
            self.monitor_group.update()

            self._draw(self.surface)
            for sprite in self.pen_images:
                image = self.pen_images[sprite]
                self.surface.blit(image, (0, 0))

            self.visible_sprites.draw(self.surface)
            self.bubbles.draw(self.surface)
            self.input_manager.draw(self.surface)

            self.monitor_group.draw(self.surface)

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
            self.timer += dt

        pygame.quit()
