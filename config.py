import os
from flask_jwt_extended import JWTManager
from pymongo import MongoClient


class Config:

    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/'
    DATABASE_NAME = os.environ.get('DATABASE_NAME') or 'electronics_store'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt_secret'


    @classmethod
    def get_db(cls):
        client = MongoClient(cls.MONGO_URI)
        return client[cls.DATABASE_NAME]

    def init_jwt(app):
        app.config['JWT_SECRET_KEY'] = Config.JWT_SECRET_KEY
        JWTManager(app)