class MessageBroker():
    """Utility class for message handling.

    The message broker belongs to the stage as central element.
    """

    def __init__(self, stage):
        self.stage = stage
        self._messages = []


    def broadcast(self, message):
        self._messages.append(message)


    def get_messages(self):
        return self._messages


    def mark_completed(self):
        self._messages.clear()
