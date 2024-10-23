class UserService:
    
    def __init__(self, user_dao):
        self.user_dao = user_dao

    def create_user(self, user_data):
        existing_user = self.user_dao.get_user_by_username(user_data.get('username'))
        if existing_user:
            raise ValueError("Username already exists")
        return self.user_dao.create_user(user_data)
    
    def authenticate_user(self, user_data):
        if user_data:
            existing_user = self.user_dao.get_user_by_username(user_data.get('username'))
            if existing_user:
                return existing_user
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

    def update_user_role(self, user_id, new_role):
        if new_role not in ["user", "admin"]:
            raise ValueError("Invalid role")
        return self.user_dao.update_user_role(user_id, new_role)

    def delete_user(self, user_id):
        return self.user_dao.delete_user(user_id)
