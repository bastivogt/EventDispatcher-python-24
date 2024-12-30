from sevo.events import Event, EventDispatcher

class CounterEvent(Event):
    COUNTER_STARTED = "COUNTER_STARTED"
    COUNTER_CHANGED = "COUNTER_CHANGED"
    COUNTER_FINISHED = "COUNTER_FINISHED"

    def __init__(self, type, sender, count):
        super().__init__(type, sender)
        self._count = count
    
    @property
    def count(self):
        return self._count
    
    def __repr__(self):
        return f"CounterEvent(type={self._type}, sender={self._sender}, count={self._count})"
    


class Counter():
    def __init__(self, start=0, stop=10, step=1):
        self.reset(start, stop, step)
        self._eventDispatcher = EventDispatcher.initialize()

    def reset(self, start=0, stop=10, step=1):
        self._start = start
        self._stop = stop
        self._step = step
        self._count = self._start

    @property
    def eventDispatcher(self):
        return self._eventDispatcher

    
    @property
    def count(self):
        return self._count
    

    def run(self):
        self._count = self._start
        self._eventDispatcher.dispatch_event(CounterEvent(CounterEvent.COUNTER_STARTED, self, self._count))
        for self._count in range(self._start, self._stop, self._step):
            self._eventDispatcher.dispatch_event(CounterEvent(CounterEvent.COUNTER_CHANGED, self, self._count))
        self._eventDispatcher.dispatch_event(CounterEvent(CounterEvent.COUNTER_FINISHED, self, self._count))

    def __repr__(self):
        return f"Counter(start={self._start}, stop={self._stop}, step={self._step}, count={self._count})"
    
    def __str__(self):
        return self.__repr__()