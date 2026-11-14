# pyright: basic, reportPrivateUsage=false
import sys

import pygame

# Mixins
from pystage.core._control import _Control
from pystage.core._events import _Events
from pystage.core._looks import _LooksStage
from pystage.core._operators import _Operators
from pystage.core._sensing import _Sensing
from pystage.core._sound import _Sound
from pystage.core._variables import _Variables
from pystage.core.messages import MessageBroker
from pystage.core.sprite import CoreSprite
from pystage.core.asking import InputManager


class SpriteGroup(pygame.sprite.OrderedUpdates):
    def __init__(self):
        super().__init__()
        # Be careful, we access a private variable here
        self._spritelist = self._spritelist

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
        # print(self._spritelist)

    def to_back(self, sprite):
        if not sprite in self._spritelist:
            raise ValueError(f"Sprite {sprite} unknown.")
        self._spritelist.remove(sprite)
        self._spritelist.insert(0, sprite)
        # print(self._spritelist)

    def layer_forward(self, sprite, value=1):
        if not sprite in self._spritelist:
            raise ValueError(f"Sprite {sprite} unknown.")
        index = self._spritelist.index(sprite)
        self._spritelist.remove(sprite)
        new_index = index + value
        if new_index < 0:
            new_index = 0
        # because the sprite was already removed above, so don't need to minus 1 for the length
        if new_index > len(self._spritelist):
            new_index = len(self._spritelist)
        self._spritelist.insert(new_index, sprite)
        # print(self._spritelist)

    def layer_backward(self, sprite, value=1):
        self.layer_forward(sprite, -value)

    def move_to(self, sprite, index):
        if not sprite in self._spritelist:
            raise ValueError(f"Sprite {sprite} unknown.")
        self._spritelist.remove(sprite)
        self._spritelist.insert(index, sprite)


class CoreStage(
    _LooksStage, _Sound, _Events, _Control, _Operators, _Sensing, _Variables
):
    def __init__(self, name="Welcome to pyStage!", width=480, height=360):
        # Check pygame version
        pygame_major = int(pygame.ver.split(".")[0])
        if pygame_major < 2:
            print("pygame version 2 or higher is required for PyStage.")
            print("Update with the following command:")
            print("pip install --upgrade pygame")
            sys.exit(1)

        # This way, code blocks can consistently refer to the stage with self.stage:
        self.stage = self
        # Make sure that the core sprite can always be accessed via _core
        self._core = self
        # Above attributes need to be set first so that mixins can access them properly
        super().__init__()
        # The facade is the translated API
        self.facade = None
        self.sprite_facade_class = None

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
        self.monitor_group = pygame.sprite.Group()
        # All sprites draw on the same pen layer, it is created on demand.
        self._pen_image = None
        self.background_color = (255, 255, 255)
        # surface is where the whole stage is rendered to
        # it defines the in-game resolution
        self.surface = pygame.Surface([width, height], flags=pygame.SRCALPHA)
        # screen is the actual screen, the surface gets scaled
        self.screen = pygame.display.set_mode([width, height], pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.width = width
        self.height = height
        self.rect = pygame.rect.Rect(0, 0, width, height)
        self.center_x = int(width / 2)
        self.center_y = int(height / 2)
        # current scale factor of the stage if the window is resized
        self.scale_factor = 1
        # current offset of the top left corner if the window is resized
        self.offset_x = 0
        self.offset_y = 0

        self.timer = 0
        self._dragged_sprite = None
        self._drag_offset = pygame.Vector2(0, 0)
        self.show_sprite_boundaries = "--show-sprite-boundaries" in sys.argv

    @property
    def pen_image(self):
        if self._pen_image is None:
            self._pen_image = pygame.Surface((self.width, self.height), flags=pygame.SRCALPHA)
        return self._pen_image

    def _create_core_sprite(self, costume="default"):
        sprite = CoreSprite(self, costume)
        self.sprites.add(sprite)
        if self.sprite_facade_class:
            self.sprite_facade_class(sprite)  # pylint: disable=E1102
        return sprite

    def pystage_createsprite(self, costume="default"):
        sprite = self._create_core_sprite(costume)
        self._update_visible()
        return sprite.facade or sprite

    def _get_sprite(self, sprite):
        """Get the core sprite for a sprite of any API or for a sprite name."""
        if isinstance(sprite, str):
            for candidate in self.sprites:
                if candidate.name == sprite and not candidate.is_clone:
                    return candidate
            if sprite == "_stage_":
                return self
            raise ValueError(f"There is no sprite with the name '{sprite}'.")
        return sprite._core

    def _update_visible(self):
        self.visible_sprites.empty()
        for sprite in self.sprites:
            assert(isinstance(sprite, CoreSprite))
            if sprite.visible:
                self.visible_sprites.add(sprite)

    def _update(self, dt):
        self.code_manager._update(dt)
        # Update it so that the layering is correct while drawing
        # otherwise the no effect for to_front, to_back, etc.
        self._update_visible()

    def _draw(self, surface: pygame.Surface, offset=(0, 0)):
        surface.fill(self.background_color)
        image, position = self.costume_manager.get_backdrop()
        if image:
            surface.blit(image, (position[0] + offset[0], position[1] + offset[1]))

    def _mouse_pos(self):
        """Mouse position in stage pixels (PyGame coordinates).

        The window can be resized, so the position on the screen has to
        be scaled back to the resolution of the stage.
        """
        x, y = pygame.mouse.get_pos()
        return pygame.Vector2(
            (x - self.offset_x) / self.scale_factor,
            (y - self.offset_y) / self.scale_factor,
        )

    def _sprite_at(self, pos, sprites):
        """The topmost of the given sprites with a visible pixel at pos."""
        for sprite in reversed(sprites):
            if not sprite.rect.collidepoint(pos):
                continue
            x = int(pos[0] - sprite.rect.left)
            y = int(pos[1] - sprite.rect.top)
            if not sprite.image.get_rect().collidepoint(x, y):
                continue
            if sprite.image.get_at((x, y)).a != 0:
                return sprite
        return None

    def event_whenstageclicked(self, generator_function, name="", no_refresh=False):
        """
        Adds the code block to the event queue for clicks on the stage.
        """
        new_block = self.code_manager.register_code_block(generator_function, name, no_refresh)
        self.code_manager.clicked_blocks.append(new_block)

    def _all_code_managers(self):
        return [self.code_manager] + [sprite.code_manager for sprite in self.sprites]

    def _backdrop_switched(self):
        """Called whenever a block switches the backdrop.

        Returns
        -------
        The code blocks that were started by "when backdrop switches to".
        """
        costume = self.costume_manager.get_costume()
        if not costume:
            return []
        started = []
        for code_manager in self._all_code_managers():
            started.extend(code_manager.process_backdrop(costume.name))
        return started

    def _broadcast(self, message):
        """Start all code blocks waiting for the message and return them."""
        started = []
        for code_manager in self._all_code_managers():
            started.extend(code_manager.process_broadcast(message))
        return started

    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if self.input_manager.is_active():
                    self.input_manager.process_key(event)
                else:
                    for code_manager in self._all_code_managers():
                        code_manager.process_key_pressed(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = self._mouse_pos()
                visible = self.visible_sprites.sprites()
                sprite = self._sprite_at(pos, visible)
                if sprite:
                    sprite.code_manager.process_click()
                elif self.rect.collidepoint(pos):
                    self.code_manager.process_click()
                # Sprites can be dragged, if they are set to draggable
                self._dragged_sprite = self._sprite_at(pos, [s for s in visible if s.draggable])
                if self._dragged_sprite:
                    self._drag_offset = self._dragged_sprite._pos - pos
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self._dragged_sprite = None

        if self._dragged_sprite:
            self._dragged_sprite._set_pos(self._mouse_pos() + self._drag_offset)

    def _frame(self, dt):
        """Everything that happens in one frame, besides event handling."""
        # Handle broadcast messages
        for message in self.message_broker.get_messages():
            self._broadcast(message)
        self.message_broker.mark_completed()

        for code_manager in self._all_code_managers():
            code_manager.process_timer(self.timer)

        self._update(dt)
        self.sprites.update(dt)
        self.bubbles.update()
        self.input_manager.update(dt)
        self.monitor_group.update()

        self._draw(self.surface)
        self.surface.blit(self.pen_image, (0, 0))

        self.visible_sprites.draw(self.surface)
        self.bubbles.draw(self.surface)
        self.input_manager.draw(self.surface)

        self.monitor_group.draw(self.surface)
        self.timer += dt

    def _show(self):
        """Scale the stage to the window and show it."""
        factor_x = self.screen.get_width() / self.surface.get_width()
        factor_y = self.screen.get_height() / self.surface.get_height()
        self.scale_factor = min(factor_x, factor_y)
        scaled = pygame.transform.smoothscale(
            self.surface,
            (
                int(self.surface.get_width() * self.scale_factor),
                int(self.surface.get_height() * self.scale_factor),
            ),
        )
        self.offset_x = int((self.screen.get_width() - scaled.get_width()) / 2)
        self.offset_y = int((self.screen.get_height() - scaled.get_height()) / 2)
        self.screen.fill((0, 0, 0))
        self.screen.blit(scaled, (self.offset_x, self.offset_y,))
        pygame.display.flip()

    def pystage_play(self):
        """
        This runs the game loop
        """
        self.running = True
        dt = 0
        while self.running:
            self._process_events()
            self._frame(dt)
            self._show()
            dt = self.clock.tick(self.FPS) / 1000

        pygame.quit()
