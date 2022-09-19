class ProductMongoStorage:
    def __init__(self,client):
        self.db = client.db.products