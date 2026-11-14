from pystage.core.sprite import CoreSprite


class Sprite:
    def __init__(self, core_sprite):
        self._core: CoreSprite = core_sprite
        self._core.facade = self

    def create_clone_of_sprite(self, sprite="_myself_"):
        """create clone of %1

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite : FILL
        

        Returns
        -------

        """
        return self._core.control_create_clone_of_sprite(sprite)

    def create_clone_of_myself(self):
        """create clone of myself

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.control_create_clone_of_myself()
        
    def delete_this_clone(self):
        """delete this clone

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.control_delete_this_clone()

    def when_i_start_as_a_clone(
        self, generator_function, name="", no_refresh=False
    ):
        """when I start as a clone

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        generator_function : FILL
        name : FILL
        no_refresh : FILL
        

        Returns
        -------

        """
        return self._core.control_start_as_clone(
            generator_function, name, no_refresh
        )

    def stop_all(self):
        """stop all

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.control_stop_all()

    def stop_other_scripts_in_sprite(self):
        """stop other scripts in sprite

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.control_stop_other()

    def stop_this_script(self):
        """stop this script

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.control_stop_this()

    def wait(self, secs):
        """wait %1 seconds

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        secs : FILL
        

        Returns
        -------

        """
        return self._core.control_wait(secs)

    def change_variable_by(self, name, value):
        """change %1 by %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL
        value : FILL
        

        Returns
        -------

        """
        return self._core.data_changevariableby(name, value)

    def hide_variable(self, name):
        """hide variable %1

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL
        

        Returns
        -------

        """
        return self._core.data_hidevariable(name)

    def set_variable(self, name, value):
        """set %1 to %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL
        value : FILL
        

        Returns
        -------

        """
        return self._core.data_setvariableto(name, value)

    def show_variable(self, name):
        """show variable %1

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL
        

        Returns
        -------

        """
        return self._core.data_showvariable(name)

    def get_variable(self, name):
        """

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL
        

        Returns
        -------

        """
        return self._core.data_variable(name)

    def broadcast(self, message):
        """broadcast %1

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        message : FILL
        

        Returns
        -------

        """
        return self._core.event_broadcast(message)

    def broadcast_and_wait(self, message):
        """broadcast %1 and wait

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        message : FILL
        

        Returns
        -------

        """
        return self._core.event_broadcastandwait(message)

    def when_backdrop_switches_to(
        self, backdrop, generator_function, name="", no_refresh=False
    ):
        """when backdrop switches to %1

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        backdrop : FILL
        generator_function : FILL
        name : FILL
        no_refresh : FILL
        

        Returns
        -------

        """
        return self._core.event_whenbackdropswitchesto(
            backdrop, generator_function, name, no_refresh
        )

    def when_i_receive_message(
        self, message, generator_function, name="", no_refresh=False
    ):
        """when I receive %1

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        message : FILL
        generator_function : FILL
        name : FILL
        no_refresh : FILL
        

        Returns
        -------

        """
        return self._core.event_whenbroadcastreceived(
            message, generator_function, name, no_refresh
        )

    def when_program_starts(self, generator_function, name="", no_refresh=False):
        """when <greenflag> clicked

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        generator_function : FILL
        name : FILL
        no_refresh : FILL
        

        Returns
        -------

        """
        return self._core.event_whenflagclicked(
            generator_function, name, no_refresh
        )

    def when_loudness_greater_than(
        self, value, generator_function, name="", no_refresh=False
    ):
        """when loudness <greater> %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        generator_function : FILL
        name : FILL
        no_refresh : FILL
        

        Returns
        -------

        """
        return self._core.event_whengreaterthan_loudness(
            value, generator_function, name, no_refresh
        )

    def when_timer_greater_than(
        self, value, generator_function, name="", no_refresh=False
    ):
        """when timer <greater> %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        generator_function : FILL
        name : FILL
        no_refresh : FILL
        

        Returns
        -------

        """
        return self._core.event_whengreaterthan_timer(
            value, generator_function, name, no_refresh
        )

    def when_key_pressed(self, key, generator_function, name="", no_refresh=False):
        """when %1 key pressed

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        key : FILL
        generator_function : FILL
        name : FILL
        no_refresh : FILL
        

        Returns
        -------

        """
        return self._core.event_whenkeypressed(
            key, generator_function, name, no_refresh
        )

    def when_this_sprite_clicked(self, generator_function, name="", no_refresh=False):
        """when this sprite clicked

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        generator_function : FILL
        name : FILL
        no_refresh : FILL
        

        Returns
        -------

        """
        return self._core.event_whenthisspriteclicked(
            generator_function, name, no_refresh
        )

    def backdrop_name(self):
        """Returns the name of the current backdrop of the stage.

        Scratch block: (backdrop [name])

        Returns
        -------
        str
            The name of the current backdrop, or an empty text if there is no backdrop.
        """
        return self._core.looks_backdropnumbername_name()

    def backdrop_number(self):
        """Returns the number of the current backdrop of the stage (starting with 1).

        Scratch block: (backdrop [number])

        Returns
        -------
        int
            The number of the current backdrop.
        """
        return self._core.looks_backdropnumbername_number()

    def change_brightness_effect_by(self, value):
        """Changes the brightness effect of the sprite by the given amount. Negative values make the costume darker.

        Scratch block: change brightness effect by (25)

        Parameters
        ----------
        value : number
            The change of the effect. The effect goes from -100 (black) to 100 (white).
        """
        return self._core.looks_changeeffectby_brightness(value)

    def change_color_effect_by(self, value):
        """Changes the color effect of the sprite by the given amount. The color effect changes the colors of the costume.

        Scratch block: change color effect by (25)

        Parameters
        ----------
        value : number
            The change of the effect. The effect goes from 0 to 200 and starts again at 0 after 200.
        """
        return self._core.looks_changeeffectby_color(value)

    def change_fisheye_effect_by(self, value):
        """Changes the fisheye effect of the sprite by the given amount. The fisheye effect bends the costume like a fish-eye lens.

        Scratch block: change fisheye effect by (25)

        Parameters
        ----------
        value : number
            The change of the effect. 0 means no effect.
        """
        return self._core.looks_changeeffectby_fisheye(value)

    def change_ghost_effect_by(self, value):
        """Changes the ghost effect of the sprite by the given amount. The higher the effect, the more transparent the sprite becomes.

        Scratch block: change ghost effect by (25)

        Parameters
        ----------
        value : number
            The change of the effect. 0 means visible, 100 means invisible.
        """
        return self._core.looks_changeeffectby_ghost(value)

    def change_mosaic_effect_by(self, value):
        """Changes the mosaic effect of the sprite by the given amount. The mosaic effect repeats the costume as small tiles.

        Scratch block: change mosaic effect by (25)

        Parameters
        ----------
        value : number
            The change of the effect. 0 means no effect.
        """
        return self._core.looks_changeeffectby_mosaic(value)

    def change_pixelate_effect_by(self, value):
        """Changes the pixelate effect of the sprite by the given amount. The pixelate effect makes the costume look blocky.

        Scratch block: change pixelate effect by (25)

        Parameters
        ----------
        value : number
            The change of the effect. 0 means no effect.
        """
        return self._core.looks_changeeffectby_pixelate(value)

    def change_whirl_effect_by(self, value):
        """Changes the whirl effect of the sprite by the given amount. The whirl effect twists the costume.

        Scratch block: change whirl effect by (25)

        Parameters
        ----------
        value : number
            The change of the effect. 0 means no effect.
        """
        return self._core.looks_changeeffectby_whirl(value)

    def change_size_by(self, percent):
        """Changes the size of the sprite by the given percentage. Negative values make it smaller.

        Scratch block: change size by (10)

        Parameters
        ----------
        percent : number
            The change in percent. For example, 10 makes the sprite 10 percent bigger.
        """
        return self._core.looks_changesizeby(percent)

    def clear_graphic_effects(self):
        """Removes all graphic effects (color, fisheye, whirl, pixelate, mosaic, brightness and ghost) of the sprite.

        Scratch block: clear graphic effects
        """
        return self._core.looks_cleargraphiceffects()

    def costume_name(self):
        """Returns the name of the current costume of the sprite.

        Scratch block: (costume [name])

        Returns
        -------
        str
            The name of the current costume, or an empty text if the sprite has no costume.
        """
        return self._core.looks_costumenumbername_name()

    def costume_number(self):
        """Returns the number of the current costume of the sprite (starting with 1).

        Scratch block: (costume [number])

        Returns
        -------
        int
            The number of the current costume.
        """
        return self._core.looks_costumenumbername_number()

    def go_backward(self, value):
        """Moves the sprite backward by the given number of layers, so that it is shown behind other sprites.

        Scratch block: go backward (1) layers

        Parameters
        ----------
        value : int
            The number of layers to move backward.
        """
        return self._core.looks_goforwardbackwardlayers_backward(value)

    def go_forward(self, value):
        """Moves the sprite forward by the given number of layers, so that it is shown in front of other sprites.

        Scratch block: go forward (1) layers

        Parameters
        ----------
        value : int
            The number of layers to move forward.
        """
        return self._core.looks_goforwardbackwardlayers_forward(value)

    def go_to_back_layer(self):
        """Moves the sprite behind all other sprites.

        Scratch block: go to back layer
        """
        return self._core.looks_gotofrontback_back()

    def go_to_front_layer(self):
        """Moves the sprite in front of all other sprites.

        Scratch block: go to front layer
        """
        return self._core.looks_gotofrontback_front()

    def hide(self):
        """Hides the sprite. It is not shown on the stage until it is shown again.

        Scratch block: hide
        """
        return self._core.looks_hide()

    def next_backdrop(self):
        """Switches the stage to the next backdrop. After the last backdrop, the first one is used again.

        Scratch block: next backdrop
        """
        return self._core.looks_nextbackdrop()

    def next_costume(self):
        """Switches the sprite to the next costume. After the last costume, the first one is used again.

        Scratch block: next costume
        """
        return self._core.looks_nextcostume()

    def say(self, text):
        """Shows a speech bubble with the given text next to the sprite.

        Scratch block: say (Hello!)

        Parameters
        ----------
        text : str
            The text to show in the bubble.
        """
        return self._core.looks_say(text)

    def say_for_seconds(self, text, secs):
        """Shows a speech bubble with the given text next to the sprite for a number of seconds.

        The script waits until the time is over.

        Scratch block: say (Hello!) for (2) seconds

        Parameters
        ----------
        text : str
            The text to show in the bubble.
        secs : number
            The number of seconds the bubble is shown.
        """
        return self._core.looks_sayforsecs(text, secs)

    def set_brightness_effect_to(self, value):
        """Sets the brightness effect of the sprite. Negative values make the costume darker.

        Scratch block: set brightness effect to (0)

        Parameters
        ----------
        value : number
            The new value of the effect, from -100 (black) to 100 (white). 0 means no effect.
        """
        return self._core.looks_seteffectto_brightness(value)

    def set_color_effect_to(self, value):
        """Sets the color effect of the sprite. The color effect changes the colors of the costume.

        Scratch block: set color effect to (0)

        Parameters
        ----------
        value : number
            The new value of the effect, from 0 to 200. 0 means no effect.
        """
        return self._core.looks_seteffectto_color(value)

    def set_fisheye_effect_to(self, value):
        """Sets the fisheye effect of the sprite. The fisheye effect bends the costume like a fish-eye lens.

        Scratch block: set fisheye effect to (0)

        Parameters
        ----------
        value : number
            The new value of the effect. 0 means no effect.
        """
        return self._core.looks_seteffectto_fisheye(value)

    def set_ghost_effect_to(self, value):
        """Sets the ghost effect of the sprite. The higher the effect, the more transparent the sprite becomes.

        Scratch block: set ghost effect to (0)

        Parameters
        ----------
        value : number
            The new value of the effect. 0 means visible, 100 means invisible.
        """
        return self._core.looks_seteffectto_ghost(value)

    def set_mosaic_effect_to(self, value):
        """Sets the mosaic effect of the sprite. The mosaic effect repeats the costume as small tiles.

        Scratch block: set mosaic effect to (0)

        Parameters
        ----------
        value : number
            The new value of the effect. 0 means no effect.
        """
        return self._core.looks_seteffectto_mosaic(value)

    def set_pixelate_effect_to(self, value):
        """Sets the pixelate effect of the sprite. The pixelate effect makes the costume look blocky.

        Scratch block: set pixelate effect to (0)

        Parameters
        ----------
        value : number
            The new value of the effect. 0 means no effect.
        """
        return self._core.looks_seteffectto_pixelate(value)

    def set_whirl_effect_to(self, value):
        """Sets the whirl effect of the sprite. The whirl effect twists the costume.

        Scratch block: set whirl effect to (0)

        Parameters
        ----------
        value : number
            The new value of the effect. 0 means no effect.
        """
        return self._core.looks_seteffectto_whirl(value)

    def set_size_to(self, percent):
        """Sets the size of the sprite in percent. 100 is the normal size.

        Scratch block: set size to (100) %

        Parameters
        ----------
        percent : number
            The new size in percent. 100 is the normal size, 50 is half size.
        """
        return self._core.looks_setsizeto(percent)

    def show(self):
        """Shows the sprite on the stage.

        Scratch block: show
        """
        return self._core.looks_show()

    def size(self):
        """Returns the size of the sprite in percent. 100 is the normal size.

        Scratch block: (size)

        Returns
        -------
        number
            The size of the sprite in percent.
        """
        return self._core.looks_size()

    def switch_backdrop_to(self, backdrop):
        """Switches the stage to another backdrop.

        Scratch block: switch backdrop to (backdrop1)

        Parameters
        ----------
        backdrop : str or int
            The name of the backdrop, its number (starting with 1), or one of "next backdrop", "previous backdrop" and "random backdrop".
        """
        return self._core.looks_switchbackdropto_backdrop(backdrop)

    def switch_to_random_backdrop(self):
        """Switches the stage to a random backdrop.

        Scratch block: switch backdrop to [random backdrop]
        """
        return self._core.looks_switchbackdropto_random()

    def switch_to_next_backdrop(self):
        """Switches the stage to the next backdrop. After the last backdrop, the first one is used again.

        Scratch block: switch backdrop to [next backdrop]
        """
        return self._core.looks_switchbackdropto_next()

    def switch_to_previous_backdrop(self):
        """Switches the stage to the previous backdrop. Before the first backdrop, the last one is used.

        Scratch block: switch backdrop to [previous backdrop]
        """
        return self._core.looks_switchbackdropto_previous()

    def switch_costume_to(self, costume):
        """Switches the sprite to another costume.

        Scratch block: switch costume to (costume2)

        Parameters
        ----------
        costume : str or int
            The name of the costume, or its number (starting with 1).
        """
        return self._core.looks_switchcostumeto(costume)

    def think(self, text):
        """Shows a thought bubble with the given text next to the sprite.

        Scratch block: think (Hmm...)

        Parameters
        ----------
        text : str
            The text to show in the bubble.
        """
        return self._core.looks_think(text)

    def think_for_seconds(self, text, secs):
        """Shows a thought bubble with the given text next to the sprite for a number of seconds.

        The script waits until the time is over.

        Scratch block: think (Hmm...) for (2) seconds

        Parameters
        ----------
        text : str
            The text to show in the bubble.
        secs : number
            The number of seconds the bubble is shown.
        """
        return self._core.looks_thinkforsecs(text, secs)

    def change_x_by(self, value):
        """Moves the sprite horizontally by the given amount. Positive values move it to the right.

        Scratch block: change x by (10)

        Parameters
        ----------
        value : number
            The number of steps to move horizontally.
        """
        return self._core.motion_changexby(value)

    def change_y_by(self, value):
        """Moves the sprite vertically by the given amount. Positive values move it up.

        Scratch block: change y by (10)

        Parameters
        ----------
        value : number
            The number of steps to move vertically.
        """
        return self._core.motion_changeyby(value)

    def direction(self):
        """Returns the direction the sprite is pointing in degrees. 90 is right, 0 is up, 180 is down and -90 is left.

        Scratch block: (direction)

        Returns
        -------
        number
            The direction of the sprite, between -180 and 180.
        """
        return self._core.motion_direction()

    def glide_to_x_y(self, secs, x, y):
        """Glides the sprite to the given x and y position within the given number of seconds.

        The script waits until the glide is finished.

        Scratch block: glide (1) secs to x: (0) y: (0)

        Parameters
        ----------
        secs : number
            The duration of the glide in seconds. 0 moves the sprite at once.
        x : number
            The horizontal position to glide to.
        y : number
            The vertical position to glide to.
        """
        return self._core.motion_glidesecstoxy(secs, x, y)

    def glide_to_mouse_pointer(self, secs):
        """Glides the sprite to the position of the mouse pointer within the given number of seconds.

        The script waits until the glide is finished.

        Scratch block: glide (1) secs to [mouse-pointer]

        Parameters
        ----------
        secs : number
            The duration of the glide in seconds. 0 moves the sprite at once.
        """
        return self._core.motion_glideto_pointer(secs)

    def glide_to_random_position(self, secs):
        """Glides the sprite to a random position within the given number of seconds.

        The script waits until the glide is finished.

        Scratch block: glide (1) secs to [random position]

        Parameters
        ----------
        secs : number
            The duration of the glide in seconds. 0 moves the sprite at once.
        """
        return self._core.motion_glideto_random(secs)

    def glide_to_sprite(self, secs, sprite):
        """Glides the sprite to the position of another sprite within the given number of seconds.

        The script waits until the glide is finished.

        Scratch block: glide (1) secs to [sprite]

        Parameters
        ----------
        secs : number
            The duration of the glide in seconds. 0 moves the sprite at once.
        sprite : str
            The name of the sprite to glide to. Use "_mouse_" for the mouse pointer
            or "_random_" for a random position.
        """
        return self._core.motion_glideto_sprite(secs, sprite)

    def go_to_mouse_pointer(self):
        """Moves the sprite to the position of the mouse pointer.

        Scratch block: go to [mouse-pointer]
        """
        return self._core.motion_goto_pointer()

    def go_to_random_position(self):
        """Moves the sprite to a random position on the stage.

        Scratch block: go to [random position]
        """
        return self._core.motion_goto_random()

    def go_to_sprite(self, sprite):
        """Moves the sprite to the position of another sprite.

        Scratch block: go to [sprite]

        Parameters
        ----------
        sprite : str
            The name of the sprite to go to. Use "_mouse_" for the mouse pointer
            or "_random_" for a random position.
        """
        return self._core.motion_goto_sprite(sprite)

    def go_to_x_y(self, x, y):
        """Moves the sprite to the given x and y position. The center of the stage is x = 0, y = 0.

        Scratch block: go to x: (0) y: (0)

        Parameters
        ----------
        x : number
            The horizontal position. On the default stage of 480 by 360 pixels, x goes from -240 (left) to 240 (right).
        y : number
            The vertical position. On the default stage, y goes from -180 (bottom) to 180 (top).
        """
        return self._core.motion_gotoxy(x, y)

    def if_on_edge_bounce(self):
        """If the sprite touches the edge of the stage, it bounces back and stays on the stage.

        Scratch block: if on edge, bounce
        """
        return self._core.motion_ifonedgebounce()

    def move(self, steps):
        """Moves the sprite forward by the given number of steps, in the direction it is pointing.

        Scratch block: move (10) steps

        Parameters
        ----------
        steps : number
            How many steps to move. Negative values move the sprite backwards.
        """
        return self._core.motion_movesteps(steps)

    def point_in_direction(self, direction):
        """Turns the sprite to face the given direction.

        Scratch block: point in direction (90)

        Parameters
        ----------
        direction : number
            The direction in degrees. 0 is up, 90 is right, 180 is down and -90 is left.
        """
        return self._core.motion_pointindirection(direction)

    def point_towards_mouse_pointer(self):
        """Turns the sprite to face the mouse pointer.

        Scratch block: point towards [mouse-pointer]
        """
        return self._core.motion_pointtowards_pointer()

    def point_towards_sprite(self, sprite):
        """Turns the sprite to face another sprite.

        Scratch block: point towards [sprite]

        Parameters
        ----------
        sprite : str
            The name of the sprite to face. Use "_mouse_" for the mouse pointer
            or "_random_" for a random direction.
        """
        return self._core.motion_pointtowards_sprite(sprite)

    def point_towards_random_direction(self):
        """point towards random direction

        Returns
        -------
        None
        """
        return self._core.motion_pointtowards_random()

    def set_rotation_style_none(self):
        """Sets the rotation style to "don't rotate": the costume always looks the same, whatever direction the sprite points in.

        Scratch block: set rotation style [don't rotate]
        """
        return self._core.motion_setrotationstyle_dontrotate()

    def set_rotation_style_left_right(self):
        """Sets the rotation style to left-right: the costume only turns to face left or right and is never upside down.

        Scratch block: set rotation style [left-right]
        """
        return self._core.motion_setrotationstyle_leftright()

    def set_rotation_style_around(self):
        """Sets the rotation style to "all around": the costume turns with the direction of the sprite.

        Scratch block: set rotation style [all around]
        """
        return self._core.motion_setrotationstyle_allaround()

    def set_x(self, value):
        """Sets the horizontal position of the sprite. The center of the stage is x = 0.

        Scratch block: set x to (0)

        Parameters
        ----------
        value : number
            The new x position.
        """
        return self._core.motion_setx(value)

    def set_y(self, value):
        """Sets the vertical position of the sprite. The center of the stage is y = 0.

        Scratch block: set y to (0)

        Parameters
        ----------
        value : number
            The new y position.
        """
        return self._core.motion_sety(value)

    def turn_left(self, deg):
        """Turns the sprite to the left (counter-clockwise) by the given number of degrees.

        Scratch block: turn ↺ (15) degrees

        Parameters
        ----------
        deg : number
            The number of degrees to turn. 90 is a quarter turn.
        """
        return self._core.motion_turnleft(deg)

    def turn_right(self, deg):
        """Turns the sprite to the right (clockwise) by the given number of degrees.

        Scratch block: turn ↻ (15) degrees

        Parameters
        ----------
        deg : number
            The number of degrees to turn. 90 is a quarter turn.
        """
        return self._core.motion_turnright(deg)

    def x_position(self):
        """Returns the horizontal position of the sprite. The center of the stage is 0.

        Scratch block: (x position)

        Returns
        -------
        number
            The x position of the sprite.
        """
        return self._core.motion_xposition()

    def y_position(self):
        """Returns the vertical position of the sprite. The center of the stage is 0.

        Scratch block: (y position)

        Returns
        -------
        number
            The y position of the sprite.
        """
        return self._core.motion_yposition()

    def math_function(self, operator, number):
        """%1 of %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        operator : FILL
        number : FILL
        

        Returns
        -------

        """
        return self._core.operator_mathop(operator, number)

    def pick_random(self, start, end):
        """pick random %1 to %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        start : FILL
        end : FILL
        

        Returns
        -------

        """
        return self._core.operator_random(start, end)

    def change_pen_brightness_by(self, value):
        """change pen brightness by [VALUE]

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.pen_changePenColorParamBy_brightness(value)

    def change_pen_hue_by(self, value):
        """change pen color by [VALUE]

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.pen_changePenColorParamBy_color(value)

    def change_pen_saturation_by(self, value):
        """change pen saturation by [VALUE]

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.pen_changePenColorParamBy_saturation(value)

    def change_pen_transparency_by(self, value):
        """change pen transparency by [VALUE]

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.pen_changePenColorParamBy_transparency(value)

    def change_pen_size_by(self, value):
        """change pen size by [SIZE]

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.pen_changePenSizeBy(value)

    def erase_all(self):
        """erase all

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.pen_clear()

    def pen_down(self):
        """pen down

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.pen_penDown()

    def pen_up(self):
        """pen up

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.pen_penUp()

    def set_pen_brightness_to(self, value):
        """set pen brightness to [VALUE]

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.pen_setPenColorParamTo_brightness(value)

    def set_pen_hue_to(self, value):
        """set pen color to [VALUE]

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.pen_setPenColorParamTo_color(value)

    def set_pen_saturation_to(self, value):
        """set pen saturation to [VALUE]

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.pen_setPenColorParamTo_saturation(value)

    def set_pen_transparency_to(self, value):
        """set pen transparency to [VALUE]

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.pen_setPenColorParamTo_transparency(value)

    def set_pen_color(self, color):
        """set pen color to [COLOR]

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        color : FILL
        

        Returns
        -------

        """
        return self._core.pen_setPenColorToColor(color)

    def set_pen_size_to(self, value):
        """set pen size to [SIZE]

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.pen_setPenSizeTo(value)

    def stamp(self):
        """stamp

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.pen_stamp()

    def add_costume(self, name, center_x=None, center_y=None, factor=1):
        """Adds a costume (an image) to the sprite. The costume is added at the end of the costume list.

        Parameters
        ----------
        name : str
            The name of the image file, e.g. "cat.png". The file must be in the project folder.
        center_x : number
            The horizontal position of the costume's center in the image, in pixels. If not given, the center of the image is used.
        center_y : number
            The vertical position of the costume's center in the image, in pixels. If not given, the center of the image is used.
        factor : number
            The scaling of the image. 1 keeps the original size, 2 shows it at double size.
        """
        return self._core.pystage_addcostume(name, center_x, center_y, factor)

    def add_sound(self, name):
        """

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL
        

        Returns
        -------

        """
        return self._core.pystage_addsound(name)

    def insert_costume(self, index, name, center_x=None, center_y=None, factor=1):
        """Inserts a costume (an image) into the sprite's costume list at the given position.

        Parameters
        ----------
        index : int
            The position where the costume is inserted, starting with 1.
        name : str
            The name of the image file, e.g. "cat.png".
        center_x : number
            The horizontal position of the costume's center in the image, in pixels. If not given, the center of the image is used.
        center_y : number
            The vertical position of the costume's center in the image, in pixels. If not given, the center of the image is used.
        factor : number
            The scaling of the image. 1 keeps the original size.
        """
        return self._core.pystage_insertcostume(index, name, center_x, center_y, factor)

    def create_variable(self, name, value=0, all_sprites=True):
        """

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL
        all_sprites : FILL
        

        Returns
        -------

        """
        return self._core.pystage_makevariable(name, value, all_sprites)

    def replace_costume(self, index, name, center_x=None, center_y=None, factor=1):
        """Replaces an existing costume of the sprite with another image.

        Parameters
        ----------
        index : int
            The number of the costume to replace, starting with 1.
        name : str
            The name of the new image file.
        center_x : number
            The horizontal position of the costume's center in the image, in pixels. If not given, the center of the image is used.
        center_y : number
            The vertical position of the costume's center in the image, in pixels. If not given, the center of the image is used.
        factor : number
            The scaling of the image. 1 keeps the original size.
        """
        return self._core.pystage_replacecostume(
            index, name, center_x, center_y, factor
        )

    def set_monitor_position(self, name, x, y):
        """

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL
        x : FILL
        y : FILL
        

        Returns
        -------

        """
        return self._core.pystage_setmonitorposition(name, x, y)

    def set_monitor_style_large(self, name):
        """

        Translation string: 
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL
        

        Returns
        -------

        """
        return self._core.pystage_setmonitorstyle_large(name)

    def set_monitor_style_normal(self, name):
        """

        Translation string: 
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL
        

        Returns
        -------

        """
        return self._core.pystage_setmonitorstyle_normal(name)

    def set_monitor_style_slider(self, name, minimum=0, maximum=100, integer=True):
        """Show the variable as a slider that can be dragged with the mouse.

        Parameters
        ----------
        name : str
            The name of the variable.
        minimum, maximum : number
            The range of the slider (0 to 100 by default, like in Scratch).
        integer : bool
            If True, the slider only sets whole numbers, otherwise numbers with two decimals.
        """
        return self._core.pystage_setmonitorstyle_slider(name, minimum, maximum, integer)

    def answer(self):
        """answer

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_answer()

    def ask_and_wait(self, question):
        """ask %1 and wait

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        question : FILL
        

        Returns
        -------

        """
        return self._core.sensing_askandwait(question)

    def color_is_touching(self, sprite_color, color):
        """color %1 is touching %2?

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite_color : FILL
        color : FILL
        

        Returns
        -------

        """
        return self._core.sensing_coloristouchingcolor(sprite_color, color)

    def current_date(self):
        """current date

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_current_date()

    def current_day_of_week(self):
        """current day of week

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_current_dayofweek()

    def current_hour(self):
        """current hour

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_current_hour()

    def current_minute(self):
        """current minute

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_current_minute()

    def current_month(self):
        """current month

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_current_month()

    def current_second(self):
        """current second

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_current_second()

    def current_year(self):
        """current year

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_current_year()

    def days_since(self):
        """days since 2000

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_dayssince2000()

    def distance_to_mouse_pointer(self):
        """distance to mouse-pointer

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_distanceto_pointer()

    def distance_to_sprite(self, sprite):
        """distance to %1

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite : FILL
        

        Returns
        -------

        """
        return self._core.sensing_distanceto_sprite(sprite)

    def key_pressed(self, key):
        """key %1 pressed?

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        key : FILL
        

        Returns
        -------

        """
        return self._core.sensing_keypressed(key)

    def loudness(self):
        """loudness

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_loudness()

    def mouse_down(self):
        """mouse down?

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_mousedown()

    def mouse_x(self):
        """mouse x

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_mousex()

    def mouse_y(self):
        """mouse y

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_mousey()

    def backdrop_name_of(self, stage="_stage_"):
        """backdrop name of %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        stage : FILL
        

        Returns
        -------

        """
        return self._core.sensing_of_backdropname(stage="_stage_")

    def backdrop_of(self, stage="_stage_"):
        """backdrop # of %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        stage : FILL
        

        Returns
        -------

        """
        return self._core.sensing_of_backdropnumber(stage="_stage_")

    def costume_name_of(self, sprite):
        """costume name of %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite : FILL
        

        Returns
        -------

        """
        return self._core.sensing_of_costumename(sprite)

    def costume_of(self, sprite):
        """costume # of %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite : FILL
        

        Returns
        -------

        """
        return self._core.sensing_of_costumenumber(sprite)

    def direction_of(self, sprite):
        """direction of %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite : FILL
        

        Returns
        -------

        """
        return self._core.sensing_of_direction(sprite)

    def size_of(self, sprite):
        """size of %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite : FILL
        

        Returns
        -------

        """
        return self._core.sensing_of_size(sprite)

    def get_variable_of(self, variable, sprite="_stage_"):
        """%1 of %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        variable : FILL
        sprite : FILL
        

        Returns
        -------

        """
        return self._core.sensing_of_variable(variable, sprite="_stage_")

    def volume_of(self, sprite="_stage_"):
        """volume of %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite : FILL
        

        Returns
        -------

        """
        return self._core.sensing_of_volume(sprite="_stage_")

    def x_position_of(self, sprite):
        """x position of %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite : FILL
        

        Returns
        -------

        """
        return self._core.sensing_of_xposition(sprite)

    def y_position_of(self, sprite):
        """y position of %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite : FILL
        

        Returns
        -------

        """
        return self._core.sensing_of_yposition(sprite)

    def reset_timer(self):
        """reset timer

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_resettimer()

    def set_drag_mode_draggable(self):
        """set drag mode draggable

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_setdragmode_draggable()

    def set_drag_mode_not_draggable(self):
        """set drag mode not draggable

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_setdragmode_notdraggable()

    def timer(self):
        """timer

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_timer()

    def touching_color(self, color):
        """touching color %1?

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        color : FILL
        

        Returns
        -------

        """
        return self._core.sensing_touchingcolor(color)

    def touching_edge(self):
        """touching edge?

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_touchingobject_edge()

    def touching_mouse_pointer(self):
        """touching mouse-pointer?

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_touchingobject_pointer()

    def touching(self, sprite):
        """touching %1?

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite : FILL
        

        Returns
        -------

        """
        return self._core.sensing_touchingobject_sprite(sprite)

    def username(self):
        """username

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_username()

    def change_pan_left_right_effect_by(self, value):
        """change pan left/right effect by %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.sound_changeeffectby_pan(value)

    def change_pitch_effect_by(self, value):
        """change pitch effect by %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.sound_changeeffectby_pitch(value)

    def change_volume_by(self, value):
        """change volume by %1

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.sound_changevolumeby(value)

    def clear_sound_effects(self):
        """clear sound effects

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sound_cleareffects()

    def start_sound(self, name, loop=0):
        """start sound %1

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL
        loop : FILL
        

        Returns
        -------

        """
        return self._core.sound_play(name, loop=0)

    def play_sound_until_done(self, name):
        """play sound %1 until done

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL
        

        Returns
        -------

        """
        return self._core.sound_playuntildone(name)

    def set_pan_left_right_effect_to(self, value):
        """set pan left/right effect to %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.sound_seteffectto_pan(value)

    def set_pitch_effect_to(self, value):
        """set pitch effect to %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.sound_seteffectto_pitch(value)

    def set_volume_to(self, value):
        """set volume to %1%

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        return self._core.sound_setvolumeto(value)

    def stop_all_sounds(self):
        """stop all sounds

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sound_stopallsounds()

    def volume(self):
        """volume

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sound_volume()

    def set_name(self, name):
        """set name of the sprite to %1%

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL
        

        Returns
        -------

        """
        return self._core.pystage_setname(name)

    def create_list(self, name, values=None, all_sprites=True):
        """Create a list.

        Parameters
        ----------
        name : str
            The name of the list.
        values : list
            The initial items of the list.
        all_sprites : bool
            If True, the list can be used by the stage and all sprites.
            If False, it belongs to this sprite only.
        """
        return self._core.pystage_makelistvariable(name, values, all_sprites)

    def add_to_list(self, name, item):
        """add %1 to list %2

        Parameters
        ----------
        name : str
            The name of the list.
        item
            The item, a number or a text.
        """
        return self._core.data_addtolist(name, item)

    def delete_item_of_list(self, name, index):
        """delete %1 of list %2

        Parameters
        ----------
        name : str
            The name of the list.
        index : int or str
            The position, starting with 1. Also possible: "last" and "random". With "all", all items are deleted.
        """
        return self._core.data_deleteoflist(name, index)

    def delete_all_of_list(self, name):
        """delete all of list %1

        Parameters
        ----------
        name : str
            The name of the list.
        """
        return self._core.data_deletealloflist(name)

    def insert_at_list(self, name, item, index):
        """insert %1 at %2 of list %3

        Parameters
        ----------
        name : str
            The name of the list.
        item
            The item, a number or a text.
        index : int or str
            The position, starting with 1. Also possible: "last" and "random".
        """
        return self._core.data_insertatlist(name, item, index)

    def replace_item_of_list(self, name, index, item):
        """replace item %1 of list %2 with %3

        Parameters
        ----------
        name : str
            The name of the list.
        index : int or str
            The position, starting with 1. Also possible: "last" and "random".
        item
            The item, a number or a text.
        """
        return self._core.data_replaceitemoflist(name, index, item)

    def item_of_list(self, name, index):
        """item %1 of list %2

        Parameters
        ----------
        name : str
            The name of the list.
        index : int or str
            The position, starting with 1. Also possible: "last" and "random".

        Returns
        -------
        The item or an empty text, if there is no item at this position.
        """
        return self._core.data_itemoflist(name, index)

    def item_number_in_list(self, name, item):
        """item # of %1 in list %2

        Parameters
        ----------
        name : str
            The name of the list.
        item
            The item, a number or a text.

        Returns
        -------
        int
            The position of the first occurrence, 0 if the item is not in the list.
        """
        return self._core.data_itemnumoflist(name, item)

    def length_of_list(self, name):
        """length of list %1

        Parameters
        ----------
        name : str
            The name of the list.

        Returns
        -------
        int
        """
        return self._core.data_lengthoflist(name)

    def list_contains(self, name, item):
        """list %1 contains %2?

        Parameters
        ----------
        name : str
            The name of the list.
        item
            The item, a number or a text.

        Returns
        -------
        bool
        """
        return self._core.data_listcontainsitem(name, item)

    def get_list(self, name):
        """The list itself.

        This is the real Python list, you can use it like any other list.

        Parameters
        ----------
        name : str
            The name of the list.

        Returns
        -------
        list
        """
        return self._core.data_listvariable(name)

    def show_list(self, name):
        """show list %1

        Parameters
        ----------
        name : str
            The name of the list.
        """
        return self._core.data_showlist(name)

    def hide_list(self, name):
        """hide list %1

        Parameters
        ----------
        name : str
            The name of the list.
        """
        return self._core.data_hidelist(name)

    def set_list_monitor_position(self, name, x, y, width=None, height=None):
        """Set position and size of the list shown on the stage.

        Parameters
        ----------
        name : str
            The name of the list.
        x : int
            Left border.
        y : int
            Upper border.
        width : int
            Width in pixels, automatic if not given.
        height : int
            Height in pixels, automatic if not given.
        """
        return self._core.pystage_setlistmonitorposition(name, x, y, width, height)

    def join(self, string1, string2):
        """join %1 %2

        Parameters
        ----------
        string1
            The first text or number.
        string2
            The second text or number.

        Returns
        -------
        str
        """
        return self._core.operator_join(string1, string2)

    def letter_of(self, letter, string):
        """letter %1 of %2

        Parameters
        ----------
        letter : int
            The position of the letter, starting with 1.
        string : str
            The text.

        Returns
        -------
        str
            The letter or an empty text, if there is no letter at this position.
        """
        return self._core.operator_letter_of(letter, string)

    def length_of(self, string):
        """length of %1

        Parameters
        ----------
        string : str
            The text.

        Returns
        -------
        int
        """
        return self._core.operator_length(string)

    def contains(self, string1, string2):
        """%1 contains %2?

        Upper and lower case is ignored.

        Parameters
        ----------
        string1 : str
            The text to search in.
        string2 : str
            The text to search for.

        Returns
        -------
        bool
        """
        return self._core.operator_contains(string1, string2)

    def greater_than(self, operand1, operand2):
        """%1 > %2

        Greater than; compares like Scratch (numbers numerically, otherwise text without case).

        Returns
        -------
        bool
        """
        return self._core.operator_gt(operand1, operand2)

    def less_than(self, operand1, operand2):
        """%1 < %2

        Less than; compares like Scratch (numbers numerically, otherwise text without case).

        Returns
        -------
        bool
        """
        return self._core.operator_lt(operand1, operand2)

    def equals(self, operand1, operand2):
        """%1 = %2

        Equal; compares like Scratch (numbers numerically, otherwise text without case).

        Returns
        -------
        bool
        """
        return self._core.operator_equals(operand1, operand2)

    def round(self, number):
        """round %1

        Like in Scratch, .5 is always rounded up.

        Parameters
        ----------
        number : float

        Returns
        -------
        int
        """
        return self._core.operator_round(number)

    def divide(self, a, b):
        """%1 / %2

        Like in Scratch, dividing by 0 gives Infinity, -Infinity or NaN
        instead of an error.

        Parameters
        ----------
        a : float
        b : float

        Returns
        -------
        float
        """
        return self._core.operator_divide(a, b)

    def modulo(self, a, b):
        """%1 mod %2

        The remainder of a division, with the sign of the divisor like in
        Scratch. The modulo of 0 is NaN.

        Parameters
        ----------
        a : float
        b : float

        Returns
        -------
        float
        """
        return self._core.operator_mod(a, b)

    def show_monitor(self, reporter):
        """Show the monitor of a value, like the checkbox next to a block in Scratch.

        Parameters
        ----------
        reporter : str
            What to show: "x position", "y position", "direction",
            "costume number", "costume name", "size", "volume" (sprites and
            stage), "backdrop number", "backdrop name" (stage), "answer",
            "loudness", "timer", "year", "month", "date", "day of week",
            "hour", "minute", "second" or "username".
        """
        return self._core.pystage_showmonitor(reporter)

    def hide_monitor(self, reporter):
        """Hide the monitor of a value. See show_monitor for the values."""
        return self._core.pystage_hidemonitor(reporter)

    def set_value_monitor_position(self, reporter, x, y):
        """Set the position of the monitor of a value.

        Parameters
        ----------
        reporter : str
            The value, see show_monitor.
        x : int
            Left border (Scratch coordinates).
        y : int
            Upper border (Scratch coordinates).
        """
        return self._core.pystage_setreportermonitorposition(reporter, x, y)

    def set_value_monitor_style(self, reporter, style="normal"):
        """Set the style of the monitor of a value.

        Parameters
        ----------
        reporter : str
            The value, see show_monitor.
        style : str
            "normal" or "large".
        """
        return self._core.pystage_setreportermonitorstyle(reporter, style)
