from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, PasswordField, IntegerField, TextAreaField, DateField
from wtforms.fields import SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, data_required
from app.models import Organization,Employee, Schedule
from datetime import time



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
    ViewOwn = SubmitField("View My Schedule")

class RegisterForm(FlaskForm):
    name_company = StringField("Organization name", validators=[DataRequired()])
    type_company = StringField("Organization type", validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])
    manager_namef = StringField("First name", validators=[DataRequired()])
    manager_namel = StringField("Last name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    enter_password = PasswordField("Password",validators=[DataRequired()])
    re_password = PasswordField("Confirm Password",validators=[DataRequired()])
    business_phone_number = StringField("Business Phone number")
    manager_phone_number = StringField("Manager Phone Number", validators=[DataRequired()])
    submit = SubmitField("Submit")
    question1 = SelectField('Question 1'
    , choices = [ ('Select1', '--Select One--')
    , ('Whichcity', 'Which city was your father born in?')
    , ('Whatname', 'What is the first name of your best friend in high school?')
    , ('Whatstreet', 'What street did you grow up on?')
    , ('Whatcook', 'What was the first thing you learned to cook?')
    , ('Wherefly', 'Where did you go the first time you flew on a plane?')], validators=[DataRequired()])
    answer1 = StringField('Answer1', validators =[DataRequired()])
    question2 = SelectField('Question 2'
    , choices = [ ('Select2', '--Select One--')
    , ('FirstConcert', 'What was the first concert you attended?')
    , ('FirstCar', 'What was the name of the first car you owned?')
    , ('FavTeam', 'What is your favorit sports team?')
    , ('FavSport', 'What is your favorite sports?')
    , ('FavArtist', 'Who is your favorite actor?')], validators=[DataRequired()])
    answer2 = StringField('Answer2', validators =[DataRequired()])

    def validate_name_company(self, name_company):
        """the function makes sure that the company name is not already registered or in use"""

        org = Organization.query.filter_by(name=name_company.data).first()
        if org is not None:
            raise ValidationError('The Company has been already registered.')
    def validate_email(self, email):
        """the function makes sure that the email is not already registered or in use"""

        emp = Employee.query.filter_by(email=email.data).first()
        if emp is not None:
            raise ValidationError('This email has been already registered')
    def validate_business_phone_number(self, business_phone_number):
        """the function makes sure that the phone number is not already registerd"""

        orgph = Organization.query.filter_by(phone_number = business_phone_number.data).first()
        if orgph is not None:
            raise ValidationError('This phone number has been already registered')
        elif len(business_phone_number.data) !=10:
            raise ValidationError('Invalid Phone Number, must be 10 digits. No Space')        
    def validate_manager_phone_number(self, manager_phone_number):
        """makes sure that the phone number is not already registered"""

        empph = Employee.query.filter_by(phone_number = manager_phone_number.data).first()
        if empph is not None:
            raise ValidationError('This phone number has been already registered')
        elif len(manager_phone_number.data) !=10:
            raise ValidationError('Invalid Phone Number, must be 10 digits. No Space')
    def validate_re_password(self, re_password):
        """makes sure that the password and the repeated password match, otherwise alerts the user"""

        if (re_password.data != self.enter_password.data ):
            raise ValidationError('Passwords Do not Match!')
    def validate_question1(self, question1):
        """makes sure that a question is selected"""

        if question1.data == 'Select1':
            raise ValidationError('Please pick a question.')
    def validate_question2(self, question2):
        """makes sure that a question is selected"""

        if question2.data == 'Select2':
            raise ValidationError('Please pick a question.')   
class EmployeeForm(FlaskForm):
    first_name = StringField("First name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone_number = StringField("Phone number", validators=[DataRequired()])
    manager = SelectField('Select Role:', choices = [('Manager', 'Manager'), ('Employee','Employee')], validators = [DataRequired()])
    submit = SubmitField("Submit info", validators = [DataRequired()])

class ContactForm(FlaskForm):
    """
    Here are what this form is taking in

    name: Takes a valid name first or full name

    email: Takes in a valid email

    phone_number: Takes in a valid phone number

    subject: Takes in a small amount of text

    message: Takes in a Large amount of text

    submit: This is a button that will send the form information to the support email

    This is where the boxes are being made for the contact Page the rest of the desgin is CSS
    """
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone_number = IntegerField("Phone number", validators=[DataRequired()])
    subject = StringField("Subject", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit info")

class EditForm(FlaskForm):
    name_company = StringField("Organization name", validators=[DataRequired()])
    type_company = StringField("Organization type", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    enter_password = StringField("Password", validators=[DataRequired()])
    re_password = PasswordField("Confirm Password", validators=[DataRequired()])
    securityQuestion1 = SelectField("Security Question", choices=[], validators=[DataRequired()])
    securityAnswer1 = StringField("Password", validators=[DataRequired()])
    edit = SubmitField("Edit")
    subject = StringField("Subject", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit info")
    
class ResetPasswordForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    question1 = SelectField('Question 1: '
    , choices = [ ('Select1', '--Select One--')
    , ('Whichcity', 'Which city was your father born in?')
    , ('Whatname', 'What is the first name of your best friend in high school?')
    , ('Whatstreet', 'What street did you grow up on?')
    , ('Whatcook', 'What was the first thing you learned to cook?')
    , ('Wherefly', 'Where did you go the first time you flew on a plane?')], validators=[DataRequired()])
    answer1 = StringField('Answer1', validators =[DataRequired()])
    question2 = SelectField('Question 2'
    , choices = [ ('Select2', '--Select One--')
    , ('FirstConcert', 'What was the first concert you attended?')
    , ('FirstCar', 'What was the name of the first car you owned?')
    , ('FavTeam', 'What is your favorit sports team?')
    , ('FavSport', 'What is your favorite sports?')
    , ('FavArtist', 'Who is your favorite actor?')], validators=[DataRequired()])
    answer2 = StringField('Answer2', validators =[DataRequired()])
    newPassword = PasswordField("New Password", validators=[DataRequired()])
    newPasswordConfirm = PasswordField("Confirm New Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

    def validate_newPasswordConfirm(self, newPasswordConfirm):
        """makes sure that the confirm password matches the password"""

        if (newPasswordConfirm.data != self.newPassword.data):
            raise ValidationError('Passwords Do Not Match!')

    def validate_question1(self, question1):
        """makes sure that a question is picked"""

        if question1.data == 'Select1':
            raise ValidationError('Please pick a question.')

    def validate_question2(self, question2):
        """makes sure that a question is picked"""

        if question2.data == 'Select2':
            raise ValidationError('Please pick a question.')   
                 
class ChangeWeekForm(FlaskForm):
    previous= SubmitField('Previous')
    nextMonth = SubmitField('Next')
    thisMonth = SubmitField('This Month')
    startdatebox = DateField('Date', format = '%m/%d/%Y')
    enddatebox = DateField('Date', format = '%m/%d/%Y')
class managerhomepageForm(FlaskForm):
    startdate = DateField('Date', format = '%m/%d/%Y', validators=[DataRequired(), data_required()])
    
    starttime = SelectField('StartTime:', choices=[(time(0,0),'00:00'),(time(0,30),'00:30'),(time(1,0),'01:00'),
    (time(1,30),'01:30'),(time(2,0),'02:00'),(time(2,30),'02:30'),(time(3,0),'03:00'),(time(3,30),'03:30'),
    (time(4,0),'04:00'),(time(4,30),'04:30'),(time(5,0),'05:00'),(time(5,0),'05:30'),(time(6,0),'06:30'),
    (time(7,0),'07:00'),(time(7,30),'07:30'),(time(8,0),'08:00'),(time(8,30),'08:30'),(time(9,0),'09:00'),(time(9,30),'09:30'),(time(10,0),'10:00'),(time(10,30),'10:30'),
    (time(11,0),'11:00'),(time(11,30),'11:30'),(time(12,0),'12:00'),(time(12,30),'12:30'),(time(13,00),'13:00'),(time(13,30),'13:30'),(time(14,0),'14:00'),
    (time(14,30),'14:30'),(time(15,0),'15:00'),(time(15,30),'15:30'),(time(16,0),'16:00'),(time(16,30),'16:30'),(time(17,0),'17:00'),(time(17,30),'17:30'),
    (time(18,0),'18:00'),(time(18,30),'18:30'),(time(19,0),'19:00'),(time(19,30),'19:30'),(time(20,0),'20:00'),(time(20,30),'20:30'),(time(21,0),'21:00'),
    (time(21,30),'21:30'),(time(22,0),'22:00'),(time(22,30),'22:30'),(time(23,0),'23:00'),(time(23,30),'23:30')])
    
    endtime = SelectField('EndTime:', choices=[(time(0,0),'00:00'),(time(0,30),'00:30'),(time(1,0),'01:00'),
    (time(1,30),'01:30'),(time(2,0),'02:00'),(time(2,30),'02:30'),(time(3,0),'03:00'),(time(3,30),'03:30'),
    (time(4,0),'04:00'),(time(4,30),'04:30'),(time(5,0),'05:00'),(time(5,0),'05:30'),(time(6,0),'06:30'),
    (time(7,0),'07:00'),(time(7,30),'07:30'),(time(8,0),'08:00'),(time(8,30),'08:30'),(time(9,0),'09:00'),(time(9,30),'09:30'),(time(10,0),'10:00'),(time(10,30),'10:30'),
    (time(11,0),'11:00'),(time(11,30),'11:30'),(time(12,0),'12:00'),(time(12,30),'12:30'),(time(13,00),'13:00'),(time(13,30),'13:30'),(time(14,0),'14:00'),
    (time(14,30),'14:30'),(time(15,0),'15:00'),(time(15,30),'15:30'),(time(16,0),'16:00'),(time(16,30),'16:30'),(time(17,0),'17:00'),(time(17,30),'17:30'),
    (time(18,0),'18:00'),(time(18,30),'18:30'),(time(19,0),'19:00'),(time(19,30),'19:30'),(time(20,0),'20:00'),(time(20,30),'20:30'),(time(21,0),'21:00'),
    (time(21,30),'21:30'),(time(22,0),'22:00'),(time(22,30),'22:30'),(time(23,0),'23:00'),(time(23,30),'23:30'), (time(23,59), '23:59')])
    
    employees = SelectField('Employee:', coerce=str)
    Submit = SubmitField('Submit')

class scheduleTableForm(FlaskForm):
    datebox = DateField('datebox', format = '%m/%d/%Y', validators=[DataRequired(), data_required()])
    goTo = SubmitField('Go To') 
