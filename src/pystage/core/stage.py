# pyright: basic, reportPrivateUsage=false
import os
import sys
import traceback

import pygame

# Mixins
from pystage.core._control import _ControlStage
from pystage.core._events import _Events
from pystage.core._looks import _LooksStage
from pystage.core._operators import _Operators
from pystage.core._pen import _PenStage
from pystage.core._sensing import _Sensing
from pystage.core._sound import _Sound
from pystage.core._variables import _Variables
from pystage.core.messages import MessageBroker
from pystage.core.sprite import CoreSprite
from pystage.core.asking import InputManager
from pystage.core.values import to_string
from pystage.core import i18n


class SpriteGroup(pygame.sprite.RenderUpdates):
    """Sprite group whose drawing order (back to front) can be changed.

    pygame-ce keeps the order of sprites in the insertion-ordered dict
    ``spritedict``, so reordering means rebuilding that dict.
    """

    def _reorder(self, sprites):
        old = self.spritedict
        self.spritedict = {sprite: old[sprite] for sprite in sprites}

    def _check(self, sprite):
        if sprite not in self.spritedict:
            raise ValueError(i18n.tr("sprite_unknown", sprite=sprite))

    def get_layer(self, sprite):
        try:
            return self.sprites().index(sprite)
        except ValueError:
            return -1

    def to_front(self, sprite):
        self._check(sprite)
        self.move_to(sprite, len(self.spritedict))

    def to_back(self, sprite):
        self._check(sprite)
        self.move_to(sprite, 0)

    def layer_forward(self, sprite, value=1):
        self._check(sprite)
        sprites = self.sprites()
        index = sprites.index(sprite)
        sprites.remove(sprite)
        # the sprite was already removed, so the upper bound is the length
        new_index = max(0, min(index + value, len(sprites)))
        sprites.insert(new_index, sprite)
        self._reorder(sprites)

    def layer_backward(self, sprite, value=1):
        self.layer_forward(sprite, -value)

    def move_to(self, sprite, index):
        self._check(sprite)
        sprites = self.sprites()
        sprites.remove(sprite)
        sprites.insert(index, sprite)
        self._reorder(sprites)


class CoreStage(
    _LooksStage, _Sound, _Events, _ControlStage, _Operators, _Sensing, _Variables, _PenStage
):
    def __init__(self, name="Welcome to pyStage!", width=480, height=360, language="en"):
        # The language of messages, see pystage.core.i18n. Set first, as
        # even the first messages (pygame check, no sound) depend on it.
        i18n.set_language(language)
        # Check pygame version (pygame-ce)
        pygame_major = int(pygame.ver.split(".")[0])
        if pygame_major < 2 or not getattr(pygame, "IS_CE", False):
            print(i18n.tr("pygame_version"))
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
        # The slider monitor that is dragged
        self._dragged_monitor = None
        self._drag_offset = pygame.Vector2(0, 0)
        # Like in Scratch, sprites can't leave the stage completely. Set to
        # False to allow moving sprites fully off the stage.
        self.fencing = True
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

    def _special(self, value):
        """The canonical special sprite ("_mouse_", "_stage_", ...) for a value.

        Localized names like "Mauszeiger" are translated, unless a sprite
        really has that name. Other values are returned unchanged.
        """
        if isinstance(value, str):
            special = i18n.canonical("sprites", value)
            if special != value and not any(s.name == value for s in self.sprites):
                return special
        return value

    def _get_sprite(self, sprite):
        """Get the core sprite for a sprite of any API or for a sprite name.

        Like in Scratch, where nothing happens if a sprite does not exist,
        None is returned if there is no such sprite.
        """
        if hasattr(sprite, "_core"):
            return sprite._core
        name = self._special(to_string(sprite))
        if name == "_stage_":
            return self
        for candidate in self.sprites:
            if candidate.name == name and not candidate.is_clone:
                return candidate
        return None

    def _update_visible(self):
        self.visible_sprites.empty()
        for sprite in self.sprites:
            assert(isinstance(sprite, CoreSprite))
            if sprite.visible:
                self.visible_sprites.add(sprite)

    def _update(self, dt):
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

    def _press_slider(self, pos):
        """Start dragging the slider monitor at pos, if there is one.

        Returns True if a slider was hit, the click is then used up.
        """
        for monitor in reversed(self.monitor_group.sprites()):
            if monitor.slider_hit(pos):
                self._dragged_monitor = monitor
                monitor.drag_to(pos[0])
                return True
        return False

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
                # Sliders are on top of everything, a click on them is not a click on a sprite
                if self._press_slider(pos):
                    continue
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
                self._dragged_monitor = None

        if self._dragged_monitor:
            self._dragged_monitor.drag_to(self._mouse_pos().x)
        elif self._dragged_sprite:
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
        # Like in Scratch, the scripts of the sprite in front run first and
        # the stage runs last. Scripts that start in the same frame depend
        # on that order (e.g. one sets a variable another one tests).
        for sprite in reversed(self.sprites.sprites()):
            if sprite in self.sprites:  # not deleted by another script
                sprite.update(dt)
        self.code_manager._update(dt)
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

    def _show_error(self, error):
        """Show an error in the window until it is closed.

        The error message in the terminal is easily missed, especially
        when the terminal closes together with the program.
        """
        from pystage.core.gui import regular_font_14, wrap_text, render_lines
        tb = traceback.extract_tb(error.__traceback__)
        # The last position that is not in pyStage itself is most helpful
        own = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        frames = [f for f in tb if not os.path.abspath(f.filename).startswith(own)] or list(tb)
        text = f"{type(error).__name__}: {error}"
        if frames:
            frame = frames[-1]
            text = f"{i18n.tr('error_in', file=os.path.basename(frame.filename), line=frame.lineno)}: {frame.line or ''} --- {text}"
        lines, width, height = wrap_text(text[:600], regular_font_14, self.width - 40)
        message = render_lines(lines, regular_font_14, (255, 255, 255), width, height, 2)
        overlay = pygame.Surface((self.width, message.get_height() + 20), flags=pygame.SRCALPHA)
        overlay.fill((180, 0, 0, 230))
        overlay.blit(message, (20, 10))
        self.surface.blit(overlay, (0, self.height - overlay.get_height()))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            self._show()
            self.clock.tick(10)

    def pystage_play(self):
        """
        This runs the game loop
        """
        self.running = True
        dt = 0
        try:
            while self.running:
                self._process_events()
                self._frame(dt)
                self._show()
                dt = self.clock.tick(self.FPS) / 1000
        except Exception as error:
            traceback.print_exc()
            self._show_error(error)
            pygame.quit()
            sys.exit(1)

        pygame.quit()
