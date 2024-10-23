from flask import request, jsonify
from models.product import Product


class ProductController:
    def __init__(self, app, product_service):
        self.app = app
        self.product_service = product_service

        self.add_routes()

    def add_routes(self):
        
        @self.app.route('/products', methods=['POST'])
        def add_product():
            data = request.json
            product = Product(data['name'], data['category'], data['price'], data['stock'], data['description'], data['launch_date'])
            result = self.product_service.add_product(product)
            return jsonify({"message": "Product added", "id": str(result.inserted_id)}), 201
        
        @self.app.route('/products')
        def get_all_products():
            products = self.product_service.get_all_products()
            serialized_products = []
            for product in products:
                product["_id"] = str(product["_id"])
                serialized_products.append(product)
            return jsonify(serialized_products), 200
        
        @self.app.route('/products/category/<string:category>')
        def get_products_by_category(category):
            products = self.product_service.get_products_by_category(category)
            serialized_products = []
            for product in products:
                product["_id"] = str(product["_id"])
                serialized_products.append(product)
            return jsonify(serialized_products), 200

        @self.app.route('/products/<string:product_id>', methods=['DELETE'])
        def delete_product(product_id):
            result = self.product_service.delete_product(product_id)
            if result is not None:
                return jsonify({"message": "Product deleted"}), 200
            else:
                return jsonify({"error": "Product not found"}), 404
