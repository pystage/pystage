from pystage.core._base_sprite import BaseSprite

class _Control(BaseSprite):

    def __init__(self):
        super().__init__()

    def control_wait(self, secs):
        self.code_manager.current_block.add_to_wait_time = secs

    def control_stop_all(self):
        # not only in this sprite!
        pass
    control_stop_all.opcode="control_stop"
    control_stop_all.param="STOP_OPTION"
    control_stop_all.value="all"

    def control_stop_this_script(self):
        # This is equivalent to return
        pass
    control_stop_this_script.opcode="control_stop"
    control_stop_this_script.param="STOP_OPTION"
    control_stop_this_script.value="this script"

    def control_stop_other_scripts_in_sprite(self):
        pass
    control_stop_other_scripts_in_sprite.opcode="control_stop"
    control_stop_other_scripts_in_sprite.param="STOP_OPTION"
    control_stop_other_scripts_in_sprite.value="other scripts in sprite"

    # Cloning is probably tricky.  

    def control_create_clone_of(self, sprite="_myself_"):
        pass

    def control_delete_this_clone(self):
        pass


    # This is actually an event but Scratch has the hat block under "Control"
    def control_start_as_clone(self, key, generator_function, name="", no_refresh=False):
        pass

