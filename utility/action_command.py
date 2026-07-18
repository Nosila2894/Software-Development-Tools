class ActionCommand:

    def __init__(self, action, action_data):
        #Ensures the program fails if the action identifier is not a string.
        if not isinstance(action, str):
            raise TypeError("Action must be a string.")

        #Forces the action data to be passed as a dictionary for quick data lookup
        #When passed through the event handler and back to the state for callback functions.
        if not isinstance(action_data, dict) and action_data is not None:
            raise TypeError("Action data must be a dictionary or None.")

        self.action = action
        self.action_data = action_data if action_data is not None else {}   
    
    def __repr__(self):
        #A return of a data packet containing an action and its associated data.
        #It is used by the event handler and state to update and trigger appropriate callback functions
        #Designed for local environments with web-based scalability in mind.
        return f"ActionCommand(type={self.action!r}, data={self.action_data})"