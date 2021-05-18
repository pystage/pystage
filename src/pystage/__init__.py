import pygame
import math
import inspect
import pkg_resources
import collections


def _deg2rad(deg):
    return deg / 360 * 2 * math.pi

    
def _rad2deg(rad):
    return rad / (2 * math.pi) * 360


key_mappings = {
        "a": pygame.K_a,
        "b": pygame.K_b,
        "c": pygame.K_c,
        "d": pygame.K_d,
        "e": pygame.K_e,
        "f": pygame.K_f,
        "g": pygame.K_g,
        "h": pygame.K_h,
        "i": pygame.K_i,
        "j": pygame.K_j,
        "k": pygame.K_k,
        "l": pygame.K_l,
        "m": pygame.K_m,
        "n": pygame.K_n,
        "o": pygame.K_o,
        "p": pygame.K_p,
        "q": pygame.K_q,
        "r": pygame.K_r,
        "s": pygame.K_s,
        "t": pygame.K_t,
        "u": pygame.K_u,
        "v": pygame.K_v,
        "w": pygame.K_w,
        "x": pygame.K_x,
        "y": pygame.K_y,
        "z": pygame.K_z,
        "1": pygame.K_1,
        "2": pygame.K_2,
        "3": pygame.K_3,
        "4": pygame.K_4,
        "5": pygame.K_5,
        "6": pygame.K_6,
        "7": pygame.K_7,
        "8": pygame.K_8,
        "9": pygame.K_9,
        "0": pygame.K_0,
        "left": pygame.K_LEFT,
        "right": pygame.K_RIGHT,
        "up": pygame.K_UP,
        "down": pygame.K_DOWN,
        "space": pygame.K_SPACE,
        " ": pygame.K_SPACE,
        }



class CodeBlock():
    '''
    The CodeBlock encapsulates a generator and manages its state.
    '''
    last_id = -1

    def __init__(self, sprite_or_stage, generator, name=""):
        if len(inspect.signature(generator).parameters)!=1:
            raise ValueError(f"Your code block '{generator.__name__}' needs one parameter, usually called self.")

        self.sprite_or_stage = sprite_or_stage
        if name!="" and name!=None:
            name = f"-{name}"
        CodeBlock.last_id += 1
        # The name of a code block is unique with a global id.
        # A custom name may be provided to distinguish blocks
        # that use the same generator.
        # This is not possible in Scratch (you only can copy blocks), 
        # but could be allowed here.
        # TODO: Discuss, if we should completely prohibit the 
        # reuse of generators, it could make things easier.
        self.name = f"{generator.__name__}{name}-{CodeBlock.last_id}"
        # A copy of the generator used for restarts (e.g. when bound to events)
        self.generator = generator
        # The current state of a generator after it is started
        self.steps = generator(sprite_or_stage)
        if not isinstance(self.steps, collections.Iterable):
            raise ValueError(f"Your code block '{generator.__name__}' needs at least one yield statement.")
        # The time until the next step is executed
        self.wait_time = 0
        # Flag indicating if the block is currently running
        self.running = False


    def start_if_not_running(self):
        '''
        Start the code block. If the block is already started,
        this method does nothing.
        '''
        if self.running:
            return
        self.start_or_restart()


    def start_or_restart(self):
        '''
        (Re-)start the code block. If the block is already started,
        the current execution will not continue.
        '''
        self.running = True
        self.wait_time = 0
        self.steps = self.generator(self.sprite_or_stage)
        print(f"Start of {self.name} triggered.")


    def update(self, dt):
        '''
        Check if it is time for the next step and execute it.
        '''
        if not self.running:
            return
        self.wait_time -= dt
        if self.wait_time < 0:
            try:
                result = next(self.steps)
                self.wait_time = 0
                if isinstance(result, float) or isinstance(result, int):
                    self.wait_time = result
            except StopIteration:
                print(f"CodeBlock {self.name} has finished.")
                self.running = False


class Sprite():
    image = pygame.image.load(pkg_resources.resource_filename(__name__, "images/zombie_idle.png"))
    x = 0.0
    y = 0.0
    direction = 0
    pen = False
    color = (255,0,0)
    # name: code_block
    code_blocks = {}
    # pygame.K_?: [name, ...]
    key_pressed_blocks = {}


    def __init__(self, stage):
        self.stage = stage


    def _draw(self):
        self.stage.screen.blit(self.image, (self.x, self.y))


    def _update(self, dt):
        for name in self.code_blocks:
            self.code_blocks[name].update(dt)


    def _process_key_pressed(self, key):
        # key is a pygame constant, e.g. pygame.K_a
        # This hat block is special as it only fires again when the code block has ended. 
        # All other hat block methods stop the current execution and restart the block.
        if key in self.key_pressed_blocks:
            for name in self.key_pressed_blocks[key]:
                self.code_blocks[name].start_if_not_running()


    def _register_code_block(self, generator, name=""):
        new_block = CodeBlock(self, generator, name)
        self.code_blocks[new_block.name] = new_block
        print(f"New code block registered: {new_block.name}")
        return new_block


    def when_program_is_started(self, generator, name=""):
        new_block = self._register_code_block(generator, name)
        new_block.start_if_not_running()
        print(f"Bound to start: {new_block.name}")


    def when_key_is_pressed(self, key, generator, name=""):
        '''
        Adds the code block to the event queue for key presses.
        '''
        new_block = self._register_code_block(generator, name)
        if key not in key_mappings:
            # TODO: implement "any" key.
            raise ValueError(f"Bad key: {key}. Only a-z, 0-9 and space are allowed.")
        pg_key = key_mappings[key]
        # No defaultdict so that we can easily check if a key mapping is available
        if pg_key not in self.key_pressed_blocks:
            self.key_pressed_blocks[pg_key] = []
        self.key_pressed_blocks[pg_key].append(new_block.name)
        print(f"Bound to key press ({key}/{pg_key}): {new_block.name}")


    def pen_down(self):
        self.pen = True


    def pen_up(self):
        self.pen = False


    def pen_toggle(self):
        self.pen = not self.pen


    def set_pen_color_to(self, color):
        self.color = color


    def go_to_x_y(self, x, y):
        self.x = x
        self.y = y


    def turn_left(self, deg):
        self.direction -= deg


    def turn_right(self, deg):
        self.direction += deg


    def move(self, steps):
        old_x = self.x
        old_y = self.y
        self.x = self.x + steps * math.cos(_deg2rad(self.direction))
        self.y = self.y + steps * math.sin(_deg2rad(self.direction))


class Stage():
    running = False
    FPS = 60
    dt = 0
    sprites = []
    background_color = (255, 255, 255)

    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode([width, height])
        self.clock = pygame.time.Clock()
        self.width = width
        self.height = height


    def create_sprite(self):
        sprite = Sprite(self)
        self.sprites.append(sprite)
        return sprite


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

