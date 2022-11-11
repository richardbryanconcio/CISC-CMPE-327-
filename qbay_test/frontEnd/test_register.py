# from seleniumBase import Basecase
import selenium
# from org.openqa.selenium.By import By
from seleniumbase import BaseCase
 
 
from unittest.mock import patch
from qbay.models import User
from qbay_test.conftest import base_url
 
 
"""
This file defines all integration tests for the frontend registration.
"""
# Testing below covers the black box input coverage testing method
 

class FrontEndHomePageTest(BaseCase):
    def test_register_fail_R1_1_1(self, *_):
        """
        This is a sample front end integration test to show
        user registration failed. R1-1 Email cannot be empty,
        and the email input fails this requirement.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "")
        self.type("#name", "userR11")
        self.type("#password", "Password1!")
        self.type("#password2", "Password1!")
 
        # click enter button
        self.click('input[type="submit"]')
 
        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text(" Registration failed. Try again.", "#welcome-header")
        # other available APIs
 
    def test_register_fail_R1_1_2(self, *_):
        """
        This is a sample front end integration test to show
        user registration failed. R1-1 Email cannot be empty,
        and the email input fails this requirement.
        """
        # open login page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", " ")
        self.type("#name", "userR11")
        self.type("#password", "Password1!")
        self.type("#password2", "Password1!")
 
        # click enter button
        self.click('input[type="submit"]')
 
        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text(" Registration failed. Try again.", "#welcome-header")
        # other available APIs
 
    def test_register_fail_R1_3(self, *_):
        """
        This is a sample front end integration test to show
        user registration failed. R1-3 The email has to follow
        addr-spec defined in RFC 5322, and the email input fails
        this requirement.
        """
        # open login page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testr13@fail@test.com")
        self.type("#name", "userR11")
        self.type("#password", "Password1!")
        self.type("#password2", "Password1!")
 
        # click enter button
        self.click('input[type="submit"]')
 
        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text(" Registration failed. Try again.", "#welcome-header")
        # other available APIs
 
    # covers the test case of all 4 variable Success
    def test_register_Success_R1_3(self, *_):
        """
        This is a sample front end integration test to show
        user registration success.
        """
        # open login page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testr1@test.com")
        self.type("#name", "userR11")
        self.type("#password", "Password1!")
        self.type("#password2", "Password1!")
 
        # click enter button
        self.click('input[type="submit"]')
 
        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text(" Registration Success.", "#welcome-header")
        # other available APIs
 
    def test_register_Success_R1_7(self, *_):
        """
        This is a sample front end integration test to show
        user registration fails. R1-7: If the email has been used,
        the operation failed.
        """
        # open login page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testr1@test.com")
        self.type("#name", "userR17")
        self.type("#password", "Password1!")
        self.type("#password2", "Password1!")
 
        # click enter button
        self.click('input[type="submit"]')
 
        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text(" Registration  failed. Try again.",
                         "#welcome-header")
        # other available APIs
 
    def test_register_fail_R1_1_3(self, *_):
        """
        This is a sample front end integration test to show
        user registration failed. R1-1 Password cannot be empty,
        and the password input fails this requirement.
        """
        # open login page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", " testr113@test.com")
        self.type("#name", "userr113")
        self.type("#password", "")
        self.type("#password2", "")
 
        # click enter button
        self.click('input[type="submit"]')
 
        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text(" Registration failed. Try again.", "#welcome-header")
        # other available APIs
 
    def test_register_fail_R1_4_1(self, *_):
        """
        This is a sample front end integration test to show
        user registration failed. R1-4: Password has to meet
        the required complexity: minimum length 6,
        at least one upper case, at least one lower case,
        and at least one special character. The password input
        fails the minimum length 6 requirement.
        """
        # open login page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", " testr141@test.com")
        self.type("#name", "userr141")
        self.type("#password", "Pas1!")
        self.type("#password2", "Pas1!")
 
        # click enter button
        self.click('input[type="submit"]')
 
        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text(" Registration failed. Try again.", "#welcome-header")
        # other available APIs
 
    def test_register_fail_R1_4_2(self, *_):
        """
        This is a sample front end integration test to show
        user registration failed. R1-4: Password has to meet
        the required complexity: minimum length 6,
        at least one upper case, at least one lower case,
        and at least one special character. The password input
        fails the at least one upper case requirement.
        """
        # open login page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", " testr142@test.com")
        self.type("#name", "userr142")
        self.type("#password", "pa$s123")
        self.type("#password2", "pa$s123")
 
        # click enter button
        self.click('input[type="submit"]')
 
        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text(" Registration failed. Try again.", "#welcome-header")
        # other available APIs
 
    def test_register_fail_R1_4_3(self, *_):
        """
        This is a sample front end integration test to show
        user registration failed. R1-4: Password has to meet
        the required complexity: minimum length 6,
        at least one upper case, at least one lower case,
        and at least one special character. The password input
        fails the at least one lower case requirement.
        """
        # open login page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", " testr143@test.com")
        self.type("#name", "userr143")
        self.type("#password", "PA$S123")
        self.type("#password2", "PA$S123")
 
        # click enter button
        self.click('input[type="submit"]')
 
        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text(" Registration failed. Try again.", "#welcome-header")
        # other available APIs
 
    def test_register_fail_R1_4_4(self, *_):
        """
        This is a sample front end integration test to show
        user registration failed. R1-4: Password has to meet
        the required complexity: minimum length 6,
        at least one upper case, at least one lower case,
        and at least one special character. The password input
        fails the at least one special character requirement.
        """
        # open login page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", " testr144@test.com")
        self.type("#name", "userr144")
        self.type("#password", "pASs123")
        self.type("#password2", "pASs123")
 
        # click enter button
        self.click('input[type="submit"]')
 
        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text(" Registration failed. Try again.", "#welcome-header")
        # other available APIs
 
    def test_register_fail_R1_4_6(self, *_):
        """
        This is a sample front end integration test to show
        user registration failed. The password2 input
        does not match password1 requirement.
        """
        # open login page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", " testr144@test.com")
        self.type("#name", "userr144")
        self.type("#password", "pA$s123")
        self.type("#password2", "pASs123")
 
        # click enter button
        self.click('input[type="submit"]')
 
        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text(" Registration failed. Try again.", "#welcome-header")
        # other available APIs
 
    def test_register_success_R1_4_5(self, *_):
        """
        This is a sample front end integration test to show
        user registration success. R1-4: Password has to meet
        the required complexity: minimum length 6,
        at least one upper case, at least one lower case,
        and at least one special character. The password input
        meets all of these requirement.
        """
        # open login page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", " testr145@test.com")
        self.type("#name", "userr145")
        self.type("#password", "pA$s123")
        self.type("#password2", "pA$s123")
 
        # click enter button
        self.click('input[type="submit"]')
 
        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text(" Registration Success.", "#welcome-header")
        # other available APIs
 
    def test_register_fail_R1_5_1(self, *_):
        """
        This is a sample front end integration test to show
        user registration fails. R1-5: User name has to be
        non-empty, alphanumeric-only, and space allowed only
        if it is not as the prefix or suffix. The user name input
        fails the non-empty requirement.
        """
        # open login page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", " testr151@test.com")
        self.type("#name", "")
        self.type("#password", "pA$s123")
        self.type("#password2", "pA$s123")
 
        # click enter button
        self.click('input[type="submit"]')
 
        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text(" Registration failed. Try again.", "#welcome-header")
        # other available APIs
 
    def test_register_fail_R1_5_2(self, *_):
        """
        This is a sample front end integration test to show
        user registration fails. R1-5: User name has to be
        non-empty, alphanumeric-only, and space allowed only
        if it is not as the prefix or suffix. The user name input
        fails the no space at prefix requirement.
        """
        # open login page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", " testr152@test.com")
        self.type("#name", " userr152")
        self.type("#password", "pA$s123")
        self.type("#password2", "pA$s123")
 
        # click enter button
        self.click('input[type="submit"]')
 
        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text(" Registration failed. Try again.", "#welcome-header")
        # other available APIs
 
    def test_register_fail_R1_5_3(self, *_):
        """
        This is a sample front end integration test to show
        user registration fails. R1-5: User name has to be
        non-empty, alphanumeric-only, and space allowed only
        if it is not as the prefix or suffix. The user name input
        fails the no space at suffix requirement.
        """
        # open login page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", " testr153@test.com")
        self.type("#name", "userr153 ")
        self.type("#password", "pA$s123")
        self.type("#password2", "pA$s123")
 
        # click enter button
        self.click('input[type="submit"]')
 
        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text(" Registration failed. Try again.", "#welcome-header")
        # other available APIs
 
    def test_register_fail_R1_5_4(self, *_):
        """
        This is a sample front end integration test to show
        user registration fails. R1-5: User name has to be
        non-empty, alphanumeric-only, and space allowed only
        if it is not as the prefix or suffix. The user name input
        fails the alphanumeric-only requirement.
        """
        # open login page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", " testr154@test.com")
        self.type("#name", "userr154$")
        self.type("#password", "pA$s123")
        self.type("#password2", "pA$s123")
 
        # click enter button
        self.click('input[type="submit"]')
 
        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text(" Registration failed. Try again.", "#welcome-header")
        # other available APIs
 
    def test_register_success_R1_5_5(self, *_):
        """
        This is a sample front end integration test to show
        user registration success. R1-5: User name has to be
        non-empty, alphanumeric-only, and space allowed only
        if it is not as the prefix or suffix. The user name input
        meets the above requirement.
        """
        # open login page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", " testr155@test.com")
        self.type("#name", "userr155")
        self.type("#password", "pA$s123")
        self.type("#password2", "pA$s123")
 
        # click enter button
        self.click('input[type="submit"]')
 
        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text(" Registration success.", "#welcome-header")
        # other available APIs
 
    def test_register_fail_R1_6_1(self, *_):
        """
        This is a sample front end integration test to show
        user registration fails. R1-6: User name has to be longer
        than 2 characters and less than 20 characters. The user
        name input fails the longer than 2 characters requirement.
        """
        # open login page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", " testr161@test.com")
        self.type("#name", "u")
        self.type("#password", "pA$s123")
        self.type("#password2", "pA$s123")
 
        # click enter button
        self.click('input[type="submit"]')
 
        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text(" Registration failed. Try again.", "#welcome-header")
        # other available APIs
 
    def test_register_fail_R1_6_2(self, *_):
        """
        This is a sample front end integration test to show
        user registration fails. R1-6: User name has to be longer
        than 2 characters and less than 20 characters. The user
        name input fails the lesss than 20 characters requirement.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", " testr162@test.com")
        self.type("#name", "userr162testr162ur162")
        self.type("#password", "pA$s123")
        self.type("#password2", "pA$s123")
 
        # click enter button
        self.click('input[type="submit"]')
 
        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text(" Registration failed. Try again.", "#welcome-header")
        # other available APIs
 
    def test_register_success_R1_6_3(self, *_):
        """
        This is a sample front end integration test to show
        user registration success. R1-6: User name has to be longer
        than 2 characters and less than 20 characters. The user
        name input meets the above requirement.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", " testr163@test.com")
        self.type("#name", "userr163")
        self.type("#password", "pA$s123")
        self.type("#password2", "pA$s123")
 
        # click enter button
        self.click('input[type="submit"]')
 
        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text(" Registration success.", "#welcome-header")
        # other available APIs
 
    def test_register_success_1(self, *_):
        """
        This is a sample front end integration test to show
        user registration success. With all 4 inputs
        (email, name, password and password2) beings valid.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", " testsuccess1@test.com")
        self.type("#name", "usersuc1")
        self.type("#password", "pA$s123")
        self.type("#password2", "pA$s123")
 
        # click enter button
        self.click('input[type="submit"]')
 
        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text(" Registration success.", "#welcome-header")
        # other available APIs
 
    def test_register_fail_1(self, *_):
        """
        This is a sample front end integration test to show
        user registration Fail. With password2 not matching password.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", " testsuccess1@test.com")
        self.type("#name", "usersuc1")
        self.type("#password", "pA$s123")
        self.type("#password2", "pA$s126")
 
        # click enter button
        self.click('input[type="submit"]')
 
        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text(" Registration Fail.", "#welcome-header")
 
