from bson.objectid import ObjectId

class CustomerService:
    def __init__(self,customers_storage):
        self.customers_storage = customers_storage

    def create(self,name,email,id):
        return self.customers_storage.insert(name,email,id)
