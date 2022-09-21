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

    def filter(self,first,second):
        products = self.db.find({f'{first}':f'{second}'})
        array =  [{
            "name":product['name'],
            "price":product['price'],
            "description":product['description'],
            "created_at":product['created_at'],
            "discount":product['discount'],
            "size":product['size'],
            "color":product['color']
        } for product in products]

        if len(array)>0:
            return array
        else:
            return {'messages':'Aradığınız kriterde ürün bulunamadı'}


        # if brand:
        #     products_by_brand = self.db.find({'brand':brand})
        #     brand_array =  [{
        #         "name":product['name'],
        #         "price":product['price'],
        #         "brand":product['brand'],
        #         "description":product['description'],
        #         "created_at":product['created_at'],
        #         "discount":product['discount'],
        #         "size":product['size'],
        #         "color":product['color']
        #     } for product in products_by_brand ]
            
        #     if len(brand_array) >0:
        #         return brand_array
        #     else:
        #         print(len(brand_array))
        #         return {'messages':'Aradığınız kriterde sonuç bulunmadı'}
        # if name:
        #     products_by_name = self.db.find({'name':name})
        #     name_array =  [{
        #         "name":product['name'],
        #         "price":product['price'],
        #         "brand":product['brand'],
        #         "description":product['description'],
        #         "created_at":product['created_at'],
        #         "discount":product['discount'],
        #         "size":product['size'],
        #         "color":product['color']
        #     } for product in products_by_name ]
        #     if len(name_array) > 0 :
        #         return name_array
        #     else:
        #         return {'messages':'aradığınız kriterde sonuç bulunamadı'}

        # if color:
        #     products_by_color = self.db.find({'color':color})
        #     color_array = [{
        #         "name":product['name'],
        #         "price":product['price'],
        #         "brand":product['brand'],
        #         "description":product['description'],
        #         "created_at":product['created_at'],
        #         "discount":product['discount'],
        #         "size":product['size'],
        #         "color":product['color']
        #     } for product in products_by_color ]
            
        #     if len(color_array) > 0:
        #         return color_array
        #     else : 
        #         return {'messages':'Aradığınız kriterde sonuç bulunamadı'}
       
    

       