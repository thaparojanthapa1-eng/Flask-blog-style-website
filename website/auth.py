from flask import Blueprint, render_template, redirect, url_for, request

auth=Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    email=request.form("email")
    password=request.form("password")
    return render_template("login.html")

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    username=request.form("username")
    email=request.form("email")
    password1=request.form("password1")
    password2=request.form("password2")
    return render_template("signup.html")

@auth.route("/logout")
def logout():
    return redirect(url_for("views.home"))