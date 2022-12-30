# Here will be all the routes for the authentication

from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html', text="testing")

@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"

@auth.route('/sign-up')
def lsign_up():
    return render_template("sign_up.html")

