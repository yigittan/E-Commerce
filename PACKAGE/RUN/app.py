from flask import Flask , request, jsonify
from flask_pymongo import PyMongo
from ..Users.users_storage import UsersMongoStorage
from ..Users.users_service import UserService
from ..Customers.customers_storage import CustomerMongoStorage
from ..Customers.customers_service import CustomerService
from ..Baskets.baskets_storage import BasketsMongoStorage
from ..Baskets.baskets_service import BasketService
from ..Products.products_storage import ProductMongoStorage
from ..Products.products_service import ProductService
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)

mongo_client = PyMongo(app,uri="mongodb://localhost:27017/Commerce")

u_storage = UsersMongoStorage(mongo_client)
user_service = UserService(u_storage)
c_storage = CustomerMongoStorage(mongo_client)
customer_service = CustomerService(c_storage)
b_storage = BasketsMongoStorage(mongo_client)
basket_service = BasketService(b_storage)
p_storage = ProductMongoStorage(mongo_client)
product_service = ProductService(p_storage)

STATUS_OK = 200
STATUS_CREATED = 201
STATUS_NO_CONTENT = 204
STATUS_BAD_REQUEST = 400
STATUS_INTERNAL_SERVER_ERROR = 500
STATUS_NOT_FOUND = 404

def http_err_handler(func):

    def create_err_msg(e):
        return {'message':e}

    def handler(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except ValueError as e:
            return create_err_msg(e) , STATUS_BAD_REQUEST
        except Exception as e:
            return create_err_msg(e) , STATUS_INTERNAL_SERVER_ERROR
    return handler


@app.route('/')
def index():
    return {'messages':'You See Index Page'}

@app.route('/signup' , methods=['POST'] , endpoint='signup')
@http_err_handler
def signup():
    body = request.get_json()
    name = body['name']
    email = body['email']
    password = body['password']
    user_id = user_service.create(name,email,password)
    customer_id = customer_service.create(name,email,id=str(ObjectId(user_id)))
    basket_id = basket_service.create(id=str(ObjectId(customer_id)))    
    return {'user_id':str(ObjectId(user_id))} , STATUS_CREATED

@app.route('/products/add' , methods=['POST'] , endpoint = 'add_product')
@http_err_handler
def add_product():
    body = request.get_json()
    title = body['title']
    price = body['price']
    description = body['description']
    category = body['category']
    created_at = datetime.now()
    discount = body['discount']
    size = body['size']
    color = body['color']
    product_id = product_service.create(title,price,description,category,created_at,discount,size,color)
    return {'product_id':str(ObjectId(product_id))} , STATUS_CREATED

@app.route('/products', methods=['GET'], endpoint = 'get_all')
@http_err_handler
def get_all():
    products = product_service.get_all()
    return jsonify(products),STATUS_OK

@app.route('/products/<string:id>' , methods=['GET'], endpoint = 'get_product')
@http_err_handler
def get_product(id):
    product = product_service.get_by_id(id)
    return jsonify(product) , STATUS_OK

@app.route('/products/<string:id>/update' , methods = ['PUT'], endpoint = 'update_product')
@http_err_handler
def update_product(id):
    body = request.get_json()
    title = body['title']
    price = body['price']
    description = body['description']
    category = body['category']
    created_at = datetime.now()
    discount = body['discount']
    size = body['size']
    color = body['color']
    product = product_service.update_product(id,title,price,description,category,created_at,discount,size,color)
    return jsonify(product),STATUS_OK

@app.route('/basket/<string:id>' , methods = ['GET'], endpoint = 'get_basket')
@http_err_handler
def get_basket(id):
    basket = basket_service.get_by_id(id)
    return basket['product']

@app.route('/baskets/<string:id>/add/<string:product_id>' , methods=['POST'],endpoint = 'add_to_basket')
@http_err_handler
def add_to_basket(id,product_id):
    basket_products = basket_service.add_to_basket(id,product_id)
    return basket_products['products']

    


    

if __name__ == '__main__':
    app.secret_key = "1234"
    app.run(debug=True,host="127.0.0.1",port=3000)