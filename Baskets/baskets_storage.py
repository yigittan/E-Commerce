from bson.objectid import ObjectId

class BasketsMongoStorage:
    def __init__(self,client):
        self.db = client.db.baskets
        

    def insert(self,id):
        id = ObjectId(id)
        self.db.insert_one({
            "products":[],
            "price":0.00,
            "customer_id":id
        })

    def get_by_id(self,id):
        id = ObjectId(id)
        basket = self.db.find_one({'_id':id})
        return {
            "id":str(ObjectId(basket['_id'])),
            "products":basket['products'],
            "price":basket['price'],
            "customer_id":basket['customer_id']
        }
    
    def add_to_basket(self,basket_id,product_id):
        basket_id = ObjectId(basket_id)
        product_id = ObjectId(product_id)
        self.db.update_one({'_id':ObjectId(basket_id)} , {'$push': {'products':product_id}})
        basket = self.db.find_one({'_id':basket_id})
        return {
            "id_basket":str(ObjectId(basket['_id'])),
            "price":basket['price'],
            "customer_id":str(basket['customer_id']),
            "products":str(basket['products'])
        }

    def delete_from_basket(self,basket_id,product_id):
        basket_id = ObjectId(basket_id)
        product_id = ObjectId(product_id)
        self.db.update_one({'_id':basket_id} , {'$pull': {'products':product_id}})
        basket = self.db.find_one({'_id':basket_id})
        return str(basket['_id'])

    def delete_all(self,basket_id):
        basket_id = ObjectId(basket_id)
        self.db.update_one({'_id':basket_id} , {"$set": {'products': []}})
        basket = self.db.find_one({'_id':basket_id})
        return str(basket['_id'])
