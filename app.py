from flask import Flask, request, jsonify , session
from flask_pymongo import PyMongo
from products.products_service import ProductService
from products.products_storage import ProductMongoStorage
from baskets.baskets_service import BasketService
from baskets.baskets_storage import BasketMongoStorage
from users.users_service import UserService
from users.users_storage import UsersMongoStorage
from users.User import User
from products.Product import Product
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)

client = PyMongo(app, uri="mongodb://localhost:27017/Commerce")

p_storage = ProductMongoStorage(client)
products_service = ProductService(p_storage)
b_storage = BasketMongoStorage(client)
baskets_service = BasketService(b_storage)
u_storage = UsersMongoStorage(client)
users_service = UserService(u_storage)

def loginUser(email):
    user = users_service.getUser_by_email(email)
    session['logged_in'] = True
    session['email'] = email
    session['id'] = user['_id']


@app.route('/')
def index():
    return {'messages': "You Are At Index Page :)"}

# KULLANICI KAYDI REGİSTER

@app.route('/register', methods=['POST'])
def register():
    body = request.get_json()
    name = body['name']
    surname = body['surname']
    username = body['username']
    email = body['email']
    password = body['password']
    city = body['city']
    zip_code = body['zip_code']
    street = body['street']
    building = body['building']
    user = User(name, surname, username, email, password,
                city, zip_code, street, building)
    res = users_service.create(user)
    baskets_service.create(res)
    return res

# KULLANICI GİRİŞİ LOG İN

@app.route('/login',methods=['POST'])
def login():
    body = request.get_json()
    email = body['email']
    candidatePassword = body['password']
    user = users_service.getUser_by_email(email)
    if (user):
        if (users_service.check_password(email,candidatePassword)):
            loginUser(email)
            return jsonify({'messages':'Log in is success'})
        else:
            return jsonify({'messages':"log in is failed"})

@app.route('/products' , methods=['GET','POST'])
def products():
    if request.method == 'GET':
        products = products_service.get_all_products()
        if products is None:
            return {'message':'Products not found'}
        return jsonify(products)
    if request.method == 'POST':
        body = request.get_json()
        name = body['name']
        price = body['price']
        description = body['description']
        created_at = datetime.now()
        discount = body['discount']
        size = body['size']
        color = body['color']
        product = Product(name,price,description,created_at,discount,size,color)
        res = products_service.create(product)
        return jsonify(res)


if __name__ == '__main__':
    app.secret_key = 'secret_key'
    app.run(debug=True, host="127.0.0.1", port=3000)
