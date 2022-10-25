from flask import render_template, request, session, redirect
from qbay.models import login, register, update, User, createListing, updateListing, Listing

from qbay import app 

@app.route('/updateUserProfile/<userId>')
def updateUserProfile_get(userId):
    user = authenticate(User.query.filter_by(id=userId).first())
    return render_template('updateUserProfile.html', username=user.username)

@app.route('/updateUsername', methods=['GET'])
def updateUsername_get():
    return render_template('updateUsername.html')


@app.route('/updateUsername/<userId>', methods=['POST'])
def updateUsername_post(userId):
    user = authenticate(User.query.filter_by(id=userId).first())
    newUsername = request.form.get('username')
    
    if newUsername and usernameValidation(newUsername):
        success = update('username',user,newUsername)
        if not success:
            errorMessage.append("username is invalid")
        else:
            successMessage.append("username has been changed")

    if errorMessage:
        msg = ', '.join(x for x in errorMessage if x)
        if successMessage:
            msg = msg + ", " + ', '.join(x for x in successMessage if x)
        return render_template('updateUsername.html',
                               message=msg)
    else:
        return redirect('/updateUserProfile/' + str(user.id))

@app.route('/updateEmail', methods=['GET'])
def updateEmail_get():

    return render_template('updateUsername.html')


@app.route('/updateEmail/<userId>', methods=['POST'])
def updateEmail_post(userId):
    user = authenticate(User.query.filter_by(id=userId).first())
    newEmail = request.form.get('email')
    
    if newEmail and emailValidation(newEmail):
        success = update('email',user,newEmail)
        if not success:
            errorMessage.append("email is invalid")
        else:
            successMessage.append("email has been changed")
    
    if errorMessage:
        msg = ', '.join(x for x in errorMessage if x)
        if successMessage:
            msg = msg + ", " + ', '.join(x for x in successMessage if x)
        return render_template('updateBillingPostal.html',
                               message=msg)
    else:
        return redirect('/updateUserProfile/' + str(user.id))

@app.route('/updatePassword', methods=['GET'])
def updatePassword_get():

    return render_template('updatePassword.html')


@app.route('/updatePassword/<userId>', methods=['POST'])
def updatePassword_post(userId):
    user = authenticate(User.query.filter_by(id=userId).first())
    newPass = request.form.get('password')
    confNewPass = request.form.get('confPassword')
    
    if password and confPassword:
        if passwordValidation(newPass) and newPass == confNewPass
            success = update('password',user,newPass)
            if not success:
                errorMessage.append("password is invalid")
            else:
                successMessage.append("password has been changed")
    else:
        errorMessage.append("both fields required")
    if errorMessage:
        msg = ', '.join(x for x in errorMessage if x)
        if successMessage:
            msg = msg + ", " + ', '.join(x for x in successMessage if x)
        return render_template('updatePassword.html',
                               message=msg)
    else:
        return redirect('/updateUserProfile/' + str(user.id))

@app.route('/updateBillingPostal', methods=['GET'])
def updateBillingPostal_get():

    return render_template('updateBillingPostal.html')


@app.route('/updateBillingPostal/<userId>', methods=['POST'])
def updatePostBilling_post(userId):
    user = authenticate(User.query.filter_by(id=userId).first())
    newPostal = request.form.get('postalCode')
    newAddress = request.form.get('address')
    
    errorMessage = []
    successMessage = []

    if newPostal and checkpostal(newPostal):
        success = update('postalCode',user,newPostal)
        if not success:
            errorMessage.append("postalCode is invalid")
        else:
            successMessage.append("postalCode has been changed")
    if newAddress:
        success = update('billingAddress',user,newAddress)
        if not success:
            errorMessage.append("billingAddress is invalid")
        else:
            successMessage.append("billingAddress has been changed")

    if errorMessage:
        msg = ', '.join(x for x in errorMessage if x)
        if successMessage:
            msg = msg + ", " + ', '.join(x for x in successMessage if x)
        return render_template('updateBillingPostal.html',
                               message=msg)
    else:
        return redirect('/updateUserProfile/' + str(user.id))