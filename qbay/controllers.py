from flask import render_template, request, session, redirect
from qbay.models import login, User, register


from qbay import app


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


@app.route('/')
@authenticate
def home(user):
    # authentication is done in the wrapper function
    # see above.
    # by using @authenticate, we don't need to re-write
    # the login checking code all the time for other
    # front-end portals

    # some fake product data
    products = [
        {'name': 'prodcut 1', 'price': 10},
        {'name': 'prodcut 2', 'price': 20}
    ]
    return render_template('index.html', user=user, products=products)


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


@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in', None)
    return redirect('/')