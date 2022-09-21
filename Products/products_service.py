class ProductService:
    def __init__(self,storage):
        self.storage = storage

    def create(self,product):
        return self.storage.insert(product)

    def get_all_products(self):
        return self.storage.get_all_products()

    def get_by_id(self,product_id):
        res= self.storage.get_by_id(product_id)
        if res is None:
            return {'messages':'product not found'}
        return res

    def update(self,product,product_id):
        return self.storage.update(product,product_id)

    def remove(self,product_id):
        res = self.storage.remove(product_id)
        if res is None:
            return {'messages':'product not found'}


    def filter(self,filter_query):
        for item in list(filter_query.keys()):
            first = item
        for item in list(filter_query.values()):
            second = item
        return self.storage.filter(first,second)
