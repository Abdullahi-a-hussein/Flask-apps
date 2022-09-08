
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


# CONFIGURING LOGIN MANAGER
login_manager = LoginManager(app)

# CREATING USER LOADER
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



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
    return render_template('cafes.html', cafes=all_cafes, user=current_user)

@app.route("/add-cafe", methods=['GET', 'POST'])
def add_cafe():
    cafe_form = CafeForm()
    if not current_user.is_authenticated:
        flash('Please register to add new cafe')
        return redirect(url_for('register'))
    if request.method == 'POST':
        items = request.form
        register_new_cafe(items)
        return redirect(url_for('home'))
    return render_template('add-cafe.html', form=cafe_form)

@app.route('/join', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if request.method == 'POST':
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email registered. Please login')
            return redirect(url_for('login'))
        if request.form.get('password') != request.form.get('password_re'):
            flash('Password don not match. Please re-enter password')
            return redirect(url_for('register'))
        user = register_user(request.form)
        login_user(user)
        return redirect(url_for('home'))
    return render_template('register.html', form=register_form, user=current_user)
@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = SignInForm()
    if request.method == 'POST':
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        if not user:
            flash("Email not registered. Check email and try again")
            return redirect(url_for('login'))
        if not check_password_hash(user.password, request.form.get('password')):
            flash('incorrect Password. Try again')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('home'))
    return render_template('login.html', form=login_form, user=current_user)

        



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

def register_user(form):
    new_user = User(name=form.get('name'),
                    email=form.get('email'),
                    password=generate_password_hash(password=form.get('password'), method='pbkdf2:sha256', salt_length=8))
    db.session.add(new_user)
    db.session.commit()
    return new_user

if __name__ == "__main__":
    app.run(debug=True)