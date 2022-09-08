
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
    opening_hours = StringField(label="Opening Time e.g. 10:00am", validators=[DataRequired()], render_kw={'placeholder':'10:00am'})
    closing_hours = StringField(label="Closing Time e.g. 9:30pm", validators=[DataRequired()], render_kw={'placeholder':'9:30pm'})
    wifi_rating = SelectField(label="Wifi Rating", choices=SIGNAL, validators=[DataRequired()])
    power_rating = SelectField(label="Power Outlet Rating", choices=SIGNAL, validators=[DataRequired()])
    coffee_rating = SelectField(label="How Good is Coffee", choices=SIGNAL, validators=[DataRequired()])
    submit = SubmitField(label='Add')
    
class RegisterForm(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired()])
    email = EmailField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    password_re = PasswordField(label="Re-enter password", validators=[DataRequired()])
    submit = SubmitField(label="Register")
    
class SignInForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired()], render_kw={'placeholder':'example@mail.com'})
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Login")


class SearchCity(FlaskForm):
    city = StringField(label="Enter City Name", validators=[DataRequired()])
    submit = SubmitField(label='Search')