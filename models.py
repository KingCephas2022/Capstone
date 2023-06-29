from datetime import datetime
from extentions import db
from werkzeug.security import generate_password_hash, check_password_hash

class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500))
    short_url = db.Column(db.String(10), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('urls', lazy=True))

def __init__(self, original_url, short_url):
        self.original_url = original_url
        self.short_url = short_url


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)
