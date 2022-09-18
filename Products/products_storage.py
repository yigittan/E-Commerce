from bson.objectid import ObjectId

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

    def get_by_category(self,category):
        products = self.db.find()
        liste = []
        for product in products:
            if product['category'] == category:
                liste.append(product)
        if len(liste) ==0:
            return {'messages':"Category not found"}
        else:
            return [{
                "id":str(ObjectId(item['_id'])),
                "title":item['title'],
                "price":item['price'],
                "description":item['description'],
                "category":item['category'],
                "created_at":item['created_at'],
                "discount":item['discount'],
                "size":item['size'],
                "color":item['color']
            } for item in liste]
                    



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