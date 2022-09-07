
from flask import Flask, render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import current_user, login_required, UserMixin, login_user, LoginManager, logout_user
from forms import *
from utils import *
from datetime import datetime






app = Flask(__name__)
app.config['SECRET_KEY'] = "Assddk8hsMt3hhy"
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# ---------------------------------- Database Tables Set up ------------------------------------ #

class Cafe(db.Model):
    __tablename__ = "cafe"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    map_url = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable = False)
    location = db.Column(db.String(100), nullable=False)
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


YEAR = datetime.today().strftime('%Y')
print(YEAR)
    
@app.route('/')
def home():
    return render_template('index.html', year=YEAR)

@app.route('/cafes')
def cafes():
    all_cafes = db.session.query(Cafe).all()
    return render_template('cafes.html', cafes=all_cafes)

@app.route("/add-cafe", methods=['GET', 'POST'])
def add_cafe():
    cafe_form = CafeForm()
    if request.method == 'POST':
        items = request.form
        register_new_cafe(items)
        return redirect(url_for('home'))
    return render_template('add-cafe.html', form=cafe_form)



def register_new_cafe(form):
    new_cafe  = Cafe(name=form.get('name'),
                     map_url=form.get('url'),
                     img_url=form.get('img'),
                     location="Toronto",
                     opening_hours=form.get('opening_hours'),
                     closing_hours=form.get('closing_hours'), 
                     wifi_rating = form.get('wifi_rating'),
                     power_rating=form.get('power_rating'),
                     coffee_rating=form.get('coffee_rating')
                    )
    db.session.add(new_cafe)
    db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)