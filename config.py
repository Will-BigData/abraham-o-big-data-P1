import os
from pymongo import MongoClient


class Config:

    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/'
    DATABASE_NAME = os.environ.get('DATABASE_NAME') or 'electronics_store'

    @classmethod
    def get_db(cls):
        client = MongoClient(cls.MONGO_URI)
        return client[cls.DATABASE_NAME]

