class UserDAO:
    
    def __init__(self, db):
        self.collection = db['users']

    def create_user(self, user_data):
        return self.collection.insert_one(user_data).inserted_id
    
    def get_all_users(self):
        users = self.collection.find()
        return [
            {**user, "_id": str(user["_id"])} for user in users
        ]

    def get_user_by_username(self, username):
        return self.collection.find_one({"username": username})

    def get_user_by_id(self, user_id):
        return self.collection.find_one({"_id": user_id})

    def update_user_role(self, user_id, new_role):
        return self.collection.update_one({"_id": user_id}, {"$set": {"role": new_role}})

    def delete_user(self, user_id):
        return self.collection.delete_one({"_id": user_id})
