from flask import (render_template, request, session,
                   redirect, Flask, flash)
from flask_login import LoginManager
from qbay.models import (login, register, update, User,
                         createListing, updateListing, Listing)

from datetime import date, datetime

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Length

from qbay import app


# Create Authentication
def authenticate(inner_function):
    """
    :param inner_function: any python function that accepts a user object
    Wrap any python function and check the current session to see if 
    the user has logged in. If login, it will call the inner_function
    with the logged in user object.
    To wrap a function, we can put a decoration on that function.
    Example:
    @authenticate
    def home_page(user):
        pass
    """
    
    def wrapped_inner():
        # check did we store the key in the session
        if 'logged_in' in session:
            id = session['logged_in']
            try:
                user = User.query.filter_by(id=id).first()
                if user:
                    # if the user exists, call the inner_function
                    # with user as parameter
                    return inner_function(user)
            except Exception:
                pass
        else:
            # else, redirect to the login page
            return render_template('login.html', message="Please login to continue.")

    # return the wrapped version of the inner_function:
    wrapped_inner.__name__ = inner_function.__name__
    return wrapped_inner

@app.route('/register', methods=['GET'])
def register_get():
    # templates are stored in the templates folder
    return render_template('register.html', message='')


@app.route('/register', methods=['POST'])
def register_post():
    # get user's email address to register/sign up
    email = request.form.get('email')
    # get user's username to register
    name = request.form.get('name')
    # get user's password twice to register
    password = request.form.get('password')
    password2 = request.form.get('password2')
    error_message = None

    if password != password2:
        error_message = "The passwords do not match"
    else:
        # use backend api to register the user
        success = register(name, email, password)
        if not success:
            error_message = "Registration failed."
    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template('register.html', message=error_message)
    else:
        return redirect('/login')


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
@authenticate
def createListing_get(user):
    return render_template('createListing.html')


@app.route('/createListing', methods=['POST'])
def createListing_post():
    id = session['logged_in']
    user = User.query.filter_by(id=id).first()

    title = request.form.get('title')
    description = request.form.get('description')
    price = int(request.form.get('price'))
    startDate = datetime.strptime(request.form.get('startDate'), '%Y-%m-%d')
    endDate = datetime.strptime(request.form.get('endDate'), '%Y-%m-%d')

    success = createListing(title, description, price,
                            user, startDate, endDate)

    if not success:
        errorMessage = "creating listing failed, please try again"
        return render_template('createListing.html', message=errorMessage)
    else:
        return redirect('/')


@app.route('/chooseListingUpdate', methods=['GET'])
@authenticate
def chooseListingUpdate_get(user):

    products = Listing.query.filter_by(ownerId=user.id).all()

    return render_template('chooseListingUpdate.html', products=products)


@app.route('/updateListing/<listingId>', methods=['POST'])
def updateListing_post(listingId):
    listing = Listing.query.filter_by(id=listingId).first()
    # temporary user placeholder while waiting for login/autheticator function
    # once implemented user will be passed through wrapper function

    title = request.form.get('title')
    description = request.form.get('description')
    price = request.form.get('price')
    startDate = request.form.get('startDate')
    endDate = request.form.get('endDate')

    errorMessage = []
    successMessage = []

    if title:
        success = updateListing('title', title, listing)
        if not success:
            errorMessage.append("title is invalid")
        else:
            successMessage.append("title has been changed")
    if description:
        success = updateListing('description', description, listing)
        if not success:
            errorMessage.append("description is invalid")
        else:
            successMessage.append("description has been changed")
    if price:
        price = int(price)
        success = updateListing('price', price, listing)
        if not success:
            errorMessage.append("price is invalid")
        else:
            successMessage.append("price has been changed")
    if startDate:
        startDate = datetime.strptime(startDate, '%Y-%m-%d')
        success = updateListing('startDate', startDate, listing)
        if not success:
            errorMessage.append("startDate is invalid")
        else:
            successMessage.append("startDate has been changed")
    if endDate:
        endDate = datetime.strptime(endDate, '%Y-%m-%d')
        success = updateListing('endDate', endDate, listing)
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


# Create Login Form
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")


# Create Login Page
# GET - requesting data from a specific source
@app.route('/login', methods=['GET'])
def login_get():
    # return back to the login template
    return render_template('login.html', 
                           message='Enter your email and password')


# POST - sending data to a server to create/update a resource
@app.route('/login', methods=['POST'])
def login_post():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        error_message = None
        success_message = None

        success = login(email, password)
        if success:
            session['logged_in'] = success.id
            success_message = "Login successful!"
            return render_template('home.html', message=success_message)
        
        if not success:
            error_message = "Login failed. Please try again."
            return render_template('login.html', message=error_message)

    return redirect('/')


def logout():
    logoutMsg = None
    if 'logged_in' not in session:
        logoutMsg = "You are not currently logged in."
        return redirect('/login', message=logoutMsg)
    else:
        session.pop('logged_in', None)
        logoutMsg = "Successfully logged out!"
        return redirect('/', message=logoutMsg)


# Flask_Login Codes
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/updateUser', methods=['GET'])
@authenticate
def updateUserProfile_get(user):
    return render_template('updateUser.html', message="please input which fields to change")


@app.route('/updateUser', methods=['POST'])
def updateUserProfile_post():
    id = session['logged_in']
    user = User.query.filter_by(id=id).first()

    username = request.form.get('username')
    email = request.form.get('email')
    billingAddress = request.form.get('billingAddress')
    postalCode = request.form.get('postalCode')

    errorMessage = []
    successMessage = []

    if username:
        success = update('username', user, username)
        if not success:
            errorMessage.append("username is invalid")
        else:
            successMessage.append("username has been changed to " + username)
    if email:
        success = update('email', user, email)
        if not success:
            errorMessage.append("email is invalid")
        else:
            successMessage.append("email has been changed to " + email)
    if billingAddress:
        success = update('billingAddress', user, billingAddress)
        if not success:
            errorMessage.append("billingAddress is invalid")
        else:
            successMessage.append("billingAddress has been changed to " + billingAddress)
    if postalCode:
        success = update('postalCode', user, postalCode)
        if not success:
            errorMessage.append("postalCode is invalid")
        else:
            successMessage.append("postalCode has been changed to " + postalCode)

    if errorMessage:
        msg = ', '.join(x for x in errorMessage if x)
        if successMessage:
            msg = msg + ", " + ', '.join(x for x in successMessage if x)
        return render_template('updateUser.html',
                               message=msg)
    else:
        msg = ', '.join(x for x in successMessage if x)
        return render_template('home.html', message="Profile has been updated, " + msg)

@app.route('/logout')
def logout():
    logoutMsg = None
    if 'logged_in' not in session:
        logoutMsg = "You are not currently logged in."
        return render_template('home.html', message=logoutMsg)
    else:
        session.pop('logged_in', None)
        logoutMsg = "Successfully logged out!"
        return render_template('home.html', message=logoutMsg)

