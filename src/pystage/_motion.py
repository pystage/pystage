import enum
import math

def _deg2rad(deg):
    return deg / 360 * 2 * math.pi

    
def _rad2deg(rad):
    return rad / (2 * math.pi) * 360

class _Motion():
    ##
    # Motion
    #
    class RotationStyle(enum.Enum):
        # https://en.scratch-wiki.info/wiki/Rotation_Style
        ALL_AROUND = 1
        LEFT_RIGHT = 2
        DONT_ROTATE = 3

    def turn_left(self, deg):
        self.direction -= deg


    def turn_right(self, deg):
        self.direction += deg


    def move(self, steps):
        old_x = self.x
        old_y = self.y
        self.x = self.x + steps * math.cos(_deg2rad(self.direction))
        self.y = self.y + steps * math.sin(_deg2rad(self.direction))

    def go_to_random_position(self):
        pass

    def go_to_mouse_pointer(self):
        pass

    def go_to_sprite(self, sprite):
        pass

    def go_to_x_y(self, x, y):
        self.x = x
        self.y = y

    def glide_to_random_position(self, secs):
        # This requires special care, either this method needs to be yielded from
        # https://docs.python.org/3/reference/expressions.html#yieldexpr
        # Probably better: handle this in the game loop, i.e. enter a glide mode 
        # and only after the glide mode finished, the steps are continued.
        pass

    def glide_to_mouse_pointer(self, secs):
        pass

    def glide_to_sprite(self, sprite, secs):
        pass

    def glide_to_x_y(self, x, y, secs):
        pass

    def point_in_direction(self, direction):
        pass

    def point_towards_mouse_pointer(self):
        pass

    def point_towards_sprite(self, sprite):
        pass

    def change_x_by(self, value):
        pass

    def set_x_to(self, value):
        pass

    def change_y_by(self, value):
        pass

    def set_u_to(self, value):
        pass

    def if_on_edge_bounce(self):
        pass

    def set_rotation_style(self, style):
        # See Enum RotationStyle above
        pass

    # Setters and getters are questionable, but 
    # this way we would clearly adapt the Scratch API
    # We could get rid of them for a direct access 
    # to x, y, direction and so on. Direct access if of 
    # course available anyway.
    def get_x_position(self):
        pass

    def get_y_position(self):
        pass

    def get_direction(self):
        pass

