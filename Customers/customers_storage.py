from bson.objectid import ObjectId

class CustomerMongoStorage:
    def __init__(self,client):
        self.db = client.db.customers

    def insert(self,name,email,id):
        self.db.insert_one({
            "name":name,
            "email":email,
            "user_id":str(ObjectId(id))
        })

    def update_customer(self,customer_id,name,email):
        customer = self.db.find_one({'_id':customer_id})
        if customer is None:
            return {'messages':'customer not found'}
        self.db.update_one({'_id':customer_id} , {"$set": {"name":name,"email":email}})
        customer = self.db.find_one({'_id':customer_id})
        return {
            "id":customer['_id'],
            "name":name,
            "email":email,
            "user_id":customer['user_id']
        }