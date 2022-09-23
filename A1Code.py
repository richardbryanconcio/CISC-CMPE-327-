from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# setting up SQLAlchemy and data models so we can map data models into database tables
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app) 

class Review(db.model):
  id = db.Column(db.Integer, primary_key=True)
  """ setting up Review data model to allow verified
  guest to the listing to leave a review of their stay at the property."""
  rating = db.Column(db.Integer, primary_key=True, nullable=False)
  # Leaving an integer rating, ie 5/5.
  commentTitle = db.Column(db.string(120), nullable=False) 	
  """Short title regarding the review saved as string, ie Glass sauna was perfect for
  warming up after swim """
  comment = db.Column(db.string(2000)) 
  """Detailed review of the stay that a customer expereinced saved as string"""
  dateReviewed = db.Column(db.string(30), nullable=False)
  # Date the review was left, saved as string
  usernameReviewer = db.Column(db.String(80), nullable=False)
  # Username of the person that is leaving the review

# camel case only , no snake case
  def __repr__(self):
      return '<review id%r>' % self.id
      #Who, date of the review posted, what the actual revies
    