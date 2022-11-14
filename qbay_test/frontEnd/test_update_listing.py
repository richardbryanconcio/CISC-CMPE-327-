from seleniumbase import BaseCase

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import User, register

from datetime import date, datetime
import random

"""
This file defines all integration tests for the frontend update listing page.
"""


class FrontEndCreateListingTest(BaseCase):
    # create a user for testing, if it already exists in the db then pass
    # should be replaced with a login once authentication is up and running
    pass