class OrdersMongoStorage:
    def __init__(self,client):
        self.db = client.db.orders

    def insert(self,products_id,user_id):
        res = self.db.insert_one({
            "orders": products_id,
            "user_id":user_id
        })
        return str(res.inserted_id)

    def get(self,user_id):
        order = self.db.find_one({'user_id':user_id})
        return {
            "products":order['orders'],
            "user_id":order['user_id']
        }