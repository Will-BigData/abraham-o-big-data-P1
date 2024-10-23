from datetime import datetime


class Log:
    def __init__(self, event, username, description, timestamp=None):
        self.event = event
        self.username = username
        self.description = description
        self.timestamp = timestamp or datetime.now(datetime.timestamp.utc)

    def model_to_dict(self):
        return {
            "event": self.event,
            "username": self.username,
            "description": self.description,
            "timestamp": self.timestamp
        }

    @staticmethod
    def model_from_dict(data):
        return Log(
            event=data['event'],
            username=data['username'],
            description=data['description'],
            timestamp=data.get('timestamp', datetime.now(datetime.timestamp.utc))
        )
