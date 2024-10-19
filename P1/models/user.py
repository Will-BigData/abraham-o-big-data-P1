from passlib.hash import bcrypt


class User:
    def __init__(self, username, password, role="user"):
        self.username = username
        self.password = self.hash_password(password)
        self.role = role

    @staticmethod
    def hash_password(password):
        return bcrypt.hash(password)

    def check_password(self, password):
        return bcrypt.verify(password, self.password)

    def model_to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "role": self.role
        }

    @staticmethod
    def model_from_dict(data):
        return User(
            username=data['username'],
            password=data['password'],
            role=data.get('role', 'user')
        )