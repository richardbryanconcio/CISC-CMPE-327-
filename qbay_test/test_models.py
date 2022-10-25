from datetime import date, datetime
from qbay.models import register, login, update, createListing, updateListing


def test_r1_1_user_register():
    '''
    Testing R1-1: Email cannot be empty. password cannot be empty.
    '''

    assert register('u20', '', 'pA$s123') is None
    assert register('u30', 'test2@test.com', '') is None
    assert register('u40', '   ', 'pA$s123') is None
    assert register('u50', 'test3@test.com', 'pA$s123') is not None


def test_r1_4_user_register():
    '''
    Testing R1-4: Password has to meet the required complexity: 
    minimum length 6, 
    at least one upper case, at least one lower case, 
    and at least one special character.
    '''

    assert register('u60', 'test6@test.com', '123456') is None
    assert register('u70', 'test7@test.com', 'Ab!23456') is not None
    assert register('u80', 'test8@test.com', 'A!23456') is None
    assert register('u90', 'test9@test.com', 'a!23456') is None
    assert register('u10', 'test10@test.com', 'Ab123456') is None


def test_r1_5_user_register():
    '''
    Testing R1-5: User name has to be non-empty, alphanumeric-only, 
    and space allowed only if it is not as the prefix or suffix.
    '''

    assert register('', 'test11@test.com', 'pA$s123') is None
    assert register('u12', 'test12@test.com', 'pA$s123') is not None
    assert register(' u13', 'test13@test.com', 'pA$s123') is None
    assert register('u14 ', 'test14@test.com', 'pA$s123') is None
    assert register('u 15', 'test15@test.com', 'pA$s123') is not None


def test_r1_6_user_register():
    '''
    Testing R1-6: User name has to be longer than 2 characters 
    and less than 20 characters.
    '''

    assert register('x', 'test16@test.com', 'pA$s123') is None
    assert register('u17', 'test17@test.com', 'pA$s123') is not None
    assert register('twentycharacters0018',
                    'test18@test.com', 'pA$s123') is None
    assert register('twentycharacters019',
                    'test19@test.com', 'pA$s123') is not None


def test_r1_7_user_register():
    '''
    Testing R1-7: If the email has been used, the operation failed.
    '''

    assert register('u100', 'test0@test.com', 'pA$s123') is not None
    assert register('u00', 'test1@test.com', 'pA$s123') is not None
    assert register('u100', 'test0@test.com', 'pA$s123') is None


def test_r1_8_9_10_user_register():
    '''
    R1-8: Shipping address is empty at the time of registration.
    R1-9: Postal code is empty at the time of registration.
    R1-10: Balance should be initialized as 100 at the time of registration. 
    (free $100 dollar signup bonus).
    '''

    user = login('test0@test.com', 'pA$s123')
    assert user.postalCode is None
    assert user.billingAddress is None
    assert user.balance == 100


def test_r2_1_login():
    '''
    Testing R2-1: A user can log in using her/his email address 
      and the password.
    (will be tested after the previous test, so we already have u0, 
      u1 in database)
    '''

    user = login('test0@test.com', 'pA$s123')
    assert user is not None
    assert user.username == 'u100'

    # Case when email and password is empty
    user = login('', '')
    assert user is None

    # Case when email is empty
    user = login('', 'pA$s123')
    assert user is None

    # Case when password is empty
    user = login('test0@test.com', '')
    assert user is None

    # Case when password is less than minimum length
    user = login('test0@test.com', 'pA$s1')
    assert user is None

    # Case when password exceed length of original password
    user = login('test0@test.com', 'pA$s1234')
    assert user is None

    # Case when space as prefix
    user = login('test0@test.com', ' pA$s123')
    assert user is None

    # Case when space as suffix
    user = login('test0@test.com', 'pA$s123 ')

    assert user is None

    # Case when space not as prefix or suffix, but space inbetween
    user = login('test0@test.com', 'pA$s 123')
    assert user is None


def test_r3_1_update():
    '''
    R3-1: A user is only able to update his/her user name,
    user email, billing address, and postal code.
    '''

    user = login('test0@test.com', 'pA$s123')
    assert update('postalCode', user, 'A1K 2P0') is True
    assert update('username', user, 'test') is True
    assert update('billingAddress', user, '360 dinner rd') is True
    assert update('email', user, 'test20@test.com') is True
    assert update('password', user, 'pA$s123newpass') is False
    assert update('balance', user, 1000) is False
    assert update('id', user, 1) is False


def test_r3_2_3_update():
    '''
    R3-2: postal code should be non-empty, 
    alphanumeric-only, and no special characters such as !.
    R3-3: Postal code has to be a valid Canadian postal code.
    '''

    user = login('test20@test.com', 'pA$s123')
    assert update('postalCode', user, '') is False
    assert update('postalCode', user, 'L!L R8R') is False
    assert update('postalCode', user, 'V3Y 0A8') is True
    assert update('postalCode', user, 'D0D I2U') is False


def test_r3_4_update():
    '''
    R3-4: User name follows the requirements above. 
    (non-empty, alphanumeric-only, no special characters such as !)
    '''
    user = login('test20@test.com', 'pA$s123')
    assert update('username', user, '') is False
    assert update('username', user, ' ') is False
    assert update('username', user, 'ab99cde!') is False
    assert update('username', user, 'yourmom42') is True
    assert update('username', user, '360RushBnoStop') is True


'''
    Create a new listing
      Parameters:
        title (db collumn): title of the listing, must be no 
        longer then 80 characters 
        description (string): description of the listings, 
        must be longer then title, more then 20 characters 
        and no longer then 20000 characters
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
    # creating user to be used by all create listing test cases
    register('create listing test', 'create@listing.com', 'Ab!23456')

    user = login('create@listing.com', 'Ab!23456')
    startDate = date(2022, 10, 10)
    endDate = date(2023, 10, 10)
    assert createListing("test1", "this is a description",
                         60, user, startDate, endDate) is not None
    assert createListing("  test2", "this is a description",
                         60, user, startDate, endDate) is None
    assert createListing("test3   ", "this is a description",
                         60, user, startDate, endDate) is None
    assert createListing("te$t4", "this is a description",
                         60, user, startDate, endDate) is None


def test_r4_2_create_listing():
    '''
    R4-2: The title of the product is no longer than 80 characters.
    '''
    user = login('create@listing.com', 'Ab!23456')
    startDate = date(2022, 10, 10)
    endDate = date(2023, 10, 10)
    newTitle = ""
    while len(newTitle) <= 81:
        newTitle += "a"
    assert createListing("test5", "this is a description",
                         60, user, startDate, endDate) is not None
    assert createListing(newTitle, "this is a description",
                         60, user, startDate, endDate) is None


def test_r4_3_create_listing():
    '''
    R4-3: The description of the product can be arbitrary characters, 
    with a minimum length of 20 characters and a maximum of 2000 characters.
    '''
    user = login('create@listing.com', 'Ab!23456')
    startDate = date(2022, 10, 10)
    endDate = date(2023, 10, 10)
    assert createListing("test7", "this is a description",
                         60, user, startDate, endDate) is not None
    assert createListing("test8", "description", 60,
                         user, startDate, endDate) is None
    veryLongDescription = ""
    while len(veryLongDescription) <= 2000:
        veryLongDescription += "a"
    assert createListing("test9", veryLongDescription, 60,
                         user, startDate, endDate) is None


def test_r4_4_create_listing():
    '''
    R4-4: Description has to be longer than the product's title.
    '''
    user = login('create@listing.com', 'Ab!23456')
    startDate = date(2022, 10, 10)
    endDate = date(2023, 10, 10)
    assert createListing("test10", "this is a description",
                         60, user, startDate, endDate) is not None
    assert createListing("test 11 that is longer than 20 characters",
                         "this is a description", 60, user, startDate,
                         endDate) is None


def test_r4_5_create_listing():
    '''
    R4-5: Price has to be of range [10, 10000].
    '''
    user = login('create@listing.com', 'Ab!23456')
    startDate = date(2022, 10, 10)
    endDate = date(2023, 10, 10)
    assert createListing("test12", "this is a description",
                         60, user, startDate, endDate) is not None
    assert createListing("test13", "this is a description",
                         1, user, startDate, endDate) is None
    assert createListing("test14", "this is a description",
                         20000, user, startDate, endDate) is None


def test_r4_8_create_listing():
    '''
    R4-8: A user cannot create products that have the same title.
    '''
    user = login('create@listing.com', 'Ab!23456')
    startDate = date(2022, 10, 10)
    endDate = date(2023, 10, 10)
    assert createListing("test15", "this is a description",
                         60, user, startDate, endDate) is not None
    assert createListing("test15", "this is a description",
                         60, user, startDate, endDate) is None


def test_r5_1_update_listing():
    '''
    R5-1: One can update all attributes of the listing, 
    except owner_id and last_modified_date.
    additionall test to confirm when updateListing 
    returns true the relevant field is changed
    '''

    user = login('create@listing.com', 'Ab!23456')
    startDate = date(2022, 10, 10)
    endDate = date(2023, 10, 10)
    # updating dates is a string in the format of '%Y-%m-%d'
    newStartDate = datetime(2022, 11, 11)
    newEndDate = datetime(2023, 11, 11)
    listing = createListing(
        "test16", "this is a description", 60, user, startDate, endDate)

    assert updateListing('title', 'new title', listing) is True
    assert listing.title == 'new title'
    confirm_change = listing.query.filter_by(title='new title').all()
    assert confirm_change[0].title == 'new title'
    assert updateListing(
        'description', 'a fancy new description', listing) is True
    assert listing.description == 'a fancy new description'
    assert updateListing('price', 400, listing) is True
    assert listing.price == 400
    assert updateListing('startDate', newStartDate, listing) is True
    assert listing.startDate == date(2022, 11, 11)
    assert updateListing('endDate', newEndDate, listing) is True
    assert listing.endDate == date(2023, 11, 11)
    assert updateListing('ownerId', 1, listing) is False
    assert updateListing('id', '1', listing) is False
    assert updateListing('lastModifiedDate', date(
        2021, 10, 10), listing) is False


def test_r5_2_update_listing():
    '''
    R5-2: Price can be only increased but cannot be decreased :)
    '''
    user = login('create@listing.com', 'Ab!23456')
    startDate = date(2022, 10, 10)
    endDate = date(2023, 10, 10)
    listing = createListing(
        "test17", "this is a description", 60, user, startDate, endDate)
    assert updateListing('price', 100, listing) is True
    assert updateListing('price', 60, listing) is False


def test_r5_3_update_listing():
    '''
    R5-3: last_modified_date should be updated 
    when the update operation is successful.
    '''
    user = login('create@listing.com', 'Ab!23456')
    startDate = date(2022, 10, 10)
    endDate = date(2023, 10, 10)
    listing = createListing(
        "test18", "this is a description", 60, user, startDate, endDate)

    listing.lastModifiedDate = date(2020, 1, 1)
    assert listing.lastModifiedDate == date(2020, 1, 1)
    updateListing('price', 100, listing)
    assert listing.lastModifiedDate == date.today()


def test_r5_4_update_listing():
    '''
    R5-4: When updating an attribute, 
    one has to make sure that it follows the same requirements as above.
    '''
    user = login('create@listing.com', 'Ab!23456')
    startDate = date(2022, 10, 10)
    endDate = date(2023, 10, 10)
    listing = createListing(
        "test19", "this is a description", 60, user, startDate, endDate)

    # title is alphanumeric only, no leading or trailing spaces
    assert updateListing('title', '  invalid', listing) is False
    assert updateListing('title', 'invalid   ', listing) is False
    assert updateListing('title', '$inval*id', listing) is False
    # title is no longer then 80 characters
    newTitle = ''
    while len(newTitle) <= 90:
        newTitle += 'a'
    assert updateListing('title', newTitle, listing) is False
    # descrioption is min 20 characters and no longer then 2000
    newDescription = ''
    while len(newDescription) <= 2100:
        newDescription += 'a'
    assert updateListing('description', 'small', listing) is False
    assert updateListing('description', newDescription, listing) is False
    # description has to be longer then title
    # current description is "this is a description"
    assert updateListing(
        'title', 'title longer than 20 different characters',
        listing) is False
    # price has to be in range [10, 10000]
    # (do not have to test less than 10
    # can not be less than 10 when created and can not be reduced via updating)
    assert updateListing('price', 20000, listing) is False
    # no 2 listings can have the same title
    assert updateListing('title', 'test18', listing) is False
