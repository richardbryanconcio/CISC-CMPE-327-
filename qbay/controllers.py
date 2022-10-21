from flask import render_template, request, session, redirect
from qbay.models import login, register, update, User, createListing, updateListing, Listing

from datetime import date

from qbay import app 

@app.route('/')
def home_get():
    # templates are stored in the templates folder
    products = Listing.query.all()
    
    return render_template('home.html', products=products)


@app.route('/listing<listingId>')
def listing_get(listingId):
    
    products = Listing.query.filter_by(id=listingId)

    return render_template('home.html', products=products)

