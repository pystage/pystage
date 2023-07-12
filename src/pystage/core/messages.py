class MessageBroker():
    """Utility class for message handling.

    The message broker belongs to the stage as central element.
    """

    def __init__(self, stage):
        self.stage = stage
        self._messages = []
        self.status_checkers = []


    def broadcast(self, message):
        self._messages.append(message)
        self.status_checkers.clear()
        for sprite in self.stage.visible_sprites:
            sprite.code_manager.process_broadcast(message)
            self.status_checkers.append(lambda : sprite.code_manager.broadcast_done(message))
        self.stage.code_manager.process_broadcast(message)
        self.status_checkers.append(lambda : self.stage.code_manager.broadcast_done(message))


    def broadcast_done(self):
        # check if all sprites and the stage have done their broadcast
        return all([checker() for checker in self.status_checkers])


    def get_messages(self):
        return self._messages


    def mark_completed(self):
        self._messages.clear()
