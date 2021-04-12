import logging
import requests
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
        address1 = (orderObj["pickupAddress"]).replace(" ", "+")
        address2 = (orderObj["dropoffAddress"]).replace(" ", "+")

        #### Comment out this block when supply is up on server ####
        #response = {'status': 'OK', 'data': {
        #        "id": orderId, "publicId": publicId, "status": orderObj["status"]}}
        ########################################################################

        #### Uncomment this block when supply is up on server ####
        # routeResponse = requests.get(f"http://localhost:8081/vehicles/req?service_type={orderObj['serviceType']}&order_id={orderId}&customer_id={orderObj['customerId']}&destination={address1}")
         routeResponse = requests.get(f"https://supply.team12.sweispring21.tk/api/vehicles/req?service_type={orderObj['serviceType']}&order_id={orderId}&customer_id={orderObj['customerId']}&destination={address1}")
         routeObj = routeResponse.json()["data"]
         response = {'status': 'OK', 'data': {
              "id": orderId, "publicId": publicId, "status": orderObj["status"], "routeObj": routeObj}}
        ########################################################################

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