import pygame
import enum
import math
from pystage.core._sensing import _Sensing
from pystage.core._looks import _LooksSprite
from pystage.core.assets import CostumeManager
import random
from pystage.core.values import to_number

def _deg2rad(deg):
    return deg / 360 * 2 * math.pi


def _rad2deg(rad):
    return rad / (2 * math.pi) * 360

class _Motion(_Sensing):
    def __init__(self):
        super().__init__()
        # The direction is internally stored as common angle in degrees
        # (counter-clockwise, 0 to the right)
        # Scratch uses a clockwise angle with 0 pointing to top
        self._direction = 0
        # Position is stored internally as PyGame coordinates
        # and refers to the center of the costume.
        self._pos = pygame.Vector2(self.stage.center_x, self.stage.center_y)
        self.draggable = False

    def _set_pos(self, pos):
        """Move to a position in PyGame coordinates. Draws, if the pen is down."""
        old = pygame.Vector2(self._pos)
        self._pos.update(pos)
        if old != self._pos:
            self._pen_line(old, self._pos)

    def motion_turnleft(self, deg):
        self._direction += to_number(deg)


    def motion_turnright(self, deg):
        self._direction -= to_number(deg)


    def motion_movesteps(self, steps):
        steps = to_number(steps)
        dx = steps * math.cos(_deg2rad(self._direction))
        dy = steps * math.sin(_deg2rad(self._direction))
        self._set_pos(self._pos + pygame.Vector2(dx, -dy)) # PyGame has inverted y axis


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
        sprite = self.stage._get_sprite(sprite)
        if sprite is None:
            return
        self.motion_gotoxy(sprite.motion_xposition(), sprite.motion_yposition())

    motion_goto_sprite.opcode = "motion_goto"


    def motion_gotoxy(self, x, y):
        self._set_pos((to_number(x) + self.stage.center_x, -to_number(y) + self.stage.center_y))


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
        sprite = self.stage._get_sprite(sprite)
        if sprite is None:
            return
        return self.motion_glidesecstoxy(secs, sprite.motion_xposition(), sprite.motion_yposition())

    motion_glideto_sprite.opcode = "motion_glideto"


    def motion_glidesecstoxy(self, secs, x, y):
        secs, x, y = max(0, to_number(secs)), to_number(x), to_number(y)
        if secs == 0:
            self.motion_gotoxy(x, y)
            return
        self.code_manager.current_block.gliding_seconds = secs
        self.code_manager.current_block.add_to_wait_time = secs
        self.code_manager.current_block.gliding_start_position = (self.motion_xposition(), self.motion_yposition())
        self.code_manager.current_block.gliding_end_position = (x, y)
        self.code_manager.current_block.gliding = True

    def motion_pointindirection(self, direction):
        # Scratch uses clock-wise directions with 0 to the top
        # We have anti-clockwise with 0 to the right
        self._direction = 90 - to_number(direction)

    def motion_pointtowards_pointer(self):
        dx = self.sensing_mousex() - self.motion_xposition()
        dy = self.sensing_mousey() - self.motion_yposition()
        self._direction = _rad2deg(math.atan2(dy, dx))

    motion_pointtowards_pointer.opcode = "motion_pointtowards"
    motion_pointtowards_pointer.param = "TOWARDS"
    motion_pointtowards_pointer.value = "_mouse_"

    def motion_pointtowards_random(self):
        # Like in Scratch: A random direction between -180 and 180
        self.motion_pointindirection(random.randint(-180, 180))

    motion_pointtowards_random.opcode = "motion_pointtowards"
    motion_pointtowards_random.param = "TOWARDS"
    motion_pointtowards_random.value = "_random_"

    def motion_pointtowards_sprite(self, sprite):
        if sprite == "_mouse_":
            return self.motion_pointtowards_pointer()
        if sprite == "_random_":
            return self.motion_pointtowards_random()
        sprite = self.stage._get_sprite(sprite)
        if sprite is None:
            return
        dx = sprite.motion_xposition() - self.motion_xposition()
        dy = sprite.motion_yposition() - self.motion_yposition()
        self._direction = _rad2deg(math.atan2(dy, dx))

    motion_pointtowards_sprite.opcode = "motion_pointtowards"


    def motion_changexby(self, value):
        self._set_pos((self._pos.x + to_number(value), self._pos.y))


    def motion_setx(self, value):
        self._set_pos((to_number(value) + self.stage.center_x, self._pos.y))


    def motion_changeyby(self, value):
        self._set_pos((self._pos.x, self._pos.y - to_number(value))) # inverted y axis


    def motion_sety(self, value):
        self._set_pos((self._pos.x, -to_number(value) + self.stage.center_y))


    def motion_ifonedgebounce(self):
        self.costume_manager.update_sprite_image()
        pos = pygame.Vector2(self._pos)
        if self.rect.left < 0:
            self._direction = 180 - self._direction
            pos.x -= self.rect.left
        elif self.rect.right > self.stage.width:
            self._direction = 180 - self._direction
            pos.x -= self.rect.right - self.stage.width
        elif self.rect.top < 0:
            self._direction = -self._direction
            pos.y -= self.rect.top
        elif self.rect.bottom > self.stage.height:
            self._direction = -self._direction
            pos.y -= self.rect.bottom - self.stage.height
        else:
            return
        self._set_pos(pos)
        self.costume_manager.update_sprite_image()


    def motion_setrotationstyle_leftright(self):
        self.costume_manager.rotation_style = CostumeManager.LEFT_RIGHT

    motion_setrotationstyle_leftright.opcode = "motion_setrotationstyle"
    motion_setrotationstyle_leftright.param = "STYLE"
    motion_setrotationstyle_leftright.value = "left-right"

    def motion_setrotationstyle_dontrotate(self):
        self.costume_manager.rotation_style = CostumeManager.NO_ROTATION

    motion_setrotationstyle_dontrotate.opcode = "motion_setrotationstyle"
    motion_setrotationstyle_dontrotate.param = "STYLE"
    motion_setrotationstyle_dontrotate.value = "don't rotate"

    def motion_setrotationstyle_allaround(self):
        self.costume_manager.rotation_style = CostumeManager.ALL_AROUND

    motion_setrotationstyle_allaround.opcode = "motion_setrotationstyle"
    motion_setrotationstyle_allaround.param = "STYLE"
    motion_setrotationstyle_allaround.value = "all around"


    def motion_xposition(self):
        return self._pos.x - self.stage.center_x

    motion_xposition.return_type = float


    def motion_yposition(self):
        return -self._pos.y + self.stage.center_y

    motion_yposition.return_type = float


    def motion_direction(self):
        # Scratch always keeps angles between -180 and 180
        dir = (90 - self._direction) % 360
        if dir <= 180:
            return dir
        else:
            return dir - 360

    motion_direction.return_type = float
