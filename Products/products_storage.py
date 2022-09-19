class ProductMongoStorage:
    def __init__(self,client):
        self.db = client.db.products

    def insert(self,product):
        res = self.db.insert_one({
            "name":product.name,
            "price":product.price,
            "description":product.description,
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
            "description":product['description'],
            "created_at":product['created_at'],
            "discount":product['discount'],
            "size":product['size'],
            "color":product['color']
        } for product in products]

    
