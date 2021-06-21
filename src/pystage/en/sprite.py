from pystage.core.sprite import Sprite


class Sprite(Sprite):

    ##
    # Events
    #

    def when_program_is_started(self, generator, name=""):
        self.when_program_is_started(generator, name)


    def when_key_is_pressed(self, key, generator, name=""):
        self.when_key_is_pressed(key, generator, name)



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
        self.motion_turnleft(deg)

    turn_left.opcode = "motion_turnleft"

    def set_x_to(self, value):
        self.motion_setx(value)

    def turn_right(self, deg):
        self.motion_turnright(deg)

    def move(self, steps):
        self.motion_movesteps(steps)

    def go_to_x_y(self, x, y):
        self.motion_gotoxy(x, y)

    def wait(self, secs):
        self.wait(secs)

