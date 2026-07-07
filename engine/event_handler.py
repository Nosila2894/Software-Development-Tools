from collections import deque

class EventHandler():
    def __init__(self):
        self._queue = deque()

    def push_event(self, action):
        self._queue.append(action)

    def pop_event(self):
        if self._queue:
            return self._queue.popleft()
        return None

    def has_events(self):
        return bool(self._queue)
    
    def clear_events(self):
        self._queue.clear()

    def extract_all_events(self):
        events = list(self._queue)
        self.clear_events()
        return events




