"""
All assertions are made with the assumption that the schedule.Schedule class is functioning correctly.
If test_schedule.py tests are failing, troubleshoot those tests BEFORE troubleshooting the database.
"""

import pytest
from ..schedule import Schedule
from ..schedule import *
from app import db
from app.models import Employee

@pytest.fixture(scope='module')
def new_schedule():
    work_schedule = Schedule()
    first_name = 'Bob'
    last_name = 'Ross'
    email = 'Bob.Ross92847@gmail.com'
    phone_number = '1234567'
    organization_id = 924
    work_schedule = Schedule()
    
    start_time = '12/29/2019 10:00 PM'
    end_time = '12/30/2019 02:00 AM'
    work_schedule.edit_shift('add', start_time, end_time)
    
    
    employee = Employee(fname = first_name,
                        lname = last_name,
                        email = email,
                        employee_phone_number = phone_number,
                        manager = False,
                        organization_id = organization_id
                        work_schedule = work_schedule
                        )
    
    #employee_from_db
    
    return employee

def test_new_schedule(new_schedule):
    pass
