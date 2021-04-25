import sys
sys.path.append("..")
# Unit test for Customer Class
from classes.customer import Customer
import unittest



validEmail1 = "johndoe@email.com"
validEmail2 = "janedoe@gmail.edu"
validFirstName1 = "John"
validFirstName2 = "Jane"
validLastName1 = "Doe"
validLastName2 = "Doe"
validPassword1 = "ValidPassword1234"
validPassword2 = "MySecret987!"

invalidEmail1 = "notemail@"
invalidEmail2 = "wrong@blah."
invalidFirstName1 = ""
invalidFirstName2 = 19348
invalidLastName1 = ""
invalidLastName2 = 1299
invalidPassword1 = "password"
invalidPassword2 = "test1234"

class TestCustomer(unittest.TestCase):

    def test_valid_user_1(self):
        validUser1 = Customer(validEmail1, validFirstName1, validLastName1, validPassword1)
        registerObj = validUser1.get_register_data()
        match = {'email': validEmail1, 'first_name': validFirstName1, "last_name": validLastName1, "password": validPassword1}
        self.assertEqual(registerObj, match, msg=f"registerObj does not match\n\nregisterObj: {registerObj}\n\ncorrect: {match}")
    
    def test_valid_user_2(self):
        validUser2 = Customer(validEmail2, validFirstName2, validLastName2, validPassword2)
        registerObj = validUser2.get_register_data()
        match = {'email': validEmail2, 'first_name': validFirstName2, "last_name": validLastName2, "password": validPassword2}
        self.assertEqual(registerObj, match, msg=f"registerObj does not match\n\nregisterObj: {registerObj}\n\ncorrect: {match}")
    
    def test_invalid_user_1(self):
        with self.assertRaises(ValueError, msg="Values passed should have raised a Value Error"):
            Customer(invalidEmail1, invalidFirstName1, invalidLastName1, invalidPassword1)            
    
    def test_invalid_user_2(self):
        with self.assertRaises(ValueError, msg="Values passed should have raised a Value Error"):
            Customer(invalidEmail2, invalidFirstName2, invalidLastName2, invalidPassword2)

class TestCustomerSetters(TestCustomer):
    def test_email_setter_1(self):
        user = Customer()
        user.setEmail(validEmail1)
        correctValue = validEmail1
        self.assertEqual(Customer.getEmail(), correctValue, msg=f"Error in the email setter and getter values:\n\n{Customer.getEmail()}\n\n{correctValue}")

    def test_invalid_email_setter_1(self):
        with self.assertRaises(ValueError, msg="Values passed should have raised a Value Error"):
                user = Customer() 
                user.setEmail(invalidEmail1)
    
if __name__ == '__main__':
    unittest.main()


# class TestInit(TestCustomer):
#     def test_email(self):
#         self.assertEqual(self.customer.email, "test@test.com")

#     def test_first_name(self):
#         self.assertEqual(self.customer.first_name, "Testf")

#     def test_last_name(self):
#         self.assertEqual(self.customer.last_name, "Testl")

#     def test_password(self):
#         self.assertEqual(self.customer.password, "testpass")


# class TestFirstLastName(TestCustomer):
#     # test get set first name
#     def test_get_first_name(self):
#         self.assertEqual(self.customer.getFirstName(), "Testf")

#     def test_set_first_name(self):
#         self.customer.setFirstName("newfirstName")
#         self.assertEqual(self.customer.getFirstName(), "newfirstName")

#     # test get set last name
#     def test_get_last_name(self):
#         self.assertEqual(self.customer.getLastName(), "Testl")

#     def test_set_last_name(self):
#         self.customer.setLastName("newlastName")
#         self.assertEqual(self.customer.getLastName(), "newlastName")


# class TestEmailPass(TestCustomer):
#     def test_get_email(self):
#         self.assertEqual(self.customer.getEmail(), "test@test.com")

#     def test_set_email(self):
#         self.customer.setEmail("new@new.com")
#         self.assertEqual(self.customer.getEmail(), "new@new.com")

#     def test_set_pass(self):
#         self.customer.setPassword("newpass")
#         self.assertEqual(self.customer.password, "newpass")


# class TestGetRegisterLoginData(TestCustomer):
#     def test_get_register_data(self):
#         registerData = {'email': "test@test.com", 'first_name': "Testf",
#                         "last_name": "Testl", "password": "testpass"}
#         self.assertEqual(self.customer.get_register_data(), registerData)

#     def test_get_login_data(self):
#         self.assertEqual(self.customer.get_login_data(),
#                          ("test@test.com", "testpass"))


