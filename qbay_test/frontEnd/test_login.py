import random
import selenium
from seleniumbase import BaseCase


from unittest.mock import patch
from qbay.models import User
from qbay_test.conftest import base_url


"""
This file defines all integration tests for the frontend registration.
Testing below covers the 'black box input coverage' testing method.
The 2nd blackbox testing method used is 'input partition' testing method.
If there are repeated test cases between the blackbox testing methods,
the repeated test case has been removed.
The 3rd blackbox testing method used is 'shotgun' testing.
"""


# Contains integration tests for the login page.

# REQUIREMENTS PARTITIONING TESTING / FUNCTIONALITY
# Given a registered user's correct email and password combination,
# the user should be redirected to the home page and logged in.
# R1: Given a valid email and valid password
# R2: Given a registered email and password
# R3: Given a correct combination of a registered email and password
# R4: User is redirected to home page
# R5: User is logged in

# BLACK BOX SHOTGUN TESTING / INPUT COVERAGE
# Register multiple accounts (20+) and ensure each is logged in correctly.


class FrontEndLoginPageTest(BaseCase):

    # TEST CASE 1: LOGIN SUCCESS
    def test_login_success(self, *_):

        # Tests if the user has logged in successfully
        # with a registered account
        # Uses input testing, with partitioning

        # First register the user with valid email and password
        # Correspond to test case an see if success/fail
        self.open(base_url + '/register')
        self.type("#email", "testing01@gmail.com")
        self.type("#name", "Test01")
        self.type("#password", "Testing01!")
        self.type("#password2", "Testing01!")
        self.click('input[type="submit"]')

        # Checks that user is redirected to login page
        # after successful registration
        assert self.get_current_url() == base_url + '/login'

        # Checks if 'Sign in' header is present
        self.assert_text("Sign in", "h2")
        # Checks if line of text is present
        self.assert_text("Enter your email and password", "h4")

        # R1-1, R2-1, R3-1
        # Entered email and password of registered account
        self.type("#email", "testing01@gmail.com")
        self.type("#password", "Testing01!")

        # Clicks 'remember me' button
        self.click('input[type="checkbox"]')

        # Clicks the 'sign in' button
        self.click('input[type="submit"]')

        # R4-1
        # Checks that the user is redirected to the home page

        # R5-1
        # Once user clicked the sign in button,
        # they should be redirected to the home page

    # TEST CASE 2: LOGIN FAIL (incorrect password for email)
    def test_login_fail(self, *_):

        def test_login_fail_1(self, *_):

            # Tests if the user fails to login with incorrect password to email
            # Uses input testing, with partitioning

            # First register the user with valid email and password
            # Correspond to test case an see if success/fail
            self.open(base_url + '/register')
            self.type("#email", "testing02@gmail.com")
            self.type("#name", "Test02")
            self.type("#password", "Testing02!")
            self.type("#password2", "Testing02!")
            self.click('input[type="submit"]')

            # Checks that user is redirected to login page
            # after successful registration
            assert self.get_current_url() == base_url + '/login'

            # Checks if 'Sign in' header is present
            self.assert_text("Sign in", "h2")
            # Checks if line of text is present
            self.assert_text("Enter your email and password", "h4")

            # R1-2, R2-2
            # Enters correct email, but incorrect password
            self.type("#email", "testing02@gmail.com")
            self.type("#password", "Wrong1234!")

            # Clicks 'remember me' button
            self.click('input[type="checkbox"]')

            # Clicks the 'sign in' button
            self.click('input[type="submit"]')

            # Checks that the user is redirected to the login page
            assert self.get_current_url() == base_url + '/login'

            # Should see the flash message at the top of the page
            self.assert_text("Login failed. Please try again.", "h4")

        # TEST CASE 3: LOGIN FAIL (incorrect email for password)
        def test_login_fail_2(self, *_):

            # Tests if the user fails to login with incorrect email to password
            # Uses input testing, with partitioning

            # First register the user with valid email and password
            # Correspond to test case an see if success/fail
            self.open(base_url + '/register')
            self.type("#email", "testing03@gmail.com")
            self.type("#name", "Test03")
            self.type("#password", "Testing03!")
            self.type("#password2", "Testing03!")
            self.click('input[type="submit"]')

            # Checks that user is redirected to login page
            # after successful registration
            assert self.get_current_url() == base_url + '/login'

            # Checks if 'Sign in' header is present
            self.assert_text("Sign in", "h2")
            # Checks if line of text is present
            self.assert_text("Enter your email and password", "h4")

            # R1-3, R2-3
            # Enters incorrect email, but correct password
            self.type("#email", "incorrect@gmail.com")
            self.type("#password", "Testing03!")

            # Clicks 'remember me' button
            self.click('input[type="checkbox"]')

            # Clicks the sign in button
            self.click('input[type="submit"]')

            # Checks that the user is redirected to the login page
            assert self.get_current_url() == base_url + '/login'
            self.assert_text("Login failed. Please try again.", "h4")

        # TEST CASE 4: LOGIN FAIL (account not registered)
        def test_login_fail_3(self, *_):

            # Tests if the user has not registered an account
            # Uses input testing, with partitioning

            # First register the user with valid email and password
            # Correspond to test case an see if success/fail
            self.open(base_url + '/register')
            self.type("#email", "testing04@gmail.com")
            self.type("#name", "Test04")
            self.type("#password", "Testing04!")
            self.type("#password2", "Testing04!")
            self.click('input[type="submit"]')

            # Checks that user is redirected to login page
            # after successful registration
            assert self.get_current_url() == base_url + '/login'

            # Checks if 'Sign in' header is present
            self.assert_text("Sign in", "h2")
            # Checks if line of text is present
            self.assert_text("Enter your email and password", "h4")

            # Enters email and password of an unregistered account
            self.type("#email", "unregistered@gmail.com")
            self.type("#password", "unregistered")

            # Clicks 'remember me' button
            self.click('input[type="checkbox"]')

            # Clicks the 'sign in' button
            self.click('input[type="submit"]')

            # Checks that the user is redirected to the login page
            assert self.get_current_url() == base_url + '/login'
            self.assert_text("Login failed. Please try again.", "h4")

        # TEST CASE 5: LOGIN FAIL (no email entered)
        def test_login_fail_4(self, *_):

            # Tests if the user has not entered an email; only a password
            # Uses input testing, with partitioning
            # Uses equivalence and boundary value testing

            # First register the user with valid email and password
            # Correspond to test case an see if success/fail
            self.open(base_url + '/register')
            self.type("#email", "testing05@gmail.com")
            self.type("#name", "Test05")
            self.type("#password", "Testing05!")
            self.type("#password2", "Testing05!")
            self.click('input[type="submit"]')

            # Checks that user is redirected to login page
            # after successful registration
            assert self.get_current_url() == base_url + '/login'

            # Checks if 'Sign in' header is present
            self.assert_text("Sign in", "h2")
            # Checks if line of text is present
            self.assert_text("Enter your email and password", "h4")

            # R1-4, R2-4
            # Enters password, but no email
            self.type("#email", " ")
            self.type("#password", "Testing05!")

            # Clicks 'remember me' button
            self.click('input[type="checkbox"]')

            # Clicks the 'sign in' button
            self.click('input[type="submit"]')

            # Checks that the user is redirected to the login page
            assert self.get_current_url() == base_url + '/login'
            # Returns 'Internal Server Error' if the user inputs 
            # an invalid email/password format
            self.assert_text("Internal Server Error", "h1")

        # TEST CASE 6: LOGIN FAIL (no password entered)
        def test_login_fail_5(self, *_):

            # Tests if the user has not entered a password; only an email
            # Uses input testing, with partitioning
            # Uses equivalence and boundary value testing

            # First register the user with valid email and password
            # Correspond to test case an see if success/fail
            self.open(base_url + '/register')
            self.type("#email", "testing06@gmail.com")
            self.type("#name", "Test06")
            self.type("#password", "Testing06!")
            self.type("#password2", "Testing06!")
            self.click('input[type="submit"]')

            # Checks that user is redirected to login page
            # after successful registration
            assert self.get_current_url() == base_url + '/login'

            # Checks if 'Sign in' header is present
            self.assert_text("Sign in", "h2")
            # Checks if line of text is present
            self.assert_text("Enter your email and password", "h4")

            # R1-5, R2-5
            # Enters email, but no password
            self.type("#email", "testing06@gmail.com")
            self.type("#password", " ")

            # Clicks 'remember me' button
            self.click('input[type="checkbox"]')

            # Clicks the 'sign in' button
            self.click('input[type="submit"]')

            # Checks that the user is redirected to the login page
            assert self.get_current_url() == base_url + '/login'
            self.assert_text("Login failed. Please try again.", "h4")

        # TEST CASE 7: LOGIN FAIL (no email and password entered)
        def test_login_fail_6(self, *_):

            # Tests if the user has not entered an email or password
            # Uses input testing, with partitioning
            # Uses equivalence and boundary value testing

            # First register the user with valid email and password
            # Correspond to test case an see if success/fail
            self.open(base_url + '/register')
            self.type("#email", "testing07@gmail.com")
            self.type("#name", "Test07")
            self.type("#password", "Testing07!")
            self.type("#password2", "Testing07!")
            self.click('input[type="submit"]')

            # Checks that user is redirected to login page
            # after successful registration
            assert self.get_current_url() == base_url + '/login'

            # Checks if 'Sign in' header is present
            self.assert_text("Sign in", "h2")
            # Checks if line of text is present
            self.assert_text("Enter your email and password", "h4")

            # R1-6, R2-6
            # Enters no email and no password
            self.type("#email", " ")
            self.type("#password", " ")

            # Clicks 'remember me' button
            self.click('input[type="checkbox"]')

            # Clicks the 'sign in' button
            self.click('input[type="submit"]')

            # Checks that the user is redirected to the login page
            assert self.get_current_url() == base_url + '/login'
            self.assert_text("Login failed. Please try again.", "h4")

        # Test Case 8: LOGIN FAIL (minimum password length)
        def test_login_fail_7(self, *_):

            # Tests if the user has entered a password
            # that is less than 6 characters
            # Uses input testing, with partitioning
            # Uses equivalence and boundary value testing

            # First register the user with valid email and password
            # Correspond to test case an see if success/fail
            self.open(base_url + '/register')
            self.type("#email", "testing08@gmail.com")
            self.type("#name", "Test08")
            self.type("#password", "Testing08!")
            self.type("#password2", "Testing08!")
            self.click('input[type="submit"]')

            # Checks that user is redirected to login page
            # after successful registration
            assert self.get_current_url() == base_url + '/login'

            # Checks if 'Sign in' header is present
            self.assert_text("Sign in", "h2")
            # Checks if line of text is present
            self.assert_text("Enter your email and password", "h4")

            # R1-7, R2-7
            # Enters valid email and password that is less than 6 characters
            self.type("#email", "testing08@gmail.com")
            self.type("#password", "Test8")

            # Clicks 'remember me' button
            self.click('input[type="checkbox"]')

            # Clicks the 'sign in' button
            self.click('input[type="submit"]')

            # Checks that the user is redirected to the login page

            self.assert_text("Login failed. Please try again.", "h4")

        # Test Case 9: LOGIN FAIL (invalid email format; missing email ID)

        def test_login_fail_8(self, *_):

            # Tests if the user has entered an invalid email format
            # Uses input testing, with partitioning
            # Uses equivalence and boundary value testing

            # First register the user with valid email and password
            # Correspond to test case an see if success/fail
            self.open(base_url + '/register')
            self.type("#email", "testing09@gmail.com")
            self.type("#name", "Test09")
            self.type("#password", "Testing09!")
            self.type("#password2", "Testing09!")
            self.click('input[type="submit"]')

            # Checks that user is redirected to login page
            # after successful registration
            assert self.get_current_url() == base_url + '/login'

            # Checks if 'Sign in' header is present
            self.assert_text("Sign in", "h2")
            # Checks if line of text is present
            self.assert_text("Enter your email and password", "h4")

            # R2-8
            # Enters email without an email ID and valid password
            self.type("#email", "@gmail.com")
            self.type("#password", "Testing09!")

            # Clicks 'remember me' button
            self.click('input[type="checkbox"]')

            # Clicks the 'sign in' button
            self.click('input[type="submit"]')

            # Checks that the user is redirected to the login page
            assert self.get_current_url() == base_url + '/login'

            # Should see the flash message at the top of the page
            # Returns 'Internal Server Error' if the user inputs an 
            # invalid email/password format
            self.assert_text("Internal Server Error", "h1")

        # Test Case 10: LOGIN FAIL (invalid email format; missing @ symbol)
        def test_login_fail_9(self, *_):

            # Tests if the user has entered an invalid email format
            # Uses input testing, with partitioning
            # Uses equivalence and boundary value testing

            # First register the user with valid email and password
            # Correspond to test case an see if success/fail
            self.open(base_url + '/register')
            self.type("#email", "testing10@gmail.com")
            self.type("#name", "Test10")
            self.type("#password", "Testing10!")
            self.type("#password2", "Testing10!")
            self.click('input[type="submit"]')

            # Checks that user is redirected to login page
            # after successful registration
            assert self.get_current_url() == base_url + '/login'

            # Checks if 'Sign in' header is present
            self.assert_text("Sign in", "h2")
            # Checks if line of text is present
            self.assert_text("Enter your email and password", "h4")

            # R2-9
            # Enters email that is missing '@' symbol and valid password
            self.type("#email", "testing10gmail.com")
            self.type("#password", "Testing10!")

            # Clicks 'remember me' button
            self.click('input[type="checkbox"]')

            # Clicks the 'sign in' button
            self.click('input[type="submit"]')

            # Checks that the user is redirected to the login page
            assert self.get_current_url() == base_url + '/login'

            # Should see the flash message at the top of the page
            # Returns 'Internal Server Error' if the user inputs an 
            # invalid email/password format
            self.assert_text("Internal Server Error", "h1")

        # Test Case 11: LOGIN FAIL (invalid password format;
        # missing uppercase letter)
        def test_login_fail_10(self, *_):

            # Tests if the user has entered an invalid email format
            # Uses input testing, with partitioning
            # Uses equivalence and boundary value testing

            # First register the user with valid email and password
            # Correspond to test case an see if success/fail
            self.open(base_url + '/register')
            self.type("#email", "testing11@gmail.com")
            self.type("#name", "Test11")
            self.type("#password", "Testing11!")
            self.type("#password2", "Testing11!")
            self.click('input[type="submit"]')

            # Checks that user is redirected to login page
            # after successful registration
            assert self.get_current_url() == base_url + '/login'

            # Checks if 'Sign in' header is present
            self.assert_text("Sign in", "h2")
            # Checks if line of text is present
            self.assert_text("Enter your email and password", "h4")

            # R2-10
            # Enters valid email and password
            # that is missing an uppercase letter
            self.type("#email", "testing11@gmail.com")
            self.type("#password", "testing11!")

            # Clicks 'remember me' button
            self.click('input[type="checkbox"]')

            # Clicks the 'sign in' button
            self.click('input[type="submit"]')

            # Checks that the user is redirected to the login page
            assert self.get_current_url() == base_url + '/login'
            self.assert_text("Login failed. Please try again.", "h4")

        # Test Case 12: LOGIN FAIL (invalid password format;
        # missing special character)
        def test_login_fail_11(self, *_):

            # Tests if the user has entered an invalid email format
            # Uses input testing, with partitioning
            # Uses equivalence and boundary value testing

            # First register the user with valid email and password
            # Correspond to test case an see if success/fail
            self.open(base_url + '/register')
            self.type("#email", "testing12@gmail.com")
            self.type("#name", "Test12")
            self.type("#password", "Testing12!")
            self.type("#password2", "Testing12!")
            self.click('input[type="submit"]')

            # Checks that user is redirected to login page
            # after successful registration
            assert self.get_current_url() == base_url + '/login'

            # Checks if 'Sign in' header is present
            self.assert_text("Sign in", "h2")
            # Checks if line of text is present
            self.assert_text("Enter your email and password", "h4")

            # R2-11
            # Enters valid email and password
            # that is missing a special character
            self.type("#email", "testing12@gmail.com")
            self.type("#password", "Testing12")

            # Clicks 'remember me' button
            self.click('input[type="checkbox"]')

            # Clicks the 'sign in' button
            self.click('input[type="submit"]')

            # Checks that the user is redirected to the login page
            assert self.get_current_url() == base_url + '/login'
            self.assert_text("Login failed. Please try again.", "h4")

        # Test Case 13: LOGIN FAIL (invalid password format;
        # space as prefix)
        def test_login_fail_12(self, *_):

            # Tests if the user has entered an invalid email format
            # Uses input testing, with partitioning
            # Uses equivalence and boundary value testing

            # First register the user with valid email and password
            # Correspond to test case an see if success/fail
            self.open(base_url + '/register')
            self.type("#email", "testing13@gmail.com")
            self.type("#name", "Test13")
            self.type("#password", "Testing13!")
            self.type("#password2", "Testing13!")
            self.click('input[type="submit"]')

            # Checks that user is redirected to login page
            # after successful registration
            assert self.get_current_url() == base_url + '/login'

            # Checks if 'Sign in' header is present
            self.assert_text("Sign in", "h2")

            # Checks if line of text is present
            self.assert_text("Enter your email and password", "h4")

            # R2-12
            # Enters valid email and password
            # containing a space as a prefix
            self.type("#email", "testing13@gmail.com")
            self.type("#password", " Testing13!")

            # Clicks 'remember me' button
            self.click('input[type="checkbox"]')

            # Clicks the 'sign in' button
            self.click('input[type="submit"]')

            # Checks that the user is redirected to the register page
            # Invalid account submission
            assert self.get_current_url() == base_url + '/login'
            self.assert_text("Login failed. Please try again.", "h4")

        # Test Case 14: LOGIN FAIL (invalid password format;
        # space as suffix)
        def test_login_fail_13(self, *_):

            # Tests if the user has entered an invalid email format
            # Uses input testing, with partitioning
            # Uses equivalence and boundary value testing

            # First register the user with valid email and password
            # Correspond to test case an see if success/fail
            self.open(base_url + '/register')
            self.type("#email", "testing14@gmail.com")
            self.type("#name", "Test14")
            self.type("#password", "Testing14!")
            self.type("#password2", "Testing14!")
            self.click('input[type="submit"]')

            # Checks that user is redirected to login page
            # after successful registration
            assert self.get_current_url() == base_url + '/login'

            # Checks if 'Sign in' header is present
            self.assert_text("Sign in", "h2")

            # Checks if line of text is present
            self.assert_text("Enter your email and password", "h4")

            # R2-13
            # Enters valid email and password
            # containing a space as a suffix
            self.type("#email", "testing14@gmail.com")
            self.type("#password", "Testing14! ")

            # Clicks 'remember me' button
            self.click('input[type="checkbox"]')

            # Clicks the 'sign in' button
            self.click('input[type="submit"]')

            # Checks that the user is redirected to the login page
            # Invalid account submission
            assert self.get_current_url() == base_url + '/login'
            self.assert_text("Login failed. Please try again.", "h4")

        # Test Case 15: LOGIN FAIL (invalid password format;
        # space as prefix and suffix)
        def test_login_fail_14(self, *_):

            # Tests if the user has entered an invalid email format
            # Uses input testing, with partitioning
            # Uses equivalence and boundary value testing

            # First register the user with valid email and password
            # Correspond to test case an see if success/fail
            self.open(base_url + '/register')
            self.type("#email", "testing15@gmail.com")
            self.type("#name", "Test15")
            self.type("#password", "Testing15!")
            self.type("#password2", "Testing15!")
            self.click('input[type="submit"]')

            # Checks that user is redirected to login page
            # after successful registration
            assert self.get_current_url() == base_url + '/login'

            # Checks if 'Sign in' header is present
            self.assert_text("Sign in", "h2")

            # Checks if line of text is present
            self.assert_text("Enter your email and password", "h4")

            # R2-14
            # Enters valid email and password that contains
            # a space as prefix and suffix
            self.type("#email", "testing15@gmail.com")
            self.type("#password", " Testing15! ")

            # Clicks 'remember me' button
            self.click('input[type="checkbox"]')

            # Clicks the 'sign in' button
            self.click('input[type="submit"]')

            # Checks that the user is redirected to the register page
            # Invalid account submission
            assert self.get_current_url() == base_url + '/login'
            self.assert_text("Login failed. Please try again.", "h4")

        # SHOTGUN TESTING TEST CASES
        # Note that each test case depicts a random input for 
        # email and password.
        # It does not affect the registration process,
        # as it only accounts for login.

        # Checks for valid/invalid email and password inputs.

        def test_login_shotgun(self, *_):

            def fail():
                assert self.get_current_url() == base_url + '/login'
                self.assert_text("Login failed. Please try again.", "h4")

            def success():
                assert self.get_current_url() == base_url + '/'

            email = ''
            usedEmails = []
            usedEmails.append(email)
            for i in range(10):
                while email in usedEmails:
                    email = (''.join(random.choice("abcdefghijklmnop")
                                     for i in range(7)) + '@gmail.com')
                usedEmails.append(email)

                # generate password
                password = ''.join(random.choice("abcdefABCDEF!@#$%")
                                   for i in range(3, 9))

                username = "Test" + str(i)

                # First register the user with valid email and password
                # Correspond to test case an see if success/fail
                self.open(base_url + '/register')
                self.type("#email", email)
                self.type("#name", username)
                self.type("#password", password)
                self.type("#password2", password)
                self.click('input[type="submit"]')

                # log in
                self.open(base_url + '/login')
                self.type("#email", email)
                self.type("#password", password)
                self.click('input[type="submit"]')

                # check if the password is valid
                if (any(x.isupper() for x in password) and
                    any(x.islower() for x in password) and
                    any(x.isdigit() for x in password) and
                        len(password) >= 6) is False:
                    fail()
                else:
                    success()

        test_login_fail_1(self)
        test_login_fail_2(self)
        test_login_fail_3(self)
        test_login_fail_4(self)
        test_login_fail_5(self)
        test_login_fail_6(self)
        test_login_fail_7(self)
        test_login_fail_8(self)
        test_login_fail_9(self)
        test_login_fail_10(self)
        test_login_fail_11(self)
        test_login_fail_12(self)
        test_login_fail_13(self)
        test_login_fail_14(self)
