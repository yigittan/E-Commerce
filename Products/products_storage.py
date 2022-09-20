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
        if product is None:
            return {'messages':'product not found'}
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
        product = self.get_by_id(product_id)
        if product is None:
            return {'messages':'product not found'}
        self.db.delete_one({'_id':ObjectId(product_id)})
        return product_id

    def filter(self,brand,name):
        products_by_brand = self.db.find({'brand':brand})
        brand_array =  [{
            "name":product['name'],
            "price":product['price'],
            "brand":product['brand'],
            "description":product['description'],
            "created_at":product['created_at'],
            "discount":product['discount'],
            "size":product['size'],
            "color":product['color']
        } for product in products_by_brand ]

        products_by_name = self.db.find({'name':name})
        name_array = [{
            "name":product['name'],
            "price":product['price'],
            "brand":product['brand'],
            "description":product['description'],
            "created_at":product['created_at'],
            "discount":product['discount'],
            "size":product['size'],
            "color":product['color']
        } for product in products_by_name
        ]
        
        last_array = brand_array + name_array
        
        return last_array

       