from datetime import datetime, timezone


class LogDAO:
    
    def __init__(self, db):
        self.collection = db['logs']

    def log_event(self, event, description):
        create_new_log_entry = {
            "event": event,
            "description": description,
            "timestamp": datetime.now(timezone.utc)
        }
        return self.collection.insert_one(create_new_log_entry)

    def get_all_logs(self):
        logs = self.collection.find()
        return [
            {**log, "_id": str(log["_id"])} for log in logs
        ]        
