from datetime import datetime
from hashlib import md5

# User the UserMixin class from Flask-Login for the standard attributes
# such as is_authenticated, is_active, etc.
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship("Post", backref="author", lazy="dynamic")

    def __repr__(self):
        return "<User {user}>".format(user=self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def avatar(self, size):
        """
        Get "identicon" geometric avatar from Gravatar web service
        using email address MD5 hash.
        """
        gravatar_url_templ = "https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}"
        digest = md5(self.email.lower().encode("utf-8")).hexdigest()
        return gravatar_url_templ.format(digest=digest, size=size)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return "<Post {post}>".format(post=self.body)
