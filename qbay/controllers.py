from flask import render_template, request, session, redirect, Flask, flash, url_for
from flask_login import login_required, login_user
from qbay.models import (login, register, update, User,
                         createListing, updateListing, Listing, checkpass, LoginForm)

from qbay import app 

@app.route('/login', methods=['GET', 'POST'])
def login_get(email, password):
    form = LoginForm()
    if form.validate_on_submit():
        # Parce through the data and see if there is a
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            # Check the hash - should work with register where it takes data from saved info
            if checkpass(user.password, form.password.data):
                login_user(user)
                flash("Successfully logged in!")
                return redirect(url_for('/'))
            else:
                flash("Wrong Email or Password. Please try again.")
        else:
            flash("Email or Account does not exist. Please try again.")
    return render_template('login.html', form=form, message='Please enter your email and password')
