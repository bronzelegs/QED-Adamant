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


import json
import threading

from visualizationi import visualize_data


class Simulation:
    def __init__(self, molecules, sync_variable):

    # ... (Existing code remains unchanged)

    def run(self, num_steps, dt, output_filename="simulation_data.json"):
        self.state = "Running"

        simulation_data = {  # Create dictionary to store the complete data
            "simulation_id": "unique_id_123",  # Generate a unique ID if needed
            "parameters": {
                "num_steps": num_steps,
                "dt": dt,
                # ... other parameters you want to store
            },
            "time_steps": [],  # Initialize an empty list for time steps
            "molecules": []  # Initialize an empty list for molecule data
        }


        threads = []
        for step in range(num_steps):
            if self.state == "Stopped":
                break
            for molecule in self.molecules:
                thread = threading.Thread(target=molecule.simulate_step, args=(step, dt))
                threads.append(thread)
                thread.start()

            self.sync_event.wait()
            self.sync_event.clear()

            simulation_data["time_steps"].append(step * dt)
            molecules_data = []
            for molecule in self.molecules:
                molecules_data.append(molecule.to_dict())  # Convert and add the data

            simulation_data["molecules"].append(molecules_data)

            self.visualization_data.from_dict({"molecules": molecules_data, "time_steps": simulation_data[
                "time_steps"]})  # Update the visualization data object

            self.datastore_observer.store_results(self.visualization_data)  # Store results
            self.performance_observer.on_step_completed()
            visualize_data(self.visualization_data)  # Visualize current step's data

        with open(output_filename, 'w') as f:
            json.dump(simulation_data, f, indent=4)

        for thread in threads:
            thread.join()

        self.state = "Stopped"

    # ... (Rest of the Simulation class - pause(), resume(), stop(), etc. - remains unchanged)
