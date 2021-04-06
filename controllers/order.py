import logging
from classes.order import Order
from mongo.mongoConfig import mongoConnect

def requestOrder(orderObj):
    response = {}
    try:
        client = mongoConnect()
        db = client.team12_demand
        orders = db.orders
        publicId = orders.count_documents({}) + 1000
        orderObj["pulbicId"] = publicId
        orderId = orders.insert_one(orderObj).inserted_id
        response = {'status': 'OK', 'data': {
                "id": orderId, "publicId": publicId, "status": orderObj["status"]}}
    except Exception as err:
        logging.error(err)
        response = {'status': 'INTERNAL_SERVER_ERROR', 'data': {
            'msg': 'Server stopped working, please try again later'}}

    return response 

def getOrders(customerId):
    response = {}
    try:
        client = mongoConnect()
        db = client.team12_demand
        orders = db.orders

        orderList = orders.find({"customerId": customerId}).limit(7)
        logging.debug(orderList)
        response = {'status': "OK", 'data': orderList}

    except Exception as err:
        logging.error(err)
        response = {'status': "INTERNAL_SERVER_ERROR", 'data' : {'msg': 'Server stopped working, refresh orders again later'}}
    
    return response