class OrderService:
    
    def __init__(self, order_dao):
        self.order_dao = order_dao

    def create_order(self, order_data):
        return self.order_dao.create_order(order_data)

    def get_all_orders(self):
        return self.order_dao.get_all_orders()

    def get_orders_by_user(self, user_id):
        return self.order_dao.get_orders_by_user(user_id)

    def delete_order(self, order_id):
        return self.order_dao.delete_order(order_id)
