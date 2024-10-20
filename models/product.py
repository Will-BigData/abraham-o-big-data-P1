from datetime import datetime


class Product:
    def __init__(self, name, category, price, stock, description="", launch_date=None):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
        self.description = description
        self.launch_date = launch_date or datetime.now(datetime.timezone.utc)

    def model_to_dict(self):
        return {
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "stock": self.stock,
            "description": self.description,
            "launch_date": self.launch_date
        }

    @staticmethod
    def model_from_dict(data):
        return Product(
            name=data['name'],
            category=data['category'],
            price=data['price'],
            stock=data['stock'],
            description=data.get('description', ''),
            launch_date=data.get('launch_date')
        )
        