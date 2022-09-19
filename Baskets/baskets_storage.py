from bson.objectid import ObjectId

class BasketMongoStorage:
    def __init__(self,client):
        self.db = client.db.baskets

    def insert(self,user_id):
        self.db.insert_one({
            "products":[],
            "price":0.00,
            "user_id":user_id
        })
