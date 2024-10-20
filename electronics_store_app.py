from flask import Flask
from config import Config

from dao.user_dao import UserDAO
from services.user_service import UserService
from controllers.user_controller import UserController


class ElectronicsStoreApp:
    
    def __init__(self):
        self.app = Flask(__name__)
        
        self.app.config.from_object(Config)
        self.db = Config.get_db()

        self.user_dao = UserDAO(self.db)
        
        self.user_service = UserService(self.user_dao)
        UserController(self.app, self.user_service)

    def run(self):
        self.app.run(host='localhost', port=5000)


if __name__ == '__main__':
        ElectronicsStoreApp().run()
