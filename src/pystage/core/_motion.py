import enum
import math
from pystage.core._sensing import _Sensing
import random

def _deg2rad(deg):
    return deg / 360 * 2 * math.pi


def _rad2deg(rad):
    return rad / (2 * math.pi) * 360

class _Motion(_Sensing):
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
        self.y = self.y - steps * math.sin(_deg2rad(self.direction - 90))


    def motion_goto_random(self):
        half_width = int(self.stage.width/2)
        half_height = int(self.stage.height/2)
        x = random.randint(-half_width, half_width)
        y = random.randint(-half_height, half_height)
        return self.motion_gotoxy(x, y)

    motion_goto_random.opcode = "motion_goto"
    motion_goto_random.param = "TO"
    motion_goto_random.value = "_random_"


    def motion_goto_pointer(self):
        self.motion_gotoxy(self.sensing_mousex(), self.sensing_mousey())

    motion_goto_pointer.opcode = "motion_goto"
    motion_goto_pointer.param = "TO"
    motion_goto_pointer.value = "_mouse_"


    def motion_goto_sprite(self, sprite):
        self.motion_gotoxy(sprite.x, sprite.y)

    motion_goto_sprite.opcode = "motion_goto"


    def motion_gotoxy(self, x, y):
        self.x = x
        self.y = y


    def motion_glideto_random(self, secs):
        half_width = int(self.stage.width/2)
        half_height = int(self.stage.height/2)
        x = random.randint(-half_width, half_width)
        y = random.randint(-half_height, half_height)
        return self.motion_glidesecstoxy(secs, x, y)

    motion_glideto_random.opcode = "motion_glideto"
    motion_glideto_random.param = "TO"
    motion_glideto_random.value = "_random_"
    motion_glideto_random.position = "%2"


    def motion_glideto_pointer(self, secs):
        self.motion_glidesecstoxy(secs, self.sensing_mousex(), self.sensing_mousey())

    motion_glideto_pointer.opcode = "motion_glideto"
    motion_glideto_pointer.param = "TO"
    motion_glideto_pointer.value = "_mouse_"
    motion_glideto_pointer.position = "%2"


    def motion_glideto_sprite(self, secs, sprite):
        return self.motion_glidesecstoxy(secs, sprite.x, sprite.y)

    motion_glideto_sprite.opcode = "motion_glideto"


    def motion_glidesecstoxy(self, secs, x, y):
        self.code_manager.current_block.gliding_seconds = secs
        self.code_manager.current_block.add_to_wait_time = secs
        self.code_manager.current_block.gliding_start_position = (self.x, self.y)
        self.code_manager.current_block.gliding_end_position = (x, y)
        self.code_manager.current_block.gliding = True

    def motion_pointindirection(self, direction):
        self.direction = direction

    def motion_pointtowards_pointer(self):
        dx = self.sensing_mousex() - self.x
        dy = self.sensing_mousey() - self.y
        self.direction = 90 - _rad2deg(math.atan2(dy, dx))

    motion_pointtowards_pointer.opcode = "motion_pointtowards"
    motion_pointtowards_pointer.param = "TOWARDS"
    motion_pointtowards_pointer.value = "_mouse_"

    def motion_pointtowards_sprite(self, sprite):
        dx = sprite.x - self.x
        dy = sprite.y - self.y
        self.direction = 90 - _rad2deg(math.atan2(dy, dx))

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
        if self.rect.left < -1:
            self.direction = -self.direction
            self.rect.left = 1
            self._update_pos_from_rect()
        elif self.rect.right > self.stage.width + 1:
            self.direction = -self.direction
            self.rect.right = self.stage.width - 1
            self._update_pos_from_rect()
        elif self.rect.top < -1:
            self.direction = 180 - self.direction
            self.rect.top = 1
            self._update_pos_from_rect()
        elif self.rect.bottom > self.stage.height + 1:
            self.direction = 180 - self.direction
            self.rect.bottom = self.stage.height - 1
            self._update_pos_from_rect()


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
