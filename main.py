# Copyright (c) 2024 Terrance Alan Davis
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import time

from condmonObserver import ConditionMonitoringObserver
from datastoreObserver import DataStoreObserver
from simulation import Simulation, create_molecules

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