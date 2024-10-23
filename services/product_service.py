class ProductService:
    
    def __init__(self, product_dao):
        self.product_dao = product_dao

    def add_product(self, product):        
        return self.product_dao.add_product(product)

    def get_all_products(self):
        return self.product_dao.get_all_products()

    def get_product_by_id(self, product_id):
        return self.product_dao.get_product_by_id(product_id)
    
    def get_products_by_category(self, category):
        return self.product_dao.get_products_by_category(category)

    def delete_product(self, product_id):
        return self.product_dao.delete_product(product_id)
