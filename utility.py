# performance_monitoring_observer.py
import psutil


class PerformanceMonitoringObserver:
    def __init__(self):
        self.cpu_usage_history = []

    def on_step_completed(self):
        cpu_usage = psutil.cpu_percent()
        self.cpu_usage_history.append(cpu_usage)
        # Analyze CPU usage data (e.g., calculate average, maximum)


# condition_monitoring_observer.py
class ConditionMonitoringObserver:
    def __init__(self):
        self.temperature_threshold = 1000

    def on_temperature_update(self, temperature):
        if temperature > self.temperature_threshold:
            print("Temperature threshold exceeded!")
            # Trigger actions (e.g., pause simulation, adjust parameters)
