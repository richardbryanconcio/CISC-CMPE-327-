from seleniumBase import Basecase

import org.openqa.selenium.By as By

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import User

# Contains integration tests for the login page

class FrontEndLoginPageTest(Basecase):

    # TEST CASE 1: LOGIN SUCCESS
    def test_login_success(self, *_):

        # Tests if the user has logged in successfully with a registered account

        # Opens up the login page
        self.open(base_url + '/login')

        # Checks if 'Sign in' header is present
        self.assert_text("Sign in", "h1")
        # Checks if line of text is present
        self.assert_text("Enter your email address and password", "p")

        # Entered email and password of registered account
        self.type("#email", "testing@gmail.com")
        self.type("#password", "Testing1234!")

        # Clicks 'remember me' button
        self.findElement(By.id("remember_me")).click()
        self.click('input[type="checkbox"]')

        # Clicks the 'sign in' button
        self.click('input[type="submit"]')

        # Checks that the user is redirected to the home page
        self.assert_title(base_url)

        # Once user clicked the sign in button, they should be redirected to the home page
        # Should see the success message at the top of the page
        self.assert_text("Login Successful!", "h4")

        # Checks if 'Pocket Rentals' header redirects user to homepage when clicked
        self.findElement(By.linkText("Pocket Rentals")).click()
        self.assert_title(base_url)


    # TEST CASE 2: LOGIN FAIL (incorrect password for email)
    def test_login_fail_1(self, *_):

        # Tests if the user fails to login with incorrect password to email

        # Opens up the login page
        self.open(base_url + '/login')

        # Checks if 'Sign in' header is present
        self.assert_text("Sign in", "h1")
        # Checks if line of text is present
        self.assert_text("Enter your email address and password", "p")

        # Enters correct email, but incorrect password
        self.type("#email", "testing@gmail.com")
        self.type("#password", "1234")

        # Clicks 'remember me' button
        self.findElement(By.id("remember_me")).click()
        self.click('input[type="checkbox"]')

        # Clicks the 'sign in' button
        self.click('input[type="submit"]')

        # Checks that the user is redirected to the login page
        self.assert_title(base_url + '/login')

        # Should see the flash message at the top of the page
        self.assert_flash_message("Login failed. Please try again.", "#message")


    # TEST CASE 3: LOGIN FAIL (incorrect email for password)
    def test_login_fail_2(self, *_):

        # Tests if the user fails to login with incorrect email to password

        # Opens up the login page
        self.open(base_url + '/login')

        # Checks if 'Sign in' header is present
        self.assert_text("Sign in", "h1")
        # Checks if line of text is present
        self.assert_text("Enter your email address and password", "p")

        # Enters incorrect email, but correct password
        self.type("#email", "incorrect@gmail.com")
        self.type("#password", "Testing1234!")

        # Clicks 'remember me' button
        self.findElement(By.id("remember_me")).click()
        self.click('input[type="checkbox"]')

        # Clicks the sign in button
        self.click('input[type="submit"]')

        # Checks that the user is redirected to the login page
        self.assert_title(base_url + '/login')

        # Should see the flash message at the top of the page
        self.assert_flash_message("Login failed. Please try again.", "#message")


    # TEST CASE 4: LOGIN FAIL (account not registered)    
    def test_login_fail_3(self, *_):

        # Tests if the user has not registered an account

        # Opens up the login page
        self.open(base_url + '/login')

        # Checks if 'Sign in' header is present
        self.assert_text("Sign in", "h1")
        # Checks if line of text is present
        self.assert_text("Enter your email address and password", "p")
        
        # Enters email and password of an unregistered account
        self.type("#email", "unregistered@gmail.com")
        self.type("#password", "unregistered")

        # Clicks 'remember me' button
        self.findElement(By.id("remember_me")).click()
        self.click('input[type="checkbox"]')

        # Clicks the 'sign in' button
        self.click('input[type="submit"]')
      
        # Checks that the user is redirected to the login page
        self.assert_title(base_url + '/login')

        # Should see the flash message at the top of the page
        self.assert_flash_message("Login failed. Please try again.", "#message")

        # Checks if 'Create new account' redirects user to register page when clicked
        self.findElement(By.linkText("Create new account")).click()
        self.assert_title(base_url + '/register')
        

    # TEST CASE 5: LOGIN FAIL (no email entered)
    def test_login_fail_4(self, *_):

        # Tests if the user has not entered an email; only a password

        # Opens up the login page
        self.open(base_url + '/login')

        # Checks if 'Sign in' header is present
        self.assert_text("Sign in", "h1")
        # Checks if line of text is present
        self.assert_text("Enter your email address and password", "p")

        # Enters password, but no email
        self.type("#email", " ")
        self.type("#password", "Testing1234!")
        
        # Clicks 'remember me' button
        self.findElement(By.id("remember_me")).click()
        self.click('input[type="checkbox"]')

        # Clicks the 'sign in' button
        self.click('input[type="submit"]')

        # Checks that the user is redirected to the login page
        self.assert_title(base_url + '/login')

        # Should see the flash message at the top of the page
        self.assert_flash_message("Login failed. Please try again.", "#message")

    
    # TEST CASE 6: LOGIN FAIL (no password entered)
    def test_login_fail_5(self, *_):

        # Tests if the user has not entered a password; only an email

        # Opens up the login page
        self.open(base_url + '/login')

        # Checks if 'Sign in' header is present
        self.assert_text("Sign in", "h1")
        # Checks if line of text is present
        self.assert_text("Enter your email address and password", "p")

        # Enters email, but no password
        self.type("#email", "testing@gmail.com")
        self.type("#password", " ")

        # Clicks 'remember me' button
        self.findElement(By.id("remember_me")).click()
        self.click('input[type="checkbox"]')

        # Clicks the 'sign in' button
        self.click('input[type="submit"]')

        # Checks that the user is redirected to the login page
        self.assert_title(base_url + '/login')

        # Should see the flash message at the top of the page
        self.assert_flash_message("Login failed. Please try again.", "#message")


    # TEST CASE 7: LOGIN FAIL (no email and password entered)
    def test_login_fail_6(self, *_):

        # Tests if the user has not entered an email or password

        # Opens up the login page
        self.open(base_url + '/login')

        # Checks if 'Sign in' header is present
        self.assert_text("Sign in", "h1")
        # Checks if line of text is present
        self.assert_text("Enter your email address and password", "p")

        # Enters no email and no password
        self.type("#email", " ")
        self.type("#password", " ")

        # Clicks 'remember me' button
        self.findElement(By.id("remember_me")).click()
        self.click('input[type="checkbox"]')

        # Clicks the 'sign in' button
        self.click('input[type="submit"]')

        # Checks that the user is redirected to the login page
        self.assert_title(base_url + '/login')

        # Should see the flash message at the top of the page
        self.assert_flash_message("Login failed. Please try again.", "#message")

    

        

       

       