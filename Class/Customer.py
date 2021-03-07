from config.mongoConnect import mongoConnect
import bcrypt


class Customer:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        # TODO: somehow we will need to verify email does not exist in our database
        self.email = email
        # TODO: password will be hashed before saved into instance of object
        # self.password = hashPassword(password)
        self.password = password

    def getFirstName(self):
        return self.first_name
    
    def getLastName(self):
        return  self.last_name

    def registerUser(self):
        response = {}
        try:
            # 2. Open a new database connection
            client = mongoConnect()
            # 3. write data from the database
            db = client.team12_demand
            customer = db.customer
            if (customer.count_documents({"email": self.email}) == 0):
                customerID = customer.insert_one(self.__dict__).inserted_id
                response = {"status": "OK", "data": {"email": self.email, "id": customerID}}
            else:
                response = {"status": "CONFLICT", "data": {"msg": "Email is already registered"}}
            # TODO: create session now
        except Exception as err:
            response = {"status": "INTERNAL_SERVER_ERROR", "data": {"msg": "Server stopped working, please try again later"}}
        return response
    
    def loginUser(self):
        response = {}
        try: 
            client = mongoConnect()
            db = client.team12_demand
            customer = db.customer
            user = customer.find_one({"email": self.email, "password": self.password})
            if (user != None):
                response = {"status": "OK", "data": {"email": self.email, "id": user["_id"]}}
            else:
                response = {"status": "CONFLICT", "data": {"msg": "Credentials incorrect"}}
        except Exception as err:
            response = {"status": "INTERNAL_SERVER_ERROR", "data": {"msg": "Server stopped working, please try again later"}}
        return response

        #     #

        # def createOrder(self):
        #     #

        # def createSession(self):
        #     #
