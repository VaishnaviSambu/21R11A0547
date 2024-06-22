# File to handle server API'set
from flask import jsonify
import json
import requests


def getProducts(companyName,categoryName,top,mimPrice,maxPrice,access_token):
    # API to get all products
    url ="http://20.244.56.144/test/companies/"+companyName+"/categories/"+categoryName+"/products?top="+str(top)+"&minPrice="+str(mimPrice)+"&maxPrice="+str(maxPrice)

    headers = {
        'Authorization': "Bearer "+ access_token
    }
    response = requests.get(url, headers=headers)

    data = response.json()
    # try:
    print(url)
    print(response)
    print(data)
    # except requests.exceptions.HTTPError as err:
    #     print(f'HTTP error occurred: {err}')
    # except Exception as err:
    #     print(f'Other error occurred: {err}')

    return jsonify(data)


