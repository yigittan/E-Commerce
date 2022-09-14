from bson.objectid import ObjectId

class BasketsMongoStorage:
    def __init__(self,client):
        self.db = client.db.baskets

    def insert(self,id):
        self.db.insert_one({
            "products":[],
            "price":0.00,
            "customer_id":id
        })