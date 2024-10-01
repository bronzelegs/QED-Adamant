# mongodb_interface.py
import pymongo


class MongoDBInterface:
    def __init__(self, database_name, collection_name):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB connection string
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def insert_data(self, data):
        try:
            self.collection.insert_one(data)
        except pymongo.errors.PyMongoError as e:
            print(f"Error inserting data: {e}")

    def retrieve_data(self, query):
        try:
            results = self.collection.find(query)
            return list(results)  # Convert cursor to a list
        except pymongo.errors.PyMongoError as e:
            print(f"Error retrieving data: {e}")
            return []  # Return an empty list in case of error

    def update_data(self, query, update):
        try:
            self.collection.update_one(query, update)
        except pymongo.errors.PyMongoError as e:
            print(f"Error updating data: {e}")

    def delete_data(self, query):
        try:
            self.collection.delete_one(query)
        except pymongo.errors.PyMongoError as e:
            print(f"Error deleting data: {e}")
