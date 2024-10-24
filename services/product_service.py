from bson import ObjectId
from flask import jsonify


class ProductService:
    
    def __init__(self, product_dao, log_dao):
        self.product_dao = product_dao
        self.log_dao = log_dao

    def add_product(self, product):        
        added_product = self.product_dao.add_product(product)
        self.log_dao.log_event('Add product', product.name, 'Product added successfully.')
        return added_product
    
    def get_all_products(self):
        return self.product_dao.get_all_products()

    def get_product_by_id(self, product_id):
        product = self.product_dao.get_product_by_id(product_id)
        if not product:
            raise ValueError("Product not found")
        return product
        
    def get_products_by_category(self, category):
        return self.product_dao.get_products_by_category(category)

    def update_product_stock(self, product_id, new_stock):            
            product = self.product_dao.get_product_by_id(ObjectId(product_id))
            if not product:
                return jsonify({'error': 'Product not found'}), 404
            
            updated_product = self.product_dao.update_product_stock(product_id, new_stock) 
            jsonify({'message': 'Product quantity updated successfully'}), 200
            return updated_product
    
    def delete_product(self, product_id):
        return self.product_dao.delete_product(product_id)
