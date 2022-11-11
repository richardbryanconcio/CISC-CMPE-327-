from seleniumBase import Basecase

import org.openqa.selenium.By as By

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import User

# Contains integration tests for the user update page


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

    # TEST CASE 2: UPDATE USERNAME FAILURE (invalid name)
    def test_update_username_failure(self, *_):
        self.open(base_url + 'baseUpdate/updateUsername')

        # check that current username is displayed
        self.assert_text(user.username, "currentUsername")

        self.type("#username", " invalidname")
        self.click('input[type="submit"]')

        self.assert_title(base_url)

    # TEST CASE 3: UPDATE USERNAME FAILURE (empty string)
    def test_update_username_failure(self, *_):
        self.open(base_url + 'baseUpdate/updateUsername')

        # check that current username is displayed
        self.assert_text(user.username, "currentUsername")

        self.type("#username", "")
        self.click('input[type="submit"]')

        self.assert_title(base_url)

    # TEST CASE X: UPDATE PASSWORD SUCCESS
    def test_update_password_success(self, *_):
        self.open(base_url + 'baseUpdate/updatePassword')
        self.type("#password", "Abracadabra123$")
        self.type("#confPassword", "Abracadabra123$")
        self.click('input[type="submit"]')

    # TEST CASE X: UPDATE PASSWORD FAILURE
    def test_update_password_failure(self, *_):
        self.open(base_url + 'baseUpdate/updatePassword')
        self.type("#password", "abc")
        self.click('input[type="submit"]')

    # TEST CASE X: UPDATE EMAIL SUCCESS
    def test_update_email_success(self, *_):
        self.open(base_url + 'baseUpdate/updateEmail')
        self.type("#email", "ricky@trailerpark.com")
        self.click('input[type="submit"]')

    # TEST CASE X: UPDATE EMAIL FAILURE
    def test_update_email_failure(self, *_):
        self.open(base_url + 'baseUpdate/updateEmail')
        self.type("#email", "notanemail.com")
        self.click('input[type="submit"]')

    # TEST CASE X: UPDATE BILLING ADDRESS SUCCESS
    def test_update_address_success(self, *_):
        self.open(base_url + 'baseUpdate/updateBillingPostal')
        self.type("#address", "2525 Maple Ln")
        self.click('input[type="submit"]')

    # TEST CASE X: UPDATE BILLING ADDRESS FAILURE
    def test_update_address_failure(self, *_):
        self.open(base_url + 'baseUpdate/updateBillingPostal')
        self.type("#address", "ur moms house")
        self.click('input[type="submit"]')

    # TEST CASE X: UPDATE POSTAL CODE SUCCESS
    def test_update_postal_success(self, *_):
        self.open(base_url + 'baseUpdate/updateBillingPostal')
        self.type("#postalCode", "b7g 4k5")
        self.click('input[type="submit"]')

    # TEST CASE X: UPDATE POSTAL CODE FAILURE
    def test_update_postal_failure(self, *_):
        self.open(base_url + 'baseUpdate/updateBillingPostal')
        self.type("#postalCode", "4k5 b7g")
        self.click('input[type="submit"]')