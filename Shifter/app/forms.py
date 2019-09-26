from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, PasswordField

class LoginForm(FlaskForm):
    Username = StringField("Username")
    Password = StringField("Password")

class EditView(FlaskForm):
    View = SubmitField("Edit/View Schedule")
    AddEmpl = SubmitField("Add Employee")