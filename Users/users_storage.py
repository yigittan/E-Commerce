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

    def getUser_by_email(self,email):
        user = self.db.find_one({'email':email})
        return {
            "id":str(user['_id']),
            "name":user['name'],
            "email":user['email']
        }

    def control_password(self,email,candidatePassword):
        user = self.getUser_by_email(email)
        if candidatePassword == user['password']:
            return True
        else:
            return False
    
    