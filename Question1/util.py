data = ""
def sort_by_availability(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if data[j]['availability'] > data[j + 1]['availability']:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data




def sort_by_discount(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if data[j]['discount'] > data[j + 1]['discount']:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data



def sort_by_price(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if data[j]['price'] > data[j + 1]['price']:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data



def sort_by_product_name(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if data[j]['productName'] > data[j + 1]['productName']:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data



def sort_by_rating(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if data[j]['rating'] < data[j + 1]['rating']:  
                data[j], data[j + 1] = data[j + 1], data[j]
    return data




def filter_by_availability(data, availability):
    if availability is None:
        return data
    
    filtered_data = []
    for item in data:
        if item['availability'] == availability:
            filtered_data.append(item)
    
    return filtered_data

def filter_by_discount(data, discount):
    if discount is None:
        return data
    
    filtered_data = []
    for item in data:
        if item['discount'] == discount:
            filtered_data.append(item)
    
    return filtered_data

def filter_by_price(data, price):
    if price is None:
        return data
    
    filtered_data = []
    for item in data:
        if item['price'] == price:
            filtered_data.append(item)
    
    return filtered_data

def filter_by_product_name(data, productName):
    if productName is None:
        return data
    
    filtered_data = []
    for item in data:
        if item['productName'] == productName:
            filtered_data.append(item)
    
    return filtered_data

def filter_by_rating(data, rating):
    if rating is None:
        return data
    
    filtered_data = []
    for item in data:
        if item['rating'] == rating:
            filtered_data.append(item)
    
    return filtered_data
