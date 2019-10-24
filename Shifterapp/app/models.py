from datetime import datetime
from app import db
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Organization(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.String(128), index = True, unique = True)
    Address = db.Column(db.String(256), index = True, unique = True)
    PhoneNumber = db.Column(db.Integer, index = True, unique = True)
    employees = db.relationship('Employee', backref = "organization")
    
class Employee(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(128), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    Organizationi_id = db.Column(db.String(128), db.ForeignKey('Organization.id'))
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)