from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, PasswordField, IntegerField
from wtforms.fields import SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

QUESTION_CHOICES = [('1', 'What\'s your mother\'s maiden name?'), 
                    ('2', 'What\'s your favorite song?'),
                    ('3', 'What\'s your favorite movie?'),    
                    ]

class LoginForm(FlaskForm):
    Username = StringField("Username")
    Password = PasswordField("Password")
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
    re_password = PasswordField("Confirm Password",validators=[DataRequired()])
    phone_number = IntegerField("Phone number", validators=[DataRequired()])
    submit = SubmitField("Submit")

class EmployeeForm(FlaskForm):
    first_name = StringField("First name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone_number = IntegerField("Phone number", validators=[DataRequired()])
    submit = SubmitField("Submit info")

class EditForm(FlaskForm):
    name_company = StringField("Organization name", validators=[DataRequired()])
    type_company = StringField("Organization type", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    enter_password = StringField("Password", validators=[DataRequired()])
    re_password = PasswordField("Confirm Password", validators=[DataRequired()])
    securityQuestion1 = SelectField("Security Question", choices=QUESTION_CHOICES, validators=[DataRequired()])
    securityAnswer1 = StringField("Password", validators=[DataRequired()])
    edit = SubmitField("Edit")