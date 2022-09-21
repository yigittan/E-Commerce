from bson.objectid import ObjectId

class BasketMongoStorage:
    def __init__(self,client):
        self.db = client.db.baskets

    def insert(self,user_id):
        self.db.insert_one({
            "products":[],
            "price":0.00,
            "user_id":user_id
        })

    def get_by_id(self,basket_id):
        basket = self.db.find_one({'_id':ObjectId(basket_id)})
        return {
            "products":basket['products'],
            "price":basket['price'],
            "user_id":basket['user_id']
        }

    def add(self,basket_id,product_id,price):
        self.db.update_one({'_id':ObjectId(basket_id)} , {"$push": {'products':product_id}})
        self.db.update_one({'_id':ObjectId(basket_id)} , {"$set":  {'price':price}})
        basket = self.get_by_id(basket_id)
        return {
            "price":basket['price'],
            "products":basket['products'],
            "user_id":basket['user_id']
        }

    def remove(self,basket_id,product_id):
        self.db.update_one({'_id':ObjectId(basket_id)} , {"$pull" : {'products':product_id}})
        basket = self.db.find_one({'_id':ObjectId(basket_id)})
        return {"products":basket['products']}

    def clear(self,basket_id):
        self.db.update_one({'_id':ObjectId(basket_id)} , {"$set": {'products': [] , 'price':0}})
        basket = self.db.find_one({'_id':ObjectId(basket_id)})
        return {"products":basket['products']}
