import json
import os
from pymongo import MongoClient


class MongoDBImporter:
    
    def __init__(self, db_name='electronics_store', datasource = 'P1/collections'):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client[db_name]
        self.datasource = datasource

    def load_datasource_file(self, file_name):
        file_path = os.path.join(self.datasource, file_name)
        with open(file_path, 'r') as file:
            return json.load(file)
        
    def import_file_data(self, collection_name, file_data):
        collection = self.db[collection_name]
        result = collection.insert_many(file_data)
        print(f'Inserted {len(result.inserted_ids)} documents into {collection_name}')
        
    def import_logs_to_db(self):
        logs = self.load_datasource_file('C:/Users/abrah/Desktop/BigData-project-repo/Project_1/P1/collections/logs.json')
        self.import_file_data('logs', logs)

    def import_orders_to_db(self):
        orders = self.load_datasource_file('C:/Users/abrah/Desktop/BigData-project-repo/Project_1/P1/collections/orders.json')
        self.import_file_data('orders', orders)

    def import_products_to_db(self):
        products = self.load_datasource_file('C:/Users/abrah/Desktop/BigData-project-repo/Project_1/P1/collections/products.json')
        self.import_file_data('products', products)

    def import_users_to_db(self):
        users = self.load_datasource_file('C:/Users/abrah/Desktop/BigData-project-repo/Project_1/P1/collections/users.json')
        self.import_file_data('users', users)

    def import_files_to_db(self):
        self.import_logs_to_db()
        self.import_orders_to_db()
        self.import_products_to_db()
        self.import_users_to_db()
        print("All data has been imported successfully.")


if __name__ == "__main__":
    importer = MongoDBImporter(db_name='electronics_store')
    importer.import_files_to_db()