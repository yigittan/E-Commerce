from bson.objectid import ObjectId

class ProductMongoStorage:
    def __init__(self,client):
        self.db = client.db.products

    def insert(self,product_name,product_price):
        self.db.insert_one({
            "product_name":product_name,
            "product_price":product_price
        })

    def get_all(self):
        products = self.db.find()
        return [{
            "id":str(ObjectId(product['_id'])),
            "product_name":product['product_name'],
            "product_price":product['product_price']
        } for product in products]

    def get_by_id(self,id):
        id = ObjectId(id)
        product = self.db.find_one({'_id':id})
        return {
            "id":str(ObjectId(product['_id'])),
            "name":product['product_name'],
            "price":product['product_price']
        }

    def update_product(self,id,new_product_name,new_product_price):
        print("asdsad")
        id = ObjectId(id)
        print("id oluştu")
        product = self.db.find_one({'_id':id})
        print("product oluştu")
        self.db.update_one({'_id':id} , {"$set": {"product_name":new_product_name}})
        self.db.update_one({'_id':id} , {"$set": {"product_price":new_product_price}})
        return {
            "id":str(ObjectId(product['_id'])),
            "product_name":product['product_name'],
            "product_price":product['product_price']
        }