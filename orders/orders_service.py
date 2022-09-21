class OrderService:
    def __init__(self,storage):
        self.storage = storage

    def create(self,products_id,user_id):
        return self.storage.insert(products_id,user_id)

    def get(self,user_id):
        return self.storage.get(user_id)