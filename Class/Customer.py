from config.mongoConnect import mongoConnect


class Customer:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        # TODO: somehow we will need to verify email does not exist in our database
        self.email = email
        # TODO: password will be hashed before saved into instance of object
        self.password = password

    def getName(self):
        return self.first_name + self.last_name

    def registerUser(self):
        # 2. Open a new database connection
        client = mongoConnect()
        # 3. write data from the database
        db = client.team12_demand
        customer = db.customer
        customerID = customer.insert_one(self.__dict__).inserted_id
        print("CustomerID", customerID)

        # TODO: create session now

        data = "build data response"
        return data

        # 4. Store a response using a container like the responseBody defined above

        # def loginUser(self):
        #     #

        # def createOrder(self):
        #     #

        # def createSession(self):
        #     #
