import bcrypt
from bson.objectid import ObjectId
from flask import session

class UserService:
    def __init__(self,users_storage):
        self.users_storage = users_storage

    def create(self,name,email,password):
        byte_pass = password.encode('utf-8')
        hash = bcrypt.hashpw(byte_pass,bcrypt.gensalt())
        return self.users_storage.insert(name,email,hash)

    def getUser_by_email(self,email):
        user = self.users_storage.getUser_by_email(email)
        return user

    def control_password(self,email,candidatePassword):
        self.users_storage.control_password(email,candidatePassword)
        
        