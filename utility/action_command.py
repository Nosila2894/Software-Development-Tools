class ActionCommand():
    def __init__(self, action, action_data):
        self.action = action
        self.action_data = action_data if action_data is not None else {}   

    def __repr__(self):
        return f"ActionCommand(type={self.action!r}, data={self.action_data})"