from seleniumBase import Basecase

import org.openqa.selenium.By as By

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import User

# Contains integration tests for the user update page
'''
Requirements 

R3-1: A user is only able to update his/her user name, user email, 
billing address, password, and postal code.

R3-2: Postal code should be non-empty, alphanumeric-only, 
and no special characters such as !.

R3-3: Postal code has to be a valid Canadian postal code.

R3-4: User name follows the requirements above (non-empty, 
alphanumeric-only, no special characters such as !).
'''


class FrontEndUserUpdatePageTest(Basecase):
    # login to an existing account
    self.open(base_url + '/login')
    self.type("#email", "testing@gmail.com")
    self.type("#password", "Testing1234!")

    # redirect to update page
    self.open(base_url + '/baseUpdate')

    # TEST CASE 1: UPDATE USERNAME SUCCESS
    def test_update_username_success(self, *_):
        self.open(base_url + 'baseUpdate/updateUsername')

        # check that current username is displayed
        self.assert_text(user.username, "currentUsername")

        self.type("#username", "newname")
        self.click('input[type="submit"]')

        # check returned to home page
        self.assert_title(base_url)

    # TEST CASE 2: UPDATE USERNAME FAILURE (R3-4: alphanumeric-only)
    def test_update_username_failure(self, *_):
        self.open(base_url + 'baseUpdate/updateUsername')

        # check that current username is displayed
        self.assert_text(user.username, "currentUsername")

        self.type("#username", " invalidname")
        self.click('input[type="submit"]')

        # check returned to home page
        self.assert_title(base_url)

    # TEST CASE 3: UPDATE USERNAME FAILURE (R3-4: non-empty)
    def test_update_username_failure(self, *_):
        self.open(base_url + 'baseUpdate/updateUsername')

        # check that current username is displayed
        self.assert_text(user.username, "currentUsername")

        self.type("#username", "")
        self.click('input[type="submit"]')

        # check returned to home page
        self.assert_title(base_url)

    # TEST CASE 4: UPDATE USERNAME FAILURE 
    # (R3-4: no special characters such as !)
    def test_update_username_failure(self, *_):
        self.open(base_url + 'baseUpdate/updateUsername')

        # check that current username is displayed
        self.assert_text(user.username, "currentUsername")

        self.type("#username", "!notvalid")
        self.click('input[type="submit"]')

        # check returned to home page
        self.assert_title(base_url)

    # TEST CASE 5: UPDATE PASSWORD SUCCESS
    def test_update_password_success(self, *_):
        self.open(base_url + 'baseUpdate/updatePassword')

        self.type("#password", "Abracadabra123$")
        self.type("#confPassword", "Abracadabra123$")
        self.click('input[type="submit"]')

        # check returned to home page
        self.assert_title(base_url)

    # TEST CASE 6: UPDATE PASSWORD FAILURE 
    # (length greater than 6)
    def test_update_password_failure(self, *_):
        self.open(base_url + 'baseUpdate/updatePassword')

        self.type("#password", "abc")
        self.type("#confPassword", "abc")
        self.click('input[type="submit"]')

        # check returned to home page
        self.assert_title(base_url)

    # TEST CASE 8: UPDATE PASSWORD FAILURE (non-empty)
    def test_update_password_failure(self, *_):
        self.open(base_url + 'baseUpdate/updatePassword')

        self.type("#password", "")
        self.type("#confPassword", "")
        self.click('input[type="submit"]')

        # check returned to home page
        self.assert_title(base_url)

    # TEST 9: UPDATE PASSWORD FAILURE (password doesnt match confirmation)
    def test_update_username_failure(self, *_):
        self.open(base_url + 'baseUpdate/updateUsername')

        # check that current username is displayed
        self.assert_text(user.username, "currentUsername")

        self.type("#username", "password1")
        self.type("#confPassword", "password2")
        self.click('input[type="submit"]')

        # check returned to home page
        self.assert_title(base_url)

    # TEST CASE 10: UPDATE EMAIL SUCCESS
    def test_update_email_success(self, *_):
        self.open(base_url + 'baseUpdate/updateEmail')
        self.type("#email", "ricky@trailerpark.com")
        self.click('input[type="submit"]')

    # TEST CASE 11: UPDATE EMAIL FAILURE (invalid email)
    def test_update_email_failure(self, *_):
        self.open(base_url + 'baseUpdate/updateEmail')

        self.type("#email", "notanemail.com")
        self.click('input[type="submit"]')

        # check returned to home page
        self.assert_title(base_url)

    # TEST CASE 12: UPDATE BILLING ADDRESS SUCCESS
    def test_update_address_success(self, *_):
        self.open(base_url + 'baseUpdate/updateBillingPostal')

        self.type("#address", "2525 Maple Ln")
        self.click('input[type="submit"]')

        # check returned to home page
        self.assert_title(base_url)

    # TEST CASE 13: UPDATE BILLING ADDRESS FAILURE 
    # (invalid address)
    def test_update_address_failure(self, *_):
        self.open(base_url + 'baseUpdate/updateBillingPostal')

        self.type("#address", "ur moms house")
        self.click('input[type="submit"]')

        # check returned to home page
        self.assert_title(base_url)

    # TEST CASE 14: UPDATE POSTAL CODE SUCCESS
    def test_update_postal_success(self, *_):
        self.open(base_url + 'baseUpdate/updateBillingPostal')

        self.type("#postalCode", "b7g 4k5")
        self.click('input[type="submit"]')

        # check returned to home page
        self.assert_title(base_url)

    # TEST CASE 15: UPDATE POSTAL CODE FAILURE 
    # (R3-3: Must be valid Canadian postal code)
    def test_update_postal_failure(self, *_):
        self.open(base_url + 'baseUpdate/updateBillingPostal')

        self.type("#postalCode", "4k5 b7g")
        self.click('input[type="submit"]')

        # check returned to home page
        self.assert_title(base_url)

    # TEST CASE 16: UPDATE POSTAL CODE FAILURE (R3-2: non-empty)
    def test_update_postal_failure(self, *_):
        self.open(base_url + 'baseUpdate/updateBillingPostal')

        self.type("#postalCode", "")
        self.click('input[type="submit"]')

        # check returned to home page
        self.assert_title(base_url)