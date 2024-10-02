# performance_monitoring_observer.py
import psutil


class PerformanceMonitoringObserver:
    def __init__(self):
        self.cpu_usage_history = []

    def on_step_completed(self):
        cpu_usage = psutil.cpu_percent()
        self.cpu_usage_history.append(cpu_usage)
        # Analyze CPU usage data (e.g., calculate average, maximum)
