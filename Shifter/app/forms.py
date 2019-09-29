from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, PasswordField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email


class LoginForm(FlaskForm):
    Username = StringField("Username")
    Password = StringField("Password")
    Login = SubmitField("Login")
    RememberMe = BooleanField("Remember Me")
class LogoutForm(FlaskForm):
    Logout = SubmitField("Logout")

class EditView(FlaskForm):
    View = SubmitField("Edit/View Schedule")
    AddEmpl = SubmitField("Add Employee")


class EmployeeForm(FlaskForm):
    first_name = StringField("First name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone_number = IntegerField("Phone number", validators=[DataRequired()])
    submit = SubmitField("Submit info")