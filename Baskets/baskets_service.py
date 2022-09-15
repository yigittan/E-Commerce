from bson.objectid import ObjectId

class BasketService:
    def __init__(self,baskets_storage):
        self.baskets_storage= baskets_storage

    def create(self,id):
        return self.baskets_storage.insert(str(ObjectId(id)))

    def get_by_id(self,id):
        basket = self.baskets_storage.get_by_id(id)
        if basket is None:
            return {'message':"Basket not found"}
        return basket

    def add_to_basket(self,id,product_id):
        basket = self.baskets_storage.get_by_id(id)
        product = product_service.get_by_id(product_id)
        if basket and product is None:
            return {'message':"basket or product is not found"}
        basket_prdoducts = self.baskets_storage.add_to_basket(id,product_id) 
        return basket_prdoducts