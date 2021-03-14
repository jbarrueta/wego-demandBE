# Unit test for Customer Class
import sys
import unittest
sys.path.append("..")
from Class.Customer import Customer

class TestCustomer(unittest.TestCase):
      def setUp(self):
          self.customer = Customer("test@test.com", "Testf", "Testl", "testpass")
 
 
class TestInit(TestCustomer):
    def test_email(self):
        self.assertEqual(self.customer.email, "test@test.com")
 
    def test_first_name(self):
        self.assertEqual(self.customer.first_name, "Testf")
 
    def test_last_name(self):
        self.assertEqual(self.customer.last_name, "Testl")
 
    def test_password(self):
        self.assertEqual(self.customer.password, "testpass")
 
 
class TestFirstLastName(TestCustomer):
    # test get set first name
    def test_get_first_name(self):
        self.assertEqual(self.customer.getFirstName(), "Testf")
    
    def test_set_first_name(self):
        self.customer.setFirstName("newfname")
        self.assertEqual(self.customer.getFirstName(), "newfname")
    
    # test get set last name
    def test_get_last_name(self):
        self.assertEqual(self.customer.getLastName(), "Testl")
    
    def test_set_last_name(self):
        self.customer.setLastName("newlname")
        self.assertEqual(self.customer.getLastName(), "newlname")
    
class TestEmailPass(TestCustomer):
    def test_get_email(self):
        self.assertEqual(self.customer.getEmail(), "test@test.com")
    
    def test_set_email(self):
        self.customer.setEmail("new@new.com")
        self.assertEqual(self.customer.getEmail(), "new@new.com")
    
    def test_set_pass(self):
        self.customer.setPassword("newpass")
        self.assertEqual(self.customer.password, "newpass")

class TestGetRegisterLoginData(TestCustomer):
    def test_get_register_data(self):
        registerData = {'email' : "test@test.com", 'first_name' : "Testf", "last_name": "Testl", "password" : "testpass"}
        self.assertEqual(self.customer.get_register_data(), registerData)
    
    def test_get_login_data(self):
        self.assertEqual(self.customer.get_login_data(), ("test@test.com", "testpass"))

if __name__ == '__main__':
    unittest.main()