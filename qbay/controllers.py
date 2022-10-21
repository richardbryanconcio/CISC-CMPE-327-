from flask import render_template, request, session, redirect
from qbay.models import login, register, update, User, createListing, updateListing, Listing

from qbay import app 

@app.route('/', methods=['GET'])
def home_get():
    # templates are stored in the templates folder
    return render_template('home.html', message='')

