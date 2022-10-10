from qbay import app
from flask_sqlalchemy import SQLAlchemy


'''
This file defines data models and related business logics
'''


db = SQLAlchemy(app)


# User defines listings of the time it is available and also the price
# of listings for the day.
class Listing(db.Model):
    # ID of the user.
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(120), unique=True, nullable=False)
    # ID of the user who created the listing.
    createdById = db.Column(db.Integer, unique=False, nullable=False)
    pricePerDay = db.Column(db.Float, unique=False, nullable=False)
    # First available day of the listing.
    startDate = db.Column(db.Date, nullable=False)
    # Last available day of the listing.
    endDate = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<Listing %r>' % self.address


# Allows users to book existing listings.
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # ID of the available listings being booked.
    listingId = db.Column(db.Integer, nullable=False)
    # ID of the user who is booking the listing.
    bookedById = db.Column(db.Integer, nullable=False)
    listingConfirmed = db.Column(db.Boolean, nullable=False)
    # First day that the booking starts.
    startDate = db.Column(db.Date, nullable=False)
    # Last day that the booking starts.
    endDate = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<Booking ID %r>' % self.id


# Within the database model - it contains an id, username, and email column
# Therefore, the model has access to id, username, and email databases
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    # email address of the user.
    email = db.Column(db.String(120), unique=True, nullable=False)
    # Money currently available on the user's account
    money = db.Column(db.Float, unique=False, nullable=False)
    # Currently no constraints for password generation other than uniqueness.
    password = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


# Setting up a Review data model to allow verified
# guest to the listing to leave a review of their stay at the property.
class Review(db.model):
    # Unique id of the user is saved as an integer.
    id = db.Column(db.Integer, primary_key=True)
    # Leaving an integer rating, i.e. 5/5.
    rating = db.Column(db.Integer, primary_key=True, nullable=False)
    # Short title regarding the review saved as string, ie Glass sauna was
    # perfect for warming up after swim
    commentTitle = db.Column(db.string(120), nullable=False)
    # Detailed review of the stay that a customer experienced saved as a string
    comment = db.Column(db.string(2000))
    # Date the review was left, saved as a string.
    dateReviewed = db.Column(db.string(30), nullable=False)
    # Username of the person that is leaving the review
    usernameReviewer = db.Column(db.String(80), nullable=False)

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
    '''
    Update login information
      Parameters:
        field (db collumn): pointer to field to be changed 
        new (string): value to replace field
      Returns:
        True if the change went through false if operation failed
    '''
