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