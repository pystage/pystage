from pystage.core import CoreStage
from pystage.en import Sprite


class Stage():

    def __init__(self, title="Welcome to pyStage!"):
        """Create the stage. The title is shown in the window title."""
        self._core = CoreStage(title)
        self._core.facade = self
        self._core.sprite_facade_class = Sprite

    def add_a_sprite(self, costume="default") -> Sprite:
        return self._core.pystage_createsprite(costume=costume)

    def play(self):
        self._core.pystage_play()

    def create_clone_of_sprite(self, sprite='_myself_'):
        """create clone of %1

        Translation string: create clone of %1
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite : FILL
        

        Returns
        -------

        """
        return self._core.control_create_clone_of_sprite(sprite)

    def stop_all(self):
        """stop all

        Translation string: stop all
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.control_stop_all()

    def stop_other_scripts_in_stage(self):
        """stop other scripts in stage

        Translation string: stop other scripts in stage
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.control_stop_other()

    def stop_this_script(self):
        """stop this script

        Translation string: stop this script
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.control_stop_this()

    def wait(self, secs):
        """wait %1 seconds

        Translation string: wait %1 seconds
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

        Translation string: change %1 by %2
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

        Translation string: hide variable %1
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

        Translation string: set %1 to %2
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

        Translation string: show variable %1
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

        Translation string: 
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
        """Sends a message to all sprites and the stage. Every "when I receive" block with this message starts running. The script does not wait for them.

        Scratch block: broadcast (message1)

        Parameters
        ----------
        message : str
            The name of the message. Upper and lower case do not matter.
        """
        return self._core.event_broadcast(message)

    def broadcast_and_wait(self, message):
        """Sends a message to all sprites and the stage and waits until all scripts that receive it are finished.

        Scratch block: broadcast (message1) and wait

        Parameters
        ----------
        message : str
            The name of the message. Upper and lower case do not matter.
        """
        return self._core.event_broadcastandwait(message)

    def when_backdrop_switches_to(self, backdrop, generator_function, name='', no_refresh=False):
        """Runs the code when the stage switches to the given backdrop.

        Scratch block: when backdrop switches to (backdrop1)

        Parameters
        ----------
        backdrop : str
            The name of the backdrop. Upper and lower case do not matter.
        generator_function : function
            The function with the code to be executed.
        name : str
            A name to distinguish code blocks using the same function.
        no_refresh : bool
            If True, the code is executed in one go without screen refresh.
        """
        return self._core.event_whenbackdropswitchesto(backdrop, generator_function, name, no_refresh)

    def when_i_receive_message(self, message, generator_function, name='', no_refresh=False):
        """Runs the code when the given message is broadcast.

        Scratch block: when I receive (message1)

        Parameters
        ----------
        message : str
            The name of the message. Upper and lower case do not matter.
        generator_function : function
            The function with the code to be executed.
        name : str
            A name to distinguish code blocks using the same function.
        no_refresh : bool
            If True, the code is executed in one go without screen refresh.
        """
        return self._core.event_whenbroadcastreceived(message, generator_function, name, no_refresh)

    def when_program_starts(self, generator_function, name='', no_refresh=False):
        """Runs the code when the green flag is clicked, i.e. when the program starts.

        Scratch block: when [green flag] clicked

        Parameters
        ----------
        generator_function : function
            The function with the code to be executed.
        name : str
            A name to distinguish code blocks using the same function.
        no_refresh : bool
            If True, the code is executed in one go without screen refresh.
        """
        return self._core.event_whenflagclicked(generator_function, name, no_refresh)

    def when_loudness_greater_than(self, value, generator_function, name='', no_refresh=False):
        """Runs the code when the loudness of the microphone is greater than the given value.

        This is only a stub: the microphone is not supported, the loudness is always -1 and the code never runs.

        Scratch block: when [loudness] > (10)

        Parameters
        ----------
        value : number
            The loudness value that must be exceeded.
        generator_function : function
            The function with the code to be executed.
        name : str
            A name to distinguish code blocks using the same function.
        no_refresh : bool
            If True, the code is executed in one go without screen refresh.
        """
        return self._core.event_whengreaterthan_loudness(value, generator_function, name, no_refresh)

    def when_timer_greater_than(self, value, generator_function, name='', no_refresh=False):
        """Runs the code when the timer is greater than the given value.

        The code runs once each time the timer becomes greater than the value. It runs again after the timer has been reset.

        Scratch block: when [timer] > (10)

        Parameters
        ----------
        value : number
            The number of seconds the timer must exceed.
        generator_function : function
            The function with the code to be executed.
        name : str
            A name to distinguish code blocks using the same function.
        no_refresh : bool
            If True, the code is executed in one go without screen refresh.
        """
        return self._core.event_whengreaterthan_timer(value, generator_function, name, no_refresh)

    def when_key_pressed(self, key, generator_function, name='', no_refresh=False):
        """Runs the code when a key is pressed.

        Scratch block: when (space) key pressed

        Parameters
        ----------
        key : str
            The key, e.g. "a", "1", "space", "left arrow", "right arrow", "up arrow", "down arrow" or "any" (any key). Upper and lower case do not matter.
        generator_function : function
            The function with the code to be executed.
        name : str
            A name to distinguish code blocks using the same function.
        no_refresh : bool
            If True, the code is executed in one go without screen refresh.
        """
        return self._core.event_whenkeypressed(key, generator_function, name, no_refresh)

    def when_this_sprite_clicked(self, generator_function, name='', no_refresh=False):
        """Runs the code when the sprite is clicked with the mouse.

        Scratch block: when this sprite clicked

        Parameters
        ----------
        generator_function : function
            The function with the code to be executed.
        name : str
            A name to distinguish code blocks using the same function.
        no_refresh : bool
            If True, the code is executed in one go without screen refresh.
        """
        return self._core.event_whenthisspriteclicked(generator_function, name, no_refresh)

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

    def clear_graphic_effects(self):
        """Removes all graphic effects (color, fisheye, whirl, pixelate, mosaic, brightness and ghost) of the sprite.

        Scratch block: clear graphic effects
        """
        return self._core.looks_cleargraphiceffects()

    def next_backdrop(self):
        """Switches the stage to the next backdrop. After the last backdrop, the first one is used again.

        Scratch block: next backdrop
        """
        return self._core.looks_nextbackdrop()

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

    def switch_backdrop_to_and_wait(self, backdrop):
        """Switches the stage to another backdrop and waits until all scripts started by "when backdrop switches to" are finished.

        Scratch block: switch backdrop to (backdrop1) and wait

        Parameters
        ----------
        backdrop : str or int
            The name of the backdrop, its number (starting with 1), or one of "next backdrop", "previous backdrop" and "random backdrop".
        """
        return self._core.looks_switchbackdroptoandwait(backdrop)

    def math_function(self, operator, number):
        """%1 of %2

        Translation string: %1 of %2
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

        Translation string: pick random %1 to %2
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

    def add_backdrop(self, name, center_x=None, center_y=None, factor=1):
        """Adds a backdrop (an image) to the stage. The backdrop is added at the end of the backdrop list.

        Parameters
        ----------
        name : str
            The name of the image file, e.g. "forest.png". The file must be in the project folder.
        center_x : number
            The horizontal position of the image's center, in pixels. If not given, the center of the image is used.
        center_y : number
            The vertical position of the image's center, in pixels. If not given, the center of the image is used.
        factor : number
            The scaling of the image. 1 keeps the original size.
        """
        return self._core.pystage_addbackdrop(name, center_x, center_y, factor)

    def add_sound(self, name):
        """Loads a sound file, so that the sprite or stage can play it.

        Sounds are also loaded automatically when they are played for the first time.

        Parameters
        ----------
        name : str
            The name of the sound file, e.g. "pop.wav". The file must be in the project folder.
        """
        return self._core.pystage_addsound(name)

    def insert_backdrop(self, index, name, center_x=None, center_y=None, factor=1):
        """Inserts a backdrop (an image) into the stage's backdrop list at the given position.

        Parameters
        ----------
        index : int
            The position where the backdrop is inserted, starting with 1.
        name : str
            The name of the image file, e.g. "forest.png".
        center_x : number
            The horizontal position of the image's center, in pixels. If not given, the center of the image is used.
        center_y : number
            The vertical position of the image's center, in pixels. If not given, the center of the image is used.
        factor : number
            The scaling of the image. 1 keeps the original size.
        """
        return self._core.pystage_insertbackdrop(index, name, center_x, center_y, factor)

    def create_variable(self, name, value=0, all_sprites=True):
        """

        Translation string: 
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

    def replace_backdrop(self, index, name, center_x=None, center_y=None, factor=1):
        """Replaces an existing backdrop of the stage with another image.

        Parameters
        ----------
        index : int
            The number of the backdrop to replace, starting with 1.
        name : str
            The name of the new image file.
        center_x : number
            The horizontal position of the image's center, in pixels. If not given, the center of the image is used.
        center_y : number
            The vertical position of the image's center, in pixels. If not given, the center of the image is used.
        factor : number
            The scaling of the image. 1 keeps the original size.
        """
        return self._core.pystage_replacebackdrop(index, name, center_x, center_y, factor)

    def set_monitor_position(self, name, x, y):
        """

        Translation string: 
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

        Translation string: answer
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_answer()

    def ask_and_wait(self, question):
        """ask %1 and wait

        Translation string: ask %1 and wait
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        question : FILL
        

        Returns
        -------

        """
        return self._core.sensing_askandwait(question)

    def current_date(self):
        """current date

        Translation string: current date
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_current_date()

    def current_day_of_week(self):
        """current day of week

        Translation string: current day of week
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_current_dayofweek()

    def current_hour(self):
        """current hour

        Translation string: current hour
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_current_hour()

    def current_minute(self):
        """current minute

        Translation string: current minute
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_current_minute()

    def current_month(self):
        """current month

        Translation string: current month
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_current_month()

    def current_second(self):
        """current second

        Translation string: current second
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_current_second()

    def current_year(self):
        """current year

        Translation string: current year
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_current_year()

    def days_since(self):
        """days since 2000

        Translation string: days since 2000
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_dayssince2000()

    def key_pressed(self, key):
        """key %1 pressed?

        Translation string: key %1 pressed?
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

        Translation string: loudness
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_loudness()

    def mouse_down(self):
        """mouse down?

        Translation string: mouse down?
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_mousedown()

    def mouse_x(self):
        """mouse x

        Translation string: mouse x
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_mousex()

    def mouse_y(self):
        """mouse y

        Translation string: mouse y
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_mousey()

    def backdrop_name_of(self, stage='_stage_'):
        """backdrop name of %2

        Translation string: backdrop name of %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        stage : FILL
        

        Returns
        -------

        """
        return self._core.sensing_of_backdropname(stage)

    def backdrop_of(self, stage='_stage_'):
        """backdrop # of %2

        Translation string: backdrop # of %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        stage : FILL
        

        Returns
        -------

        """
        return self._core.sensing_of_backdropnumber(stage)

    def costume_name_of(self, sprite):
        """costume name of %2

        Translation string: costume name of %2
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

        Translation string: costume # of %2
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

        Translation string: direction of %2
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

        Translation string: size of %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite : FILL
        

        Returns
        -------

        """
        return self._core.sensing_of_size(sprite)

    def get_variable_of(self, variable, sprite='_stage_'):
        """%1 of %2

        Translation string: %1 of %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        variable : FILL
        sprite : FILL
        

        Returns
        -------

        """
        return self._core.sensing_of_variable(variable, sprite)

    def volume_of(self, sprite='_stage_'):
        """volume of %2

        Translation string: volume of %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite : FILL
        

        Returns
        -------

        """
        return self._core.sensing_of_volume(sprite)

    def x_position_of(self, sprite):
        """x position of %2

        Translation string: x position of %2
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

        Translation string: y position of %2
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

        Translation string: reset timer
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_resettimer()

    def set_drag_mode_draggable(self):
        """set drag mode draggable

        Translation string: set drag mode draggable
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_setdragmode_draggable()

    def set_drag_mode_not_draggable(self):
        """set drag mode not draggable

        Translation string: set drag mode not draggable
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_setdragmode_notdraggable()

    def timer(self):
        """timer

        Translation string: timer
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_timer()

    def username(self):
        """username

        Translation string: username
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        return self._core.sensing_username()

    def change_pan_left_right_effect_by(self, value):
        """Changes the pan effect of the sound by the given amount. The pan effect moves the sound between the left and the right speaker.

        Scratch block: change pan left/right effect by (10)

        Parameters
        ----------
        value : number
            The change of the pan effect. -100 is all left, 0 is the middle and 100 is all right.
        """
        return self._core.sound_changeeffectby_pan(value)

    def change_pitch_effect_by(self, value):
        """Changes the pitch effect of the sound by the given amount. Positive values make the sound higher.

        Scratch block: change pitch effect by (10)

        Parameters
        ----------
        value : number
            The change of the pitch effect. The effect goes from -360 to 360, and 0 is the normal pitch.
        """
        return self._core.sound_changeeffectby_pitch(value)

    def change_volume_by(self, value):
        """Changes the volume of the sprite's sounds by the given amount. Negative values make the sound quieter.

        Scratch block: change volume by (-10)

        Parameters
        ----------
        value : number
            The change of the volume. The volume goes from 0 to 100.
        """
        return self._core.sound_changevolumeby(value)

    def clear_sound_effects(self):
        """Removes all sound effects (pitch and pan) of the sprite.

        Scratch block: clear sound effects
        """
        return self._core.sound_cleareffects()

    def start_sound(self, name, loop=0):
        """Starts playing a sound. The script does not wait until the sound is finished.

        Scratch block: start sound (pop)

        Parameters
        ----------
        name : str or int
            The name of the sound file, e.g. "pop.wav", or the number of the sound (starting with 1).
        loop : int
            How often the sound is repeated after the first time. 0 plays it once, -1 repeats it forever.
        """
        return self._core.sound_play(name, loop)

    def play_sound_until_done(self, name):
        """Plays a sound and waits until it is finished.

        Scratch block: play sound (pop) until done

        Parameters
        ----------
        name : str or int
            The name of the sound file, e.g. "pop.wav", or the number of the sound (starting with 1).
        """
        return self._core.sound_playuntildone(name)

    def set_pan_left_right_effect_to(self, value):
        """Sets the pan effect of the sound. The pan effect moves the sound between the left and the right speaker.

        Scratch block: set pan left/right effect to (0)

        Parameters
        ----------
        value : number
            The new pan effect. -100 is all left, 0 is the middle and 100 is all right.
        """
        return self._core.sound_seteffectto_pan(value)

    def set_pitch_effect_to(self, value):
        """Sets the pitch effect of the sound. Higher values make the sound higher.

        Scratch block: set pitch effect to (0)

        Parameters
        ----------
        value : number
            The new pitch effect, from -360 to 360. 0 is the normal pitch.
        """
        return self._core.sound_seteffectto_pitch(value)

    def set_volume_to(self, value):
        """Sets the volume of the sprite's sounds. 100 is the loudest and 0 is silent.

        Scratch block: set volume to (100) %

        Parameters
        ----------
        value : number
            The new volume, from 0 to 100 percent. Values outside this range are limited to it.
        """
        return self._core.sound_setvolumeto(value)

    def stop_all_sounds(self):
        """Stops all sounds that are playing, of all sprites and the stage.

        Scratch block: stop all sounds
        """
        return self._core.sound_stopallsounds()

    def volume(self):
        """Returns the volume of the sprite's sounds, from 0 to 100.

        Scratch block: (volume)

        Returns
        -------
        number
            The current volume, from 0 to 100.
        """
        return self._core.sound_volume()

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

    def when_stage_clicked(self, generator_function, name="", no_refresh=False):
        """when stage clicked

        Parameters
        ----------
        generator_function : function
            The function with the code to be executed.
        name : str
            A name to distinguish code blocks using the same function.
        no_refresh : bool
            If True, the code is executed in one go without screen refresh.
        """
        return self._core.event_whenstageclicked(generator_function, name, no_refresh)

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

    def erase_all(self):
        """erase all

        Clears everything that was drawn with the pen.

        Returns
        -------
        None
        """
        return self._core.pen_clear()

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
