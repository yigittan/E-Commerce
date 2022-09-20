class ProductService:
    def __init__(self,storage):
        self.storage = storage

    def create(self,product):
        return self.storage.insert(product)

    def get_all_products(self):
        return self.storage.get_all_products()

    def get_by_id(self,product_id):
        return self.storage.get_by_id(product_id)

    def update(self,product,product_id):
        return self.storage.update(product,product_id)

    def remove(self,product_id):
        return self.storage.remove(product_id)

    def filter(self,brand,name):
        return self.storage.filter(brand,name)
