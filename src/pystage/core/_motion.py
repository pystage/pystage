import enum
import math

def _deg2rad(deg):
    return deg / 360 * 2 * math.pi


def _rad2deg(rad):
    return rad / (2 * math.pi) * 360

class _Motion():
    def __init__(self):
        super().__init__()
        self.x = 0.0
        self.y = 0.0
        self.direction = 90

    def motion_turnleft(self, deg):
        self.direction -= deg


    def motion_turnright(self, deg):
        self.direction += deg


    def motion_movesteps(self, steps):
        old_x = self.x
        old_y = self.y
        self.x = self.x + steps * math.cos(_deg2rad(self.direction - 90))
        self.y = self.y + steps * math.sin(_deg2rad(self.direction - 90))


    def motion_goto_random(self):
        pass

    motion_goto_random.opcode = "motion_goto"
    motion_goto_random.param = "TO"
    motion_goto_random.value = "_random_"


    def motion_goto_pointer(self):
        pass

    motion_goto_pointer.opcode = "motion_goto"
    motion_goto_pointer.param = "TO"
    motion_goto_pointer.value = "_mouse_"


    def motion_goto_sprite(self, sprite):
        pass

    motion_goto_sprite.opcode = "motion_goto"


    def motion_gotoxy(self, x, y):
        self.x = x
        self.y = y


    def motion_glideto_random(self, secs):
        # Handle this in the game loop, i.e. enter a glide mode 
        # and only after the glide mode finished, the steps are continued.
        pass

    motion_glideto_random.opcode = "motion_glideto"
    motion_glideto_random.param = "TO"
    motion_glideto_random.value = "_random_"
    motion_glideto_random.position = "%2"


    def motion_glideto_pointer(self, secs):
        pass

    motion_glideto_pointer.opcode = "motion_glideto"
    motion_glideto_pointer.param = "TO"
    motion_glideto_pointer.value = "_mouse_"
    motion_glideto_pointer.position = "%2"

    def motion_glideto_sprite(self, secs, sprite):
        pass

    motion_glideto_sprite.opcode = "motion_glideto"


    def motion_glidesecstoxy(self, secs, x, y):
        pass

    def motion_pointindirection(self, direction):
        pass

    def motion_pointtowards_pointer(self):
        pass

    motion_pointtowards_pointer.opcode = "motion_pointtowards"
    motion_pointtowards_pointer.param = "TOWARDS"
    motion_pointtowards_pointer.value = "_mouse_"

    def motion_pointtowards_sprite(self, sprite):
        pass

    motion_pointtowards_sprite.opcode = "motion_pointtowards"

    def motion_changexby(self, value):
        self.x += value

    def motion_setx(self, value):
        self.x = value

    def motion_changeyby(self, value):
        self.y += value

    def motion_sety(self, value):
        self.y = value

    def motion_ifonedgebounce(self):
        pass

    def motion_setrotationstyle_leftright(self):
        pass

    motion_setrotationstyle_leftright.opcode = "motion_setrotationstyle"
    motion_setrotationstyle_leftright.param = "STYLE"
    motion_setrotationstyle_leftright.value = "left-right"
    motion_setrotationstyle_leftright.translation="looks_effect_brightness"

    def motion_setrotationstyle_dontrotate(self):
        pass
    motion_setrotationstyle_dontrotate.opcode = "motion_setrotationstyle"
    motion_setrotationstyle_dontrotate.param = "STYLE"
    motion_setrotationstyle_dontrotate.value = "don't rotate"

    def motion_setrotationstyle_allaround(self):
        pass
    motion_setrotationstyle_allaround.opcode = "motion_setrotationstyle"
    motion_setrotationstyle_allaround.param = "STYLE"
    motion_setrotationstyle_allaround.value = "all around"

    # Setters and getters are questionable, but 
    # this way we would clearly adapt the Scratch API
    # We could get rid of them for a direct access 
    # to x, y, direction and so on. Direct access is of 
    # course available anyway.
    def motion_xposition(self):
        return self.x

    motion_xposition.return_type = float


    def motion_yposition(self):
        return self.y

    motion_yposition.return_type = float


    def motion_direction(self):
        # Scratch always keeps angles between -180 and 180
        dir = self.direction % 360
        if dir <= 180:
            return dir
        else:
            return dir - 360

    motion_direction.return_type = float
