# Here i will be storing the routes(location) of my website visible to the user

from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route("/")
def home():
    return render_template("home.html")