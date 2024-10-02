# datastore_observer.py
from mongodbi import MongoDBInterface

class DataStoreObserver:
    def __init__(self):
        self.mongo_interface = MongoDBInterface(database_name="qed_adamant", collection_name="simulation_results")

    def store_results(self, results):
        self.mongo_interface.insert_data(results)
