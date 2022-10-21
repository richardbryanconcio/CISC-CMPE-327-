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

    if title:
        updateListing('title', title, listing, user)
    if description:
        updateListing('description', description, listing, user)
    if price:
        price = int(price)
        updateListing('price', price, listing, user)
    if startDate:
        startDate = datetime.strptime(startDate, '%Y-%m-%d')
        updateListing('startDate', startDate, listing, user)
    if endDate:
        endDate = datetime.strptime(endDate, '%Y-%m-%d')
        updateListing('endDate', endDate, listing, user)

    return redirect('/listing/' + str(listing.id))


@app.route('/updateListing/<listingId>', methods=['GET'])
def updateListing_get(listingId):

    # temporary user placeholder while waiting for login/autheticator function
    # once implemented user will be passed through wrapper function
    users = User.query.all()
    user = users[0]

    products = Listing.query.filter_by(ownerId=user.id).all()

    return render_template('updateListing.html',
                           message="please input which fields to change")

@app.route('/updateUserProfile/<userId>')
def updateUserProfile_get(userId):
    user = User.query.filter_by(id=userId).first()
    return render_template('updateUserProfile.html', username=user.username)

@app.route('/updateUsername', methods=['GET'])
def updateUsername_get():

    return render_template('updateUsername.html')


@app.route('/updateUsername/<userId>', methods=['POST'])
def updateUsername_post(userId):
    #Need to get current user
    newUsername = request.form.get('username')
    
    if username:
        update('username',user,newusername)

    return redirect('/updateUserProfile/' + str(user.id))

@app.route('/updateEmail', methods=['GET'])
def updateEmail_get():

    return render_template('updateUsername.html')


@app.route('/updateEmail/<userId>', methods=['POST'])
def updateEmail_post(userId):
    #Need to get current user
    newEmail = request.form.get('email')
    
    if email:
        update('email',user,newEmail)

    return redirect('/updateUserProfile/' + str(user.id))

@app.route('/updatePassword', methods=['GET'])
def updatePassword_get():

    return render_template('updatePassword.html')


@app.route('/updatePassword/<userId>', methods=['POST'])
def updatePassword_post(userId):
    #Need to get current user
    newPass = request.form.get('password')
    
    if password:
        update('password',user,newPass)

    return redirect('/updateUserProfile/' + str(user.id))

@app.route('/updateBillingPostal', methods=['GET'])
def updateBillingPostal_get():

    return render_template('updateBillingPostal.html')


@app.route('/updateBillingPostal/<userId>', methods=['POST'])
def updateEmail_post(userId):
    #Need to get current user
    newPostal = request.form.get('postalCode')
    newAddress = request.form.get('address')
    
    if postalCode:
        update('postalCode',user,newPostal)
    if address:
        update('billingAddress',user,newAddress)

    return redirect('/updateUserProfile/' + str(user.id))