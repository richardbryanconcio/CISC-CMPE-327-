from seleniumbase import BaseCase

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import User, Listing, changeLastModifiedDate

from datetime import date, datetime
import random

"""
This file defines all integration tests for the frontend update listing page.

R5-1: One can update all attributes of the listing, 
except owner_id and last_modified_date. 
R5-2: Price can be only increased but cannot be decreased :)
R5-3: last_modified_date should be updated 
when the update operation is successful.
R5-4: When updating an attribute, one has to make sure 
that it follows the same requirements as above.
"""


class FrontEndCreateListingTest(BaseCase):
    # create a user for testing, if it already exists in the db then pass
    # should be replaced with a login once authentication is up and running

    def test_r5_1_update_listing(self, *_):
        '''
        R5-1: One can update all attributes of the listing, 
        except owner_id and last_modified_date.

        tested using input testing
        no blackbox testing methods can be used here 
        since the output is either true or false
        '''
        listings = Listing.query.all()
        listing = listings[0]
        id = listing.id

        # update the listing title
        self.open(base_url + "/updateListing/" + str(id))
        self.update_text("input[name='title']", "updated title")
        self.click('input[type="submit"]')
        assert self.get_current_url() == base_url + '/listing/' + str(id)
        self.assert_text("updated title", "h1")

        # update the listing description
        self.open(base_url + "/updateListing/" + str(id))
        self.update_text("input[name='description']",
                         "updated description longer then 20 chars")
        self.click('input[type="submit"]')
        assert self.get_current_url() == base_url + '/listing/' + str(id)
        self.assert_text("updated description longer then 20 chars", "h2")

        # update the listing price
        self.open(base_url + "/updateListing/" + str(id))
        self.update_text("input[name='price']", "200")
        self.click('input[type="submit"]')
        assert self.get_current_url() == base_url + '/listing/' + str(id)
        self.assert_text("200", "h3")

        # update the listing start date
        self.open(base_url + "/updateListing/" + str(id))
        self.update_text("input[name='startDate']", "09/09/2023")
        self.click('input[type="submit"]')
        assert self.get_current_url() == base_url + '/listing/' + str(id)
        self.assert_text("avalible from (2023-09-09)-(2023-10-10)", "h4")

        # update the listing end date
        self.open(base_url + "/updateListing/" + str(id))
        self.update_text("input[name='endDate']", "10/10/2024")
        self.click('input[type="submit"]')
        assert self.get_current_url() == base_url + '/listing/' + str(id)
        self.assert_text("avalible from (2023-09-09)-(2024-10-10)", "h4")

    def test_r5_2_update_listing(self, *_):
        '''
        R5-2: Price can be only increased but cannot be decreased :)

        tested using input partion testing
        '''
        listings = Listing.query.all()
        listing = listings[0]
        id = listing.id

        # raise the listing price
        self.open(base_url + "/updateListing/" + str(id))
        self.update_text("input[name='price']", "300")
        self.click('input[type="submit"]')
        assert self.get_current_url() == base_url + '/listing/' + str(id)
        self.assert_text("300", "h3")

        # lower the listing price
        self.open(base_url + "/updateListing/" + str(id))
        self.update_text("input[name='price']", "100")
        self.click('input[type="submit"]')
        assert self.get_current_url() == ((base_url +
                                           '/updateListing/' + str(id)))
        self.assert_text("price is invalid", "h4")

    def test_r5_3_update_listing(self, *_):
        '''
        R5-3: last_modified_date should be updated 
        when the update operation is successful.

        tested using input partion testing
        '''

        listings = Listing.query.all()
        listing = listings[0]
        id = listing.id

        # set last modified date to a date in the past
        changeLastModifiedDate(listing, date(2021, 2, 2))

        # assert last modfied date is a day in the past
        self.open(base_url + "/listing/" + str(id))
        self.assert_text("listing was last modified on: 2021-02-02", "h5")

        # update the listing
        self.open(base_url + "/updateListing/" + str(id))
        self.update_text("input[name='title']", "updated title2")
        self.click('input[type="submit"]')
        assert self.get_current_url() == base_url + '/listing/' + str(id)
        self.assert_text("updated title2", "h1")

        # assert last modified date is today
        self.assert_text("listing was last modified on: " +
                         str(date.today()), "h5")

    def test_r5_4_update_listing(self, *_):
        '''
        R5-4: When updating an attribute, one has to make sure 
        that it follows the same requirements as create listing.

        tested using a variety of nested functions to test each attribute
        '''

        def test_r4_1(self, *_):
            '''
            R4-1: The title of the product has to be alphanumeric-only,
            and space allowed only if it is not as prefix and suffix.

            tested using input partion testing where the input is title
            '''
            listings = Listing.query.all()
            listing = listings[0]
            id = listing.id

            # p1 = title with a space prefix
            # expected = fail
            self.open(base_url + "/updateListing/" + str(id))
            self.update_text("input[name='title']", " title")
            self.click('input[type="submit"]')
            assert self.get_current_url() == ((base_url +
                                               '/updateListing/' + str(id)))
            self.assert_text("title is invalid", "h4")

            # p2 = title with a space suffix
            # expected = fail
            self.open(base_url + "/updateListing/" + str(id))
            self.update_text("input[name='title']", "title ")
            self.click('input[type="submit"]')
            assert self.get_current_url() == ((base_url +
                                               '/updateListing/' + str(id)))
            self.assert_text("title is invalid", "h4")

            # p3 = title is non-alphanumeric
            # expected = fail
            self.open(base_url + "/updateListing/" + str(id))
            self.update_text("input[name='title']", "title!")
            self.click('input[type="submit"]')
            assert self.get_current_url() == ((base_url +
                                               '/updateListing/' + str(id)))
            self.assert_text("title is invalid", "h4")

            # p4 = title is alphanumeric without space as prefix or suffix
            # expected = pass
            self.open(base_url + "/updateListing/" + str(id))
            self.update_text("input[name='title']", "updatedtitle")
            self.click('input[type="submit"]')
            assert self.get_current_url() == base_url + '/listing/' + str(id)
            self.assert_text("updatedtitle", "h1")

        def test_r4_2(self, *_):
            '''
            R4-2: The title of the product is no longer than 80 characters.

            tested using hybrid testing using input partion testing 
            and boundary value analysis
            '''
            listings = Listing.query.all()
            listing = listings[0]
            id = listing.id

            # set description to be longer than 80 characters
            description = ''.join(random.choice(
                'abcdefghijklmnopqrstuvwxyz') for i in range(161))
            self.open(base_url + "/updateListing/" + str(id))
            self.update_text("input[name='description']", description)
            self.click('input[type="submit"]')

            # p1 = title is 80 characters
            # expected = pass
            self.open(base_url + "/updateListing/" + str(id))
            self.update_text("input[name='title']", "a" * 80)
            self.click('input[type="submit"]')
            assert self.get_current_url() == base_url + '/listing/' + str(id)
            self.assert_text("a" * 80, "h1")

            # p2 = title is 81 characters
            # expected = fail
            self.open(base_url + "/updateListing/" + str(id))
            self.update_text("input[name='title']", "a" * 81)
            self.click('input[type="submit"]')
            assert self.get_current_url() == ((base_url +
                                               '/updateListing/' + str(id)))
            self.assert_text("title is invalid", "h4")

            # p3 = title is 79 characters
            # expected = pass
            self.open(base_url + "/updateListing/" + str(id))
            self.update_text("input[name='title']", "a" * 79)
            self.click('input[type="submit"]')
            assert self.get_current_url() == base_url + '/listing/' + str(id)
            self.assert_text("a" * 79, "h1")

            # p4 = title is 100 characters
            # expected = fail
            self.open(base_url + "/updateListing/" + str(id))
            self.update_text("input[name='title']", "a" * 100)
            self.click('input[type="submit"]')
            assert self.get_current_url() == ((base_url +
                                               '/updateListing/' + str(id)))
            self.assert_text("title is invalid", "h4")

        def test_r4_3(self, *_):
            '''
            R4-3: The description of the product can be arbitrary characters, 
                with a minimum length of 20 characters 
                and a maximum of 2000 characters.
            tested using hybrid testing using input partion testing 
            and boundary value analysis
            '''
            listings = Listing.query.all()
            listing = listings[0]
            id = listing.id

            # set title to be less than 20 characters
            title = ''.join(random.choice(
                'abcdefghijklmnopqrstuvwxyz') for i in range(18))
            self.open(base_url + "/updateListing/" + str(id))
            self.update_text("input[name='title']", title)
            self.click('input[type="submit"]')

            # p1 = description is 20 characters
            # expected = pass
            self.open(base_url + "/updateListing/" + str(id))
            self.update_text("input[name='description']", "a" * 20)
            self.click('input[type="submit"]')
            assert self.get_current_url() == base_url + '/listing/' + str(id)
            self.assert_text("a" * 20, "h2")

            # p2 = description is 21 characters
            # expected = pass
            self.open(base_url + "/updateListing/" + str(id))
            self.update_text("input[name='description']", "a" * 21)
            self.click('input[type="submit"]')
            assert self.get_current_url() == base_url + '/listing/' + str(id)
            self.assert_text("a" * 21, "h2")

            # p3 = description is 19 characters
            # expected = fail
            self.open(base_url + "/updateListing/" + str(id))
            self.update_text("input[name='description']", "a" * 19)
            self.click('input[type="submit"]')
            assert self.get_current_url() == ((base_url +
                                               '/updateListing/' + str(id)))
            self.assert_text("description is invalid", "h4")

            # p4 = description is 2000 characters
            # expected = pass
            self.open(base_url + "/updateListing/" + str(id))
            self.update_text("input[name='description']", "a" * 2000)
            self.click('input[type="submit"]')
            assert self.get_current_url() == base_url + '/listing/' + str(id)
            self.assert_text("a" * 2000, "h2")

            # p5 = description is 2001 characters
            # expected = fail
            self.open(base_url + "/updateListing/" + str(id))
            self.update_text("input[name='description']", "a" * 2001)
            self.click('input[type="submit"]')
            assert self.get_current_url() == ((base_url +
                                               '/updateListing/' + str(id)))
            self.assert_text("description is invalid", "h4")

            # p6 = description is 1999 characters
            # expected = pass
            self.open(base_url + "/updateListing/" + str(id))
            self.update_text("input[name='description']", "a" * 1999)
            self.click('input[type="submit"]')
            assert self.get_current_url() == base_url + '/listing/' + str(id)
            self.assert_text("a" * 1999, "h2")

        def test_r4_4(self, *_):
            '''
            R4-4: Description has to be longer than the product's title.
            tested using hybrid testing with input partioning 
            '''
            listings = Listing.query.all()
            listing = listings[0]
            id = listing.id

            # p1 = description is longer than title
            # expected = pass
            self.open(base_url + "/updateListing/" + str(id))
            self.update_text("input[name='title']", "a" * 20)
            self.update_text("input[name='description']", "a" * 21)
            self.click('input[type="submit"]')
            assert self.get_current_url() == base_url + '/listing/' + str(id)
            self.assert_text("a" * 20, "h1")
            self.assert_text("a" * 21, "h2")

            # p2 = description is shorter than title
            # expected = fail
            self.open(base_url + "/updateListing/" + str(id))
            self.update_text("input[name='title']", "a" * 21)
            self.update_text("input[name='description']", "a" * 20)
            self.click('input[type="submit"]')
            assert self.get_current_url() == ((base_url +
                                               '/updateListing/' + str(id)))
            self.assert_text(
                "description is invalid, title has been changed", "h4")

            # p3 = description is equal to title
            # expected = fail
            self.open(base_url + "/updateListing/" + str(id))
            self.update_text("input[name='title']", "a" * 20)
            self.update_text("input[name='description']", "a" * 20)
            self.click('input[type="submit"]')
            assert self.get_current_url() == ((base_url +
                                               '/updateListing/' + str(id)))
            self.assert_text(
                "description is invalid, title has been changed", "h4")

            # p4 = change title to be longer than description
            # expected = fail
            self.open(base_url + "/updateListing/" + str(id))
            self.update_text("input[name='title']", "a" * 21)
            self.update_text("input[name='description']", "a" * 22)
            self.click('input[type="submit"]')

            self.open(base_url + "/updateListing/" + str(id))
            self.update_text("input[name='title']", "a" * 23)
            self.click('input[type="submit"]')
            assert self.get_current_url() == ((base_url +
                                               '/updateListing/' + str(id)))
            self.assert_text("title is invalid", "h4")

        def test_r4_5(self, *_):
            '''
            R4-5: Price has to be of range [10, 10000].

            tested using boundary anaylsis testing
            do not have to test lower bound
            price can not be reduced (r5_2)
            '''
            listings = Listing.query.all()
            listing = listings[0]
            id = listing.id

            # p1 = price is 9999
            # expected = pass
            self.open(base_url + "/updateListing/" + str(id))
            self.update_text("input[name='price']", "9999")
            self.click('input[type="submit"]')
            assert self.get_current_url() == base_url + '/listing/' + str(id)
            self.assert_text("$9999", "h3")

            # p2 = price is 10000
            # expected = pass
            self.open(base_url + "/updateListing/" + str(id))
            self.update_text("input[name='price']", "10000")
            self.click('input[type="submit"]')
            assert self.get_current_url() == base_url + '/listing/' + str(id)
            self.assert_text("$10000", "h3")

            # p3 = price is 10001
            # expected = fail
            self.open(base_url + "/updateListing/" + str(id))
            self.update_text("input[name='price']", "10001")
            self.click('input[type="submit"]')
            assert self.get_current_url() == ((base_url +
                                               '/updateListing/' + str(id)))
            self.assert_text("price is invalid", "h4")

        def test_r4_8(self, *_):
            '''
            R4-8: A user cannot create products that have the same title.
            tested using input partion testing
            '''
            listings = Listing.query.all()
            listing = listings[0]
            id = listing.id

            otherListing = listings[1]

            # p1 = title is same as other listing
            # expected = fail
            self.open(base_url + "/updateListing/" + str(id))
            self.update_text("input[name='title']", otherListing.title)
            self.click('input[type="submit"]')
            assert self.get_current_url() == ((base_url +
                                               '/updateListing/' + str(id)))
            self.assert_text("title is invalid", "h4")

            # p2 = title is different from other listing
            # expected = pass
            self.open(base_url + "/updateListing/" + str(id))
            self.update_text("input[name='title']", "a" * 20)
            self.click('input[type="submit"]')
            assert self.get_current_url() == base_url + '/listing/' + str(id)
            self.assert_text("a" * 20, "h1")

        test_r4_1(self)
        test_r4_2(self)
        test_r4_3(self)
        test_r4_4(self)
        test_r4_5(self)
        test_r4_8(self)
