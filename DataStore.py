 import pymongo

class DataStore:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = client["simulation_data"]
        self.collection = db["simulation_results"]

    def store_results(self, results):
        self.collection.insert_one(results)

    # visualization.py TODO
    #def visualize_results(results):
    # ... (create visualizations)
