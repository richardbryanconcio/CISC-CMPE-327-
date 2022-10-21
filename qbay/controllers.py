from flask import render_template, request, session, redirect
from qbay.models import (login, register, update, User,
                         createListing, updateListing, Listing)

from datetime import date, datetime

from qbay import app


@app.route('/')
def home_get():
    # templates are stored in the templates folder
    products = Listing.query.all()

    return render_template('home.html', products=products)


@app.route('/listing/<listingId>')
def listing_get(listingId):

    listing = Listing.query.filter_by(id=listingId).first()

    return render_template('listing.html', listing=listing)


@app.route('/createListing', methods=['GET'])
def createListing_get():

    return render_template('createListing.html')


@app.route('/createListing', methods=['POST'])
def createListing_post():
    title = request.form.get('title')
    description = request.form.get('description')
    price = int(request.form.get('price'))
    startDate = datetime.strptime(request.form.get('startDate'), '%Y-%m-%d')
    endDate = datetime.strptime(request.form.get('endDate'), '%Y-%m-%d')

    # temporary user placeholder while waiting for login/autheticator function
    # once implemented user will be passed through wrapper function
    users = User.query.all()
    user = users[0]

    success = createListing(title, description, price,
                            user, startDate, endDate)

    if not success:
        errorMessage = "creating listing failed, please try again"
        return render_template('createListing.html', message=errorMessage)
    else:
        return redirect('/')


@app.route('/chooseListingUpdate', methods=['GET'])
def chooseListingUpdate_get():

    # temporary user placeholder while waiting for login/autheticator function
    # once implemented user will be passed through wrapper function
    users = User.query.all()
    user = users[0]

    products = Listing.query.filter_by(ownerId=user.id).all()

    return render_template('chooseListingUpdate.html', products=products)


@app.route('/updateListing/<listingId>', methods=['POST'])
def updateListing_post(listingId):
    listing = Listing.query.filter_by(id=listingId).first()
    # temporary user placeholder while waiting for login/autheticator function
    # once implemented user will be passed through wrapper function
    users = User.query.all()
    user = users[0]

    title = request.form.get('title')
    description = request.form.get('description')
    price = request.form.get('price')
    startDate = request.form.get('startDate')
    endDate = request.form.get('endDate')

    errorMessage = []
    successMessage = []

    if title:
        success = updateListing('title', title, listing, user)
        if not success:
            errorMessage.append("title is invalid")
        else:
            successMessage.append("title has been changed")
    if description:
        success = updateListing('description', description, listing, user)
        if not success:
            errorMessage.append("description is invalid")
        else:
            successMessage.append("description has been changed")
    if price:
        price = int(price)
        success = updateListing('price', price, listing, user)
        if not success:
            errorMessage.append("price is invalid")
        else:
            successMessage.append("price has been changed")
    if startDate:
        startDate = datetime.strptime(startDate, '%Y-%m-%d')
        success = updateListing('startDate', startDate, listing, user)
        if not success:
            errorMessage.append("startDate is invalid")
        else:
            successMessage.append("startDate has been changed")
    if endDate:
        endDate = datetime.strptime(endDate, '%Y-%m-%d')
        success = updateListing('endDate', endDate, listing, user)
        if not success:
            errorMessage.append("endDate is invalid")
        else:
            successMessage.append("endDate has been changed")

    if errorMessage:
        msg = ', '.join(x for x in errorMessage if x)
        if successMessage:
            msg = msg + ", " + ', '.join(x for x in successMessage if x)
        return render_template('updateListing.html',
                               message=msg)
    else:
        return redirect('/listing/' + str(listing.id))


@app.route('/updateListing/<listingId>', methods=['GET'])
def updateListing_get(listingId):

    # temporary user placeholder while waiting for login/autheticator function
    # once implemented user will be passed through wrapper function

    return render_template('updateListing.html',
                           message="please input which fields to change")
