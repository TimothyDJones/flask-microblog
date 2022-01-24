from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse

from app import app
from app.forms import LoginForm
from app.models import User

@app.route("/")
@app.route("/index")
@login_required
def index():
#    return "Hello, world!"
    user = {"username": "Tim"}
    posts = [
        {
            "author": {"username": "John"},
            "body": "Beautiful day in Portland!"
        },
        {
            "author": {"username": "Susan"},
            "body": "The Avengers movie was so cool!"
        }
    ]
    return render_template("index.html", title="Home", posts=posts)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
#        flash("Log in requested for user {user}, remember_me={r}"
#            .format(user=form.username.data, r=form.remember_me.data))
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid user name or password!")
            return redirect(url_for("index"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netlog != "":
            next_page = url_for("index")
        return redirect(next_page)
    return render_template("login.html", title="Sign In", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
