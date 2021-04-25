import re
# Customer class
class Customer:
    def __init__(self, email, first_name=None, last_name=None, password=None):
        if not(first_name == None or last_name == None):
            self.setFirstName(first_name)
            self.setLastName(last_name)
        self.setEmail(email)
        self.setPassword(password)
    
    def setFirstName(self, first_name):
        if isinstance(first_name, str):
            self.first_name = first_name
        else:
            raise ValueError("First name must be a string and at least 2 characters")

    def setLastName(self, last_name):
        if isinstance(last_name, str):
            self.last_name = last_name
        else:
            raise ValueError("Last name must be a string and at least 2 characters")
    
    def setEmail(self, email):
        if re.match("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$", email):
            self.email = email
        else: 
            raise ValueError("Invalid email passed!")
    
    def setPassword(self, password):
        if(re.match("^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,20}$", password)):
            self.password = password
        else:
            raise ValueError("Passwords must be 6 to 20 characters which contain at least one numeric digit, one uppercase and one lowercase letter")
    
    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def getEmail(self):
        return self.email

    def get_register_data(self):
        return self.__dict__
    
    def get_login_data(self):
        return self.email, self.password


