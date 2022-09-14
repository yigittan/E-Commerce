import bcrypt
from bson.objectid import ObjectId

class UserService:
    def __init__(self,users_storage):
        self.users_storage = users_storage

    def create(self,name,email,password):
        byte_pass = password.encode('utf-8')
        hash = bcrypt.hashpw(byte_pass,bcrypt.gensalt())
        return self.users_storage.insert(name,email,hash)
        