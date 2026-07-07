from .state_manager import StateManager
from .event_handler import EventHandler


class Engine():
    def __init__(self, data):
        self.running = False
        self.data = data
        self.event_handler = EventHandler()
        self.state_manager = StateManager(data=self.data,
                                         event_handler=self.event_handler)


    def handle_inputs(self):
        self.state_manager.handle_inputs()
    
    def update(self):
        self.state_manager.update()

    def render(self):
        self.state_manager.render()

    def run(self):
        self.running = True
        self.state_manager.render();
        while self.running:
            if not self.state_manager.states:
                self.running = False
            self.handle_inputs()
            self.update()
            self.render()

    def register_state(self, state_name, state_class):
        self.state_manager.register_state(state_name, state_class)

    def set_start_state(self, state_name, *args, **kwargs):
        self.state_manager.push_state(state_name, *args, **kwargs)