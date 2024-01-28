from flask import Blueprint, render_template, request, flash, redirect, url_for
from . models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.index"))
            else:
                flash("Incorect password", category="error")
            
        else:
            flash("Incorect email", category="error")
    return render_template("login.html", user = current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists", category="error")
        elif len(email) < 4 and "@" not in email:
            flash("You must enter a valid email!", category="error")
        elif len(first_name) < 2:
            flash("Your name must be more than 2 letters", category="error")
        elif len(password1) < 5:
            flash("Please choose a strong password", category="error")
        elif password1 != password2:
            flash("Password did not match", category="error")
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user, remember=True)
            flash("Account created successfully", category="success")
            return redirect(url_for("views.index"))
    return render_template("signup.html", user=current_user)
