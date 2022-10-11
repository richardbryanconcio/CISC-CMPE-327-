from qbay import app
from flask_sqlalchemy import SQLAlchemy
import re
from datetime import date

'''
This file defines data models and related business logics
'''


db = SQLAlchemy(app)


# User defines listings of the time it is available and also the price
# of listings for the day.
class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique = True, nullable = False)
    description = db.Column(db.String(2000))
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

    # create a new user
    user = User(username=name, email=email, password=password, balance=100)
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
def createListing(title, description, price, user, startDate, endDate):
    '''
    Create a new listing
      Parameters:
        title (string): title of the listing, must be no longer then 80 characters 
        description (string): description of the listings, 
        must be longer then title, more then 20 characters and no longer then 20000 characters
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
    # option avalible trim title in the future instead of not creating the listing
    if title[0] == ' ' or title[len(title) - 1] == ' ':
        return None

    # check if title is alphanumeric excluding spaces 
    tempTitle = title.replace(' ', '')
    if  not tempTitle.isalnum():
        return None

    # check if title is proper length
    if len(title) > 80 or title == '':
        return None
    
    # check if description is proper length
    if len(description) > 2000 or len(description) < 20:
        return None

    # check if description is shorter then title
    if len(description) < len(title):
        return None

    # check if price is within proper range
    if price < 10 or price > 10000:
        return None

    # check if end date is after start date 
    if endDate < startDate:
        return None

    # if all checks pass create the listing 
    listing = Listing(title=title, description=description, price=price, lastModifiedDate=date.today(), ownerId=user.id, startDate=startDate, endDate=endDate)  

    db.session.add(listing)

    db.session.commit()

    return listing

def updateListing(field, new, listing, user):
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
    # if listing was not created by the user then don't let them modify the listing
    if listing.ownerId != user.id:
        return False
    # want to put a match-case statement here but ide is flagging me, will try to include later
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
        if  not tempTitle.isalnum():
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
        # new description must be between 20-2000 characters, must contain more characters then the title
        if len(new) < 20 or len(new) > 2000 or len(new) < len(listing.title):
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
        if new < date.today() or new > listing.endDate:
            return False
        
        listing.startDate = new
        return True
    elif field == 'endDate':
        if new < listing.startDate:
            return False
        
        listing.endDate = new
        listing.lastModifiedDate = date.today()
        db.session.commit()
        return True
    else:
        return False

    

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