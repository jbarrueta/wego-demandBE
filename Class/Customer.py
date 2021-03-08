from config.mongoConnect import mongoConnect
import bcrypt


class Customer:
    def __init__(self, email, first_name=None, last_name=None, password=None):
        self.first_name = first_name
        self.last_name = last_name
        # TODO: somehow we will need to verify email does not exist in our database
        self.email = email
        self.password = hashPassword(password)
    

    def getFirstName(self):
        return self.first_name

    def setFirstName(self, first_name):
        self.first_name = first_name
    
    def getLastName(self):
        return  self.last_name

    def setLastName(self, last_name):
        self.last_name = last_name

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
                response = {"status": "OK", "data": {"email": self.email, 'fName': self.first_name, 'lName': self.last_name, "id": customerID}}
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
                self.setFirstName(user['first_name'])
                self.setLastName(user['last_name'])
                response = {"status": "OK", "data": {"email": self.email, 'fName': self.first_name, 'lName': self.last_name, "id": user["_id"]}}
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
def hashPassword(password):

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    print(hashed)
       
    return hashed
