from flask import request, jsonify


class LogController:
    def __init__(self, app, log_service):
        self.app = app
        self.log_service = log_service
        self.add_routes()

    def add_routes(self):
        
        @self.app.route('/logs', methods=['POST'])
        def log_event():
            data = request.get_json()
            result = self.log_service.log_event(data)
            return jsonify({"log_id": str(result.inserted_id)}), 201

        @self.app.route('/logs')
        def get_all_logs():
            logs = self.log_service.get_all_logs()
            return jsonify(logs), 200

        @self.app.route('/logs/<username>')
        def get_logs_by_user(username):
            try:
                logs = self.log_service.get_logs_by_user(username)
                return jsonify(logs), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 400
