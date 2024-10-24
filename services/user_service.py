class UserService:
    
    def __init__(self, user_dao, log_dao):
        self.user_dao = user_dao
        self.log_dao = log_dao
        
    def create_user(self, user_data):
        existing_user = self.user_dao.get_user_by_username(user_data.get('username'))
        if existing_user:
            raise ValueError("Username already exists")
        user = self.user_dao.create_user(user_data)
        self.log_dao.log_event('Register', user_data['username'], 'User registered successfully.')
        return user
    
    def authenticate_user(self, user_data):
        if user_data:
            existing_user = self.user_dao.get_user_by_username(user_data.get('username'))
            if existing_user:
                self.log_dao.log_event('Login', existing_user['username'], 'Logged in successfully.')
                return existing_user
            self.log_dao.log_event('Login Failed', existing_user['username'], 'Failed login attempt.')
            return None

    def get_all_users(self):
        return self.user_dao.get_all_users()

    def get_user_by_id(self, user_id):
        user = self.user_dao.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        return user

    def get_user_by_username(self, username):
        user = self.user_dao.get_user_by_username(username)
        if not user:
            raise ValueError("User not found")
        return user

    def delete_user(self, user_id):
        return self.user_dao.delete_user(user_id)
