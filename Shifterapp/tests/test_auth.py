import pytest
from app.models import Employee, Organization, Schedule

def test_get_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Email' in response.data
    assert b'Password' in response.data
    assert b'Register Your Organization' in response.data

def test_add_organization_to_db(db):
    org1 = Organization(name='Testers',
                         email='FlaskTesting2384626@gmail.com',
                         typeofbusiness='Code Testing',
                         address='123 Fake Street',
                         phone_number='444555888888')
    
    db.session.add(org1)
    db.session.commit()
    assert len(Organization.query.all()) == 1
    org_from_db = Organization.query.get(1)
    assert org_from_db.name == org1.name
    assert org_from_db.email == org1.email
    assert org_from_db.typeofbusiness == org1.typeofbusiness
    assert org_from_db.address == org1.address
    assert org_from_db.address == org1.address
    assert org_from_db.phone_number == org1.phone_number

def test_persistent_db_between_tests(db):
    org_from_db = Organization.query.get(1)
    assert len(Organization.query.all()) == 1
    assert org_from_db.name == 'Testers'
    
def test_add_employee_to_db(db):
    emp1 = Employee(fname='Testy',
                     lname='McTest',
                     email='TestyMcTest822@gmail.com',
                     phone_number='9998887777',
                     organization_id='1',
                     firsttimelogin = True)
    emp1.setManager('Employee') # 'Employee' arg sets to False, 'Manager' arg sets to True
    emp1.set_password(emp1.phone_number)
    db.session.add(emp1)
    assert len(Employee.query.all()) == 1
    emp_from_db = Employee.query.get(1)
    assert emp_from_db.fname == emp1.fname
    assert emp_from_db.lname == emp1.lname
    assert emp_from_db.email == emp1.email
    assert emp_from_db.phone_number == emp1.phone_number
    assert emp_from_db.organization_id == emp1.organization_id
    assert emp_from_db.firsttimelogin == emp1.firsttimelogin
    assert emp_from_db.manager == False
    
    # An employee's password should be their phone number by default, but the password
    # in the database should be hashed.
    
    assert emp_from_db.password_hash != emp1.phone_number
    
    emp2 = Employee(fname='Sam',
                    lname='TheManager',
                    email='SamTheManager822@gmail.com',
                    phone_number='8372934823',
                    organization_id='1',
                    firsttimelogin = True)
    emp2.setManager('Manager')
    emp2.set_password(emp2.phone_number)
    db.session.add(emp2)
    assert len(Employee.query.all()) == 2
    manager_from_db = Employee.query.get(2)
    assert manager_from_db.manager == True
    
    
    