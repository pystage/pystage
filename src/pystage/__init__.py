import pygame
import math

def _deg2rad(deg):
    return deg / 360 * 2 * math.pi
    
def _rad2deg(rad):
    return rad / (2 * math.pi) * 360


class CodeBlock():
    '''
    The CodeBlock encapsulates a generator and manages its state.
    '''

    def __init__(self, sprite, generator):
        self.sprite = sprite
        self.name = generator.__name__
        self.generator = generator
        self.steps = generator()
        self.wait_time = 0
        self.stopped = False


    def update(self, dt):
        if self.stopped:
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
                self.stopped = True




class Sprite():
    image = pygame.image.load("images/zombie_idle.png")
    x = 0.0
    y = 0.0
    direction = 0
    pen = False
    color = (255,0,0)
    code_blocks = {}


    def __init__(self, stage):
        self.stage = stage

    def update(self, dt):
        for name in self.code_blocks:
            self.code_blocks[name].update(dt)

    def do(self, generator):
        self.code_blocks[generator.__name__] = CodeBlock(self, generator)

    def when_key_pressed(self, key, generator):
        pass


    def draw(self):
        self.stage.screen.blit(self.image, (self.x, self.y))

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


key_mappings = {
    pygame.K_a: ["a"],
    pygame.K_b: ["b"],
    pygame.K_c: ["c"],
    pygame.K_d: ["d"],
    pygame.K_e: ["e"],
    pygame.K_f: ["f"],
    pygame.K_g: ["g"],
    pygame.K_h: ["h"],
    pygame.K_i: ["i"],
    pygame.K_j: ["j"],
    pygame.K_k: ["k"],
    pygame.K_l: ["l"],
    pygame.K_m: ["m"],
    pygame.K_n: ["n"],
    pygame.K_o: ["o"],
    pygame.K_p: ["p"],
    pygame.K_q: ["q"],
    pygame.K_r: ["r"],
    pygame.K_s: ["s"],
    pygame.K_t: ["t"],
    pygame.K_u: ["u"],
    pygame.K_v: ["v"],
    pygame.K_w: ["w"],
    pygame.K_x: ["x"],
    pygame.K_y: ["y"],
    pygame.K_z: ["z"],
    pygame.K_1: ["1"],
    pygame.K_2: ["2"],
    pygame.K_3: ["3"],
    pygame.K_4: ["4"],
    pygame.K_5: ["5"],
    pygame.K_6: ["6"],
    pygame.K_7: ["7"],
    pygame.K_8: ["8"],
    pygame.K_9: ["9"],
    pygame.K_0: ["0"],
    pygame.K_LEFT: ["left"],
    pygame.K_RIGHT: ["right"],
    pygame.K_UP: ["up"],
    pygame.K_DOWN: ["down"],
    pygame.K_SPACE: ["space", " "],
        }


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
                    pass

            self.screen.fill(self.background_color)

            for sprite in self.sprites:
                sprite.update(dt)
                sprite.draw()

            pygame.display.flip()
            dt = self.clock.tick(self.FPS) / 1000

        pygame.quit()

