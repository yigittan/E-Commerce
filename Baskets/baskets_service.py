
class BasketService:
    def __init__(self,baskets_storage,product_storage):
        self.baskets_storage= baskets_storage
        self.product_storage = product_storage

    def create(self,id):
        return self.baskets_storage.insert(id)

    def get_by_id(self,id):
        basket = self.baskets_storage.get_by_id(id)
        if basket is None:
            return {'message':"Basket not found"}
        return basket

    def add_to_basket(self,basket_id,product_id):
        basket = self.baskets_storage.add_to_basket(basket_id,product_id)
        return basket

    def delete_from_basket(self,basket_id,product_id):
        basket = self.baskets_storage.delete_from_basket(basket_id,product_id)
        return basket

    def delete_all(self,basket_id):
        basket = self.baskets_storage.delete_all(basket_id)
        return basket