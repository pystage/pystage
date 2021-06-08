from pystage.core.constants import KEY_MAPPINGS
from pystage.core.code_block import CodeBlock, CodeManager


class _Events():

    def __init__(self):
        super().__init__()
        self.code_manager = CodeManager(self)
    ##
    # Events
    #

    def when_program_is_started(self, generator_function, name="", no_refresh=False):
        new_block = self.code_manager.register_code_block(generator_function, name)
        print(f"Bound to start: {new_block.name}")
        new_block.start_or_restart()


    def when_key_is_pressed(self, key, generator_function, name="", no_refresh=False):
        '''
        Adds the code block to the event queue for key presses.
        '''
        new_block = self.code_manager.register_code_block(generator_function, name, no_refresh)
        if key not in KEY_MAPPINGS:
            # TODO: implement "any" key.
            raise ValueError(f"Bad key: {key}. Only a-z, 0-9 and space are allowed.")
        pg_key = KEY_MAPPINGS[key]
        # No defaultdict so that we can easily check if a key mapping is available
        if pg_key not in self.code_manager.key_pressed_blocks:
            self.code_manager.key_pressed_blocks[pg_key] = []
        self.code_manager.key_pressed_blocks[pg_key].append(new_block.name)
        print(f"Bound to key press ({key}/{pg_key}): {new_block.name}")


    def when_clicked(self, generator_function, name="", no_refresh=False):
        pass


    def when_backdrop_switches_to(self, backdrop, generator_function, name="", no_refresh=False):
        pass

    def when_loudness_greater_than(self, value, generator_function, name="", no_refresh=False):
        # Not sure if this can/should be implemented, requires microphone access.
        pass

    def when_timer_greater_than(self, value, generator_function, name="", no_refresh=False):
        # Scratch has a timer that can be reset. 
        pass

    def when_i_receive_message(self, message, generator_function, name="", no_refresh=False):
        pass

    def broadcast(self, message):
        pass

    def broadcast_and_wait(self, message):
        # waits until all receiver scripts finish. Tricky.
        pass

