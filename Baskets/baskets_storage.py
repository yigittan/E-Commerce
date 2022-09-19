class BasketMongoStorage:
    def __init__(self,client):
        self.db = client.db.baskets
