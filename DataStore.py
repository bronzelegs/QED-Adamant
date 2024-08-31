import pymongo


class DataStore:
    def __init__(self, database_name, collection_name):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def store_results(self, results):
        self.collection.insert_one(results)

    def retrieve_results(self, query=None):
        if query:
            return self.collection.find(query)
        else:
            return self.collection.find()

    def delete_results(self, query=None):
        if query:
            self.collection.delete_many(query)
        else:
            self.collection.delete_many({})