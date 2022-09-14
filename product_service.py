

class ProductService:
    def __init__(self, product_storage):
        self.product_storage = product_storage

    def create(self, product_name, product_price):
        return self.product_storage.insert(product_name, product_price)

    def get_all(self):
        return self.product_storage.get_all()        

    def get_by_id(self,id):
        product = self.product_storage.get_by_id(id)
        if product is None:
            return {'message':'Product not found'}
        return product

    def update_product(self,id,new_product_name,new_product_price):
        self.product_storage.update_product(id,new_product_name,new_product_price)
        product = self.product_storage.get_by_id(id)
        return product