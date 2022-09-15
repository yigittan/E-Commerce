from bson.objectid import ObjectId
from .ProductsClass import Product

class ProductMongoStorage:
    def __init__(self,client):
        self.db = client.db.products

    def insert(self,title,price,description,category,created_at,discount,size,color):
        self.db.insert_one({
            "title":title,
            "price":price,
            "description":description,
            "category":category,
            "created_at":created_at,
            "discount":discount,
            "size":size,
            "color":color
        })

    def get_all(self):
        products = self.db.find()
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
        } for product in products]

    def get_by_id(self,id):
        id = ObjectId(id)
        product = self.db.find_one({'_id':id})
        return {
            "id":str(ObjectId(product['_id'])),
            "title":product['title'],
            "price":product['price'],
            "description":product['description'],
            "category":product['category'],
            "created_at":product['created_at'],
            "discount":product['discount'],
            "size":product['size'],
            "color":product['color']
        }

    def update_product(self,id,title,price,description,category,created_at,discount,size,color):
        print("asdsad")
        id = ObjectId(id)
        print("id oluştu")
        product = self.db.find_one({'_id':id})
        print("product oluştu")
        self.db.update_one({'_id':id} , {"$set": {"title":title , "price":price , "description":description, "category":category , "created_at":created_at , "discount":discount , "size": size , "color":color}})
        return {
            "id":str(ObjectId(product['_id'])),
            "title":product['title'],
            "price":product['price'],
            "description":product['description'],
            "category":product['category'],
            "created_at": product['created_at'],
            "discount": product['discount'],
            "size":product['size'],
            "color":product['color']
        }