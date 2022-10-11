from qbay import app
from flask_sqlalchemy import SQLAlchemy
import re

'''
This file defines data models and related business logics
'''


db = SQLAlchemy(app)


# User defines listings of the time it is available and also the price
# of listings for the day.
class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique = True, nullable = False)
    description = db.Column(db.String)
    price = db.Column(db.Float, nullable = False)
    lastModifiedDate = db.Column(db.Date, nullable = False)
    ownerId = db.Column(db.Integer, nullable = False)
    # describes from which dates the property is avalible 
    startDate = db.Column(db.Date, nullable=False)
    endDate = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<Listing Title %r>' % self.title


# Allows users to book existing listings.
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    listingId = db.Column(db.Integer, nullable=False)
    userId = db.Column(db.Integer, nullable=False)
    listingConfirmed = db.Column(db.Boolean, nullable=False)
    startDate = db.Column(db.Date, nullable=False)
    endDate = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<Booking ID %r>' % self.id


# Within the database model - it contains an id, username, and email column
# Therefore, the model has access to id, username, and email databases
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    billingAddress = db.Column(db.String)
    postalCode = db.Column(db.String)
    balance = db.Column(db.Float, nullable = False)


    def __repr__(self):
        return '<User %r>' % self.username


# Setting up a Review data model to allow verified
# guest to the listing to leave a review of their stay at the property.
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reviewTitle = db.Column(db.String(120), nullable=False)
    reviewText = db.Column(db.String)
    dateReviewed = db.Column(db.String(30), nullable=False)
    userId = db.Column(db.Integer, nullable = False)
    listingId = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return '<Review ID %r>' % self.id

# create all tables
db.create_all()


def register(name, email, password):
    '''
    Register a new user
    Parameters:
        name (string):     user name
        email (string):    user email
        password (string): user password
    Returns:
        True if registration succeeded otherwise False
    '''
    # check if the email has been used:
    existed = User.query.filter_by(email=email).all()
    if len(existed) > 0:
        return False

    if (emailEmptyTest(email) is True) and (emailValidation(email) is True):
        name.email = email

    if (passwordEmptyTest(password)
            is True) and (passwordValidation(password) is True):
        name.password = password

    if usernameValidation(name) is True:
        name.username = name

    # R1-8: Shipping address is empty at the time of registration.
    name.billingAddress = None
    # R1-9: Postal code is empty at the time of registration.
    name.postalCode = None
    # R1-10: Balance should be initialized as 100 at the time
    # of registration. (free $100 dollar signup bonus).
    name.balance = 100

    # R1-1: Email cannot be empty. password cannot be empty.
    # Check if input email is empty given that input is the string.
    def emailEmptyTest(email: str):
        if len(email) == 0:
            print("Email cannot be empty")
            return False
        else:
            return True

    # R1-1: Email cannot be empty. password cannot be empty.
    # Check if input password is empty given that input is the string.
    def passwordEmptyTest(password: str):
        if len(password) == 0:
            print("Password cannot be empty")
            return False
        else:
            return True

    # R1-3: The email has to follow addr-spec defined in RFC 5322
    # (see https://en.wikipedia.org/wiki/Email_address for a human-friendly
    # explanation). You can use external libraries/imports.
    # Check if input email is valid based on the given regular expression.
    def emailValidation(email):
        regex = re.compile(r'([A-Za-z0-9]+[.-_+])*[A-Za-z0-9]+@'
                           r'[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, email):
            print("This is a valid email")
            return True
        else:
            print("This is an invalid email")
            return False

    # R1-4: Password has to meet the required complexity: minimum length 6,
    # at least one upper case, at least one lower case,
    # and at least one special character.
    def passwordValidation(password):
        upper, lower, special = 0, 0, 0
        specialChar = ".!@#$%&*"
        if (len(password) < 6):
            print("Password is too short")
            return False
        if (len(password) >= 6):
            for i in password:
                # Counting uppercase letter
                if (i.isupper()):
                    upper += 1
                if (i.islower()):
                    lower += 1
                if (i in specialChar):
                    special += 1
            if (upper >= 1 and lower >= 1 and special >= 1):
                print("Valid Password")
                return True
            else:
                print("password does not meet the required complexity")
                return False

    # R1-5: User name has to be non-empty, alphanumeric-only, and space
    # allowed only if it is not as the prefix or suffix.
    # R1-6: User name has to be longer than 2 characters and
    # less than 20 characters.
    def usernameValidation(username: str):
        if len(username) <= 2:
            print("username is too short. \
            It cannot be empty and has to be longer than 2 character")
            return False
        if len(username) >= 20:
            print("username cannot be longer than 20 characters")
            return False
        if username[0] == " " or username[-1] == " ":
            print("username prefeix or suffix cannot be space")
            return False
        if not all(i.isalnum() or i.isspace() for i in username):
            print("User name can only be alphanumeric with space \
                allowed(but not at the start or end of a username)")
            return False
        else:
            return True

    # create a new user
    user = User(username=name, email=email, password=password)
    # add it to the current database session
    db.session.add(user)
    # actually save the user object
    db.session.commit()
    return True


def login(email, password):
    '''
    Check login information
      Parameters:
        email (string):    user email
        password (string): user password
      Returns:
        The user object if login succeeded otherwise None
    '''
    valids = User.query.filter_by(email=email, password=password).all()
    if len(valids) != 1:
        return None
    return valids[0]

def update(field, new):
    '''
    Update login information
      Parameters:
        field (db collumn): pointer to field to be changed 
        new (string): value to replace field
      Returns:
        True if the change went through false if operation failed
    '''

def checkpass(password):
    regexpass = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{6,}$"
    if re.fullmatch(regexpass, password):
        return True
    else:
        return False


def checkpostal(postal):
    regexpostal = "^[a-zA-Z][0-9][a-zA-Z] ?[0-9][a-zA-Z][0-9]"
    if re.fullmatch(regexpostal, postal):
        return True
    else:
        return False