class UsersMongoStorage:
    def __init__(self,client):
        self.db = client.db.users