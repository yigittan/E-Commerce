class ProductService:
    def __init__(self,storage):
        self.storage = storage

    def create(self,product):
        return self.storage.insert(product)

    def get_all_products(self):
        return self.storage.get_all_products()
