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
        # Should see the success message at the top of the page
        self.assert_text("Login Successful!", "h4")

        # Checks if 'Pocket Rentals' header
        # redirects user to homepage when clicked
        self.assert_text("Pocket Rentals", "h1").click()
        assert self.get_current_url() == base_url + '/'

    # TEST CASE 2: LOGIN FAIL (incorrect password for email)
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
        self.assert_text("Login failed. Please try again.", "h4")

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
        self.assert_text("Login failed. Please try again.", "h4")

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
        self.assert_text("Login failed. Please try again.", "h4")

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
    # Note that each test case depicts a random input for email and password.
    # It does not affect the registration process,
    # as it only accounts for login.

    # Checks for valid/invalid email and password inputs.

    # Test Case 16: SHOTGUN TESTING
    def test_login_shotgun_1(self, *_):

        """
        This is a sample black box shotgun test case for LOGIN.
        Password too long.
        """

        self.open(base_url + '/register')
        self.type("#email", "failedshotgun@gmail.com")
        self.type("#name", "Failure00!")
        self.type("#password", "Failure00!")
        self.type("#password2", "Failure00!")
        self.click('input[type="submit"]')

        # After successful registration, test login

        self.open(base_url + '/login')
        self.type("#email", "failedshotgun@gmail.com")
        self.type("#password", "Long99!Long99!Long99!Long99!Long99!")
        self.click('input[type="submit"]')
        assert self.get_current_url() == base_url + '/login'
        self.assert_text("Login failed. Please try again.", "h4")

    def test_login_shotgun_2(self, *_):

        """
        This is a sample black box shotgun test case for LOGIN.
        Password too short.
        """

        self.open(base_url + '/register')
        self.type("#email", "failingn@gmail.com")
        self.type("#name", "Random00!")
        self.type("#password", "Random00!")
        self.type("#password2", "Random00!")
        self.click('input[type="submit"]')

        # After successful registration, test login

        self.open(base_url + '/login')
        self.type("#email", "failing@gmail.com")
        self.type("#password", "ran0!")
        self.click('input[type="submit"]')
        assert self.get_current_url() == base_url + '/login'
        self.assert_text("Login failed. Please try again.", "h4")
    
    def test_login_shotgun_3(self, *_):

        """
        This is a sample black box shotgun test case for LOGIN.
        """

        self.open(base_url + '/register')
        self.type("#email", "sik3@gmail.com")
        self.type("#name", "K1DDING")
        self.type("#password", "J0Ke$rr!")
        self.type("#password2", "J0Ke$rr!")
        self.click('input[type="submit"]')

        # After successful registration, test login

        self.open(base_url + '/login')
        self.type("#email", "sik3@gmail.com")
        self.type("#password", "J0Ke$rr!")
        self.click('input[type="submit"]')

        self.assert_text("Login Successful!", "h4")
    
    def test_login_shotgun_4(self, *_):

        """
        This is a sample black box shotgun test case for LOGIN.
        Email ID too long.
        """

        self.open(base_url + '/register')
        self.type("#email", "drinkingwater@gmail.com")
        self.type("#name", "WaTer!09")
        self.type("#password", "WaTer!09")
        self.type("#password2", "WaTer!09")
        self.click('input[type="submit"]')

        # After successful registration, test login

        self.open(base_url + '/login')
        self.type("#email", "drinkingwaterrrrrrrrrrrrrrrr@gmail.com")
        self.type("#password", "WaTer!09")
        self.click('input[type="submit"]')
        assert self.get_current_url() == base_url + '/login'
        self.assert_text("Login failed. Please try again.", "h4")
    
    def test_login_shotgun_5(self, *_):

        """
        This is a sample black box shotgun test case for LOGIN.
        Email ID too short.
        """

        self.open(base_url + '/register')
        self.type("#email", "eatingwater@gmail.com")
        self.type("#name", "EaTiNg!08")
        self.type("#password", "EaTiNg!08")
        self.type("#password2", "EaTiNg!08")
        self.click('input[type="submit"]')

        # After successful registration, test login

        self.open(base_url + '/login')
        self.type("#email", "f@gmail.com")
        self.type("#password", "EaTiNg!08")
        self.click('input[type="submit"]')
        assert self.get_current_url() == base_url + '/login'
        self.assert_text("Login failed. Please try again.", "h4")

    def test_login_shotgun_6(self, *_):

        """
        This is a sample black box shotgun test case for LOGIN.
        """

        self.open(base_url + '/register')
        self.type("#email", "project5PRINT@gmail.com")
        self.type("#name", "sprintPROJECT")
        self.type("#password", "spr1ntPROJ$")
        self.type("#password2", "spr1ntPROJ$")
        self.click('input[type="submit"]')

        # After successful registration, test login

        self.open(base_url + '/login')
        self.type("#email", "project5PRINT@gmail.com")
        self.type("#password", "spr1ntPROJ$")
        self.click('input[type="submit"]')

        self.assert_text("Login Successful!", "h4")

    def test_login_shotgun_7(self, *_):

        """
        This is a sample black box shotgun test case for LOGIN.
        Incorrect input for email.
        """

        self.open(base_url + '/register')
        self.type("#email", "throwingfart@gmail.com")
        self.type("#name", "fArT!99")
        self.type("#password", "fArT!99")
        self.type("#password2", "fArT!99")
        self.click('input[type="submit"]')

        # After successful registration, test login

        self.open(base_url + '/login')
        self.type("#email", "incorrect@gmail.com")
        self.type("#password", "fArT!99")
        self.click('input[type="submit"]')
        assert self.get_current_url() == base_url + '/login'
        self.assert_text("Login failed. Please try again.", "h4")
    
    def test_login_shotgun_8(self, *_):

        """
        This is a sample black box shotgun test case for LOGIN.
        """

        self.open(base_url + '/register')
        self.type("#email", "takeiteasy@gmail.com")
        self.type("#name", "Breezy1")
        self.type("#password", "L1ghtBreeze$")
        self.type("#password2", "L1ghtBreeze$")
        self.click('input[type="submit"]')

        # After successful registration, test login

        self.open(base_url + '/login')
        self.type("#email", "takeiteasy@gmail.com")
        self.type("#password", "L1ghtBreeze$")
        self.click('input[type="submit"]')

        self.assert_text("Login Successful!", "h4")

    def test_login_shotgun_9(self, *_):

        """
        This is a sample black box shotgun test case for LOGIN.
        Incorrect input for email.
        """

        self.open(base_url + '/register')
        self.type("#email", "blanketTowel@gmail.com")
        self.type("#name", "townketBlankel8")
        self.type("#password", "wARM$weather76")
        self.type("#password2", "wARM$weather76")
        self.click('input[type="submit"]')

        # After successful registration, test login

        self.open(base_url + '/login')
        self.type("#email", "towelBlanket@gmail.com")
        self.type("#password", "wARM$weather76")
        self.click('input[type="submit"]')
        assert self.get_current_url() == base_url + '/login'
        self.assert_text("Login failed. Please try again.", "h4")

    def test_login_shotgun_10(self, *_):

        """
        This is a sample black box shotgun test case for LOGIN.
        Missing @ symbol in email.
        Space as prefix in password.
        """

        self.open(base_url + '/register')
        self.type("#email", "TickingTime@gmail.com")
        self.type("#name", "clockMaster99")
        self.type("#password", "getAwatch567$")
        self.type("#password2", "getAwatch567$")
        self.click('input[type="submit"]')

        # After successful registration, test login

        self.open(base_url + '/login')
        self.type("#email", "TickingTimegmail.com")
        self.type("#password", " getAwatch567$")
        self.click('input[type="submit"]')
        assert self.get_current_url() == base_url + '/login'
        self.assert_text("Login failed. Please try again.", "h4")
    
    def test_login_shotgun_11(self, *_):

        """
        This is a sample black box shotgun test case for LOGIN.
        Space as suffix in password.
        """

        self.open(base_url + '/register')
        self.type("#email", "mikaeljacksun@gmail.com")
        self.type("#name", "MikaelJacksun")
        self.type("#password", "$till4liv3")
        self.type("#password2", "$till4liv3")
        self.click('input[type="submit"]')

        # After successful registration, test login

        self.open(base_url + '/login')
        self.type("#email", "mikaeljacksun@gmail.com")
        self.type("#password", "$till4liv3 ")
        self.click('input[type="submit"]')
        assert self.get_current_url() == base_url + '/login'
        self.assert_text("Login failed. Please try again.", "h4")

    def test_login_shotgun_12(self, *_):

        """
        This is a sample black box shotgun test case for LOGIN.
        """

        self.open(base_url + '/register')
        self.type("#email", "thisIsFalse@gmail.com")
        self.type("#name", "False1")
        self.type("#password", "Fal$ePass")
        self.type("#password2", "Fal$ePass")
        self.click('input[type="submit"]')

        # After successful registration, test login

        self.open(base_url + '/login')
        self.type("#email", "thisIsFalse@gmail.com")
        self.type("#password", "Fal$ePass")
        self.click('input[type="submit"]')
        
        self.assert_text("Login Successful!", "h4")

    def test_login_shotgun_13(self, *_):

        """
        This is a sample black box shotgun test case for LOGIN.
        Space as prefix in email.
        """

        self.open(base_url + '/register')
        self.type("#email", "hungryNOW@gmail.com")
        self.type("#name", "EatLeftOvers55")
        self.type("#password", "yuMMy33$f")
        self.type("#password2", "yuMMy33$f")
        self.click('input[type="submit"]')

        # After successful registration, test login

        self.open(base_url + '/login')
        self.type("#email", " hungryNOW@gmail.com")
        self.type("#password", "yuMMy33$f")
        self.click('input[type="submit"]')
        assert self.get_current_url() == base_url + '/login'
        self.assert_text("Login failed. Please try again.", "h4")

    def test_login_shotgun_14(self, *_):

        """
        This is a sample black box shotgun test case for LOGIN.
        Password does not match.
        """

        self.open(base_url + '/register')
        self.type("#email", "SADman@gmail.com")
        self.type("#name", "SADMAN00")
        self.type("#password", "notHAPPY77!")
        self.type("#password2", "notHAPPY77!")
        self.click('input[type="submit"]')

        # After successful registration, test login

        self.open(base_url + '/login')
        self.type("#email", "SADman@gmail.com")
        self.type("#password", "superHAPPY88!")
        self.click('input[type="submit"]')
        assert self.get_current_url() == base_url + '/login'
        self.assert_text("Login failed. Please try again.", "h4")

    def test_login_shotgun_15(self, *_):

        """
        This is a sample black box shotgun test case for LOGIN.
        Password missing special character.
        Password all lower case. No upper case letter.
        """

        self.open(base_url + '/register')
        self.type("#email", "c0dingL0L@gmail.com")
        self.type("#name", "h4ck3r")
        self.type("#password", "Password123$")
        self.type("#password2", "Password123$")
        self.click('input[type="submit"]')

        # After successful registration, test login

        self.open(base_url + '/login')
        self.type("#email", "c0dingL0L@gmail.com")
        self.type("#password", "password123")
        self.click('input[type="submit"]')
        assert self.get_current_url() == base_url + '/login'
        self.assert_text("Login failed. Please try again.", "h4")

    def test_login_shotgun_16(self, *_):

        """
        This is a sample black box shotgun test case for LOGIN.
        Password only contains numbers.
        """

        self.open(base_url + '/register')
        self.type("#email", "why25tests@gmail.com")
        self.type("#name", "RegrettingIt99")
        self.type("#password", "myFAULT$0rry")
        self.type("#password2", "myFAULT$0rry")
        self.click('input[type="submit"]')

        # After successful registration, test login

        self.open(base_url + '/login')
        self.type("#email", "why25tests@gmail.com")
        self.type("#password", "37548753")
        self.click('input[type="submit"]')
        assert self.get_current_url() == base_url + '/login'
        self.assert_text("Login failed. Please try again.", "h4")

    def test_login_shotgun_17(self, *_):

        """
        This is a sample black box shotgun test case for LOGIN.
        Email ID is only 2 letters long.
        Incorrect email.
        """

        self.open(base_url + '/register')
        self.type("#email", "cravingICEcream@gmail.com")
        self.type("#name", "scream4ICEcream")
        self.type("#password", "freeICEcream$")
        self.type("#password2", "freeICEcream$")
        self.click('input[type="submit"]')

        # After successful registration, test login

        self.open(base_url + '/login')
        self.type("#email", "ic@gmail.com")
        self.type("#password", "freeICEcream$")
        self.click('input[type="submit"]')
        assert self.get_current_url() == base_url + '/login'
        self.assert_text("Login failed. Please try again.", "h4")

    def test_login_shotgun_18(self, *_):

        """
        This is a sample black box shotgun test case for LOGIN.
        Space as a suffix for email.
        """

        self.open(base_url + '/register')
        self.type("#email", "emptySPACE9@gmail.com")
        self.type("#name", "AstroNOT")
        self.type("#password", "emptySPACE$")
        self.type("#password2", "emptySPACE$")
        self.click('input[type="submit"]')

        # After successful registration, test login

        self.open(base_url + '/login')
        self.type("#email", "emptySPACE9@gmail.com ")
        self.type("#password", "emptySPACE$")
        self.click('input[type="submit"]')
        assert self.get_current_url() == base_url + '/login'
        self.assert_text("Login failed. Please try again.", "h4")

    def test_login_shotgun_19(self, *_):

        """
        This is a sample black box shotgun test case for LOGIN.
        """

        self.open(base_url + '/register')
        self.type("#email", "correctEmail@gmail.com")
        self.type("#name", "Correct1")
        self.type("#password", "correctPass$")
        self.type("#password2", "correctPass$")
        self.click('input[type="submit"]')

        # After successful registration, test login

        self.open(base_url + '/login')
        self.type("#email", "correctEmail@gmail.com")
        self.type("#password", "correctPass$")
        self.click('input[type="submit"]')

        self.assert_text("Login Successful!", "h4")

    def test_login_shotgun_20(self, *_):

        """
        This is a sample black box shotgun test case for LOGIN.
        """

        self.open(base_url + '/register')
        self.type("#email", "tiredAlready@gmail.com")
        self.type("#name", "AlreadyTired7")
        self.type("#password", "tieHeard7!")
        self.type("#password2", "tieHeard7!")
        self.click('input[type="submit"]')

        # After successful registration, test login

        self.open(base_url + '/login')
        self.type("#email", "tiredAlready@gmail.com")
        self.type("#password", "tieHeard7!")
        self.click('input[type="submit"]')

        self.assert_text("Login Successful!", "h4")

    def test_login_shotgun_21(self, *_):

        """
        This is a sample black box shotgun test case for LOGIN.
        """

        self.open(base_url + '/register')
        self.type("#email", "randC0RRECT@gmail.com")
        self.type("#name", "C0rrectRand")
        self.type("#password", "coreR3ctRand!")
        self.type("#password2", "coreR3ctRand!")
        self.click('input[type="submit"]')

        # After successful registration, test login

        self.open(base_url + '/login')
        self.type("#email", "randC0RRECT@gmail.com")
        self.type("#password", "coreR3ctRand!")
        self.click('input[type="submit"]')

        self.assert_text("Login Successful!", "h4")

    def test_login_shotgun_22(self, *_):

        """
        This is a sample black box shotgun test case for LOGIN.
        """

        self.open(base_url + '/register')
        self.type("#email", "cl0wn@gmail.com")
        self.type("#name", "H0NK")
        self.type("#password", "cl0wn!RL")
        self.type("#password2", "cl0wn!RL")
        self.click('input[type="submit"]')

        # After successful registration, test login

        self.open(base_url + '/login')
        self.type("#email", "cl0wn@gmail.com")
        self.type("#password", "cl0wn!RL")
        self.click('input[type="submit"]')

        self.assert_text("Login Successful!", "h4")

    def test_login_shotgun_23(self, *_):

        """
        This is a sample black box shotgun test case for LOGIN.
        """

        self.open(base_url + '/register')
        self.type("#email", "fakeAF@gmail.com")
        self.type("#name", "ImFake")
        self.type("#password", "fak3AF!")
        self.type("#password2", "fak3AF!")
        self.click('input[type="submit"]')

        # After successful registration, test login

        self.open(base_url + '/login')
        self.type("#email", "fakeAF@gmail.com")
        self.type("#password", "fak3AF!")
        self.click('input[type="submit"]')

        self.assert_text("Login Successful!", "h4")

    def test_login_shotgun_24(self, *_):

        """
        This is a sample black box shotgun test case for LOGIN.
        """

        self.open(base_url + '/register')
        self.type("#email", "FINALdone@gmail.com")
        self.type("#name", "CELEBRAT3")
        self.type("#password", "LeTSG0!")
        self.type("#password2", "LeTSG0!")
        self.click('input[type="submit"]')

        # After successful registration, test login

        self.open(base_url + '/login')
        self.type("#email", "FINALdone@gmail.com")
        self.type("#password", "LeTSG0!")
        self.click('input[type="submit"]')

        self.assert_text("Login Successful!", "h4")

    def test_login_shotgun_25(self, *_):

        """
        This is a sample black box shotgun test case for LOGIN.
        Incorrect password. Only contains special characters.
        """

        self.open(base_url + '/register')
        self.type("#email", "FINALfail@gmail.com")
        self.type("#name", "FAILur3")
        self.type("#password", "DissAP0INT!")
        self.type("#password2", "DissAP0INT!")
        self.click('input[type="submit"]')

        # After successful registration, test login

        self.open(base_url + '/login')
        self.type("#email", "FINALfail@gmail.com")
        self.type("#password", "!!$$$!!$$!")
        self.click('input[type="submit"]')
        assert self.get_current_url() == base_url + '/login'
        self.assert_text("Login failed. Please try again.", "h4")