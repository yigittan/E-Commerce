class OrdersMongoStorage:
    def __init__(self,client):
        self.db = client.db.orders

    def insert(self,products_id):
        res = self.db.insert_one({
            "orders": products_id
        })
        return str(res.inserted_id)