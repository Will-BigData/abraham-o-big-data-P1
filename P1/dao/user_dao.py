from bson import ObjectId
from models.user import User


class UserDAO:
    
    def __init__(self, db):
        self.collection = db['users']

    def create_user(self, username, password, role="user"):
        new_user = User(username, password, role)
        user_dict = new_user.to_dict()
        return self.collection.insert_one(user_dict)
    
    def get_all_users(self):
        users = self.collection.find()
        return [
            {**user, "_id": str(user["_id"])} for user in users
        ]

    def get_user_by_username(self, username):
        return self.collection.find_one({"username": username})

    def get_user_by_id(self, user_id):
        return self.collection.find_one({"_id": ObjectId(user_id)})

    def update_user_role(self, username, new_role):
        return self.collection.update_one({"username": username}, {"$set": {"role": new_role}})

    def delete_user(self, user_id):
        return self.collection.delete_one({"_id": ObjectId(user_id)})
