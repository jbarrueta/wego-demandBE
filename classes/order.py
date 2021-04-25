import re


class Order:
    def __init__(self, serviceType, pickupAddress, dropoffAddress, customerId,  status="pending confirmation", route=None):
        self.serviceType = serviceType
        self.pickupAddress = pickupAddress
        self.dropoffAddress = dropoffAddress
        self.customerId = customerId
        self.route = route
        self.status = status

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