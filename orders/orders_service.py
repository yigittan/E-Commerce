class OrderService:
    def __init__(self,storage):
        self.storage = storage

    def create(self,products_id):
        return self.storage.insert(products_id)