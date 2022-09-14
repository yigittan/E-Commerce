from bson.objectid import ObjectId

class BasketService:
    def __init__(self,baskets_storage):
        self.baskets_storage= baskets_storage

    def create(self,id):
        return self.baskets_storage.insert(str(ObjectId(id)))

