from flask import Blueprint

auth=Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return "Login"

@auth.route("/signup")
def login():
    return "Signup"

@auth.route("/logout")
def login():
    return "Logout"