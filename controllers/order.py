import json
import logging
from bson.objectid import ObjectId
import requests
from classes.order import Order
from mongo.mongoConfig import mongoConnect


def requestOrder(postBody):
    response = {}
    try:
        order = Order(postBody["serviceType"], postBody["pickupAddress"],
                      postBody["dropoffAddress"], postBody["customerId"])
        orderObj = order.__dict__
        client = mongoConnect()
        db = client.team12_demand
        orders = db.orders
        publicId = orders.count_documents({}) + 1000
        orderObj["publicId"] = publicId
        orderId = orders.insert_one(orderObj).inserted_id
        address1 = (orderObj["pickupAddress"]).replace(" ", "+")
        address2 = (orderObj["dropoffAddress"]).replace(" ", "+")
        routeResponse = requests.get(
            f"https://supply.team12.sweispring21.tk/api/vehicles/req?service_type={orderObj['serviceType']}&order_id={orderId}&customer_id={orderObj['customerId']}&destination={address1}")
        responseObj = routeResponse.json()
        routeObj = responseObj["data"]
        if responseObj['status'] == "OK":
            order.setStatus("vehicle on route")
            response = {'status': responseObj['status'], 'data': {
                "_id": orderId, "publicId": publicId, "status": order.getStatus(), "routeObj": routeObj}}
            dbRouteObj = routeObj
        else:
            response = {
                'status': responseObj['status'], 'data': responseObj['data']}
            order.setStatus("unfulfilled")
            dbRouteObj = routeObj

        orders.update_one({"_id": orderId}, {
                          "$set": {"status": order.getStatus(), "routeObj": dbRouteObj}})
    except ValueError as err:
        response = {'status': 'CONFLICT', 'data': {
            'msg': err
        }}
    except Exception as err:
        logging.error(err)
        response = {'status': 'INTERNAL_SERVER_ERROR', 'data': {
            'msg': 'Server stopped working, please try again later'}}

    return response


def updateOrder(postBody):
    response = {}
    try:
        requestObj = {"vehicle_id": str(
            postBody['vehicle_id']), 'current_location': postBody['current_location'], 'vehicle_status': postBody['vehicle_status']}
        updateResponse = requests.post(
            "https://supply.team12.sweispring21.tk/api/vehicle/update", json.dumps(requestObj))
        responseObj = updateResponse.json()
        updateObj = responseObj["data"]
        client = mongoConnect()
        db = client.team12_demand
        orders = db.orders
        update = orders.update_one({"_id": ObjectId(postBody['order_id'])}, {
            "$set": {"status": postBody['order_status']}})
        response = {'status': responseObj['status'], 'data': updateObj}

    except Exception as err:
        logging.error(err)
        response = {'status': 'INTERNAL_SERVER_ERROR', 'data': {
            'msg': 'Server stopped working, please try again later'}}

    return response


def getOrders(orderParams):
    response = {}
    try:
        client = mongoConnect()
        db = client.team12_demand
        orders = db.orders
        if("_id" in orderParams):
            orderParams['_id'] = ObjectId(orderParams['_id'])
        docs = orders.find(orderParams)
        orderList = []
        for doc in docs:
            orderList.append(doc)
        logging.debug(orderList)
        response = {'status': "OK", 'data': orderList}
    except ValueError as err:
        response = {'status': 'CONFLICT', 'data': {
            'msg': err
        }}
    except Exception as err:
        logging.error(err)
        response = {'status': "INTERNAL_SERVER_ERROR", 'data': {
            'msg': 'Server stopped working, refresh orders again later'}}

    return response
