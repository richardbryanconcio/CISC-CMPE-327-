from flask import render_template, request, session, redirect
from qbay.models import login, register, update, User, createListing, updateListing, Listing

from datetime import date, datetime

from qbay import app 

@app.route('/')
def home_get():
    # templates are stored in the templates folder
    products = Listing.query.all()
    
    return render_template('home.html', products=products)


@app.route('/listing/<listingId>')
def listing_get(listingId):
    
    listing = Listing.query.filter_by(id=listingId)

    return render_template('listing.html', listing=listing[0])

@app.route('/createListing', methods=['GET'])
def createListing_get():

    return render_template('createListing.html')

@app.route('/createListing', methods=['POST'])
def register_post():
    title = request.form.get('title')
    description = request.form.get('description')
    price = int(request.form.get('price'))
    startDate = datetime.strptime(request.form.get('startDate'), '%Y-%m-%d')
    endDate = datetime.strptime(request.form.get('endDate'), '%Y-%m-%d')

    # temporary user placeholder while waiting for login/autheticator function
    # once implemented user will be passed through wrapper function
    users = User.query.all()
    user = users[0]

    success = createListing(title, description, price, user, startDate, endDate)


    return redirect('/')
