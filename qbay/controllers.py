from flask import render_template, request, session, redirect
from qbay.models import (login, register, update, User,
                         createListing, updateListing, Listing)

from datetime import date, datetime
from qbay import app


@app.route('/updateUserProfile/<userId>')
@authenticate
def updateUserProfile_get(userId):
    user = User.query.filter_by(id=userId).first()
    return render_template('updateUserProfile.html', username=user.username)


@app.route('/updateUsername', methods=['GET'])
def updateUsername_get():
    return render_template('updateUsername.html')


@app.route('/updateUsername/<userId>', methods=['POST'])
@authenticate
def updateUsername_post(userId):
    user = User.query.filter_by(id=userId).first()
    newUsername = request.form.get('username')
    msg = []

    success = update('username', user, newUsername)
    if not success:
        msg.append("username is invalid")
    else:
        msg.append("username has been changed")

    if msg:
        return render_template("updateUserProfile.html", message=msg)


@app.route('/updateEmail', methods=['GET'])
def updateEmail_get():

    return render_template('updateEmail.html')


@app.route('/updateEmail/<userId>', methods=['POST'])
@authenticate
def updateEmail_post(userId):
    user = User.query.filter_by(id=userId).first()
    newEmail = request.form.get('email')
    
    msg = []

    success = update('email', user, newEmail)
    if not success:
        msg.append("email is invalid")
    else:
        msg.append("email has been changed")

    if msg:
        return render_template("updateUserProfile.html", message=msg)


@app.route('/updatePassword', methods=['GET'])
def updatePassword_get():

    return render_template('updatePassword.html')


@app.route('/updatePassword/<userId>', methods=['POST'])
@authenticate
def updatePassword_post(userId):
    user = User.query.filter_by(id=userId).first()
    newPass = request.form.get('password')
    confNewPass = request.form.get('confPassword')
    
    msg = []
    
    success = update('password', user, newPass)
    if not success:
        msg.append("password is invalid")
    else:
        msg.append("password has been changed")

    if msg:
        return render_template("updateUserProfile.html", message=msg)


@app.route('/updateBillingAddress', methods=['GET'])
def updateBillingPostal_get():

    return render_template('updateBillingPostal.html')


@app.route('/updateBillingAddress/<userId>', methods=['POST'])
@authenticate
def updateBillingAddress(userId):
    user = User.query.filter_by(id=userId).first()
    newPostal = request.form.get('postalCode')
    newAddress = request.form.get('address')
    
    msg = []
    if newPostal:
        success = update('postalCode', user, newPostal)
        if not success:
            msg.append("postal code is invalid")
        else:
            msg.append("postal code has been changed")

        if msg:
            return render_template("updateUserProfile.html", message=msg)
    if newAddress:
        success = update('billingAddress', user, newPostal)
        if not success:
            msg.append("billing address is invalid")
        else:
            msg.append("billing address has been changed")

        if msg:
            return render_template("updateUserProfile.html", message=msg)