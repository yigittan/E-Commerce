from unicodedata import category
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

#  ÜRÜNLERİ LİSTELEMEK VE ÜRÜN EKLEMEK İÇİN

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
        brand = body['brand']
        description = body['description']
        category = body['category']
        created_at = datetime.now()
        discount = body['discount']
        size = body['size']
        color = body['color']
        product = Product(name,price,brand,description,category,created_at,discount,size,color)
        res = products_service.create(product)
        return jsonify(res)

@app.route('/products/filter')
def params():
    brand = request.args['brand']
    products = products_service.filter(brand)
    return jsonify(products)

@app.route('/products/<string:product_id>' , methods=['GET','PUT','DELETE'])
def productss(product_id):
    if request.method == 'GET':
        product = products_service.get_by_id(product_id)
        return jsonify(product)
    
    if request.method == 'PUT':
        body = request.get_json()
        name = body['name']
        price = body['price']
        brand= body['brand']
        description = body['description']
        category = body['category']
        created_at = datetime.now()
        discount = body['discount']
        size = body['size']
        color = body['color']
        product = Product(name,price,brand,description,category,created_at,discount,size,color)
        res = products_service.update(product,product_id)
        return jsonify(res)

    if request.method == 'DELETE':
        return products_service.remove(product_id)

@app.route('/users/<string:user_id>' , methods=['GET','DELETE','PUT'])
def users(user_id):
    if request.method == 'GET':
        user = users_service.get_by_id(user_id)
        return jsonify(user)

    if request.method == 'PUT':
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
        res = users_service.update(user,user_id)
        return jsonify(res)

    if request.method == 'DELETE':
        return users_service.remove(user_id)

@app.route('/baskets<string:basket_id>' , methods=['GET'])
def basket(basket_id):
    if request.method == 'GET':
        basket = baskets_service.get_by_id(basket_id)
        return jsonify(basket)

@app.route('/baskets/<string:basket_id>/products/<string:product_id>' , methods=['POST','DELETE'])
def basket_cd(basket_id,product_id):
    if request.method == 'POST':
        basket = baskets_service.add(basket_id,product_id)
        return jsonify(basket['products'])

    if request.method == 'DELETE':
        basket = baskets_service.remove(basket_id,product_id)
        return jsonify(basket)

@app.route('/baskets/<string:basket_id>' , methods=['DELETE'])
def basket_clear(basket_id):
    basket  = baskets_service.clear(basket_id)
    return jsonify(basket)

    
    



if __name__ == '__main__':
    app.secret_key = 'secret_key'
    app.run(debug=True, host="127.0.0.1", port=3000)
