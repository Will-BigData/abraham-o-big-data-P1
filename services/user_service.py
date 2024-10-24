class UserService:
    
    def __init__(self, user_dao, log_dao):
        self.user_dao = user_dao
        self.log_dao = log_dao
        
    def create_user(self, user_data):
        existing_user = self.user_dao.get_user_by_username(user_data.get('username'))
        if existing_user:
            raise ValueError("Username already exists")
        user = self.user_dao.create_user(user_data)
        self.log_dao.log_event(f'Register {user_data["username"]}', 'User registered successfully.')
        return user
    
    def authenticate_user(self, user_data):
        if user_data:
            existing_user = self.user_dao.get_user_by_username(user_data.get('username'))
            if existing_user:
                self.log_dao.log_event(f"Login, {existing_user['username']}", 'Logged in successfully.')
                return existing_user
            self.log_dao.log_event(f'Login Failed {user_data["username"]}', 'Failed login attempt.')
            return None

    def get_all_users(self):
        users = self.user_dao.get_all_users()
        self.log_dao.log_event(f"Retrieve all users", 'All users retrieved successfully.')
        return users
    
    def get_user_by_id(self, user_id):
        user = self.user_dao.get_user_by_id(user_id)
        self.log_dao.log_event(f'Retrieve user by id: {user_id}', 'User retrieved successfully')
        if not user:
            self.log_dao.log_event(f'Retrieve user: {user_id}', 'User not found')
            raise ValueError("User not found")
        return user

    def get_user_by_username(self, username):
        user = self.user_dao.get_user_by_username(username)
        self.log_dao.log_event(f'Retrieve username: {username}', 'User retrieved successfully')
        if not user:
            self.log_dao.log_event(f'Retrieve username: {username}', 'User not found')
            raise ValueError("User not found")
        return user
    
    def update_user_role(self, user_id, new_role):
        if new_role not in ["user", "admin"]:
            self.log_dao.log_event(f'Update role of: {user_id}', 'Invalid role')
            raise ValueError("Invalid role")
        updated = self.user_dao.update_user_role(user_id, new_role)
        self.log_dao.log_event(f'Update role of: {user_id}', 'Role updated successfully')
        return updated
    
    def delete_user(self, user_id):
        deleted = self.user_dao.delete_user(user_id)
        self.log_dao.log_event(f'Delete user: {user_id}', 'User deleted successfully')
        return deleted
    