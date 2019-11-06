from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, PasswordField, IntegerField
from wtforms.fields import SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import Organization,Employee, Question

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
    business_phone_number = IntegerField("Business Phone number")
    manager_phone_number = IntegerField("Manager Phone Number", validators=[DataRequired()])
    submit = SubmitField("Submit")

    def validate_name_company(self, name_company):
        org = Organization.query.filter_by(name=name_company.data).first()
        if org is not None:
            raise ValidationError('The Company has been already registered.')
    def validate_email(self, email):
        emp = Employee.query.filter_by(email=email.data).first()
        if emp is not None:
            raise ValidationError('This email has been already registered')

    def validate_phone_emp(self, manager_phone_number):
        empph = Employee.query.filter_by(phone_number = manager_phone_number.data).first()
        if empph is not None:
            raise ValidationError('This phone number has been already registered')
        elif len(manager_phone_number.data) !=10:
            raise ValidationError('Invalid Phone Number, must be 10 digits. No Space')
class EmployeeForm(FlaskForm):
    first_name = StringField("First name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone_number = StringField("Phone number", validators=[DataRequired()])
    submit = SubmitField("Submit info")

class ResetPasswordForm(FlaskForm):
    Question1 = SelectField('Question1'
    , choices = [('whichcity', 'Which city was your father born in?')], validators=[DataRequired()])
    answer1 = StringField('answer1', validators =[DataRequired()])
