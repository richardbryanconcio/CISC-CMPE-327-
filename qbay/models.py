from qbay import app
from flask_sqlalchemy import SQLAlchemy
import re
from email_validator import validate_email, EmailNotValidError
from datetime import date, datetime
 
from flask_login import UserMixin
 
'''
This file defines data models and related business logics
'''
 
 
db = SQLAlchemy(app)
 
 
# User defines listings of the time it is available and also the price
# of listings for the day.
class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(2000))
    price = db.Column(db.Float, nullable=False)
    lastModifiedDate = db.Column(db.Date, nullable=False)
    ownerId = db.Column(db.Integer, nullable=False)
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
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    billingAddress = db.Column(db.String)
    postalCode = db.Column(db.String)
    balance = db.Column(db.Float, nullable=False)
 
    def __repr__(self):
        return '<User %r>' % self.username
 
 
# Setting up a Review data model to allow verified
# guest to the listing to leave a review of their stay at the property.
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reviewTitle = db.Column(db.String(120), nullable=False)
    reviewText = db.Column(db.String)
    dateReviewed = db.Column(db.String(30), nullable=False)
    userId = db.Column(db.Integer, nullable=False)
    listingId = db.Column(db.Integer, nullable=False)
 
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
        return None
 
    if len(email) == 0 or (checkemail(email) is False):
        return None
 
    if len(password) == 0 or (passwordValidation(password) is False):
        return None
 
    if usernameValidation(name) is False:
        return None
 
    # R1-8: Shipping address is empty at the time of registration.
    # name.billingAddress = None
    # R1-9: Postal code is empty at the time of registration.
    # name.postalCode = None
    # R1-10: Balance should be initialized as 100 at the time
    # of registration. (free $100 dollar signup bonus).
    # name.balance = 100
 
    # create a new user
    user = User(email=email, password=password, username=name,
                billingAddress=None, postalCode=None, balance=100)
 
    # add it to the current database session
    db.session.add(user)
    # actually save the user object
    db.session.commit()
    return user
 
 
def login(email, password):
    '''
    Check login information
      Parameters:dsd
        email (string):    user email
        password (string): user password
      Returns:
        The user object if login succeeded otherwise None
    '''
    # Case for when length of email is false
    if len(email) == 0:
        return None
        print("Email is empty")
 
    if len(password) == 0:
        return None
        print("Password is empty")
 
    # Tests if it has an uppercase, lowercase, contains a digit,
    # or if string length is above 6
    if (any(x.isupper() for x in password) and
        any(x.islower() for x in password) and
        any(x.isdigit() for x in password) and
            len(password) >= 6) is False:
        return None
 
    # Validating the data of emails and passwords from the database
    validatedAccounts = User.query.filter_by(
        email=email, password=password).all()
    if len(validatedAccounts) != 1:
        return None
    return validatedAccounts[0]
 
 
def update(field, user, new):
    '''
    Update login information
      Parameters:
        field (db collumn): pointer to field to be changed
        new (string): value to replace field
      Returns:
        True if the change went through false if operation failed
    '''
 
    if field == 'username':
        if len(new) <= 0 or len(new) > 80:
            return False
        if new[0] == ' ' or new[len(new) - 1] == ' ':
            return False
 
        temp = new.replace(' ', '')
        if not temp.isalnum():
            return False
 
        existed = User.query.filter_by(username=new).all()
        if len(existed) > 0:
            return False
 
        user.username = new
        db.session.commit()
        return True
 
    elif field == 'email':
        if len(new) <= 0 or len(new) > 120:
            return False
        if new[0] == ' ' or new[len(new) - 1] == ' ':
            return False
 
        existed = User.query.filter_by(email=new).all()
        if len(existed) > 0:
            return False
 
        if not checkemail(new):
            return False
 
        user.email = new
        db.session.commit()
        return True
 
    elif field == "billingAddress":
        if new[0] == ' ' or new[len(new) - 1] == ' ':
            return False
        if len(new) <= 0:
            return False
 
        user.billingAddress = new
        db.session.commit()
        return True
 
    elif field == "postalCode":
        if len(new) <= 0 or len(new) > 7:
            return False
        if new[0] == ' ' or new[len(new) - 1] == ' ':
            return False
 
        if not checkpostal(new):
            return False
 
        existed = User.query.filter_by(postalCode=new).all()
        if len(existed) > 0:
            return False
 
        user.postalCode = new
        db.session.commit()
        return True
 
    return False


def createListing(title, description, price, userId, startDate, endDate):
    '''
    Create a new listing
      Parameters:
        title (string): (title of the listing, must
        be no longer then 80 characters)
        description (string): (description of the listings,
        must be longer then title, more then 20 characters
        and no longer then 20000 characters)
        price (float): price of the listing bounded to [10, 10000]
        user (int): userId of the user who created the listing
        startDate (date): starting date of avalibilty for the listing
        endDate (date): last day of avalibility for the listing
      Returns:
        Returns the listing if succussful, None otherwise
    '''
    # check if title has been used
    existed = Listing.query.filter_by(title=title).all()
    if len(existed) > 0:
        return None
 
    # check if title has leading or trailing white space
    # option avalible trim title in the future
    # instead of not creating the listing
    if title[0] == ' ' or title[len(title) - 1] == ' ':
        return None
 
    # check if title is alphanumeric excluding spaces
    tempTitle = title.replace(' ', '')
    if not tempTitle.isalnum():
        return None
 
    # check if title is proper length
    if len(title) > 80 or title == '':
        return None
 
    # check if description is proper length
    if len(description) > 2000 or len(description) < 20:
        return None
 
    # check if description is shorter then title
    if len(description) <= len(title):
        return None
 
    # check if price is within proper range
    if price < 10 or price > 10000:
        return None
 
    # check if end date is after start date
    if endDate < startDate:
        return None
 
    # if all checks pass create the listing
    listing = Listing(title=title, description=description, price=price,
                      lastModifiedDate=date.today(),
                      ownerId=userId, startDate=startDate, endDate=endDate)

    db.session.add(listing)
 
    db.session.commit()
 
    return listing
 
 
def updateListing(field, new, listing):
    '''
    Update an existing listing
      Parameters:
        field (String): field to be changed
        new (any): value to replace field
        listing (db.model): the listing object to be changed
        user (db.model): user to confirm user is the owner of the listing
      Returns:
        True if the change went through false if operation failed
    '''
    # want to put a match-case statement here but ide is flagging me,
    # will try to include later
    if field == 'title':
        # new title can not have leading or trailing white spaces
        if new[0] == ' ' or new[len(new) - 1] == ' ':
            return False
        # new title can not be the same as any other titles
        existed = Listing.query.filter_by(title=new).all()
        if len(existed) > 0:
            return False
        # new title must be alphanumeric (excluding spaces)
        tempTitle = new.replace(' ', '')
        if not tempTitle.isalnum():
            return False
        # new title must be less then 80 characters and not empty
        if len(new) > 80 or new == '':
            return False
        # length of title can not be longer then description
        if len(new) > len(listing.description):
            return False
 
        listing.title = new
        listing.lastModifiedDate = date.today()
        db.session.commit()
        return True
    elif field == 'description':
        # new description must be between 20-2000 characters,
        # must contain more characters then the title
        if len(new) < 20 or len(new) > 2000 or len(new) <= len(listing.title):
            return False
 
        listing.description = new
        listing.lastModifiedDate = date.today()
        db.session.commit()
        return True
    elif field == 'price':
        # price can not be reduced, price can not be above 10000
        if new > 10000 or new < listing.price:
            return False
 
        listing.price = new
        listing.lastModifiedDate = date.today()
        db.session.commit()
        return True
    elif field == 'startDate':
        # convert datetime to date
        new = datetime.date(new)
        if new < date.today() or new > listing.endDate:
            return False
 
        listing.startDate = new
        listing.lastModifiedDate = date.today()
        db.session.commit()
        return True
    elif field == 'endDate':
        # convert datetime to date
        new = datetime.date(new)
        if new < listing.startDate:
            return False
 
        listing.endDate = new
        listing.lastModifiedDate = date.today()
        db.session.commit()
        return True
    else:
        return False
 
 
def checkpass(password):
    regexpass = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{6,}$"
    if re.fullmatch(regexpass, password):
        return True
    else:
        return False
 
 
def checkpostal(postal):
    regexpostal = r"^[a-zA-Z][0-9][a-zA-Z] ?[0-9][a-zA-Z][0-9]"
    if re.fullmatch(regexpostal, postal):
        return True
    else:
        return False
 
 
def checkemail(email):
    try:
        v = validate_email(email)
        email = v["email"]
        return True
    except EmailNotValidError as e:
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


def changeLastModifiedDate(listing, d):
    listing.lastModifiedDate = d
    db.session.commit()