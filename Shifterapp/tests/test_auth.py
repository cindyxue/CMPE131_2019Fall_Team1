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

