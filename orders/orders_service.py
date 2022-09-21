class OrderService:
    def __init__(self,storage):
        self.storage = storage

    def create(self,products_id,user_id,price):
        return self.storage.insert(products_id,user_id,price)

    def get(self,user_id):
        return self.storage.get(user_id)