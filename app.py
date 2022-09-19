from flask import Flask , request , jsonify
from flask_pymongo import PyMongo
from products.products_service import ProductService
from products.products_storage import ProductMongoStorage
from baskets.baskets_service import BasketService
from baskets.baskets_storage import BasketMongoStorage
from users.users_service import UserService
from users.users_storage import UsersMongoStorage

app = Flask(__name__)

client = PyMongo(app,uri="mongodb://localhost:27017/Commerce")

p_storage = ProductMongoStorage(client)
products_service = ProductService(p_storage)
b_storage = BasketMongoStorage(client)
baskets_service = BasketService(b_storage)
u_storage = UsersMongoStorage(client)
users_service = UserService(u_storage)

@app.route('/')
def index():
    return {'messages':"You Are At Index Page :)"}
    


if __name__ == '__main__':
    app.secret_key= 'secret_key'
    app.run(debug=True,host="127.0.0.1", port=3000)