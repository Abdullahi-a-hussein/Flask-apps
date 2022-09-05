
from flask import Flask, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import current_user, login_required, UserMixin, login_user, LoginManager, logout_user





app = Flask(__name__)
app.config['SECRET_KEY'] = "Assddk8hsMt3hhy"
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)




class Cafe(db.Model):
    __tablename__ = "cafes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    img = db.Column(db.String, nullable = False)
    opening_hours = db.Column(db.String, nullable=False)
    closing_hours = db.Column(db.String, nullable=False)
    wifi_rating = db.Column(db.String, nullable=False)
    power_rating = db.Column(db.String, nullable=False)
    coffee_rating = db.Column(db.String, nullable=False)
    
    
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    