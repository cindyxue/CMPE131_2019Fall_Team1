from datetime import datetime
from datetime import date
from datetime import time
from app import db
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Organization(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128), index = True, unique = True)
    email = db.Column(db.String(128), index = True, unique = True)
    typeofbusiness = db.Column(db.String(128))
    address = db.Column(db.String(256), index = True)
    phone_number = db.Column(db.String(256), index = True)
    employees = db.relationship('Employee', backref = "Organization")
    schedule = db.relationship('Schedule', backref='Organization')
   

    
class Employee(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fname = db.Column(db.String(128), index = True)
    lname = db.Column(db.String(128), index = True)
    email = db.Column(db.String(128), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    phone_number = db.Column(db.String(128) ,index = True, unique = True)
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'))
    firsttimelogin = db.Column(db.Boolean, index = True, nullable = False)
    manager = db.Column(db.Boolean, index = True, nullable = False)
    question1 = db.Column(db.String(2056), index = True)
    answer1 = db.Column(db.String (128), index = True)
    question2 = db.Column(db.String(2056), index = True)
    answer2 = db.Column(db.String (128), index = True)
    schedule = db.relationship('Schedule', backref = 'Employee')

    def setManager(self, data):
        """Toggles the manager column of each employee"""

        if data == 'Employee':
            self.manager = False
        elif data == 'Manager':
            self.manager = True

    def setfirstlogin(self, firsttime):
        """Toggles the firsttime login column of each employee"""

        self.firsttimelogin=firsttime

    def setQuestion(self, question1, question2):
        """set the security questions of each employee"""

        self.question1 = question1
        self.question2 = question2

    def setAnswer (self, answer1, answer2):
        """set the security questions' answers of each employee"""

        self.answer1 = answer1
        self.answer2 = answer2

    def set_password(self, password):
        """sets the password of each employee"""

        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        """checks the password with data base, if matches, returns True"""

        return check_password_hash(self.password_hash, password)

    def set_orgid(self, id):
        """sets the Organization Id of each employee"""
        
        self.organization_id = id
    
    
class Schedule(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key = True)
    thedates = db.Column(db.Date, nullable = True)
    starttime = db.Column(db.Time, nullable = True)
    endtime = db.Column(db.Time, nullable = True)
    emp_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    org_id = db.Column(db.Integer, db.ForeignKey('organization.id'))

   # def showschedule(self):
        
    
@login.user_loader
def load_user(id):
    return Employee.query.get(int(id))



