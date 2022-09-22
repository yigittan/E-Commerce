from bson.objectid import ObjectId

class ProductMongoStorage:
    def __init__(self,client):
        self.db = client.db.products

    def insert(self,product):
        res = self.db.insert_one({
            "name":product.name,
            "price":product.price,
            "brand":product.brand,
            "description":product.description,
            "category":product.category,
            "created_at":product.created_at,
            "discount":product.discount,
            "size":product.size,
            "color":product.color
            
        })
        return str(res.inserted_id)
    
    def get_all_products(self):
        products = self.db.find()
        return [{
            "id":str(product['_id']),
            "name":product['name'],
            "price":product['price'],
            "brand":product['brand'],
            "description":product['description'],
            "category":product['category'],
            "created_at":product['created_at'],
            "discount":product['discount'],
            "size":product['size'],
            "color":product['color']
        } for product in products]

    def get_by_id(self,product_id):
        product = self.db.find_one({'_id':ObjectId(product_id)})
        return {
            "id":str(product['_id']),
            "name":product['name'],
            "price":product['price'],
            "brand":product['brand'],
            "description":product['description'],
            "created_at":product['created_at'],
            "discount":product['discount'],
            "size":product['size'],
            "color":product['color']
        }

    def update(self,product,product_id):
        self.db.update_one({'_id':ObjectId(product_id)} , {"$set": {"name":product.name , "price":product.price ,"brand":product.brand , "description":product.description , "category":product.category, "created_at":product.created_at, "discount":product.discount,"size":product.size,"color":product.color}})
        product = self.get_by_id(product_id)
        return {
            "name":product['name'],
            "price":product['price'],
            "brand":product['brand'],
            "description":product['description'],
            "created_at":product['created_at'],
            "discount":product['discount'],
            "size":product['size'],
            "color":product['color']
        }

    def remove(self,product_id):
        self.db.delete_one({'_id':ObjectId(product_id)})
        return product_id

    def filter(self,key,value):
        products = self.db.find({key:value})
        array =  [{
            "name":product['name'],
            "price":product['price'],
            "description":product['description'],
            "brand":product['brand'],
            "created_at":product['created_at'],
            "discount":product['discount'],
            "size":product['size'],
            "color":product['color']
        } for product in products]

        if len(array)>0:
            return array
        else:
            return {'messages':'Aradığınız kriterde ürün bulunamadı'}

    

       