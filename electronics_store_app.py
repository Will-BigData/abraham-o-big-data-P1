from flask import Flask
from config import Config

from dao.user_dao import UserDAO
from services.user_service import UserService
from controllers.user_controller import UserController

from dao.product_dao import ProductDAO
from services.product_service import ProductService
from controllers.product_controller import ProductController

from dao.order_dao import OrderDAO
from services.order_service import OrderService
from controllers.order_controller import OrderController

from dao.log_dao import LogDAO
from services.log_service import LogService
from controllers.log_controller import LogController


class ElectronicsStoreApp:
    
    def __init__(self):
        self.app = Flask(__name__)
        
        self.app.config.from_object(Config)
        self.db = Config.get_db()

        self.user_dao = UserDAO(self.db)
        self.user_service = UserService(self.user_dao)
        UserController(self.app, self.user_service)
        
        self.product_dao = ProductDAO(self.db)
        self.product_service = ProductService(self.product_dao)
        self.product_controller = ProductController(self.app, self.product_service)

        self.order_dao = OrderDAO(self.db)
        self.order_service = OrderService(self.order_dao)
        self.order_controller = OrderController(self.app, self.order_service)
        
        log_dao = LogDAO(self.db)
        log_service = LogService(log_dao)
        self.log_controller = LogController(self.app, log_service)


        
    def run(self):
        self.app.run(host='localhost', port=5000)


if __name__ == '__main__':
        ElectronicsStoreApp().run()
