from datetime import datetime
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
   

    
class Employee(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fname = db.Column(db.String(128), index = True)
    lname = db.Column(db.String(128), index = True)
    email = db.Column(db.String(128), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    phone_number = db.Column(db.String(128) ,index = True, unique = True)
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'))
    manager = db.Column(db.Boolean, index = True, nullable = False)
    questions = db.relationship('Question', backref = "Employee")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def set_orgid(self, id):
        self.organization_id = id
        
class Question(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    question = db.Column(db.String(128))
    answer = db.Column(db.String(128))
    employee_id = db.Column(db.String(128), db.ForeignKey('employee.id'))
@login.user_loader
def load_user(id):
    return Employee.query.get(int(id))



