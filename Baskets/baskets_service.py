class BasketService:
    def __init__(self,storage):
        self.storage = storage

    def create(self,user_id):
        return self.storage.insert(user_id)

    def get_by_id(self,basket_id):
        return self.storage.get_by_id(basket_id)

    def add(self,basket_id,product_id):
        return self.storage.add(basket_id,product_id)