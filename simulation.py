# simulation.py
import threading

from performance_monitoring_observer import PerformanceMonitoringObserver
from visualization_data import VisualizationData

from visualizationdata import visualize_data


class Simulation(VisualizationData):
    def __init__(self, molecules, sync_variable):
        super().__init__()
        self.molecules = molecules
        self.sync_variable = sync_variable
        self.sync_event = threading.Event()
        self.state = "Initialized"
        self.performance_observer = PerformanceMonitoringObserver()
        self.visualization_data = VisualizationData()

    def run(self, num_steps, dt):
        self.state = "Running"
        threads = []
        for step in range(num_steps):
            if self.state == "Stopped":  # Check if stopped
                break
            for molecule in self.molecules:
                thread = threading.Thread(target=molecule.simulate_step, args=(step, dt))
                threads.append(thread)
                thread.start()

            # Wait for all threads to finish the current step
            self.sync_event.wait()
            self.sync_event.clear()

            # Store visualization data
            self.time_steps.append(step * dt)  # Store time step
            self.update_visualization_data()  # Update visualization data
            self.performance_observer.on_step_completed()  # Performance monitoring

            # Visualize the data
            visualize_data(self.visualization_data)

        for thread in threads:
            thread.join()
        self.state = "Stopped"

    def update_visualization_data(self):
        # Update visualization data from molecules
        self.electron_positions = []
        self.atom_positions = []
        for molecule in self.molecules:
            for atom in molecule.atoms:
                self.atom_positions.append(atom.position)
            for electron in molecule.electrons:
                self.electron_positions.append(electron.position)

    def pause(self):
        if self.state == "Running":
            self.state = "Paused"

    def resume(self):
        if self.state == "Paused":
            self.state = "Running"

    def stop(self):
        self.state = "Stopped"


# Example usage:
def create_molecules():
    # ... (Implementation to create molecules)

    molecules = create_molecules()  # Create a list of molecules
    simulation = Simulation(molecules, sync_variable=True)

# ... (Start the simulation, use pause, resume, and stop as needed)
