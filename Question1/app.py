
from flask import Flask, request, jsonify
from os import environ
import server
import util
import json

app = Flask(__name__)
app.config['TOKEN_TYPE'] = environ.get('TOKEN_TYPE')
app.config['ACCESS_TOKEN'] = environ.get('ACCESS_TOKEN')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/categories/<string:category>/products")
def allProducts(category):
    company = request.args.get('company')
    items = int(request.args.get('items'))
    min_price = int(request.args.get('min_price'))
    max_price = int(request.args.get('max_price'))

    availability = request.args.get('availability')
    discount = request.args.get('discount')
    price = request.args.get('price')
    productName = request.args.get('productName')
    rating = request.args.get('rating')

    sort = request.args.get('sort')
    
    if(items > 10):
        page = int(request.args.get('page'))
        if(page is None):
            return "pagination params page is are required"
        else:
            items = 10*page
    
    access_token = app.config['ACCESS_TOKEN']
    response = server.getProducts("AMZ",category,items,min_price,max_price,access_token)
    json.loads(jsonify(response))
    print(response)
    print(response.leng)

    if (sort):
        if availability is not None:
            response = util.sort_by_availability(response)

        if discount is not None:
            response = util.sort_by_discount(response)

        if price is not None:
            response = util.sort_by_price(response)

        if productName is not None:
            response = util.sort_by_product_name(response)

        if rating is not None:
            response = util.sort_by_rating(response)

    if availability is not None:
        availability = str(availability)
        filtered_data = util.filter_by_availability(filtered_data, availability)

    if discount is not None:
        discount = float(discount)
        filtered_data = util.filter_by_discount(filtered_data, discount)

    if price is not None:
        price = float(price)
        filtered_data = util.filter_by_price(filtered_data, price)

    if productName is not None:
        productName = str(productName)
        filtered_data = util.filter_by_product_name(filtered_data, productName)

    if rating is not None:
        rating = float(rating)
        filtered_data = util.filter_by_rating(filtered_data, rating)


    return response

# TODO
@app.route("/categories/<string:category>/products/<int:product_id>")
def Product(category,product_id):
    company = request.args.get('company')
    items = request.args.get('items')
    min_price = request.args.get('min_price')
    max_price = request.args.get('max_price')
    response = server.getProducts("AMZ","Laptop","10","1","10000")
    return response
