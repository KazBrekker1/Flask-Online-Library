from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    movies = db.relationship('Movie', backref='author', lazy=True)
    books = db.relationship('Series', backref='author', lazy=True)
    series = db.relationship('Book', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    link = db.Column(db.String(), nullable=False)
    watched = db.Column(db.Boolean, nullable=False)
    anime = db.Column(db.Boolean, nullable=False)
    dubbed = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Movie('{self.title}', '{self.link}')"


class Series(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    link = db.Column(db.String(), nullable=False)
    watching = db.Column(db.Boolean, nullable=False)
    anime = db.Column(db.Boolean, nullable=False)
    dubbed = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Series('{self.title}', '{self.link}')"


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    writer = db.Column(db.String(20), nullable=False)
    link = db.Column(db.String(), nullable=False)
    pages = db.Column(db.Integer, nullable=False)
    finished = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Book('{self.title}', '{self.link}')"
