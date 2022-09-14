from .ProductsClass import Product

class ProductService:
    def __init__(self, product_storage):
        self.product_storage = product_storage

    def create(self, title,price,description,category,created_at,discount,size,color):
        return self.product_storage.insert(title,price,description,category,created_at,discount,size,color)

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