from counter import Counter, CounterEvent

counter = Counter()

def counter_started_handler(event):
    print(event)
    # print(f"{event.type} count: {event.count} count_from_sender: {event.sender.count}")


def counter_changed_handler(event):
    print(event)
    # print(f"{event.type} count: {event.count} count_from_sender: {event.sender.count}")

def counter_finished_handler(event):
    print(event)
    # print(f"{event.type} count: {event.count} count_from_sender: {event.sender.count}")


counter.eventDispatcher.add_listener(CounterEvent.COUNTER_STARTED, counter_started_handler)
counter.eventDispatcher.add_listener(CounterEvent.COUNTER_CHANGED, counter_changed_handler)
counter.eventDispatcher.add_listener(CounterEvent.COUNTER_FINISHED, counter_finished_handler)

# counter.eventDispatcher.remove_listener(CounterEvent.COUNTER_CHANGED, counter_changed_handler)

print(id(counter.eventDispatcher.listeners_copy))
print(id(counter.eventDispatcher._listeners))
print(counter.eventDispatcher)
counter.run()
