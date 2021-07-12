
from pystage.core.sprite import CoreSprite


class Sprite():
    def __init__(self, core_sprite):
        self._core : CoreSprite = core_sprite
        self._core.facade = self


            
    def create_clone_of(self, sprite='_myself_'):
        """create clone of %1

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite : FILL
        

        Returns
        -------

        """
        self._core.control_create_clone_of(sprite='_my_')
                
    def delete_this_clone(self):
        """delete this clone

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.control_delete_this_clone()
                
    def when_i_start_as_a_clone(self, key, generator_function, name='', no_refresh=False):
        """when I start as a clone

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
        self._core.control_start_as_clone(key, generator_function, name='', no_refresh=False)
                
    def stop_all(self):
        """stop all

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.control_stop_all()
                
    def stop_other_scripts_in_sprite(self):
        """stop other scripts in sprite

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.control_stop_other()
                
    def stop_this_script(self):
        """stop this script

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.control_stop_this()
                
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
        self._core.control_wait(secs)
                
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
        self._core.data_changevariableby(name, value)
                
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
        self._core.data_hidevariable(name)
                
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
        self._core.data_setvariableto(name, value)
                
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
        self._core.data_showvariable(name)
                
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
        self._core.data_variable(name)
                
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
        self._core.event_broadcast(message)
                
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
        self._core.event_broadcastandwait(message)
                
    def when_backdrop_switches_to(self, backdrop, generator_function, name='', no_refresh=False):
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
        self._core.event_whenbackdropswitchesto(backdrop, generator_function, name='', no_refresh=False)
                
    def when_i_receive_message(self, message, generator_function, name='', no_refresh=False):
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
        self._core.event_whenbroadcastreceived(message, generator_function, name='', no_refresh=False)
                
    def when_program_starts(self, generator_function, name='', no_refresh=False):
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
        self._core.event_whenflagclicked(generator_function, name='', no_refresh=False)
                
    def when_loudness_greater_than(self, value, generator_function, name='', no_refresh=False):
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
        self._core.event_whengreaterthan_loudness(value, generator_function, name='', no_refresh=False)
                
    def when_timer_greater_than(self, value, generator_function, name='', no_refresh=False):
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
        self._core.event_whengreaterthan_timer(value, generator_function, name='', no_refresh=False)
                
    def when_key_pressed(self, key, generator_function, name='', no_refresh=False):
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
        self._core.event_whenkeypressed(key, generator_function, name='', no_refresh=False)
                
    def when_this_sprite_clicked(self, generator_function, name='', no_refresh=False):
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
        self._core.event_whenthisspriteclicked(generator_function, name='', no_refresh=False)
                
    def backdrop_name(self):
        """backdrop name

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.looks_backdropnumbername_name()
                
    def backdrop_number(self):
        """backdrop number

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.looks_backdropnumbername_number()
                
    def change_brightness_effect_by(self, value):
        """change brightness effect by %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        self._core.looks_changeeffectby_brightness(value)
                
    def change_color_effect_by(self, value):
        """change color effect by %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        self._core.looks_changeeffectby_color(value)
                
    def change_fisheye_effect_by(self, value):
        """change fisheye effect by %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        self._core.looks_changeeffectby_fisheye(value)
                
    def change_ghost_effect_by(self, value):
        """change ghost effect by %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        self._core.looks_changeeffectby_ghost(value)
                
    def change_mosaic_effect_by(self, value):
        """change mosaic effect by %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        self._core.looks_changeeffectby_mosaic(value)
                
    def change_pixelate_effect_by(self, value):
        """change pixelate effect by %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        self._core.looks_changeeffectby_pixelate(value)
                
    def change_whirl_effect_by(self, value):
        """change whirl effect by %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        self._core.looks_changeeffectby_whirl(value)
                
    def change_size_by(self, percent):
        """change size by %1

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        percent : FILL
        

        Returns
        -------

        """
        self._core.looks_changesizeby(percent)
                
    def clear_graphic_effects(self):
        """clear graphic effects

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.looks_cleargraphiceffects()
                
    def costume_name(self):
        """costume name

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.looks_costumenumbername_name()
                
    def costume_number(self):
        """costume number

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.looks_costumenumbername_number()
                
    def go_backward(self, value):
        """go backward %2 layers

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        self._core.looks_goforwardbackwardlayers_backward(value)
                
    def go_forward(self, value):
        """go forward %2 layers

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        self._core.looks_goforwardbackwardlayers_forward(value)
                
    def go_to_back_layer(self):
        """go to back layer

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.looks_gotofrontback_back()
                
    def go_to_front_layer(self):
        """go to front layer

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.looks_gotofrontback_front()
                
    def hide(self):
        """hide

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.looks_hide()
                
    def next_backdrop(self):
        """next backdrop

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.looks_nextbackdrop()
                
    def next_costume(self):
        """next costume

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.looks_nextcostume()
                
    def say(self, text):
        """say %1

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        text : FILL
        

        Returns
        -------

        """
        self._core.looks_say(text)
                
    def say_for_seconds(self, text, secs):
        """say %1 for %2 seconds

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        text : FILL
        secs : FILL
        

        Returns
        -------

        """
        self._core.looks_sayforsecs(text, secs)
                
    def set_brightness_effect_to(self, value):
        """set brightness effect to %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        self._core.looks_seteffectto_brightness(value)
                
    def set_color_effect_to(self, value):
        """set color effect to %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        self._core.looks_seteffectto_color(value)
                
    def set_fisheye_effect_to(self, value):
        """set fisheye effect to %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        self._core.looks_seteffectto_fisheye(value)
                
    def set_ghost_effect_to(self, value):
        """set ghost effect to %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        self._core.looks_seteffectto_ghost(value)
                
    def set_mosaic_effect_to(self, value):
        """set mosaic effect to %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        self._core.looks_seteffectto_mosaic(value)
                
    def set_pixelate_effect_to(self, value):
        """set pixelate effect to %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        self._core.looks_seteffectto_pixelate(value)
                
    def set_whirl_effect_to(self, value):
        """set whirl effect to %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        self._core.looks_seteffectto_whirl(value)
                
    def set_size_to(self, percent):
        """set size to %1 %

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        percent : FILL
        

        Returns
        -------

        """
        self._core.looks_setsizeto(percent)
                
    def show(self):
        """show

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.looks_show()
                
    def size(self):
        """size

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.looks_size()
                
    def switch_backdrop_to(self, backdrop):
        """switch backdrop to %1

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        backdrop : FILL
        

        Returns
        -------

        """
        self._core.looks_switchbackdropto(backdrop)
                
    def switch_costume_to(self, costume):
        """switch costume to %1

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        costume : FILL
        

        Returns
        -------

        """
        self._core.looks_switchcostumeto(costume)
                
    def think(self, text):
        """think %1

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        text : FILL
        

        Returns
        -------

        """
        self._core.looks_think(text)
                
    def think_for_seconds(self, text, secs):
        """think %1 for %2 seconds

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        text : FILL
        secs : FILL
        

        Returns
        -------

        """
        self._core.looks_thinkforsecs(text, secs)
                
    def change_x_by(self, value):
        """change x by %1

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        self._core.motion_changexby(value)
                
    def change_y_by(self, value):
        """change y by %1

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        self._core.motion_changeyby(value)
                
    def direction(self):
        """direction

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.motion_direction()
                
    def glide_to_x_y(self, secs, x, y):
        """glide %1 secs to x: %2 y: %3

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        secs : FILL
        x : FILL
        y : FILL
        

        Returns
        -------

        """
        self._core.motion_glidesecstoxy(secs, x, y)
                
    def glide_to_mouse_pointer(self, secs):
        """glide %1 secs to mouse-pointer

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        secs : FILL
        

        Returns
        -------

        """
        self._core.motion_glideto_pointer(secs)
                
    def glide_to_random_position(self, secs):
        """glide %1 secs to random position

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        secs : FILL
        

        Returns
        -------

        """
        self._core.motion_glideto_random(secs)
                
    def glide_to_sprite(self, secs, sprite):
        """glide %1 secs to %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        secs : FILL
        sprite : FILL
        

        Returns
        -------

        """
        self._core.motion_glideto_sprite(secs, sprite)
                
    def go_to_mouse_pointer(self):
        """go to mouse-pointer

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.motion_goto_pointer()
                
    def go_to_random_position(self):
        """go to random position

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.motion_goto_random()
                
    def go_to_sprite(self, sprite):
        """go to %1

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite : FILL
        

        Returns
        -------

        """
        self._core.motion_goto_sprite(sprite)
                
    def go_to_x_y(self, x, y):
        """go to x: %1 y: %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        x : FILL
        y : FILL
        

        Returns
        -------

        """
        self._core.motion_gotoxy(x, y)
                
    def if_on_edge_bounce(self):
        """if on edge, bounce

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.motion_ifonedgebounce()
                
    def move(self, steps):
        """move %1 steps

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        steps : FILL
        

        Returns
        -------

        """
        self._core.motion_movesteps(steps)
                
    def point_in_direction(self, direction):
        """point in direction %1

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        direction : FILL
        

        Returns
        -------

        """
        self._core.motion_pointindirection(direction)
                
    def point_towards_mouse_pointer(self):
        """point towards mouse-pointer

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.motion_pointtowards_pointer()
                
    def point_towards_sprite(self, sprite):
        """point towards %1

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite : FILL
        

        Returns
        -------

        """
        self._core.motion_pointtowards_sprite(sprite)
                

    def set_rotation_style_none(self):
        """set rotation style %1

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        """
        self._core.motion_setrotationstyle_dontrotate()
                
    def set_rotation_style_left_right(self):
        """set rotation style %1

        Engl. Translation for your reference: ...
        Engl. Documentation when available...


        """
        self._core.motion_setrotationstyle_leftright()


    def set_rotation_style_around(self):
        """set rotation style %1

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        """
        self._core.motion_setrotationstyle_allaround()


    def set_x(self, value):
        """set x to %1

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        self._core.motion_setx(value)
                
    def set_y(self, value):
        """set y to %1

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        self._core.motion_sety(value)
                
    def turn_left(self, deg):
        """turn left %2 degrees

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        deg : FILL
        

        Returns
        -------

        """
        self._core.motion_turnleft(deg)
                
    def turn_right(self, deg):
        """turn right %2 degrees

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        deg : FILL
        

        Returns
        -------

        """
        self._core.motion_turnright(deg)
                
    def x_position(self):
        """x position

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.motion_xposition()
                
    def y_position(self):
        """y position

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.motion_yposition()
                
    def calculate(self, operator, number):
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
        self._core.operator_mathop(operator, number)
                
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
        self._core.operator_random(start, end)
                
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
        self._core.pen_changePenColorParamBy_brightness(value)
                
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
        self._core.pen_changePenColorParamBy_color(value)
                
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
        self._core.pen_changePenColorParamBy_saturation(value)
                
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
        self._core.pen_changePenColorParamBy_transparency(value)
                
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
        self._core.pen_changePenSizeBy(value)
                
    def erase_all(self):
        """erase all

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.pen_clear()
                
    def pen_down(self):
        """pen down

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.pen_penDown()
                
    def pen_up(self):
        """pen up

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.pen_penUp()
                
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
        self._core.pen_setPenColorParamTo_brightness(value)
                
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
        self._core.pen_setPenColorParamTo_color(value)
                
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
        self._core.pen_setPenColorParamTo_saturation(value)
                
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
        self._core.pen_setPenColorParamTo_transparency(value)
                
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
        self._core.pen_setPenColorToColor(color)
                
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
        self._core.pen_setPenSizeTo(value)
                
    def stamp(self):
        """stamp

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.pen_stamp()
                
    def add_costume(self, name, center_x=None, center_y=None):
        """

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        name : FILL
        center_x : FILL
        center_y : FILL
        

        Returns
        -------

        """
        self._core.pystage_addcostume(name, center_x=None, center_y=None)
                
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
        self._core.pystage_addsound(name)
                
    def insert_costume(self, index, name, center_x=None, center_y=None):
        """

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        index : FILL
        name : FILL
        center_x : FILL
        center_y : FILL
        

        Returns
        -------

        """
        self._core.pystage_insertcostume(index, name, center_x=None, center_y=None)
                
    def create_variable(self, name, all_sprites=True):
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
        self._core.pystage_makevariable(name, all_sprites=True)
                
    def replace_costume(self, index, name, center_x=None, center_y=None):
        """

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        index : FILL
        name : FILL
        center_x : FILL
        center_y : FILL
        

        Returns
        -------

        """
        self._core.pystage_replacecostume(index, name, center_x=None, center_y=None)
                
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
        self._core.pystage_setmonitorposition(name, x, y)
                
    def answer(self):
        """answer

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_answer()
                
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
        self._core.sensing_askandwait(question)
                
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
        self._core.sensing_coloristouchingcolor(sprite_color, color)
                
    def current_date(self):
        """current date

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_current_date()
                
    def current_day_of_week(self):
        """current day of week

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_current_dayofweek()
                
    def current_hour(self):
        """current hour

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_current_hour()
                
    def current_minute(self):
        """current minute

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_current_minute()
                
    def current_month(self):
        """current month

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_current_month()
                
    def current_second(self):
        """current second

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_current_second()
                
    def current_year(self):
        """current year

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_current_year()
                
    def days_since(self):
        """days since 2000

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_dayssince2000()
                
    def distance_to_mouse_pointer(self):
        """distance to mouse-pointer

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_distanceto_pointer()
                
    def distance_to_sprite(self, sprite):
        """distance to %1

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_distanceto_sprite(sprite)
                
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
        self._core.sensing_keypressed(key)
                
    def loudness(self):
        """loudness

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_loudness()
                
    def mouse_down(self):
        """mouse down?

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_mousedown()
                
    def mouse_x(self):
        """mouse x

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_mousex()
                
    def mouse_y(self):
        """mouse y

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_mousey()
                
    def backdrop_name_of(self, stage='_stage_'):
        """backdrop name of %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        stage : FILL
        

        Returns
        -------

        """
        self._core.sensing_of_backdropname(stage='_stage_')
                
    def backdrop_of(self, stage='_stage_'):
        """backdrop # of %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        stage : FILL
        

        Returns
        -------

        """
        self._core.sensing_of_backdropnumber(stage='_stage_')
                
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
        self._core.sensing_of_costumename(sprite)
                
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
        self._core.sensing_of_costumenumber(sprite)
                
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
        self._core.sensing_of_direction(sprite)
                
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
        self._core.sensing_of_size(sprite)
                
    def get_variable_of(self, variable, sprite='_stage_'):
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
        self._core.sensing_of_variable(variable, sprite='_stage_')
                
    def volume_of(self, sprite='_stage_'):
        """volume of %2

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        sprite : FILL
        

        Returns
        -------

        """
        self._core.sensing_of_volume(sprite='_stage_')
                
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
        self._core.sensing_of_xposition(sprite)
                
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
        self._core.sensing_of_yposition(sprite)
                
    def reset_timer(self):
        """reset timer

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_resettimer()
                
    def set_drag_mode_draggable(self):
        """set drag mode draggable

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_setdragmode_draggable()
                
    def set_drag_mode_not_draggable(self):
        """set drag mode not draggable

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_setdragmode_notdraggable()
                
    def timer(self):
        """timer

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_timer()
                
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
        self._core.sensing_touchingcolor(color)
                
    def touching_edge(self):
        """touching edge?

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_touchingobject_edge()
                
    def touching_mouse_pointer(self):
        """touching mouse-pointer?

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_touchingobject_pointer()
                
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
        self._core.sensing_touchingobject_sprite(sprite)
                
    def username(self):
        """username

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_username()
                
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
        self._core.sound_changeeffectby_pan(value)
                
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
        self._core.sound_changeeffectby_pitch(value)
                
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
        self._core.sound_changevolumeby(value)
                
    def clear_sound_effects(self):
        """clear sound effects

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sound_cleareffects()
                
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
        self._core.sound_play(name, loop=0)
                
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
        self._core.sound_playuntildone(name)
                
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
        self._core.sound_seteffectto_pan(value)
                
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
        self._core.sound_seteffectto_pitch(value)
                
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
        self._core.sound_setvolumeto(value)
                
    def stop_all_sounds(self):
        """stop all sounds

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sound_stopallsounds()
                
    def volume(self):
        """volume

        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sound_volume()
                
