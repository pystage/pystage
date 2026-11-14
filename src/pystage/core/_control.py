import pygame

from pystage.core._base_sprite import BaseSprite

class _Control(BaseSprite):

    def __init__(self):
        super().__init__()

    def control_wait(self, secs):
        self.code_manager.current_block.add_to_wait_time = secs

    def control_stop_all(self):
        # Like the stop sign in Scratch: all scripts and sounds stop,
        # clones and speech bubbles are removed.
        for s in list(self.stage.sprites):
            s.code_manager.stop_running_blocks()
            s.bubble_manager.kill()
            if s.is_clone:
                s.control_delete_this_clone()
        self.stage.code_manager.stop_running_blocks()
        self.stage.input_manager.cancel_asking()
        self.stage.sound_stopallsounds()

    control_stop_all.opcode="control_stop"
    control_stop_all.param="STOP_OPTION"
    control_stop_all.value="all"

    def control_stop_this(self):
        self.code_manager.current_block.stop()

    control_stop_this.opcode="control_stop"
    control_stop_this.param="STOP_OPTION"
    control_stop_this.value="this script"

    def control_stop_other(self):
        current = self.code_manager.current_block
        for block in self.code_manager.code_blocks.values():
            if block is not current:
                block.stop()

    control_stop_other.opcode="control_stop"
    control_stop_other.param="STOP_OPTION"
    control_stop_other.value="other scripts in sprite"

    def control_create_clone_of_sprite(self, sprite):
        if sprite == "_myself_":
            sprite = self
        self.stage._get_sprite(sprite).clone()

    control_create_clone_of_sprite.opcode = "control_create_clone_of"


class _ControlSprite(_Control):

    # In Scratch, there can only be a maximum of 300 clones
    MAX_CLONES = 300

    def __init__(self):
        super().__init__()

    def control_create_clone_of_myself(self):
        self.clone()

    control_create_clone_of_myself.opcode="control_create_clone_of"
    control_create_clone_of_myself.param="CLONE_OPTION"
    control_create_clone_of_myself.value="_myself_"

    def control_delete_this_clone(self):
        if not self.is_clone:
            return
        self.code_manager.stop_running_blocks()
        self.bubble_manager.kill()
        self.kill()
        self.stage._update_visible()
    control_delete_this_clone.translation = "control_deletethisclone"


    # This is actually an event but Scratch has the hat block under "Control"
    def control_start_as_clone(self, generator_function, name="", no_refresh=False):
        '''
        Adds the code block to the event queue for new clones.
        '''
        new_block = self.code_manager.register_code_block(generator_function, name, no_refresh)
        self.code_manager.cloned_blocks.append(new_block)
    control_start_as_clone.translation = "control_startasclone"

    def clone(self):
        if len([s for s in self.stage.sprites if s.is_clone]) >= _ControlSprite.MAX_CLONES:
            return
        clone = self.stage._create_core_sprite(None)
        clone.is_clone = True
        clone.name = self.name
        # The clone appears directly behind the original
        self.stage.sprites.move_to(clone, self.stage.sprites.get_layer(self))
        cloned_attributes = [
            # Motion
            "_direction", "draggable",
            # Pen
            "pen", "pen_size",
            # Looks
            "size", "visible",
            "ghost", "color", "fisheye", "whirl", "pixelate", "mosaic", "brightness",
            # Sound, the sounds itself are shared
            "sound_manager", "current_pan", "current_pitch", "current_volume",
            ]
        for attr in cloned_attributes:
            setattr(clone, attr, getattr(self, attr))
        clone.pen_color = pygame.Color(self.pen_color)
        clone._pos.update(self._pos)
        # clones have own variables and lists
        clone.variables = self.variables.copy()
        clone.list_variables = {name: list(values) for name, values in self.list_variables.items()}
        # But only the original variable can be monitored.
        # However, monitors can be shown and hidden, so we need access
        clone.var_monitors = self.var_monitors
        clone.list_monitors = self.list_monitors

        # Costumes are shared
        clone.costume_manager.costumes = self.costume_manager.costumes
        clone.costume_manager.current_costume = self.costume_manager.current_costume
        clone.costume_manager.rotation_style = self.costume_manager.rotation_style
        clone.costume_manager.update_sprite_image()
        self.stage._update_visible()

        # Code
        clone.code_manager = self.code_manager.clone(clone)
        for code_block in clone.code_manager.cloned_blocks:
            code_block.start_or_restart()
