from pystage.core.constants import KEY_MAPPINGS
from pystage.core._base_sprite import BaseSprite


class _Events(BaseSprite):

    def __init__(self):
        super().__init__()
    ##
    # Events
    #

#"",
#"",
#"",
#"",
#"",
#"",
#"",
#"",

    def event_whenflagclicked(self, generator_function, name="", no_refresh=False):
        new_block = self.code_manager.register_code_block(generator_function, name)
        print(f"Bound to start: {new_block.name}")
        new_block.start_or_restart()


    def event_whenkeypressed(self, key, generator_function, name="", no_refresh=False):
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


    def event_whenthisspriteclicked(self, generator_function, name="", no_refresh=False):
        pass


    def event_whenbackdropswitchesto(self, backdrop, generator_function, name="", no_refresh=False):
        pass

    def event_whengreaterthan_loudness(self, value, generator_function, name="", no_refresh=False):
        # Not sure if this can/should be implemented, requires microphone access.
        pass
    event_whengreaterthan_loudness.opcode="event_whengreaterthan"
    event_whengreaterthan_loudness.param="WHENGREATERTHANMENU"
    event_whengreaterthan_loudness.value="LOUDNESS"

    def event_whengreaterthan_timer(self, value, generator_function, name="", no_refresh=False):
        # Scratch has a timer that can be reset. 
        pass
    event_whengreaterthan_timer.opcode="event_whengreaterthan"
    event_whengreaterthan_timer.param="WHENGREATERTHANMENU"
    event_whengreaterthan_timer.value="TIMER"

    def event_whenbroadcastreceived(self, message, generator_function, name="", no_refresh=False):
        pass

    def event_broadcast(self, message):
        pass

    def event_broadcastandwait(self, message):
        # waits until all receiver scripts finish. Tricky.
        pass

