from pystage.core.constants import KEY_MAPPINGS
from pystage.core.code_block import _message_key
from pystage.core._base_sprite import BaseSprite


class _Events(BaseSprite):

    def __init__(self):
        super().__init__()
    ##
    # Events
    #

    def event_whenflagclicked(self, generator_function, name="", no_refresh=False):
        new_block = self.code_manager.register_code_block(generator_function, name, no_refresh)
        new_block.start_or_restart()


    def event_whenkeypressed(self, key, generator_function, name="", no_refresh=False):
        '''
        Adds the code block to the event queue for key presses.
        '''
        key = str(key).lower()
        if key != "any" and key not in KEY_MAPPINGS:
            raise ValueError(f"Bad key: {key}. Allowed are a-z, 0-9, space, enter, the arrow keys (e.g. 'left arrow') and any.")
        new_block = self.code_manager.register_code_block(generator_function, name, no_refresh)
        if key == "any":
            self.code_manager.any_key_blocks.append(new_block)
            return
        pg_key = KEY_MAPPINGS[key]
        # No defaultdict so that we can easily check if a key mapping is available
        if pg_key not in self.code_manager.key_pressed_blocks:
            self.code_manager.key_pressed_blocks[pg_key] = []
        self.code_manager.key_pressed_blocks[pg_key].append(new_block.name)


    def event_whenthisspriteclicked(self, generator_function, name="", no_refresh=False):
        '''
        Adds the code block to the event queue for clicks.
        '''
        new_block = self.code_manager.register_code_block(generator_function, name, no_refresh)
        self.code_manager.clicked_blocks.append(new_block)


    def event_whenbackdropswitchesto(self, backdrop, generator_function, name="", no_refresh=False):
        '''
        Adds the code block to the event queue for backdrop switches.
        '''
        new_block = self.code_manager.register_code_block(generator_function, name, no_refresh)
        key = str(backdrop).strip().lower()
        self.code_manager.backdrop_blocks.setdefault(key, []).append(new_block)


    def event_whengreaterthan_loudness(self, value, generator_function, name="", no_refresh=False):
        # There is no microphone access, so the loudness is always 0
        # and this event never happens.
        # See https://github.com/pystage/pystage/issues/116
        self.code_manager.register_code_block(generator_function, name, no_refresh)
    event_whengreaterthan_loudness.opcode="event_whengreaterthan"
    event_whengreaterthan_loudness.param="WHENGREATERTHANMENU"
    event_whengreaterthan_loudness.value="LOUDNESS"


    def event_whengreaterthan_timer(self, value, generator_function, name="", no_refresh=False):
        '''
        Adds the code block to the event queue for the timer.
        '''
        new_block = self.code_manager.register_code_block(generator_function, name, no_refresh)
        self.code_manager.timer_blocks.append([value, new_block, True])
    event_whengreaterthan_timer.opcode="event_whengreaterthan"
    event_whengreaterthan_timer.param="WHENGREATERTHANMENU"
    event_whengreaterthan_timer.value="TIMER"


    def event_whenbroadcastreceived(self, message, generator_function, name="", no_refresh=False):
        '''
        Adds the code block to the event queue for broadcasts.
        '''
        new_block = self.code_manager.register_code_block(generator_function, name, no_refresh)
        key = _message_key(message)
        # No defaultdict so that we can easily check if a mapping is available
        if key not in self.code_manager.broadcast_blocks:
            self.code_manager.broadcast_blocks[key] = []
        self.code_manager.broadcast_blocks[key].append(new_block.name)


    def event_broadcast(self, message):
        self.stage.message_broker.broadcast(message)


    def event_broadcastandwait(self, message):
        # The receivers are started immediately, this code block
        # continues when all of them are finished.
        current = self.code_manager.current_block
        started = self.stage._broadcast(message)
        current.waiting_for = [block for block in started if block is not current]
