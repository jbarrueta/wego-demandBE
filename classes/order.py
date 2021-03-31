class Order:
    def __init__(self, serviceType, pickupAddress, dropoffAddress, customerId,  status="pending confirmation"):
        self.serviceType = serviceType
        self.pickupAddress = pickupAddress
        self.dropoffAddress = dropoffAddress
        self.customerId = customerId
        self.status = status

    def setStatus(self, status):
        self.status = status

    def getStatus(self):
        return self.status