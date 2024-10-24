from datetime import datetime


class Log:
    def __init__(self, event, description, timestamp=None):
        self.event = event
        self.description = description
        self.timestamp = timestamp or datetime.now(datetime.timestamp.utc)

    def model_to_dict(self):
        return {
            "event": self.event,
            "description": self.description,
            "timestamp": self.timestamp
        }

    @staticmethod
    def model_from_dict(data):
        return Log(
            event=data['event'],
            description=data['description'],
            timestamp=data.get('timestamp', datetime.now(datetime.timestamp.utc))
        )
