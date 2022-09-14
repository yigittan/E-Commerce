from bson.objectid import ObjectId

class CustomerMongoStorage:
    def __init__(self,client):
        self.db = client.db.customers

    def insert(self,name,email,id):
        self.db.insert_one({
            "name":name,
            "email":email,
            "user_id":str(ObjectId(id))
        })