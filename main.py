from simulation import Simulation
from datastore import DataStore
from datastore_observer import DatastoreObserver

def main():
    datastore_client = DataStore()
    datastore_observer = DatastoreObserver(datastore_client)
    datastore_observer.start()

    simulation = Simulation(datastore_client)
    simulation.run(num_steps)

if __name__ == "__main__":
    main()
