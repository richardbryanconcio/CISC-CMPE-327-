from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# setting up SQLAlchemy and data models so we can map data models into database tables
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app) 

class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(120), unique=True, nullable=False)
    createdById = db.Column(db.Integer, unique=False, nullable=False)
    pricePerDay = db.Column(db.Float, unique=False, nullable=False)
    startDate = db.Column(db.Date, nullable=False)
    endDate = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<Listing %r>' % self.address

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    listingId = db.Column(db.Integer, nullable=False)
    bookedById = db.Column(db.Integer, nullable=False)
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

    # added columns for user data model
    money = db.Column(db.Float, unique=False, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
        
class Review(db.model):
    # Setting up Review data model to allow verified
    # guest to the listing to leave a review of their stay at the property.
    id = db.Column(db.Integer, primary_key=True)
    # Leaving an integer rating, i.e. 5/5.
    rating = db.Column(db.Integer, primary_key=True, nullable=False)
    # Short title regarding the review saved as string, ie Glass sauna was 
    # perfect for warming up after swim
    commentTitle = db.Column(db.string(120), nullable=False) 	 
    # Detailed review of the stay that a customer expereinced saved as string
    comment = db.Column(db.string(2000)) 
    # Date the review was left, saved as string
    dateReviewed = db.Column(db.string(30), nullable=False)
    # Username of the person that is leaving the review
    usernameReviewer = db.Column(db.String(80), nullable=False)
  
    def __repr__(self):
        return '<Review ID %r>' % self.id
