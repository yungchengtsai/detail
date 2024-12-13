# models.py
from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    favorite_movies = db.relationship(
        "Movie", secondary="user_favorites", backref="favorited_by"
    )
    bookings = db.relationship("Booking", backref="user", lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    genre = db.Column(db.String(100))
    screening_times = db.relationship("ScreeningTime", backref="movie", lazy=True)
    is_current = True
    rating = 5.0


class Cinema(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(300))
    screening_times = db.relationship("ScreeningTime", backref="cinema", lazy=True)


class ScreeningTime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), nullable=False)
    cinema_id = db.Column(db.Integer, db.ForeignKey("cinema.id"), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    bookings = db.relationship("Booking", backref="screening", lazy=True)


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    screening_id = db.Column(
        db.Integer, db.ForeignKey("screening_time.id"), nullable=False
    )
    seat_number = db.Column(db.String(10), nullable=False)


user_favorites = db.Table(
    "user_favorites",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("movie_id", db.Integer, db.ForeignKey("movie.id"), primary_key=True),
)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
