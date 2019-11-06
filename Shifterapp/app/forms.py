from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, PasswordField, IntegerField
from wtforms.fields import SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo


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
    Business_phone_number = IntegerField("Business Phone number")
    Manager_phone_number = IntegerField("Manager Phone Number", validators=[DataRequired()])
    submit = SubmitField("Submit")

class EmployeeForm(FlaskForm):
    first_name = StringField("First name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone_number = IntegerField("Phone number", validators=[DataRequired()])
    submit = SubmitField("Submit info")

class ResetPasswordForm(FlaskForm):
    question1 = SelectField('--Question 1 Select One--'
    , choices = [('Whichcity', 'Which city was your father born in?')
    , ('Whatname', 'What is the first name of your best friend in high school?')
    , ('Whatstreet', 'What street did you grow up on?')
    , ('Whatcook', 'What was the first thing you learned to cook?')
    , ('Wherefly', 'Where did you go the first time you flew on a plane?')], validators=[DataRequired()])
    answer1 = StringField('Answer1', validators =[DataRequired()])
    question2 = SelectField('--Question 2 Select One--'
    , choices = [('Whichcity', 'Which city was your father born in?')
    , ('Whatname', 'What is the first name of your best friend in high school?')
    , ('Whatstreet', 'What street did you grow up on?')
    , ('Whatcook', 'What was the first thing you learned to cook?')
    , ('Wherefly', 'Where did you go the first time you flew on a plane?')], validators=[DataRequired()])
    answer2 = StringField('Answer2', validators =[DataRequired()])
