from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# setting up SQLAlchemy and data models so we can map data models
# into database tables
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


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
