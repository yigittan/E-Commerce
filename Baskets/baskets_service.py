class BasketService:
    def __init__(self,storage):
        self.storage = storage

    def create(self,user_id):
        return self.storage.insert(user_id)