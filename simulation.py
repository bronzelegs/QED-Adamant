import threading

from datastoreObserver import DataStoreObserver
from perfmonObserver import PerformanceMonitoringObserver
from visualization import visualize_data
from visualizationdata import VisualizationData


class Simulation:
    def __init__(self, molecules, sync_variable):
        self.molecules = molecules
        self.sync_variable = sync_variable
        self.sync_event = threading.Event()
        self.state = "Initialized"
        self.performance_observer = PerformanceMonitoringObserver()
        self.visualization_data = VisualizationData()
        self.datastore_observer = DataStoreObserver()  # Add DataStoreObserver instance

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

            # Store simulation results
            self.datastore_observer.store_results(self.visualization_data)  # Store results to MongoDB

        for thread in threads:
            thread.join()
        self.state = "Stopped"

    def update_visualization_data(self):
        # Update visualization data from molecules
        self.visualization_data.electron_positions = []
        self.visualization_data.atom_positions = []
        for molecule in self.molecules:
            for atom in molecule.atoms:
                self.visualization_data.atom_positions.append(atom.position)
            for electron in molecule.electrons:
                self.visualization_data.electron_positions.append(electron.position)

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
    print("ToDo: create_molecules() in simulation.py")
molecules = create_molecules()  # Create a list of molecules
simulation = Simulation(molecules, sync_variable=True)

# ... (Start the simulation, use pause, resume, and stop as needed)