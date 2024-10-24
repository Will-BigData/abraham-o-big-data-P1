from datetime import datetime, timezone


class LogDAO:
    
    def __init__(self, db):
        self.collection = db['logs']

    def log_event(self, event, username, description):
        create_new_log_entry = {
            "event": event,
            "username": username,
            "description": description,
            "timestamp": datetime.now(timezone.utc)
        }
        return self.collection.insert_one(create_new_log_entry)

    def get_all_logs(self):
        logs = self.collection.find()
        return [
            {**log, "_id": str(log["_id"])} for log in logs
        ]        

    def get_logs_by_user(self, username):
        return list(self.collection.find({"username": username}))