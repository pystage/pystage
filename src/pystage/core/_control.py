from pystage.core._base_sprite import BaseSprite

class _Control(BaseSprite):

    def __init__(self):
        super().__init__()

    def control_wait(self, secs):
        self.code_manager.current_block.add_to_wait_time = secs

    def control_stop_all(self):
        for s in self.stage.sprites:
            s.code_manager.stop_running_blocks()
        self.stage.code_manager.stop_running_blocks()

    control_stop_all.opcode="control_stop"
    control_stop_all.param="STOP_OPTION"
    control_stop_all.value="all"

    def control_stop_this(self):
        self.code_manager.stop_running_blocks()

    control_stop_this.opcode="control_stop"
    control_stop_this.param="STOP_OPTION"
    control_stop_this.value="this script"

    def control_stop_other(self):
        for s in self.stage.sprites:
            if s is not self:
                s.code_manager.stop_running_blocks()
        self.stage.code_manager.stop_running_blocks()

    control_stop_other.opcode="control_stop"
    control_stop_other.param="STOP_OPTION"
    control_stop_other.value="other scripts in sprite"

    # Cloning is probably tricky.  

    def control_create_clone_of(self, sprite="_myself_"):
        pass

    control_create_clone_of.translation = "control_createcloneof"


class _ControlSprite(_Control):

    def __init__(self):
        super().__init__()


    def control_delete_this_clone(self):
        pass
    control_delete_this_clone.translation = "control_deletethisclone"


    # This is actually an event but Scratch has the hat block under "Control"
    def control_start_as_clone(self, generator_function, name="", no_refresh=False):
        pass
    control_start_as_clone.translation = "control_startasclone"

