import uuid

class UserService:
    def __init__(self,storage):
        self.storage = storage

    def create(self,user):
        return self.storage.insert(user)

    def getUser_by_email(self,email):
        return self.storage.getUser_by_email(email)

    def check_password(self,email,candidatePassword):
        return self.storage.check_password(email,candidatePassword)
