from flask import jsonify, request
from bson.objectid import ObjectId


class UserController:
    def __init__(self, app, user_service):
        self.app = app
        self.user_service = user_service

        self.add_routes()

    def add_routes(self):
        @self.app.route('/users', methods=['POST'])
        def create_user():
            try:
                user_data = request.json
                new_user = self.user_service.create_user(user_data)
                return jsonify(str(new_user)), 201
            except ValueError as e:
                return jsonify({"error": str(e)}), 400
            except Exception as e:
                return jsonify({"error": str(e)}), 500

        @self.app.route('/users')
        def get_all_users():
            try:
                users = self.user_service.get_all_users()
                for user in users:
                    user['_id'] = str(user['_id'])
                return jsonify(users), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 500

        @self.app.route('/users/<user_id>')
        def get_user_by_id(user_id):
            user_id = user_id.strip()
            try:
                user = self.user_service.get_user_by_id(ObjectId(user_id))
                user['_id'] = str(user['_id'])
                return jsonify(user), 200
            except ValueError as e:
                return jsonify({"error": str(e)}), 404
            except Exception as e:
                return jsonify({"error": str(e)}), 500

        @self.app.route('/users/username/<username>')
        def get_user_by_username(username):
            username = username.strip()
            try:
                user = self.user_service.get_user_by_username(username)
                user['_id'] = str(user['_id'])
                return jsonify(user), 200
            except ValueError as e:
                return jsonify({"error": str(e)}), 404
            except Exception as e:
                return jsonify({"error": str(e)}), 500

        @self.app.route('/users/<user_id>', methods=['PATCH'])
        def update_user_role(user_id):
            try:
                new_role = request.json.get('role')
                self.user_service.update_user_role(ObjectId(user_id), new_role)
                return jsonify({"message": "User role updated successfully"}), 200
            except ValueError as e:
                return jsonify({"error": str(e)}), 400
            except Exception as e:
                return jsonify({"error": str(e)}), 500

        @self.app.route('/users/<user_id>', methods=['DELETE'])
        def delete_user(user_id):
            try:
                self.user_service.delete_user(ObjectId(user_id))
                return jsonify({"message": "User deleted successfully"}), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 500