class Customer:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def getName (self):
        return self.first_name + self.last_name
    
    def registerUser(self):
           # Implement your service here
            # 1. Access POST parameters using your postBody
            # 2. Open a new database connection
            # 3. Read or write data from the database
            # 4. Store a response using a container like the responseBody defined above
    
    def loginUser(self):
        #
    
    def createOrder(self):
        #
    
    def createSession(self):
        #
