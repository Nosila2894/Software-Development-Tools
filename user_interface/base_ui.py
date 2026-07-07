from abc import ABC, abstractmethod

class BaseUI(ABC):
    def __init__(self, state):
        self.state = state
        self.data = state.data
        self.event_handler = state.event_handler
    
    @abstractmethod
    def handle_input(self):
        pass

    @abstractmethod
    def render(self):
        pass


