import sys
sys.path.append("..")
# Unit test for Customer Class
from classes.order import Order
import unittest



validService1 = "pet2vet"
validService2 = "pharma"
validPickup1 = "2501 Leon St. Austin, Texas"
validPickup2 = "2518 Leon St. Austin, Texas"
validDropoff1 = "3527 Durhill St. Houston, Texas"
validDropoff2 = "3518 Durhill St. Houston, Texas"
validCustomerId1 = "60484c83e5f472f4ff46714e"
validCustomerId2 = "604d74914f823dc82af15b77"
validStatus1 = "vehicle on route"
validRoute1 = [["97.332", "30.556"]]
validRoute2 = None

invalidService1 = 1
invalidService2 = 33
invalidPickup1 = 1
invalidPickup2 = ""
invalidDropoff1 = ""
invalidDropoff2 = 1299
invalidCustomerId1 = ""
invalidCustomerId2 = "wowow"
invalidStatus1 = "this is not right"
invalidStatus2 = "pending conf"

class TestOrder(unittest.TestCase):

    def test_valid_order_1(self):
        validOrder1 = Order(validService1, validPickup1, validDropoff1, validCustomerId1, route=validRoute1)
        orderObj = validOrder1.__dict__
        match = {'serviceType': validService1, 'pickupAddress': validPickup1, "dropoffAddress": validDropoff1, "customerId": validCustomerId1, "route": validRoute1, "status": "pending confirmation"}
        self.assertEqual(orderObj, match, msg=f"orderObj does not match\n\norderObj: {orderObj}\n\ncorrect: {match}")
    
    def test_valid_order_2(self):
        validOrder2 = Order(validService2, validPickup2, validDropoff2, validCustomerId2)
        orderObj = validOrder2.__dict__
        match = {'serviceType': validService2, 'pickupAddress': validPickup2, "dropoffAddress": validDropoff2, "customerId": validCustomerId2, "route": None, "status": "pending confirmation"}
        self.assertEqual(orderObj, match, msg=f"orderObj does not match\n\norderObj: {orderObj}\n\ncorrect: {match}")
    
    def test_invalid_order_1(self):
        with self.assertRaises(ValueError, msg="Values passed should have raised a Value Error"):
            Order(invalidService1, invalidPickup1, invalidDropoff1, invalidCustomerId1, invalidStatus1)            
    
    def test_invalid_order_2(self):
        with self.assertRaises(ValueError, msg="Values passed should have raised a Value Error"):
            Order(invalidService2, invalidPickup2, invalidDropoff2, invalidCustomerId2, invalidStatus2)

class TestOrderSetters(TestOrder):
    def test_valid_customerId_setter(self):
        order = Order()
        order.setCustomerId(validCustomerId1)
        correctValue = validCustomerId1
        self.assertEqual(order.getCustomerId(), correctValue, msg=f"Error in the customerId setter and getter values:\n\n{order.getCustomerId()}\n\n{correctValue}")

    def test_invalid_customerId_setter(self):
        with self.assertRaises(ValueError, msg="Values passed should have raised a Value Error"):
                order = Order() 
                order.setCustomerId(invalidCustomerId1)

    def test_valid_status_setter(self):
        order = Order()
        order.setStatus(validStatus1)
        correctValue = validStatus1
        self.assertEqual(order.getStatus(), correctValue, msg=f"Error in the email setter and getter values:\n\n{order.getStatus()}\n\n{correctValue}")

    def test_invalid_status_setter(self):
        with self.assertRaises(ValueError, msg="Values passed should have raised a Value Error"):
                order = Order() 
                order.setStatus(invalidStatus1)
    
if __name__ == '__main__':
    unittest.main()