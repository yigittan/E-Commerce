from bson.objectid import ObjectId

class UsersMongoStorage:
    def __init__(self,client):
        self.db = client.db.users

    def insert(self,name,email,hash):
        res = self.db.insert_one({
            "name":name,
            "email":email,
            "password":hash
        })