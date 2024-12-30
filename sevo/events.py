

class Event():
    def __init__(self, type, sender):
        self._type = type
        self._sender = sender
    
    @property
    def type(self):
        return self._type
    
    @property
    def sender(self):
        return self._sender
    
    def __repr__(self):
        return f"Event(type={self._type}, sender={self._sender})"
    
    def __str__(self):
        return self.__repr__()
    


class EventDispatcher():

    @classmethod
    def initialize(cls):
        return cls()
    
    def __init__(self):
        # [{"type": "STARTED", "listener": func}]
        self._listeners = []

    @property
    def listeners_copy(self):
        return list(self._listeners)

    def has_listener(self, type, listener):
        for item in self._listeners:
            if item["type"] == type and item["listener"] == listener:
                return True
        return False
    
    def add_listener(self, type, listener):
        if not self.has_listener(type, listener):
            self._listeners.append({"type": type, "listener": listener})
            return True
        return False
    
    def remove_listener(self, type, listener):
        if self.has_listener(type, listener):
            for item in self._listeners:
                if item["type"] == type:
                    self._listeners.remove(item)
                    return True
        return False
    
    def dispatch_event(self, event):
        for item in self._listeners:
            if item["type"] == event.type:
                item["listener"](event)
                return True
        return False
    
    def __repr__(self):
        return f"EventDispatcher(listeners={self._listeners})"
