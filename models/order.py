from datetime import datetime


class Order:
    def __init__(self, user_id, product_id, quantity, total_price, order_date=None):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity
        self.total_price = total_price
        self.order_date = order_date or datetime.now(datetime.timestamp.utc)
        self.id = None

    def model_to_dict(self):
        return {
            "user_id": self.user_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "total_price": self.total_price,
            "order_date": self.order_date
        }

    @staticmethod
    def model_from_dict(data):
        return Order(
            user_id=data['user_id'],
            product_id=data['product_id'],
            quantity=data['quantity'],
            total_price=data['total_price'],
            order_date=data.get('order_date')
        )
