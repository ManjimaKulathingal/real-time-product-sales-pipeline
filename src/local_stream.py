from queue import Queue


class LocalStream:
    def __init__(self):
        self.events = Queue()

    def put_event(self, event):
        self.events.put(event)

    def get_event(self):
        return self.events.get()

    def size(self):
        return self.events.qsize()