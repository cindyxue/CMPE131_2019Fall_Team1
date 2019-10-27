from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, PasswordField, IntegerField
from wtforms.fields import SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    Username = StringField("Username",validators=[DataRequired()])
    Password = StringField("Password",validators=[DataRequired()])
    Login = SubmitField("Login")
    ResetPassword = SubmitField("ResetPassword")
    Register = SubmitField("Register")
    RememberMe = BooleanField("Remember Me")
class LogoutForm(FlaskForm):
    Logout = SubmitField("Logout")

class EditViewForm(FlaskForm):
    View = SubmitField("Edit/View Schedule")
    AddEmpl = SubmitField("Add Employee")
    EditEmpl = SubmitField("Edit Employee")

class RegisterForm(FlaskForm):
    name_company = StringField("Organization name", validators=[DataRequired()])
    type_company = StringField("Organization type", validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])
    manager_namef = StringField("First name", validators=[DataRequired()])
    manager_namel = StringField("Last name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    enter_password = StringField("Password",validators=[DataRequired()])
    re_password = StringField("Confirm Password",validators=[DataRequired()])
    phone_number = IntegerField("Phone number", validators=[DataRequired()])
    submit = SubmitField("Submit")

class EmployeeForm(FlaskForm):
    first_name = StringField("First name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone_number = IntegerField("Phone number", validators=[DataRequired()])
    submit = SubmitField("Submit info")