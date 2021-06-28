from pystage.core.sprite import CoreSprite


class Sprite():
    def __init__(self, core_sprite):
        self._core : CoreSprite = core_sprite
        self._core.facade = self


    ##
    # Events
    #

    def when_program_is_started(self, generator, name=""):
        self._core.event_whenflagclicked(generator, name)


    def when_key_is_pressed(self, key, generator, name=""):
        self._core.event_whenkeypressed(key, generator, name)


    def when_key_is_pressed(self, key):
        self._core.sensing_keypressed(key)

    ##
    # Motion
    #

    def turn_left(self, deg):
        """
        Turn the sprite by given angle.

        Parameters
        ----------
        deg : The angle in degree.

        Returns
        -------
        None
        """
        self._core.motion_turnleft(deg)

    turn_left.opcode = "motion_turnleft"

    def set_x_to(self, value):
        self._core.motion_setx(value)

    def turn_right(self, deg):
        self._core.motion_turnright(deg)

    def move(self, steps):
        self._core.motion_movesteps(steps)

    def go_to_x_y(self, x, y):
        self._core.motion_gotoxy(x, y)

    def wait(self, secs):
        self._core.control_wait(secs)

