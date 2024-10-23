class LogService:
    
    def __init__(self, log_dao):
        self.log_dao = log_dao

    def create_new_log_entry(self, log_data):
        return self.log_dao.create_new_log_entry(log_data)

    def get_all_logs(self):
        logs = self.log_dao.get_all_logs()
        return [{"_id": str(log["_id"]), "event": log["event"], "username": log["username"], "description": log["description"], "timestamp": log["timestamp"]} for log in logs]

    def get_logs_by_user(self, username):
        logs = self.log_dao.get_logs_by_user(username)
        return [{"_id": str(log["_id"]), "event": log["event"], "username": log["username"], "description": log["description"], "timestamp": log["timestamp"]} for log in logs]
