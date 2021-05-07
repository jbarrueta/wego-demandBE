import sys
sys.path.append("..")
from classes.customer import Customer
import unittest
# Unit test for Customer Class


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
        validUser1 = Customer(validEmail1, validFirstName1,
                              validLastName1, validPassword1)
        registerObj = validUser1.get_register_data()
        match = {'email': validEmail1, 'first_name': validFirstName1,
                 "last_name": validLastName1, "password": validPassword1}
        self.assertEqual(
            registerObj, match, msg=f"registerObj does not match\n\nregisterObj: {registerObj}\n\ncorrect: {match}")

    def test_valid_user_2(self):
        validUser2 = Customer(validEmail2, validFirstName2,
                              validLastName2, validPassword2)
        registerObj = validUser2.get_register_data()
        match = {'email': validEmail2, 'first_name': validFirstName2,
                 "last_name": validLastName2, "password": validPassword2}
        self.assertEqual(
            registerObj, match, msg=f"registerObj does not match\n\nregisterObj: {registerObj}\n\ncorrect: {match}")

    def test_invalid_user_1(self):
        with self.assertRaises(ValueError, msg="Values passed should have raised a Value Error"):
            Customer(invalidEmail1, invalidFirstName1,
                     invalidLastName1, invalidPassword1)

    def test_invalid_user_2(self):
        with self.assertRaises(ValueError, msg="Values passed should have raised a Value Error"):
            Customer(invalidEmail2, invalidFirstName2,
                     invalidLastName2, invalidPassword2)


class TestCustomerSetters(TestCustomer):
    def test_email_setter_1(self):
        user = Customer()
        user.setEmail(validEmail1)
        correctValue = validEmail1
        self.assertEqual(user.getEmail(), correctValue, msg=f"Error in the email setter and getter values:\n\n{user.getEmail()}\n\n{correctValue}")

    def test_invalid_email_setter_1(self):
        with self.assertRaises(ValueError, msg="Values passed should have raised a Value Error"):
            user = Customer()
            user.setEmail(invalidEmail1)


if __name__ == '__main__':
    unittest.main()
