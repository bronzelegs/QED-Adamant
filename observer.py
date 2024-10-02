class Observer:
    def __init__(self):
        pass

    def notify(self, event_data):
        """
        This method is called when an event occurs that the observer is interested in.
        """
        raise NotImplementedError("Subclasses must implement the notify method")

    def on_step_completed(self):
        """
        This method is called when a simulation step is completed.
        """
        pass

    def on_temperature_update(self, temperature):
        """
        This method is called when the simulation's temperature is updated.
        """
        pass

    # ... (Add other methods for specific events as needed)
