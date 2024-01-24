from flask import Blueprint

auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return "login page"


@auth.route("/logout")
def logout():
    return "logout page"


@auth.route("/sign-up")
def sign_up():
    return "sign up"