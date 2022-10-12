from qbay import app
from flask_sqlalchemy import SQLAlchemy
import re
from email_validator import validate_email, EmailNotValidError

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
    #username, email, password, billingAddress, postalCode
    '''
    Update login information
      Parameters:
        field (db collumn): pointer to field to be changed 
        new (string): value to replace field
      Returns:
        True if the change went through false if operation failed
    '''
    if field == 'username':
        if new[0] == ' ' or new[len(new) - 1] == ' ':
            return False
        if len(new) <= 0 or len(new) > 80:
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
        if new[0] == ' ' or new[len(new) - 1] == ' ':
            return False
        if len(new) <= 0 or len(new) > 120:
            return False

        existed = User.query.filter_by(email=new).all()
        if len(existed) > 0:
            return False
        
        if not checkemail(new):
            return False

        user.email = new
        db.session.commit()
        return True
        
    elif field == 'password':
        if not checkpass(new):
            return False
        
        if len(new) > 120:
            return False
        
        user.password = new
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
    
    elif field = "postalCode":
        if new[0] == ' ' or new[len(new) - 1] == ' ':
            return False
        if len(new) <= 0 or len(new) > 6:
            return False
        
        if not checkpostal(new):
            return False

        existed = User.query.filter_by(postalCode=new).all()
        if len(existed) > 0:
            return False
        
        user.postalCode = new
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

def checkemail(email):
    regexemail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regexemail, email)):
        return True
    else:
        return False