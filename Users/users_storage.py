class UsersMongoStorage:
    def __init__(self,client):
        self.db = client.db.users

    def insert(self,user):
        res = self.db.insert_one({
            "name":user.name,
            "surname":user.surname,
            "username":user.username,
            "email":user.email,
            "password":user.password,
            "city":user.city,
            "zip_code":user.zip_code,
            "street":user.street,
            "building":user.building,
        })
        return str(res.inserted_id)

    def getUser_by_email(self,email):
        user = self.db.find_one({'email':email})
        return {
            "id":str(user['_id']),
            "name":user['name'],
            "surname":user['surname'],
            "username":user['username']
        }

    def check_password(self,email,candidatePassword):
        user = self.getUser_by_email(email)
        if candidatePassword == user['password']:
            return True
        return False
        
        