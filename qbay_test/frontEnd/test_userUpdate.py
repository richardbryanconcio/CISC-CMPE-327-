from seleniumBase import Basecase

import org.openqa.selenium.By as By

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import User

# Contains integration tests for the user update page

class FrontEndUserUpdatePageTest(Basecase):
    #login to an existing account
    self.open(base_url + '/login')
    self.type("#email", "testing@gmail.com")
    self.type("#password", "Testing1234!")
    #redirect to update page
    self.open(base_url + '/baseUpdate')

    #TEST CASE 1: UPDATE USERNAME SUCCESS
    def test_update_username_success(self, *_):
        self.open(base_url + '/updateUsername')
        self.type("#username", "newname")
        self.click('input[type="submit"]')

    #TEST CASE 2: UPDATE USERNAME FAILURE
    def test_update_username_failure(self, *_):
        self.open(base_url + '/updateUsername')
        self.type("#username", " invalidname")
        self.click('input[type="submit"]')

    #TEST CASE 3: UPDATE PASSWORD SUCCESS
    def test_update_password_success(self, *_):
        self.open(base_url + '/updatePassword')
        self.type("#password", "Abracadabra123$")
        self.click('input[type="submit"]')

    #TEST CASE 4: UPDATE PASSWORD FAILURE
    def test_update_password_failure(self, *_):
        self.open(base_url + '/updatePassword')
        self.type("#password", "abc")
        self.click('input[type="submit"]')

    #TEST CASE 5: UPDATE EMAIL SUCCESS
    def test_update_email_success(self, *_):
        self.open(base_url + '/updateEmail')
        self.type("#email", "ricky@trailerpark.com")
        self.click('input[type="submit"]')

    #TEST CASE 6: UPDATE EMAIL FAILURE
    def test_update_email_failure(self, *_):
        self.open(base_url + '/updateEmail')
        self.type("#email", "notanemail.com")
        self.click('input[type="submit"]')

    #TEST CASE 7: UPDATE BILLING ADDRESS SUCCESS
    def test_update_address_success(self, *_):
        self.open(base_url + '/updateBillingPostal')
        self.type("#address", "2525 Maple Ln")
        self.click('input[type="submit"]')

    #TEST CASE 8: UPDATE BILLING ADDRESS FAILURE
    def test_update_address_failure(self, *_):
        self.open(base_url + '/updateBillingPostal')
        self.type("#address", "ur moms house")
        self.click('input[type="submit"]')

    #TEST CASE 9: UPDATE POSTAL CODE SUCCESS
    def test_update_postal_success(self, *_):
        self.open(base_url + '/updateBillingPostal')
        self.type("#postalCode", "b7g 4k5")
        self.click('input[type="submit"]')

    #TEST CASE 10: UPDATE POSTAL CODE FAILURE
    def test_update_postal_failure(self, *_):
        self.open(base_url + '/updateBillingPostal')
        self.type("#postalCode", "4k5 b7g")
        self.click('input[type="submit"]')