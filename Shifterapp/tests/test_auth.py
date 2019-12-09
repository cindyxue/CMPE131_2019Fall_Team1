import pytest
from app.models import Employee, Organization, Schedule

def test_get_login_page(client):
    response = client.get('/login')
    assert response.status_code == 200
