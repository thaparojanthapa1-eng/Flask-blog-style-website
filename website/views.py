from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Post
from . import Db

views=Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
@login_required
def home():
    posts=Post.query.all()
    return render_template("home.html", user=current_user, posts=posts)

@views.route("/create_post", methods=["GET", "POST"])
def create_post():
    if request.method=="POST":
        text=request.form.get("text")

        if not text:
            flash("Post can't be empty", category="error")
        else:
            post=Post(text=text,  author_id=current_user.id)
            Db.session.add(post)
            Db.session.commit()
            flash("Post created", category="success")
            return(redirect(url_for("views.home")))

    return render_template("createpost.html")

@views.route("/delete-post/<id>")
@login_required
def delete_post(id):
    post=Post.query.filter_by(id=id).first()

    if not post:
        flash("Post doesn't exist.", category="error")
    elif current_user.id!=post.id:
        flash("You don't have permission to delete the post.")
    else:
        Db.session.delete(post)
        Db.session.commit()
        flash("Post deleted", category="success")

    return redirect(url_for("views.home"))