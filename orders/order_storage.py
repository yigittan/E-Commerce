class OrderMongoStorage:
    def __init__(self,client):
        self.db = client.db.orders