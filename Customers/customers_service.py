from bson.objectid import ObjectId


class CustomerService:
    def __init__(self,customers_storage):
        self.customers_storage = customers_storage

    def create(self,name,email,id):
        id = ObjectId(id)
        return self.customers_storage.insert(name,email,id)
    
    def update_customer(self,customer_id,name,email):
        return self.customers_storage.update_customer(customer_id,name,email)

    def set_customer_info(self,customer_id,city,street_no,building_no,phone_no):
        return self.customers_storage.set_customer_info(customer_id,city,street_no,building_no,phone_no)

    def update_customer_info(self,customer_id,city,street_no,building_no,phone_no):
        return self.customers_storage.update_customer_info(customer_id,city,street_no,building_no,phone_no)