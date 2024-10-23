class LogDAO:
    
    def __init__(self, db):
        self.collection = db['logs']

    def create_new_log_entry(self, log_data):
        return self.collection.insert_one(log_data)

    def get_all_logs(self):
        logs = self.collection.find()
        return [
            {**log, "_id": str(log["_id"])} for log in logs
        ]        

    def get_logs_by_user(self, username):
        return list(self.collection.find({"username": username}))