rom
simulation
import time

import Simulation
import create_molecules
from condition_monitoring_observer import ConditionMonitoringObserver
from datastore_observer import DataStoreObserver

if __name__ == "__main__":
    # Create molecules
    molecules = create_molecules()  # Implement this function

    # Initialize simulation
    simulation = Simulation(molecules, sync_variable=True)

    # Initialize observers
    datastore_observer = DataStoreObserver()
    condition_observer = ConditionMonitoringObserver()

    # Run simulation
    simulation.run(num_steps=100, dt=0.1)

    # Example of using observers:
    # Simulate temperature updates (for condition observer)
    for _ in range(10):
        temperature = 1000 + 50 * _  # Example temperature change
        condition_observer.on_temperature_update(temperature)
        time.sleep(0.1)  # Simulate time passing

    # Example of storing results (for datastore observer)
    datastore_observer.store_results(simulation.visualization_data)  # Store results to MongoDB
