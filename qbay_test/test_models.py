from datetime import date, datetime
from qbay.models import register, login, update, createListing




def test_r1_1_user_register():
    '''
    Testing R1-1: Email cannot be empty. password cannot be empty.
    '''

    assert register('u2', '', '123456') is False
    assert register('u3', 'test2@test.com', '') is False
    assert register('u4', '   ', '123456') is False
    assert register('u5', 'test3@test.com', '123456') is True 

def test_r1_4_user_register():
    '''
    Testing R1-4: Password has to meet the required complexity: minimum length 6, 
    at least one upper case, at least one lower case, and at least one special character.
    '''

    assert register('u6', 'test6@test.com', '123456') is False
    assert register('u7', 'test7@test.com', 'Ab!23456') is True
    assert register('u8', 'test8@test.com', 'A!23456') is False
    assert register('u9', 'test9@test.com', 'a!23456') is False
    assert register('u10', 'test10@test.com', 'Ab123456') is False

def test_r1_5_user_register():
    '''
    Testing R1-5: User name has to be non-empty, alphanumeric-only, 
    and space allowed only if it is not as the prefix or suffix.
    '''

    assert register('', 'test11@test.com', '123456') is False
    assert register('u12', 'test12@test.com', '123456') is True
    assert register(' u13', 'test13@test.com', '123456') is False
    assert register('u14 ', 'test14@test.com', '123456') is False
    assert register('u 15', 'test15@test.com', '123456') is True

def test_r1_6_user_register():
    '''
    Testing R1-6: User name has to be longer than 2 characters and less than 20 characters.
    '''

    assert register('x', 'test16@test.com', '123456') is False
    assert register('u17', 'test17@test.com', '123456') is True
    assert register('twentycharacters0018', 'test18@test.com', '123456') is False
    assert register('twentycharacters019', 'test19@test.com', '123456') is True

def test_r1_7_user_register():
    '''
    Testing R1-7: If the email has been used, the operation failed.
    '''

    assert register('u0', 'test0@test.com', '123456') is True
    assert register('u0', 'test1@test.com', '123456') is True
    assert register('u1', 'test0@test.com', '123456') is False

def test_r1_8_9_10_user_register():
    '''
    R1-8: Shipping address is empty at the time of registration.
    R1-9: Postal code is empty at the time of registration.
    R1-10: Balance should be initialized as 100 at the time of registration. (free $100 dollar signup bonus).
    '''

    user = login('test0@test.com', 123456)
    assert user.postalCode == None 
    assert user.billingAddress == None
    assert user.balance == 100


def test_r2_1_login():
    '''
    Testing R2-1: A user can log in using her/his email address 
      and the password.
    (will be tested after the previous test, so we already have u0, 
      u1 in database)
    '''

    user = login('test0@test.com', 123456)
    assert user is not None
    assert user.username == 'u0'

    user = login('test0@test.com', 1234567)
    assert user is None

def test_r3_1_update():
    '''
    R3-1: A user is only able to update his/her user name, user email, billing address, and postal code.
    '''
    user = login('test0@test.com', 123456)
    assert update(user.postalCode, 'A1K 2P0') is True
    assert update(user.username, 'test') is True
    assert update(user.billingAddress, '360 dinner rd') is True
    assert update(user.email, "test20@test.com") is True
    assert update(user.address, "360 dinner rd") is False
    assert update(user.password, '1234567') is False

def test_r3_2_3_update():
    '''
    R3-2: postal code should be non-empty, alphanumeric-only, and no special characters such as !.
    R3-3: Postal code has to be a valid Canadian postal code.
    '''
    user = login('test0@test.com', 123456)
    assert update(user.postalCode, '') is False
    assert update(user.postalCode, 'L!L R8R') is False
    assert update(user.postalCode, 'V3Y 0A8') is True
    assert update(user.postalCode, 'D0D I2U') is False

'''
    Create a new listing
      Parameters:
        title (db collumn): title of the listing, must be no longer then 80 characters 
        description (string): description of the listings, 
        must be longer then title, more then 20 characters and no longer then 20000 characters
        price (float): price of the listing bounded to [10, 10000]
        user (int): userId of the user who created the listing
        startDate (date): starting date of avalibilty for the listing
        endDate (date): last day of avalibility for the listing
      Returns:
        Returns the listingId if succussful, None otherwise
    '''

def test_r4_1_create_listing():
    '''
    R4-1: The title of the product has to be alphanumeric-only, 
    and space allowed only if it is not as prefix and suffix.
    '''
    user = login('test3@test.com', '123456')
    startDate = date(2022, 10, 10)
    endDate = date(2023, 10, 10)
    assert createListing("test1", "this is a description", 60, user, startDate, endDate) is not None
    assert createListing("  test2", "this is a description", 60, user, startDate, endDate) is None
    assert createListing("test3   ", "this is a description", 60, user, startDate, endDate) is None
    assert createListing("te$t4", "this is a description", 60, user, startDate, endDate) is None

def test_r4_2_create_listing():
    '''
    R4-2: The title of the product is no longer than 80 characters.
    '''
    user = login('test3@test.com', '123456')
    startDate = date(2022, 10, 10)
    endDate = date(2023, 10, 10)
    assert createListing("test5", "this is a description", 60, user, startDate, endDate) is not None
    assert createListing("1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"
    , "this is a description", 60, user, startDate, endDate) is None
    

def test_r4_3_create_listing():
    '''
    R4-3: The description of the product can be arbitrary characters, 
    with a minimum length of 20 characters and a maximum of 2000 characters.
    '''
    user = login('test3@test.com', '123456')
    startDate = date(2022, 10, 10)
    endDate = date(2023, 10, 10)
    assert createListing("test7", "this is a description", 60, user, startDate, endDate) is not None
    assert createListing("test8", "description", 60, user, startDate, endDate) is None
    veryLongDescription = ""
    while len(veryLongDescription) < 2000:
        veryLongDescription += "a"
    assert createListing("test9", veryLongDescription, 60, user, startDate, endDate) is None

def test_r4_4_create_listing():
    '''
    R4-4: Description has to be longer than the product's title.
    '''
    user = login('test3@test.com', '123456')
    startDate = date(2022, 10, 10)
    endDate = date(2023, 10, 10)
    assert createListing("test10", "this is a description", 60, user, startDate, endDate) is not None
    assert createListing("test 11 that is longer than 20 characters", "this is a description", 60, user, startDate, endDate) is None

def test_r4_5_create_listing():
    '''
    R4-5: Price has to be of range [10, 10000].
    '''
    user = login('test3@test.com', '123456')
    startDate = date(2022, 10, 10)
    endDate = date(2023, 10, 10)
    assert createListing("test12", "this is a description", 60, user, startDate, endDate) is not None
    assert createListing("test13", "this is a description", 1, user, startDate, endDate) is None
    assert createListing("test14", "this is a description", 20000, user, startDate, endDate) is None


def test_r4_8_create_listing():
    '''
    R4-8: A user cannot create products that have the same title.
    '''
    user = login('test3@test.com', '123456')
    startDate = date(2022, 10, 10)
    endDate = date(2023, 10, 10)
    assert createListing("test15", "this is a description", 60, user, startDate, endDate) is not None
    assert createListing("test15", "this is a description", 60, user, startDate, endDate) is None


