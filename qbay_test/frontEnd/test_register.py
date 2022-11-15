import selenium
from seleniumbase import BaseCase


from unittest.mock import patch
from qbay.models import User
from qbay_test.conftest import base_url
import random

""" 
This file defines all integration tests for the frontend registration.
Testing below covers the black box input coverage testing method.
The 2nd blackbox testing method used is Input partition testing method.
If there are repeted test cases between the blackbox testing methods, 
the repeted test case has been removed.
The 3rd blackbox testing method used is shotgun testing. 
"""


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
        # test to make sure no header message appears or redirected
        self.assert_text("", "#email") 

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
        # test if the message is correct
        self.assert_text("Registration failed.", "h4")

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
        # test if the message is correct
        self.assert_text("Registration failed.", "h4")

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
        # test if the message is correct
        self.assert_text("Enter your email and password", "h4")
 
    def test_register_fail_R1_7(self, *_):
        """
        This is a sample front end integration test to show
        user registration fails. R1-7: If the email has been used,
        the operation failed.
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
        # test if the message is correct
        self.assert_text("Registration failed.", "h4")
 
    def test_register_fail_R1_1_3(self, *_):
        """
        This is a sample front end integration test to show
        user registration failed. R1-1 Password cannot be empty,
        and the password input fails this requirement.
        """
        # open login page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testr113@test.com")
        self.type("#name", "userr113")
        self.type("#password", "")
        self.type("#password2", "")
 
        # click enter button
        self.click('input[type="submit"]')
        # test to make sure no header message appears or redirected
        self.assert_text("", "#password")

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
        self.type("#email", "testr141@test.com")
        self.type("#name", "userr141")
        self.type("#password", "Pas1!")
        self.type("#password2", "Pas1!")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("Registration failed.", "h4")

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
        self.type("#email", "testr142@test.com")
        self.type("#name", "userr142")
        self.type("#password", "pa$s123")
        self.type("#password2", "pa$s123")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("Registration failed.", "h4")
 
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
        self.type("#email", "testr143@test.com")
        self.type("#name", "userr143")
        self.type("#password", "PA$S123")
        self.type("#password2", "PA$S123")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("Registration failed.", "h4")

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
        self.type("#email", "testr144@test.com")
        self.type("#name", "userr144")
        self.type("#password", "pASs123")
        self.type("#password2", "pASs123")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("Registration failed.", "h4")

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
        self.type("#email", "testr145@test.com")
        self.type("#name", "userr145")
        self.type("#password", "pA$s123")
        self.type("#password2", "pA$s123")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("Enter your email and password", "h4")
 
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
        self.type("#email", "testr151@test.com")
        self.type("#name", "")
        self.type("#password", "pA$s123")
        self.type("#password2", "pA$s123")
 
        # click enter button
        self.click('input[type="submit"]')
        # test to make sure no header message appears or redirected
        self.assert_text("", "#name")
 
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
        self.type("#email", "testr152@test.com")
        self.type("#name", " userr152")
        self.type("#password", "pA$s123")
        self.type("#password2", "pA$s123")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("Registration failed.", "h4")
 
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
        self.type("#email", "testr153@test.com")
        self.type("#name", "userr153 ")
        self.type("#password", "pA$s123")
        self.type("#password2", "pA$s123")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("Registration failed.", "h4")
 
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
        self.type("#email", "testr154@test.com")
        self.type("#name", "userr154$")
        self.type("#password", "pA$s123")
        self.type("#password2", "pA$s123")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("Registration failed.", "h4")

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
        self.type("#email", "testr155@test.com")
        self.type("#name", "userr155")
        self.type("#password", "pA$s123")
        self.type("#password2", "pA$s123")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("Enter your email and password", "h4")
 
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
        self.type("#email", "testr161@test.com")
        self.type("#name", "u")
        self.type("#password", "pA$s123")
        self.type("#password2", "pA$s123")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("Registration failed.", "h4")
 
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
        self.type("#email", "testr162@test.com")
        self.type("#name", "userr162testr162ur162")
        self.type("#password", "pA$s123")
        self.type("#password2", "pA$s123")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("Registration failed.", "h4")

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
        self.type("#email", "testr163@test.com")
        self.type("#name", "userr163")
        self.type("#password", "pA$s123")
        self.type("#password2", "pA$s123")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("Enter your email and password", "h4")

    def test_register_fail_partition_1(self, *_):
        """
        This is a sample front end integration test using input partitoning 
        testing to show user registration Fail with password2 not 
        matching password.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testfailpart1@test.com")
        self.type("#name", "userfailpart1")
        self.type("#password", "pA$s123")
        self.type("#password2", "pA$s126")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("The passwords do not match", "h4")

    def test_register_fail_partition_2(self, *_):
        """
        Test using input partitoning testing to show user registration 
        Fail with password2 not matching password.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testfailpart2@test.com")
        self.type("#name", "userfailpart2")
        self.type("#password", "pAss123")
        self.type("#password2", "pA$s1234")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("The passwords do not match", "h4")
 
    def test_register_fail_partition_3(self, *_):
        """
        This is a sample front end integration test using input partitoning 
        testingto show user registration Fail with invalid username and
        password2 not matching password.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testfailpart3@test.com")
        self.type("#name", "userfailpart3#$")
        self.type("#password", "pA$s123")
        self.type("#password2", "pA$s126")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("The passwords do not match", "h4")

    def test_register_fail_partition_4(self, *_):
        """
        This is a sample front end integration testtest using input partitoning 
        testing to show user registration Fail with invalid username 
        and password.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testfailpart4@test.com")
        self.type("#name", "userfailpart4#$")
        self.type("#password", "pAss123")
        self.type("#password2", "pAss123")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("Registration failed.", "h4")

    def test_register_fail_partition_5(self, *_):
        """
        This is a sample front end integration test using input partitoning 
        testing to show user registration Fail. With invalid Username, 
        invalid password, and password2 not matching password.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testfailpart5@test.com")
        self.type("#name", "userfailpart5#$")
        self.type("#password", "pAss123")
        self.type("#password2", "pAss126")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("The passwords do not match", "h4")

    def test_register_fail_partition_6(self, *_):
        """
        This is a sample front end integration test  using input partitoning 
        testing to show user registration Fail. With invalid email and 
        password2 not matching password.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testfail@part6@test.com")
        self.type("#name", "userfailpart6")
        self.type("#password", "pA$s123")
        self.type("#password2", "pAss126")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("The passwords do not match", "h4")

    def test_register_fail_partition_7(self, *_):
        """
        This is a sample front end integration test  using input partitioning 
        testing to show user registration Fail. With invalid email and 
        password.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testfail@part7@test.com")
        self.type("#name", "userfailpart7")
        self.type("#password", "pAss123")
        self.type("#password2", "pAss123")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("Registration failed.", "h4")

    def test_register_fail_partition_8(self, *_):
        """
        This is a sample front end integration test  using input partitioning 
        testing to show user registration Fail. With invalid email, 
        password, and password 2 not matching password.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testfail@part8@test.com")
        self.type("#name", "userfailpart8")
        self.type("#password", "pAss123")
        self.type("#password2", "pAss126")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("The passwords do not match", "h4")

    def test_register_fail_partition_9(self, *_):
        """
        This is a sample front end integration test  using input partitioning 
        testing to show user registration Fail with invalid email, 
        and username.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testfail@part9@test.com")
        self.type("#name", "userfailpart#!9")
        self.type("#password", "pA$s123")
        self.type("#password2", "pA$s123")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("Registration failed.", "h4")

    def test_register_fail_partition_10(self, *_):
        """
        This is a sample front end integration test  using input partitioning 
        testing to show user registration Fail with invalid email, username,
        and password2 not matching password.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testfail@part10@test.com")
        self.type("#name", "userfailpart#!10")
        self.type("#password", "pA$s123")
        self.type("#password2", "pAss123")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("The passwords do not match", "h4")

    def test_register_fail_partition_11(self, *_):
        """
        This is a sample front end integration test  using input partitioning 
        testing to show user registration Fail with invalid email, username,
        and password while password2 matches password.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testfail@part11@test.com")
        self.type("#name", "userfailpart#!11")
        self.type("#password", "pAss123")
        self.type("#password2", "pAss123")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("Registration failed.", "h4")

    def test_register_fail_partition_12(self, *_):
        """
        This is a sample front end integration test  using input partitioning 
        testing to show user registration Fail with invalid email, username,
        password, and password2.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testfail@part12@test.com")
        self.type("#name", "userfailpart#!12")
        self.type("#password", "pAss123")
        self.type("#password2", "pAfs123")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("The passwords do not match", "h4")

    def test_register_shotgun_test_test_1(self, *_):
        """
        Random shotgun testing for email on register page.
        Some invalid characters that may be entered in email are 
        removed to improve the liklihood of successful user regestration.
        """
        for k in range(15):
            # open register page
            self.open(base_url + '/register')
            length = random.randint(0, 20)
            # fill email, name, password and password2
            prefix = ''.join(random.choice('@abcdefghijklmnopqrstuvwxyzABCDE' + 
                             'FGHIJKLMNOPQRSTUVWXYZ0123456789._-+&')
                             for i in range(length))
            length = random.randint(0, 10)
            suffix = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDE' + 
                             'FGHIJKLMNOPQRSTUVWXYZ01234')
                             for i in range(length))
            length = random.randint(0, 10)
            
            domain = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDE' + 
                             'FGHIJKLMNOPQRSTUVWXYZ0123456789!#')
                             for i in range(length))
            includeAt = random.randint(0, 10)
            if (includeAt == 0):
                atInclude = ""
            else:
                atInclude = '@'
            includeDot = random.randint(0, 10)
            if (includeDot == 0):
                dotInclude = ""
            else:
                dotInclude = '.'
            email = (prefix + atInclude + suffix + dotInclude + 
                     random.choice([domain, "com", "ca", "org", "edu", "net"]))

            print(email)
            includeAt = random.randint(0, 5)
            if (includeAt == 0):
                email = ""
            self.type("#email", email)
            
            self.type("#name", "userR11")
            self.type("#password", "Password1!")
            self.type("#password2", "Password1!")
    
            # click enter button
            
            self.click('input[type="submit"]')
            
            if len(email) == 0:
                self.assert_text("", "#email")
            elif (self.get_current_url() == base_url + '/register'):
                # test to make sure no header message appears or redirected
                self.assert_text("Registration failed.", "h4") 
            else: 
                self.assert_text("Enter your email and password", "h4")
   
    def test_register_shotgun_test_test_2(self, *_):
        """
        Random shotgun testing for name on register page
        """
        for i in range(15):
            # open register page
            self.open(base_url + '/register')
            i = i + 1
            workingEmail = ("emailworking" + str(i) + "@testmail.com")
            self.type("#email", workingEmail)
            length = random.randint(0, 30)
            nameTest = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz' +
                               'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#')
                               for i in range(length))
            self.type("#name", nameTest)
            self.type("#password", "Password1!")
            self.type("#password2", "Password1!")
    
            # click enter button
            print(workingEmail, "    ", nameTest)
            
            self.click('input[type="submit"]')
            
            if len(nameTest) == 0:
                self.assert_text("", "#name")
            elif (self.get_current_url() == base_url + '/register'):
                # test to make sure no header message appears or redirected
                self.assert_text("Registration failed.", "h4") 
            else: 
                self.assert_text("Enter your email and password", "h4")

    def test_register_shotgun_test_test_3(self, *_):
        """
        Random shotgun testing for password on register page
        """
        for i in range(15):
            # open register page
            self.open(base_url + '/register')
            i = i + 1
            workingEmail = ("emailworking" + str(i) + "@testmail.com")
            self.type("#email", workingEmail)
            self.type("#name", "nameTest1")
            length = random.randint(0, 30)
            testPassword = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz' + 
                                   'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@' +
                                                 '#$%^&*()_-+=\\//')
                                   for i in range(length))
            self.type("#password", testPassword)
            self.type("#password2", testPassword)
    
            # click enter button            
            self.click('input[type="submit"]')
            
            if len(testPassword) == 0:
                self.assert_text("", "#password")
            elif (self.get_current_url() == base_url + '/register'):
                # test to make sure no header message appears or redirected
                self.assert_text("Registration failed.", "h4") 
            else: 
                self.assert_text("Enter your email and password", "h4")

    def test_register_shotgun_test_test_4(self, *_):
        """
        Random shotgun testing for password and password2 matching or 
        being empty on register page
        """
        for i in range(25):
            # open register page
            self.open(base_url + '/register')
            i = i + 1
            workingEmail = ("emailworking" + str(i) + "@testmail.com")
            self.type("#email", workingEmail)
            self.type("#name", "nameTest1")
            length = random.randint(0, 30)
            testPassword = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz' +
                                   'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@' +
                                                 '#$%^&*()_-+=\\//') 
                                   for i in range(length))
            self.type("#password", testPassword)
            testPassword2 = ""
            if random.randint(0, 1) == 1:
                testPassword2 = "pA$s123"
            else:
                testPassword = testPassword2
            self.type("#password2", testPassword2)
    
            # click enter button         
            self.click('input[type="submit"]')
            
            if ((len(testPassword) == 0) or (len(testPassword) == 0)):
                self.assert_text("", "#password")
            elif (testPassword != testPassword2):
                self.assert_text("The passwords do not match", "h4") 
            else: 
                self.assert_text("Enter your email and password", "h4")

    def test_register_shotgun_1(self, *_):
        """
        This is a sample black box shotgun test case.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testshot1@test.com")
        self.type("#name", "usershot1")
        self.type("#password", "pA$s123")
        self.type("#password2", "pA$s123")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("Enter your email and password", "h4")

    def test_register_shotgun_2(self, *_):
        """
        This is a sample black box shotgun test case.
        Here, name is 2 characters.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testregshot2@test.com")
        self.type("#name", "Re")
        self.type("#password", "Rental$123")
        self.type("#password2", "Rental$123")

        # click enter button
        self.click('input[type="submit"]')
        # Test if the message is correct.
        self.assert_text("Registration failed.", "h4")

    def test_register_shotgun_3(self, *_):
        """
        This is a sample black box shotgun test case. Registration Fails.
        Here, input is long email, but password2 does not match with password.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testshotreallyreallylongstrquenessint3@test.com")
        self.type("#name", "usershot3")
        self.type("#password", "pA#s123")
        self.type("#password2", "pA$s123")
 
        # click enter button
        self.click('input[type="submit"]')
        # Test if the message is correct.
        self.assert_text("The passwords do not match", "h4")
 
    def test_register_shotgun_4(self, *_):
        """
        This is a sample black box shotgun test case.
        Here, just password does not meet requirements.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testshot4@test.com")
        self.type("#name", "usershot4")
        self.type("#password", "prop")
        self.type("#password2", "prop")
 
        # click enter button
        self.click('input[type="submit"]')
        # Test if the message is correct.
        self.assert_text("Registration failed.", "h4")
 
    def test_register_shotgun_5(self, *_):
        """
        This is a sample black box shotgun test case.
        Here, name is incorrect because name begins with a space.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testshotdance5@test.com")
        self.type("#name", " junioruser5")
        self.type("#password", "Pa#dance5")
        self.type("#password2", "Pa#dance5")
 
        # click enter button
        self.click('input[type="submit"]')
        # Test if the message is correct.
        self.assert_text("Registration failed.", "h4")
 
    def test_register_shotgun_6(self, *_):
        """
        This is a sample black box shotgun test case.
        Here, more than one special character is used in password.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testshot6@test.com")
        self.type("#name", "usershot6")
        self.type("#password", "Pa!danc#$6")
        self.type("#password2", "Pa!danc#$6")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("Enter your email and password", "h4")
 
    def test_register_shotgun_7(self, *_):
        """
        This is a sample black box shotgun test case.
        Here, username is in all capitals. However, there is
        no lowercase character in the password.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "test.shot7@test.com")
        self.type("#name", "USERSHOT7")
        self.type("#password", "PA!USERS$7")
        self.type("#password2", "PA!USERS$7")
 
        # click enter button
        self.click('input[type="submit"]')
        # Test if the message is correct.
        self.assert_text("Registration failed.", "h4")
 
    def test_register_shotgun_8(self, *_):
        """
        This is a sample black box shotgun test case.
        Here, password has no character with a lowercase and
        email does not have @ character.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "test-shot8test.com")
        self.type("#name", "USERSHOT8")
        self.type("#password", "YO?USERS#8")
        self.type("#password2", "YO?USERS#8")
 
        # click enter button
        self.click('input[type="submit"]')
        # Test if the message is correct.
        self.assert_text("Registration failed.", "h4")
   
    def test_register_shotgun_9(self, *_):
        """
        This is a sample black box shotgun test case.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testshot9@test.com")
        self.type("#name", "usershot9")
        self.type("#password", "Apuff%123")
        self.type("#password2", "Apuff$s123")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("The passwords do not match", "h4")
 
    def test_register_shotgun_10(self, *_):
        """
        This is a sample black box shotgun test case.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "tests+hot10@test.com")
        self.type("#name", "usershot10")
        self.type("#password", "Pa$S123")
        self.type("#password2", "Pa$S123")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("Enter your email and password", "h4")

    def test_register_shotgun_11(self, *_):
        """
        This is a sample black box shotgun test case.
        Here, password do not have any alphabet.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testshot11@test.com")
        self.type("#name", "usershot11")
        self.type("#password", "$@$#$123")
        self.type("#password2", "$@$#$123")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("Registration failed.", "h4")
 
    def test_register_shotgun_12(self, *_):
        """
        This is a sample black box shotgun test case.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testshot12@test.com")
        self.type("#name", "usershot12")
        self.type("#password", "s@$#$123")
        self.type("#password2", "$@$#$123")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("The passwords do not match", "h4")
   
    def test_register_shotgun_13(self, *_):
        """
        This is a sample black box shotgun test case.
        Here, name is invalid.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testshot13@test.com")
        self.type("#name", "#5usershot!13")
        self.type("#password", "pA$s123")
        self.type("#password2", "pA$s123")
 
        # click enter button
        self.click('input[type="submit"]')
        # Test if the message is correct.
        self.assert_text("Registration failed.", "h4")
 
    def test_register_shotgun_14(self, *_):
        """
        This is a sample black box shotgun test case.
        Here, email contains space, so registration fail.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "test - shot14@test.com")
        self.type("#name", "USERSHOT14")
        self.type("#password", "wOrd$123")
        self.type("#password2", "wOrd$123")
 
        # click enter button
        self.click('input[type="submit"]')
        # Test if the message is correct.
        self.assert_text("Registration failed.", "h4")
   
    def test_register_shotgun_15(self, *_):
        """
        This is a sample black box shotgun test case.
        Here, email contains brackets and symbol, so registration fail.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testshot(1+5)@test.com")
        self.type("#name", "usershotg15")
        self.type("#password", "wOrd$123")
        self.type("#password2", "wOrd$123")
 
        # click enter button
        self.click('input[type="submit"]')
 
        # Test if the message is correct.
        self.assert_text("Registration failed.", "h4")
   
    def test_register_shotgun_16(self, *_):
        """
        This is a sample black box shotgun test case.
        Here, name has upper, lowecase and numebers; registration test pass.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testshot15@test.com")
        self.type("#name", "16Usershot")
        self.type("#password", "576$Pell")
        self.type("#password2", "576$Pell")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("Enter your email and password", "h4")
 
    def test_register_shotgun_17(self, *_):
        """
        This is a sample black box shotgun test case.
        Here, email has just 2 characters before @.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "be@test.com")
        self.type("#name", "usershot17")
        self.type("#password", "576$Pell")
        self.type("#password2", "576$Pell")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("Enter your email and password", "h4")
   
    def test_register_shotgun_18(self, *_):
        """
        This is a sample black box shotgun test case.
        Here, email has just numbers and special characters.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "+18-5@test.com")
        self.type("#name", "usershot18")
        self.type("#password", "5d76$Pell")
        self.type("#password2", "5d76$Pell")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("Enter your email and password", "h4")
   
    def test_register_shotgun_19(self, *_):
        """
        This is a sample black box shotgun test case.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "tests_7hot19@test.com")
        self.type("#name", "userShot19")
        self.type("#password", "Pa$S123")
        self.type("#password2", "Pa$S123")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("Enter your email and password", "h4")
 
    def test_register_shotgun_20(self, *_):
        """
        This is a sample black box shotgun test case.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testshot20@test.com")
        self.type("#name", "usershotisreallyreallyreallyreallylong20")
        self.type("#password", "Spell#123")
        self.type("#password2", "Spell#123")
 
        # click enter button
        self.click('input[type="submit"]')
 
        # Test if the message is correct.
        self.assert_text("Registration failed.", "h4")
   
    def test_register_shotgun_21(self, *_):
        """
        This is a sample black box shotgun test case.
        Here, name is too long.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "testshot21@test.com")
        self.type("#name", "usershotisreallyreallyreallyreallylong21")
        self.type("#password", "SpellSpellSpellSpellSpellSpellSpellSpell#123")
        self.type("#password2", "SpellSpellSpellSpellSpellSpellSpellSpell#123")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("Registration failed.", "h4")
 
    def test_register_shotgun_22(self, *_):
        """
        This is a sample black box shotgun test case.
        Here, email
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "test234143343143143431234123413shot21@test.com")
        self.type("#name", "usershot22")
        self.type("#password", "pA$s723")
        self.type("#password2", "pA$s723")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("Enter your email and password", "h4")
   
    def test_register_shotgun_23(self, *_):
        """
        This is a sample black box shotgun test case.
        Here, email has numbers in between.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "test21shot_94s@test.com")
        self.type("#name", "usershoT23")
        self.type("#password", "pA$ss823")
        self.type("#password2", "pA$ss823")
 
        # click enter button
        self.click('input[type="submit"]')
        # test if the message is correct
        self.assert_text("Enter your email and password", "h4")
 
    def test_register_shotgun_24(self, *_):
        """
        This is a sample black box shotgun test case.
        Here, name has non alphanumeric symbols.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "test24shotg@test.com")
        self.type("#name", "user$$hoT23")
        self.type("#password", "pA$ss824")
        self.type("#password2", "pA$ss824")
 
        # click enter button
        self.click('input[type="submit"]')
        # Test if the message is correct.
        self.assert_text("Registration failed.", "h4")
   
    def test_register_shotgun_25(self, *_):
        """
        This is a sample black box shotgun test case.
        Here, password2 does not match password.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, name, password and password2
        self.type("#email", "test24shotg@test.com")
        self.type("#name", "usershot25")
        self.type("#password", "mI$ss825")
        self.type("#password2", "mIsss825")
 
        # click enter button
        self.click('input[type="submit"]')
        # Test if the message is correct.
        self.assert_text("The passwords do not match", "h4")
