class OrderService:
    
    def __init__(self, order_dao, log_dao):
        self.order_dao = order_dao
        self.log_dao = log_dao

    def create_order(self, order_data):
        created_order = self.order_dao.create_order(order_data)
        self.log_dao.log_event(f'Order placed: {order_data["_id"]}', 'Order placed successfully')
        return created_order

    def get_all_orders(self):
        orders = self.order_dao.get_all_orders()
        self.log_dao.log_event('Retrieve all orders', 'All orders retrieved successfully')
        return orders
    
    def get_orders_by_user(self, user_id):
        orders = self.order_dao.get_orders_by_user(user_id)
        return orders
    
    def delete_order(self, order_id):
        deleted = self.order_dao.delete_order(order_id)
        self.log_dao.log_event(f'Delete order: {order_id}', 'Order deleted successfully')
        return deleted