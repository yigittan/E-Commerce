from bson.objectid import ObjectId

class UsersMongoStorage:
    def __init__(self, client):
        self.db = client.db.users

    def insert(self, user):
        res = self.db.insert_one({
            "name": user.name,
            "surname": user.surname,
            "username": user.username,
            "email": user.email,
            "password": user.password,
            "city": user.city,
            "zip_code": user.zip_code,
            "street": user.street,
            "building": user.building,
        })
        return str(res.inserted_id)

    def getUser_by_email(self, email):
        user = self.db.find_one({'email': email})
        return {
            "id": str(user['_id']),
            "name": user['name'],
            "surname": user['surname'],
            "username": user['username']
        }

    def check_password(self, email, candidatePassword):
        user = self.getUser_by_email(email)
        if candidatePassword == user['password']:
            return True
        return False

    def get_by_id(self,user_id):
        user = self.db.find_one({'_id':ObjectId(user_id)})
        return {
            "id": str(user['_id']),
            "name": user['name'],
            "surname": user['surname'],
            "username": user['username']
        }

    def update(self,user,user_id):
        res = self.get_by_id(user_id)
        if res is None:
            return {'message':'User not found'}
        self.db.update_one({'_id':ObjectId(user_id)} , {"$set" : {"name":user.name , "surname":user.surname , "username" : user.username , "email": user.email , "password":user.password , "city":user.city , "zip_code":user.zip_code , "street":user.street , "building":user.building}})
        user = self.get_by_id(user_id)
        return {
            "id": user_id,
            "name": user['name'],
            "surname": user['surname'],
            "username": user['username']
        }

    def remove(self,user_id):
        user = self.get_by_id(user_id)
        if user is None:
            return {'messages':'User not found'}
        self.db.delete_one({'_id':ObjectId(user_id)})
        return user_id