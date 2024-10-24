from flask import request, jsonify


class OrderController:
    def __init__(self, app, order_service):
        self.app = app
        self.order_service = order_service
        self.add_routes()

    def add_routes(self):

        @self.app.route('/orders', methods=['POST'])
        def create_order():
            data = request.get_json()
            result = self.order_service.create_order(data)
            return jsonify({"order_id": str(result.inserted_id)}), 201

        @self.app.route('/orders')
        def get_all_orders():
            orders = self.order_service.get_all_orders()
            return jsonify(orders), 200
        
        @self.app.route('/orders/<order_id>', methods=['DELETE'])
        def delete_order(order_id):
            result = self.order_service.delete_order(order_id)
            if result.deleted_count == 0:
                return jsonify({"error": "Order not found"}), 404
            return jsonify({"message": "Order deleted successfully"}), 200
