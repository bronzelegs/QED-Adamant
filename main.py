
import Simulation
from google.cloud import firestore
from DataStore import DataStore
import DataStoreObserver

def main():
    datastore = DataStore("my_simulation_data", "simulation_results")
    datastore_client = firestore.Client()
    datastore_observer = DataStoreObserver(datastore_client)
    datastore_observer.start()

    simulation = Simulation.Simulation(datastore_client)
    simulation.run(num_steps)

if __name__ == "__main__":
    main()

