class _Control():
    ##
    # Control
    #

    # Controls obviously should mostly be done in Python
    # or this would be no help in learning python.

    # TODO: document this
    # repeat is for i in range()
    # forever is while True
    # if is if
    # wait until is while COND: yield
    # repeat until is while not

    def wait(self, secs):
        self.code_manager.current_block.add_to_wait_time = secs

    def stop_all(self):
        # not only in this sprite!
        pass

    def stop_this_script(self):
        # This is equivalent to return
        pass

    def stop_other_scripts_in_sprite(self):
        pass

    # Cloning is probably tricky.  

    def create_clone_of_sprite(self, sprite):
        pass

