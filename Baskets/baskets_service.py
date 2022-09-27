class BasketService:
    def __init__(self,storage):
        self.storage = storage

    def create(self,user_id):
        return self.storage.insert(user_id)

    def get_by_id(self,user_id):
        return self.storage.get_by_id(user_id)

    def add(self,user_id,product_id,price):
        return self.storage.add(user_id,product_id,price)

    def remove(self,user_id,product_id):
        return self.storage.remove(user_id,product_id)

    def delete(self,user_id):
        return self.storage.delete(user_id)

    def clear(self,user_id):
        return self.storage.clear(user_id)
