import re


class Order:
    def __init__(self, serviceType=None, pickupAddress=None, dropoffAddress=None, customerId=None,  status="pending confirmation", route=None):
        if serviceType != None:
            self.setServiceType(serviceType) 
        if pickupAddress != None:
            self.setPickupAddress(pickupAddress)
        if dropoffAddress != None:
            self.setDropoffAddress(dropoffAddress)
        if customerId != None:
            self.setCustomerId(customerId)
        self.route = route
        if status != None:
            self.setStatus(status)

    def setServiceType(self, serciveType):
        if isValidStringInput(serciveType):
            self.serviceType = serciveType
        else:
            raise ValueError("Service type must be a string and cannot be blank")
        
    def setPickupAddress(self, pickupAddress):
        if isValidStringInput(pickupAddress):
            self.pickupAddress = pickupAddress
        else:
            raise ValueError("The pickup address entered was not valid!")

    def setDropoffAddress(self, dropoffAddress):
        if isValidStringInput(dropoffAddress):
            self.dropoffAddress = dropoffAddress
        else:
            raise ValueError("The dropoff address entered was not valid!")
        
    def setCustomerId(self, customerId):
        if re.match("[0-9a-fA-F]{24}", customerId):
            self.customerId = customerId
        else:
            raise ValueError("There was an error in assigning customer to the order. Please try again later!")

    def setStatus(self, status):
        if status in ["pending confirmation", "vehicle on route", "arrived", "unfulfilled", "fulfilled"]:
            self.status = status
        else:
            raise ValueError("There was an error in changing the vehicle status. Please try again later!")

    def getServiceType(self):
        return self.serviceType

    def getPickupAddress(self):
        return self.pickupAddress

    def getDropoffAddress(self):
        return self.dropoffAddress

    def getCustomerId(self):
        return self.customerId

    def getStatus(self):
        return self.status

def isValidStringInput(str1):
    if isinstance(str1, str) and len(str1) > 0:
        return True
    return False