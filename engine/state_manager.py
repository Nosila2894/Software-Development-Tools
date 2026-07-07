class StateManager():
    def __init__(self, data=None, event_handler=None):
        self.data = data
        self.event_handler = event_handler
        self.states = []
        
        self.state_registry = {}

    def register_state(self, state_name, state_class):
        self.state_registry[state_name] = state_class

    def handle_inputs(self):
        if self.states:
            self.states[-1].handle_inputs()

    def update(self):
        if self.states:
            self.states[-1].update()

    def render(self):
        if self.states:
            self.states[-1].render()

    def push_state(self,state, *args, **kwargs):
        if state not in self.state_registry:
            raise ValueError(f"State '{state}' is not registered.")

        if self.states:
            self.states[-1].on_exit()
       
        state_class = self.state_registry[state]
        new_state = state_class(self, *args, **kwargs)
        
        self.states.append(new_state)
        new_state.on_enter()

    def pop_state(self):
        if self.states:
            self.states[-1].on_exit()
            self.states.pop()
        if self.states:
            self.states[-1].on_enter()

    def change_state(self,state, *args, **kwargs):
        if state not in self.state_registry:
            raise ValueError(f"State '{state}' is not registered.")

        if self.states:
            self.states[-1].on_exit()
        self.states.clear()

        state_class = self.state_registry[state]
        new_state = state_class(self, *args, **kwargs)
        self.states.append(new_state)
        new_state.on_enter()


