from bson.objectid import ObjectId

class BasketsMongoStorage:
    def __init__(self,client):
        self.db = client.db.baskets

    def insert(self,id):
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
    
    def add_to_basket(self,id,product_id):
        product = product_service.get_by_id(ObjectId(product_id))
        basket = self.db.find_one({'_id':ObjectId(id)})
        self.db.update_one({'_id':ObjectId(id)}, {'$push': {"product":product}})
        basket = self.db.find_one({'_id':ObjectId(id)})
        return [{
            "id":str(ObjectId(product['_id'])),
            "title":product['title'],
            "price":product['price'],
            "description":product['description'],
            "category":product['category'],
            "created_at":product['created_at'],
            "discount":product['discount'],
            "size":product['size'],
            "color":product['color']
        } for product in basket['products']]
