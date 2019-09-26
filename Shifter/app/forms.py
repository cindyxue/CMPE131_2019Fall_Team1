from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField

class LoginForm(FlaskForm):
    Username = StringField("Username")
    Password = StringField("Password")