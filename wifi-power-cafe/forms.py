
from ast import Sub
from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, EmailField
from wtforms.validators import DataRequired, URL, Email


SIGNAL = [0, 1, 2, 3, 4, 5]



class CafeForm(FlaskForm):
    name = StringField(label="Cafe Name", validators=[DataRequired()])
    url = StringField(label="Address on Google Maps", validators=[DataRequired(), URL()])
    img = StringField(label="Photo Link", validators=[DataRequired()])
    opening_hours = StringField(label="Opening Time e.g. 10:00 AM", validators=[DataRequired()], render_kw={'placeholder':'10:00 AM'})
    closing_hours = StringField(label="Closing Time e.g. 9:30 PM", validators=[DataRequired()], render_kw={'placeholder':'9:30 PM'})
    wifi_rating = SelectField(label="Wifi Rating", choices=SIGNAL, validators=[DataRequired()])
    power_rating = SelectField(label="Power Outlet Rating", choices=SIGNAL, validators=[DataRequired()])
    coffee_rating = SelectField(label="How Good is Coffee", choices=SIGNAL, validators=[DataRequired()])
    submit = SubmitField(label='Add')
    
class RegisterForm(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired()])
    email = EmailField(label="Email", validators=[DataRequired(), Email()])
    password = StringField(label="Enter Password", validators=[DataRequired()], render_kw={'placeholder':"password must be at least 8 characters"})
    password_re = StringField(label="Enter password again", validators=[DataRequired()])
    submit = SubmitField(label="Register")
    
class SignInForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired()], render_kw={'placeholder':'example@mail.com'})
    password = StringField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Login")
