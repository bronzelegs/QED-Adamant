
from google.cloud import firestore

import DataStoreObserver
import Simulation
from DataStoreObserver import DataStoreObserver


def main():
    num_steps = 1

    datastore_observer = DataStoreObserver
    datastore_client = firestore.Client()
    datastore_observer.start()

    simulation = Simulation.Simulation(datastore_client)
    simulation.run(num_steps)

if __name__ == "__main__":
    main()

