import config
from pymongo import MongoClient


class Mongo:
    def __init__(self):
        self.client = MongoClient(config.MONGO_DSN)
        self.db = self.client[config.MONGO_DATABASE]

    def find_one(self, collection, document_id):
        return self.db[collection].find_one({'id': document_id})

    def close(self):
        self.client.close()
