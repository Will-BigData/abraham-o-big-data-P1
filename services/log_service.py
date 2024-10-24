class LogService:
    
    def __init__(self, log_dao):
        self.log_dao = log_dao

    def log_event(self, log_data):
        return self.log_dao.log_event(log_data.event, log_data.description)

    def get_all_logs(self):
        logs = self.log_dao.get_all_logs()
        return [{"_id": str(log["_id"]), "event": log["event"], "description": log["description"], "timestamp": log["timestamp"]} for log in logs]
