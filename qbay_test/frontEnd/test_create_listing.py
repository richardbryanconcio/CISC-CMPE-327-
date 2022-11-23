from seleniumbase import BaseCase

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import User, register

from datetime import date, datetime
import random

"""
This file defines all integration tests for the frontend create listing page.
"""

"""
class FrontEndCreateListingTest(BaseCase):
    # create a user for testing, if it already exists in the db then pass
    # should be replaced with a login once authentication is up and running
    try:
        register("createListingTest", "test@test.com", "!Q1q12345")
    except Exception:
        pass

    def test_r4_1_create_listing(self, *_):
        '''
        R4-1: The title of the product has to be alphanumeric-only,
        and space allowed only if it is not as prefix and suffix.

        tested using input partion testing where the input is title
        '''
        # a set of valid inputs for creating a listing
        desciption = "This is a test description"
        price = "100"
        startDate = "01/01/2022"
        endDate = "01/01/2024"

        # p1 = title with a space prefix
        # expected = fail
        self.open(base_url + '/createListing')
        self.type("#title", " title with prefix")
        self.type("#description", desciption)
        self.type("#price", price)
        self.type("#startDate", startDate)
        self.type("#endDate", endDate)
        self.click('input[type="submit"]')
        # check invalid message is shown
        assert self.get_current_url() == base_url + '/createListing'
        self.assert_text(
            "creating listing failed, please try again", "#message")

        # p2 = title with a space suffix
        # expected = fail
        self.open(base_url + '/createListing')
        self.type("#title", "title with suffix ")
        self.type("#description", desciption)
        self.type("#price", price)
        self.type("#startDate", startDate)
        self.type("#endDate", endDate)
        self.click('input[type="submit"]')
        # check invalid message is shown
        assert self.get_current_url() == base_url + '/createListing'
        self.assert_text(
            "creating listing failed, please try again", "#message")

        # p3 = title is non-alphanumeric
        # expected = fail
        self.open(base_url + '/createListing')
        self.type("#title", "non-alphanumeric!")
        self.type("#description", desciption)
        self.type("#price", price)
        self.type("#startDate", startDate)
        self.type("#endDate", endDate)
        self.click('input[type="submit"]')
        # check invalid message is shown
        assert self.get_current_url() == base_url + '/createListing'
        self.assert_text(
            "creating listing failed, please try again", "#message")

        # p4 = title is alphanumeric without space as prefix or suffix
        # expected = fail
        self.open(base_url + '/createListing')
        self.type("#title", "valid title")
        self.type("#description", desciption)
        self.type("#price", price)
        self.type("#startDate", startDate)
        self.type("#endDate", endDate)
        self.click('input[type="submit"]')
        # check we are redirected to home
        assert self.get_current_url() == base_url + "/"

    def test_r4_2_create_listing(self, *_):
        '''
        R4-2: The title of the product is no longer than 80 characters.

        tested using hybrid testing with input partioning and shotgun testing
        '''
        # a set of valid inputs for creating a listing
        # description must be longer then title
        description = ''.join(random.choice(
            'abcdefghijklmnopqrstuvwxyz') for i in range(161))
        price = "100"
        startDate = "01/01/2022"
        endDate = "01/01/2024"

        # p1 = title is 80 characters long
        # expected = pass
        self.open(base_url + '/createListing')
        self.type("#title", ''.join(random.choice(
            'abcdefghijklmnopqrstuvwxyz') for i in range(80)))
        self.type("#description", description)
        self.type("#price", price)
        self.type("#startDate", startDate)
        self.type("#endDate", endDate)
        self.click('input[type="submit"]')
        # check we are redirected to home
        assert self.get_current_url() == base_url + "/"

        # p2 = title is 81 characters long
        # expected = fail
        self.open(base_url + '/createListing')
        self.type("#title", ''.join(random.choice(
            'abcdefghijklmnopqrstuvwxyz') for i in range(81)))
        self.type("#description", description)
        self.type("#price", price)
        self.type("#startDate", startDate)
        self.type("#endDate", endDate)
        self.click('input[type="submit"]')
        # check invalid message is shown
        assert self.get_current_url() == base_url + '/createListing'
        self.assert_text(
            "creating listing failed, please try again", "#message")

        # p3 = title is 100 characters long
        # expected = fail
        self.open(base_url + '/createListing')
        self.type("#title", ''.join(random.choice(
            'abcdefghijklmnopqrstuvwxyz') for i in range(100)))
        self.type("#description", description)
        self.type("#price", price)
        self.type("#startDate", startDate)
        self.type("#endDate", endDate)
        self.click('input[type="submit"]')
        # check invalid message is shown
        assert self.get_current_url() == base_url + '/createListing'
        self.assert_text(
            "creating listing failed, please try again", "#message")

        for i in range(10):
            # generate a title with length between 1 and 150
            length = random.randint(1, 160)
            title = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz')
                            for i in range(length))
            self.open(base_url + '/createListing')
            self.type("#title", title)
            self.type("#description", description)
            self.type("#price", price)
            self.type("#startDate", startDate)
            self.type("#endDate", endDate)
            self.click('input[type="submit"]')

            if (length > 80):
                # check invalid message is shown
                assert self.get_current_url() == base_url + '/createListing'
                self.assert_text(
                    "creating listing failed, please try again", "#message")
            else:
                # check that we are redirected to home page
                assert self.get_current_url() == base_url + "/"

    def test_r4_3_create_listing(self, *_):
        '''
        R4-3: The description of the product can be arbitrary characters, 
            with a minimum length of 20 characters 
            and a maximum of 2000 characters.

        tested using hybrid testing with input partioning and shotgun testing
        '''
        # a set of valid inputs for creating a listing
        title = title = "r4 3 1"
        price = "100"
        startDate = "01/01/2022"
        endDate = "01/01/2024"

        # p1 = description is 20 characters long
        # expected = pass
        self.open(base_url + '/createListing')
        self.type("#title", 'p1')
        self.type("#description", ''.join(random.choice(
            'abcdefghijklmnopqrstuvwxyz') for i in range(20)))
        self.type("#price", price)
        self.type("#startDate", startDate)
        self.type("#endDate", endDate)
        self.click('input[type="submit"]')
        # check we are redirected to home
        assert self.get_current_url() == base_url + "/"

        # p2 = description is 21 characters long
        # expected = pass
        self.open(base_url + '/createListing')
        self.type("#title", 'p2')
        self.type("#description", ''.join(random.choice(
            'abcdefghijklmnopqrstuvwxyz') for i in range(21)))
        self.type("#price", price)
        self.type("#startDate", startDate)
        self.type("#endDate", endDate)
        self.click('input[type="submit"]')
        # check we are redirected to home
        assert self.get_current_url() == base_url + "/"

        # p3 = description is 2000 characters long
        # expected = pass
        self.open(base_url + '/createListing')
        self.type("#title", 'p3')
        self.type("#description", ''.join(random.choice(
            'abcdefghijklmnopqrstuvwxyz') for i in range(2000)))
        self.type("#price", price)
        self.type("#startDate", startDate)
        self.type("#endDate", endDate)
        self.click('input[type="submit"]')
        # check we are redirected to home
        assert self.get_current_url() == base_url + "/"

        # p4 = description is 2001 characters long
        # expected = fail
        self.open(base_url + '/createListing')
        self.type("#title", 'p4')
        self.type("#description", ''.join(random.choice(
            'abcdefghijklmnopqrstuvwxyz') for i in range(2001)))
        self.type("#price", price)
        self.type("#startDate", startDate)
        self.type("#endDate", endDate)
        self.click('input[type="submit"]')
        # check invalid message is shown
        assert self.get_current_url() == base_url + '/createListing'
        self.assert_text(
            "creating listing failed, please try again", "#message")

        for i in range(10):
            # generate a description with length between 1 and 150
            length = random.randint(1, 4000)
            description = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz')
                                  for i in range(length))
            self.open(base_url + '/createListing')
            self.type("#title", title)
            self.type("#description", description)
            self.type("#price", price)
            self.type("#startDate", startDate)
            self.type("#endDate", endDate)
            self.click('input[type="submit"]')

            if (len(description) > 2000 or len(description) < 20):
                # check invalid message is shown
                assert self.get_current_url() == base_url + '/createListing'
                self.assert_text(
                    "creating listing failed, please try again", "#message")
            else:
                # check that we are redirected to home page
                assert self.get_current_url() == base_url + "/"

                # create new title if a listing was created successfully (r4_8)
                title = title[:5] + str(int(title[5:]) + 1)

    def test_r4_4_create_listing(self, *_):
        '''
        R4-4: Description has to be longer than the product's title.

        tested using hybrid testing with input partioning and shotgun testing
        '''
        # a set of valid inputs for creating a listing
        price = "100"
        startDate = "01/01/2022"
        endDate = "01/01/2024"

        # p1 = title is 20 character long, description is 22 characters long
        # expected = pass
        self.open(base_url + '/createListing')
        self.type("#title", ''.join(random.choice(
            'abcdefghijklmnopqrstuvwxyz') for i in range(20)))
        self.type("#description", ''.join(random.choice(
            'abcdefghijklmnopqrstuvwxyz') for i in range(22)))
        self.type("#price", price)
        self.type("#startDate", startDate)
        self.type("#endDate", endDate)
        self.click('input[type="submit"]')
        # check we are redirected to home
        assert self.get_current_url() == base_url + "/"

        # p2 = title is 22 character long, description is 22 character long
        # expected = fail
        self.open(base_url + '/createListing')
        self.type("#title", ''.join(random.choice(
            'abcdefghijklmnopqrstuvwxyz') for i in range(22)))
        self.type("#description", ''.join(random.choice(
            'abcdefghijklmnopqrstuvwxyz') for i in range(22)))
        self.type("#price", price)
        self.type("#startDate", startDate)
        self.type("#endDate", endDate)
        self.click('input[type="submit"]')
        # check invalid message is shown
        assert self.get_current_url() == base_url + '/createListing'
        self.assert_text(
            "creating listing failed, please try again", "#message")

        # p3 = title is 40 character long, description is 39 characters long
        # expected = fail
        self.open(base_url + '/createListing')
        self.type("#title", ''.join(random.choice(
            'abcdefghijklmnopqrstuvwxyz') for i in range(40)))
        self.type("#description", ''.join(random.choice(
            'abcdefghijklmnopqrstuvwxyz') for i in range(39)))
        self.type("#price", price)
        self.type("#startDate", startDate)
        self.type("#endDate", endDate)
        self.click('input[type="submit"]')
        # check invalid message is shown
        assert self.get_current_url() == base_url + '/createListing'
        self.assert_text(
            "creating listing failed, please try again", "#message")

        # p4 = title is 79 character long, description is 100 characters long
        # expected = pass
        self.open(base_url + '/createListing')
        self.type("#title", ''.join(random.choice(
            'abcdefghijklmnopqrstuvwxyz') for i in range(79)))
        self.type("#description", ''.join(random.choice(
            'abcdefghijklmnopqrstuvwxyz') for i in range(100)))
        self.type("#price", price)
        self.type("#startDate", startDate)
        self.type("#endDate", endDate)
        self.click('input[type="submit"]')
        # check we are redirected to home
        assert self.get_current_url() == base_url + "/"

        titlesUsed = ['']
        title = ''
        for i in range(10):
            # generate a description and title with length between 20 and 80 
            # (to fulfill r4_2 and r4_3)
            length = random.randint(20, 80)
            description = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz')
                                  for i in range(length))
            length = random.randint(20, 80)

            # ensure no duplicate titles are used
            while title in titlesUsed:
                title = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz')
                                for i in range(length))
            titlesUsed.append(title)

            self.open(base_url + '/createListing')
            self.type("#title", title)
            self.type("#description", description)
            self.type("#price", price)
            self.type("#startDate", startDate)
            self.type("#endDate", endDate)
            self.click('input[type="submit"]')

            if (len(title) >= len(description)):
                # check invalid message is shown
                assert self.get_current_url() == base_url + '/createListing'
                self.assert_text(
                    "creating listing failed, please try again", "#message")
            else:
                # check that we are redirected to home page
                assert self.get_current_url() == base_url + "/"

    def test_r4_5_create_listing(self, *_):
        '''
        R4-5: Price has to be of range [10, 10000].

        tested using hybrid testing with input partioning and shotgun testing
        '''
        # a set of valid inputs for creating a listing
        title = "r4 5 1"
        description = "This is a test description"
        price = "100"
        startDate = "01/01/2022"
        endDate = "01/01/2024"

        # p1 = price is 20
        # expected = pass
        self.open(base_url + '/createListing')
        self.type("#title", 'a1')
        self.type("#description", description)
        self.type("#price", "20")
        self.type("#startDate", startDate)
        self.type("#endDate", endDate)
        self.click('input[type="submit"]')
        # check we are redirected to home
        assert self.get_current_url() == base_url + "/"

        # p2 = price is 10
        # expected = pass
        self.open(base_url + '/createListing')
        self.type("#title", 'b1')
        self.type("#description", description)
        self.type("#price", "10")
        self.type("#startDate", startDate)
        self.type("#endDate", endDate)
        self.click('input[type="submit"]')
        # check we are redirected to home
        assert self.get_current_url() == base_url + "/"

        # p3 = price is 10000
        # expected = pass
        self.open(base_url + '/createListing')
        self.type("#title", 'c1')
        self.type("#description", description)
        self.type("#price", "10000")
        self.type("#startDate", startDate)
        self.type("#endDate", endDate)
        self.click('input[type="submit"]')
        # check we are redirected to home
        assert self.get_current_url() == base_url + "/"

        # p4 = price is 10001
        # expected = fail
        self.open(base_url + '/createListing')
        self.type("#title", 'd1')
        self.type("#description", description)
        self.type("#price", "10001")
        self.type("#startDate", startDate)
        self.type("#endDate", endDate)
        self.click('input[type="submit"]')
        # check invalid message is shown
        assert self.get_current_url() == base_url + '/createListing'
        self.assert_text(
            "creating listing failed, please try again", "#message")

        # p5 = price is 9
        # expected = fail
        self.open(base_url + '/createListing')
        self.type("#title", 'e1')
        self.type("#description", description)
        self.type("#price", "9")
        self.type("#startDate", startDate)
        self.type("#endDate", endDate)
        self.click('input[type="submit"]')
        # check invalid message is shown
        assert self.get_current_url() == base_url + '/createListing'
        self.assert_text(
            "creating listing failed, please try again", "#message")

        for i in range(10):
            # generate a description and title with length between 20 and 80 
            # (to fulfill r4_2 and r4_3)
            price = random.randint(0, 20000)
            self.open(base_url + '/createListing')
            self.type("#title", title)
            self.type("#description", description)
            self.type("#price", price)
            self.type("#startDate", startDate)
            self.type("#endDate", endDate)
            self.click('input[type="submit"]')

            if (price < 10 or price > 10000):
                # check invalid message is shown
                assert self.get_current_url() == base_url + '/createListing'
                self.assert_text(
                    "creating listing failed, please try again", "#message")
            else:
                # check that we are redirected to home page
                assert self.get_current_url() == base_url + "/"

                # create new title if a listing was created successfully (r4_8)
                title = title[:5] + str(int(title[5:]) + 1)

    def test_r4_8_create_listing(self, *_):
        '''
        R4-8: A user cannot create products that have the same title.

        tested using input partion testing
        '''

        # a set of valid inputs for creating a listing
        desciption = "This is a test description"
        price = "100"
        startDate = "01/01/2022"
        endDate = "01/01/2024"

        # p1 = create listing with a unique title
        # expected = success
        self.open(base_url + '/createListing')
        self.type("#title", "unqiue title")
        self.type("#description", desciption)
        self.type("#price", price)
        self.type("#startDate", startDate)
        self.type("#endDate", endDate)
        self.click('input[type="submit"]')
        # check we are redirected to home
        assert self.get_current_url() == base_url + "/"

        # p2 = create listing identical to p1
        # expected = fail
        self.open(base_url + '/createListing')
        self.type("#title", "unqiue title")
        self.type("#description", desciption)
        self.type("#price", price)
        self.type("#startDate", startDate)
        self.type("#endDate", endDate)
        self.click('input[type="submit"]')
        # check invalid message is shown
        assert self.get_current_url() == base_url + '/createListing'
        self.assert_text(
            "creating listing failed, please try again", "#message")

        # p3 = create listing where only the title is the same
        # expected = fail
        self.open(base_url + '/createListing')
        self.type("#title", "unqiue title")
        self.type("#description", "new description that is different")
        self.type("#price", 900)
        self.type("#startDate", "01/20/2022")
        self.type("#endDate", "01/20/2024")
        self.click('input[type="submit"]')
        # check invalid message is shown
        assert self.get_current_url() == base_url + '/createListing'
        self.assert_text(
            "creating listing failed, please try again", "#message")
"""