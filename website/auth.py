from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import Db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth=Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="POST":
        email=request.form("email")
        password=request.form("password")
        return render_template("login.html")
    
        user=User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in!")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Password is incorrect.", category=error)
        else:
            flash("User doesn't exist.", category=error)

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method=="POST":
        username=request.form("username")
        email=request.form("email")
        password1=request.form("password1")
        password2=request.form("password2")

        email_exist=User.query.filter_by(email=email).first
        username_exist=User.query.filter_by(username=username).first
        if email_exist:
            flash("Email is already in use.", category="error")
        elif username_exist:
            flash("Username already in use.", category="error")
        elif password1!=password2:
            flash("Password doesn't match", category="error")
        elif len(username)<2:
            flash("Username too short", category="error")
        elif len(password1)<2:
            flash("Password too short", category="error")
        elif len(email)<10:
            flash("Email too short", category="error")
        else:
            new_user=User(email=email, username=username, 
                          password=generate_password_hash(password1, method="sha256"))
            Db.session.add(new_user)
            Db.session.commit()
            login_user(new_user, remember=True)
            flash("User created")
            return (redirect(url_for("views.home")))

    return render_template("signup.html")

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))