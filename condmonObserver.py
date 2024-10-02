class ConditionMonitoringObserver:
    def __init__(self):
        self.temperature_threshold = 1000

    def on_temperature_update(self, temperature):
        if temperature > self.temperature_threshold:
            print("Temperature threshold exceeded!")
            # Trigger actions (e.g., pause simulation, adjust parameters)