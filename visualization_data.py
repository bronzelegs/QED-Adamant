import threading

class VisualizationData:
    lock = threading.Lock()
    def __init__(self):
        self.electron_positions = []
        self.atom_positions = []
        self.time_steps = []

    def from_dict(self, simulation_data):
        with self.lock:  # Acquire lock before updating data
            self.electron_positions = []
            self.atom_positions = []
            self.time_steps = simulation_data['time_steps']
            for molecule_data in simulation_data.get('molecules', []):
                for atom_data in molecule_data.get('atoms', []):
                    self.atom_positions.append(atom_data['position'])
                for electron_data in molecule_data.get('electrons', []):
                    self.electron_positions.append(electron_data['position'])
