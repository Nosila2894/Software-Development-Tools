from abc import ABC, abstractmethod
    
class BaseState(ABC):


    def __init__(self, state_manager):
        self.state_manager = state_manager
        self.user_interface = None
        self.data = state_manager.data
        self.event_handler = state_manager.event_handler

        self.event_registry = {}
        self.register_action("RETURN_TO_LAST_STATE", self.cb_return_to_last_state)

        self.key_bindings = {}

    def register_action(self, action, callback):
        self.event_registry[action] = callback

    @abstractmethod
    def handle_inputs(self):
        pass

    def on_enter(self):
        pass

    def on_exit(self):
        pass

    def update(self):
        events = self.event_handler.extract_all_events()

        for event in events:
            if event.action in self.event_registry:
                callback = self.event_registry[event.action]
                callback(event.action_data)

    @abstractmethod
    def _build_dynamic_action(self, action, input_value):
        pass

    @abstractmethod
    def render(self):
        pass
    
    def cb_return_to_last_state(self, action_data):
        self.state_manager.pop_state()




