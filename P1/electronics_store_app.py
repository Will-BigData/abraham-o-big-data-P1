from flask import Flask
from pymongo import MongoClient
from dao.user_dao import UserDAO
from dao.product_dao import ProductDAO
from dao.order_dao import OrderDAO
from dao.log_dao import LogDAO


class ElectronicsStoreApp:
    
    def __init__(self):
        self.app = Flask(__name__)
        
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['electronics_store']

        self.user_dao = UserDAO(self.db)
        self.product_dao = ProductDAO(self.db)
        self.order_dao = OrderDAO(self.db)
        self.log_dao = LogDAO(self.db)

        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/')
        def home():
            return "Welcome to the Electronics Appliance Store!"

        @self.app.route('/users')
        def get_users():
            products = self.user_dao.get_all_users()
            return {"products": products}
        @self.app.route('/products')
        def get_products():
            products = self.product_dao.get_all_products()
            return {"products": products}
        @self.app.route('/orders')
        def get_orders():
            products = self.order_dao.get_all_orders()
            return {"products": products}
        @self.app.route('/logs')
        def get_logs():
            products = self.log_dao.get_all_logs()
            return {"products": products}

    def run(self):
        self.app.run(debug=True, host='0.0.0.0', port=5000)


if __name__ == '__main__':
    appliance_store_app = ElectronicsStoreApp()
    appliance_store_app.run()
