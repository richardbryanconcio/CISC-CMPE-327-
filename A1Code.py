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

