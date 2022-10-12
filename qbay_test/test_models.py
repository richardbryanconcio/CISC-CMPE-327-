from qbay.models import register, login, update



def test_r1_1_user_register():
    '''
    Testing R1-1: Email cannot be empty. password cannot be empty.
    '''

    assert register('u2', '', 'pA$s123') is False
    assert register('u3', 'test2@test.com', '') is False
    assert register('u4', '   ', 'pA$s123') is False
    assert register('u5', 'test3@test.com', 'pA$s123') is True 

def test_r1_4_user_register():
    '''
    Testing R1-4: Password has to meet the required complexity: minimum length 6, 
    at least one upper case, at least one lower case, and at least one special character.
    '''

    assert register('u6', 'test6@test.com', 'pA$s123') is False
    assert register('u7', 'test7@test.com', 'Ab!23456') is True
    assert register('u8', 'test8@test.com', 'A!23456') is False
    assert register('u9', 'test9@test.com', 'a!23456') is False
    assert register('u10', 'test10@test.com', 'Ab123456') is False

def test_r1_5_user_register():
    '''
    Testing R1-5: User name has to be non-empty, alphanumeric-only, 
    and space allowed only if it is not as the prefix or suffix.
    '''

    assert register('', 'test11@test.com', 'pA$s123') is False
    assert register('u12', 'test12@test.com', 'pA$s123') is True
    assert register(' u13', 'test13@test.com', 'pA$s123') is False
    assert register('u14 ', 'test14@test.com', 'pA$s123') is False
    assert register('u 15', 'test15@test.com', 'pA$s123') is True

def test_r1_6_user_register():
    '''
    Testing R1-6: User name has to be longer than 2 characters and less than 20 characters.
    '''

    assert register('x', 'test16@test.com', 'pA$s123') is False
    assert register('u17', 'test17@test.com', 'pA$s123') is True
    assert register('twentycharacters0018', 'test18@test.com', 'pA$s123') is False
    assert register('twentycharacters019', 'test19@test.com', 'pA$s123') is True

def test_r1_7_user_register():
    '''
    Testing R1-7: If the email has been used, the operation failed.
    '''

    assert register('u0', 'test0@test.com', 'pA$s123') is True
    assert register('u0', 'test1@test.com', 'pA$s123') is True
    assert register('u1', 'test0@test.com', 'pA$s123') is False

def test_r1_8_9_10_user_register():
    '''
    R1-8: Shipping address is empty at the time of registration.
    R1-9: Postal code is empty at the time of registration.
    R1-10: Balance should be initialized as 100 at the time of registration. (free $100 dollar signup bonus).
    '''

    user = login('test0@test.com', 'pA$s123')
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

    user = login('test0@test.com', 'pA$s123')
    assert user is not None
    assert user.username == 'u0'

    user = login('test0@test.com', 'pA$s12345')
    assert user is None

def test_r3_1_update():
    '''
    R3-1: A user is only able to update his/her user name, user email, billing address, and postal code.
    '''
    user = login('test0@test.com', 'pA$s123')
    assert update(user.postalCode, 'A1K 2P0') is True
    assert update(user.username, 'test') is True
    assert update(user.billingAddress, '360 dinner rd') is True
    assert update(user.email, 'test20@test.com') is True
    assert update(user.billingAddress, '360 dinner rd') is False
    assert update(user.password, '1234567') is False

def test_r3_2_3_update():
    '''
    R3-2: postal code should be non-empty, alphanumeric-only, and no special characters such as !.
    R3-3: Postal code has to be a valid Canadian postal code.
    '''
    user = login('test0@test.com', 'pA$s123')
    assert update(user.postalCode, '') is False
    assert update(user.postalCode, 'L!L R8R') is False
    assert update(user.postalCode, 'V3Y 0A8') is True
    assert update(user.postalCode, 'D0D I2U') is False

def test_r3_4_update():
    '''
    R3-4: User name follows the requirements above. (non-empty, alphanumeric-only, no special characters such as !)
    '''
    user = login('test0@test.com', 'pA$s123')
    assert update(user.username, '') is False
    assert update(user.username, ' ') is False
    assert update(user.username, 'ab99cde!') is False
    assert update(user.username, 'yourmom42') is True
    assert update(user.username, '360RushBnoStop') is True



