
from pystage.core.stage import CoreStage
from pystage.en.sprite import Sprite


class Stage():

    def __init__(self):
        self._core = CoreStage()
        self._core.facade = self
        self._core.sprite_facade_class = Sprite

    def add_a_sprite(self, costume="default"):
        return self._core.pystage_createsprite(costume=costume)

    def play(self):
        self._core.pystage_play()
        
            
    def create_clone_of(self, sprite='_myself_'):
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
        self._core.control_create_clone_of(sprite='_my_')
                
    def stop_all(self):
        """stop all

        Translation string: stop all
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.control_stop_all()
                
    def stop_other_scripts_in_sprite(self):
        """stop other scripts in sprite

        Translation string: stop other scripts in sprite
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.control_stop_other()
                
    def stop_this_script(self):
        """stop this script

        Translation string: stop this script
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.control_stop_this()
                
    def wait_seconds(self, secs):
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
        self._core.control_wait(secs)
                
    def broadcast(self, message):
        """broadcast %1

        Translation string: broadcast %1
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

        Translation string: broadcast %1 and wait
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

        Translation string: when backdrop switches to %1
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
                
    def when_i_receive(self, message, generator_function, name='', no_refresh=False):
        """when I receive %1

        Translation string: when I receive %1
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
                
    def when_GREENFLAG_clicked(self, generator_function, name='', no_refresh=False):
        """when <greenflag> clicked

        Translation string: when <greenflag> clicked
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
                
    def when_loudness_GREATERTHAN(self, value, generator_function, name='', no_refresh=False):
        """when loudness <greater> %2

        Translation string: when loudness <greater> %2
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
                
    def when_timer_GREATERTHAN(self, value, generator_function, name='', no_refresh=False):
        """when timer <greater> %2

        Translation string: when timer <greater> %2
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

        Translation string: when %1 key pressed
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

        Translation string: when this sprite clicked
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

        Translation string: backdrop name
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.looks_backdropnumbername_name()
                
    def backdrop_number(self):
        """backdrop number

        Translation string: backdrop number
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.looks_backdropnumbername_number()
                
    def change_brightness_effect_by(self, value):
        """change brightness effect by %2

        Translation string: change brightness effect by %2
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

        Translation string: change color effect by %2
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

        Translation string: change fisheye effect by %2
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

        Translation string: change ghost effect by %2
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

        Translation string: change mosaic effect by %2
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

        Translation string: change pixelate effect by %2
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

        Translation string: change whirl effect by %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        self._core.looks_changeeffectby_whirl(value)
                
    def clear_graphic_effects(self):
        """clear graphic effects

        Translation string: clear graphic effects
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.looks_cleargraphiceffects()
                
    def next_backdrop(self):
        """next backdrop

        Translation string: next backdrop
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.looks_nextbackdrop()
                
    def set_brightness_effect_to(self, value):
        """set brightness effect to %2

        Translation string: set brightness effect to %2
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

        Translation string: set color effect to %2
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

        Translation string: set fisheye effect to %2
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

        Translation string: set ghost effect to %2
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

        Translation string: set mosaic effect to %2
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

        Translation string: set pixelate effect to %2
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

        Translation string: set whirl effect to %2
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        value : FILL
        

        Returns
        -------

        """
        self._core.looks_seteffectto_whirl(value)
                
    def switch_backdrop_to(self, backdrop):
        """switch backdrop to %1

        Translation string: switch backdrop to %1
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        backdrop : FILL
        

        Returns
        -------

        """
        self._core.looks_switchbackdropto(backdrop)
                
    def switch_backdrop_to_and_wait(self, backdrop):
        """switch backdrop to %1 and wait

        Translation string: switch backdrop to %1 and wait
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        backdrop : FILL
        

        Returns
        -------

        """
        self._core.looks_switchbackdroptoandwait(backdrop)
                
    def of(self, operator, number):
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
        self._core.operator_mathop(operator, number)
                
    def pick_random_to(self, start, end):
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
        self._core.operator_random(start, end)
                
    def pystage_addbackdrop(self, name, center_x=None, center_y=None):
        """

        Translation string: 
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
        self._core.pystage_addbackdrop(name, center_x=None, center_y=None)
                
    def pystage_addsound(self, name):
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
        self._core.pystage_addsound(name)
                
    def pystage_createsprite(self, costume='default'):
        """

        Translation string: 
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        
        Parameters
        ----------
        costume : FILL
        

        Returns
        -------

        """
        self._core.pystage_createsprite(costume='default')
                
    def pystage_insertbackdrop(self, index, name, center_x=None, center_y=None):
        """

        Translation string: 
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
        self._core.pystage_insertbackdrop(index, name, center_x=None, center_y=None)
                
    def pystage_play(self):
        """

        Translation string: 
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.pystage_play()
                
    def pystage_replacebackdrop(self, index, name, center_x=None, center_y=None):
        """

        Translation string: 
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
        self._core.pystage_replacebackdrop(index, name, center_x=None, center_y=None)
                
    def answer(self):
        """answer

        Translation string: answer
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_answer()
                
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
        self._core.sensing_askandwait(question)
                
    def current_date(self):
        """current date

        Translation string: current date
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_current_date()
                
    def current_day_of_week(self):
        """current day of week

        Translation string: current day of week
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_current_dayofweek()
                
    def current_hour(self):
        """current hour

        Translation string: current hour
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_current_hour()
                
    def current_minute(self):
        """current minute

        Translation string: current minute
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_current_minute()
                
    def current_month(self):
        """current month

        Translation string: current month
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_current_month()
                
    def current_second(self):
        """current second

        Translation string: current second
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_current_second()
                
    def current_year(self):
        """current year

        Translation string: current year
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_current_year()
                
    def days_since(self):
        """days since 2000

        Translation string: days since 2000
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_dayssince2000()
                
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
        self._core.sensing_keypressed(key)
                
    def loudness(self):
        """loudness

        Translation string: loudness
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_loudness()
                
    def mouse_down(self):
        """mouse down?

        Translation string: mouse down?
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_mousedown()
                
    def mouse_x(self):
        """mouse x

        Translation string: mouse x
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_mousex()
                
    def mouse_y(self):
        """mouse y

        Translation string: mouse y
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_mousey()
                
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
        self._core.sensing_of_backdropname(stage='_stage_')
                
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
        self._core.sensing_of_backdropnumber(stage='_stage_')
                
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
        self._core.sensing_of_costumename(sprite)
                
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
        self._core.sensing_of_costumenumber(sprite)
                
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
        self._core.sensing_of_direction(sprite)
                
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
        self._core.sensing_of_size(sprite)
                
    def of(self, variable, sprite='_stage_'):
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
        self._core.sensing_of_variable(variable, sprite='_stage_')
                
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
        self._core.sensing_of_volume(sprite='_stage_')
                
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
        self._core.sensing_of_xposition(sprite)
                
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
        self._core.sensing_of_yposition(sprite)
                
    def reset_timer(self):
        """reset timer

        Translation string: reset timer
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_resettimer()
                
    def set_drag_mode_draggable(self):
        """set drag mode draggable

        Translation string: set drag mode draggable
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_setdragmode_draggable()
                
    def set_drag_mode_not_draggable(self):
        """set drag mode not draggable

        Translation string: set drag mode not draggable
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_setdragmode_notdraggable()
                
    def timer(self):
        """timer

        Translation string: timer
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_timer()
                
    def username(self):
        """username

        Translation string: username
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sensing_username()
                
    def change_pan_left_right_effect_by(self, value):
        """change pan left/right effect by %2

        Translation string: change pan left/right effect by %2
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

        Translation string: change pitch effect by %2
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

        Translation string: change volume by %1
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

        Translation string: clear sound effects
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sound_cleareffects()
                
    def start_sound(self, name, loop=0):
        """start sound %1

        Translation string: start sound %1
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

        Translation string: play sound %1 until done
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

        Translation string: set pan left/right effect to %2
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

        Translation string: set pitch effect to %2
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

        Translation string: set volume to %1%
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

        Translation string: stop all sounds
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sound_stopallsounds()
                
    def volume(self):
        """volume

        Translation string: volume
        Engl. Translation for your reference: ...
        Engl. Documentation when available...

        

        Returns
        -------

        """
        self._core.sound_volume()
                
