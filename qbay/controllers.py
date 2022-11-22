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
            email = session['logged_in']
            try:
                user = User.query.filter_by(email=email).one_or_none()
                if user:
                    # if the user exists, call the inner_function
                    # with user as parameter
                    return inner_function(user)
            except Exception:
                pass
        else:
            # else, redirect to the login page
            return redirect('/login')

    # return the wrapped version of the inner_function:
    return wrapped_inner


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
<<<<<<< HEAD
            
=======

>>>>>>> 36f569d54b441594a5c50709de95df17e8bdc3a4
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


@app.route('/updateUserProfile/<userId>')
def updateUserProfile_get(userId):
    user = User.query.filter_by(id=userId).first()
    return render_template('updateUserProfile.html', username=user.username)


@app.route('/updateUsername', methods=['GET'])
def updateUsername_get():
    return render_template('updateUsername.html')


@app.route('/updateUsername/<userId>', methods=['POST'])
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