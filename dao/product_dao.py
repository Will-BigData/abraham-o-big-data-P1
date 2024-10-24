from bson import ObjectId


class ProductDAO:
    
    def __init__(self, db):
        self.collection = db['products']

    def add_product(self, product_data):
        return self.collection.insert_one(product_data.model_to_dict())

    def get_all_products(self):
        products = self.collection.find()
        return [
            {**product, "_id": str(product["_id"])} for product in products
        ]
    
    def get_products_by_category(self, category):
        return list(self.collection.find({"category": category}))

    def get_product_by_id(self, product_id):
        return self.collection.find_one({"_id": product_id})

    def update_product_stock(self, product_id, new_stock):
        return self.collection.update_one({"_id": ObjectId(product_id)}, {"$set": {"stock": new_stock}})
    
    def delete_product(self, product_id):
        return self.collection.delete_one({"_id": ObjectId(product_id)})