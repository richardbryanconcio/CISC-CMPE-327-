# Updated User Data Model
# CISC/CMPE 327
# Richard Bryan Concio
# 20184738
# Group 55

# importing flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# setting up SQLAlchemy and data models so we can map data models into database tables
# creating an instance of flask 
app = Flask(__name__)

# creating a configuration object
# SQLALCHEMY_TRACK_MODIFICATIONS tracks modifications of objects and emit signals
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# SQLALCHEMY_DATABASE_URI is a database URI used for the connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

# creating a database object; "SQLAlchemy"
db = SQLAlchemy(app)

# within the database model - it contains an id, username, and email column
# therefore the model has access to id, username, and email databases
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # added columns for user data model
    money = db.Column(db.float, primary_key=True)
    password = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
