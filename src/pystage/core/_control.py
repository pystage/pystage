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

    def control_stop_this(self):
        # This is equivalent to return
        pass
    control_stop_this.opcode="control_stop"
    control_stop_this.param="STOP_OPTION"
    control_stop_this.value="this script"

    def control_stop_other(self):
        pass
    control_stop_other.opcode="control_stop"
    control_stop_other.param="STOP_OPTION"
    control_stop_other.value="other scripts in sprite"

    # Cloning is probably tricky.  

    def control_create_clone_of(self, sprite="_myself_"):
        pass

    control_create_clone_of.translation = "control_createcloneof"


