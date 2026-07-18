from collections import deque

class EventHandler():
    #Implemented a deque data structure for left hand pops from the queue
    def __init__(self):
        self._queue = deque()
    
    #Provides an interface for the states to load and extract action commands.
    def push_event(self, action):
        self._queue.append(action)

    def pop_event(self):
        if self._queue:
            return self._queue.popleft()
        return None

    # Allow states to verify any pending actions remain in the handler
    def has_events(self):
        return bool(self._queue)
    
    def clear_events(self):
        self._queue.clear()
    
    # Executed during the update function of a state to clear the event handler
    # Allows game logic to update while not clogging the event handler and 
    # Freezing the application
    def extract_all_events(self):
        events = list(self._queue)
        self.clear_events()
        return events




