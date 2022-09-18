from bson.objectid import ObjectId

class CustomerMongoStorage:
    def __init__(self,client):
        self.db = client.db.customers

    def insert(self,name,email,id):
        id = ObjectId(id)
        self.db.insert_one({
            "name":name,
            "email":email,
            "user_id":str(ObjectId(id)),
            "customer_info":[]
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

    def set_customer_info(self,customer_id,city,street_no,building_no,phone_no):
        self.db.update_one({'_id':ObjectId(customer_id)} , {"$push": {'customer_info': {"city":city , "street":street_no , "building":building_no , "phone":phone_no}}})
        customer = self.db.find_one({'_id':ObjectId(customer_id)})
        return customer['customer_info']


    def update_customer_info(self,customer_id,city,street_no,building_no,phone_no):
        self.db.update_one({'_id':ObjectId(customer_id)} , {"$set": {"customer_info" : {"city":city , "street":street_no , "building":building_no , "phone":phone_no}}})
        customer = self.db.find_one({'_id':ObjectId(customer_id)})
        return customer['customer_info']