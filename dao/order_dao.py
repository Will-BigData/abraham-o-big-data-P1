from bson import ObjectId


class OrderDAO:
    
    def __init__(self, db):
        self.collection = db['orders']

    def create_order(self, order_data):
        return self.collection.insert_one(order_data)

    def get_all_orders(self):
        orders = self.collection.find()
        return [
            {**order, "_id": str(order["_id"])} for order in orders
        ]        

    def get_orders_by_user(self, user_id):
        return list(self.collection.find({"user_id": ObjectId(user_id)}))

    def delete_order(self, order_id):
        return self.collection.delete_one({"_id": order_id})
