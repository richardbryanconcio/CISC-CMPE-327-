from flask import render_template, request, session, redirect, Flask, flash, url_for
from flask_login import login_required, login_user, LoginManager, logout_user
from qbay.models import (login, register, update, User,
                         createListing, updateListing, Listing, checkpass, LoginForm)

from qbay import app 

# Create Logout Page
@app.route('/logout', methods=['GET', 'POST'])
# Requires the user to be logged in
@login_required


def logout():
    logout_user()
    flash("You have been logged out of the account.")
    return redirect(url_for('login'))


# Creating Login/Logout Dashboard Page
@app.route('/dashboard', methods=['GET', 'POST'])
# Requires the user to be logged in
@login_required


def dashboard():
    return render_template('dashboard.html')


# Create Login Page
@app.route('/login', methods=['GET', 'POST'])
def login_get(email, password):
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Parce through the data and see if there is a username
        user = User.query.filter_by(username = form.username.data).first()
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
    return render_template('login.html', form = form,
        message = 'Please enter your email and password')


# Flask_Login Codes
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader


def load_user(user_id):
    return User.query.get(int(user_id))


# Create Login Form
class LoginForm(FlaskForm):
    email = StringField("Email", validators = [DataRequired()])
    password = PasswordField("Password", validators = [DataRequired()])
    submit = SubmitField("Submit")