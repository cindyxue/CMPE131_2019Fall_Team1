from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, PasswordField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email


class LoginForm(FlaskForm):
    Username = StringField("Username",validators=[DataRequired()])
    Password = StringField("Password",validators=[DataRequired()])
    Login = SubmitField("Login")
    ResetPassword = SubmitField("ResetPassword")
    RememberMe = BooleanField("Remember Me")
class LogoutForm(FlaskForm):
    Logout = SubmitField("Logout")

class EditViewForm(FlaskForm):
    View = SubmitField("Edit/View Schedule")
    AddEmpl = SubmitField("Add Employee")
    EditEmpl = SubmitField("Edit Employee")


class EmployeeForm(FlaskForm):
    first_name = StringField("First name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone_number = IntegerField("Phone number", validators=[DataRequired()])
    submit = SubmitField("Submit info")