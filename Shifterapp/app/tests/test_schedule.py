import pytest
from ..schedule import Schedule
from ..schedule import DayAsHalfHours

@pytest.fixture(scope='module')
def new_schedule():
    schedule = Schedule()
    return schedule


@pytest.fixture(scope='module')
def added_shift():
    schedule = Schedule()
    #def add_shift(self, time_start:str, time_end:str):
    """
    Accepts a start time and end time of the form 'MM/DD/YYYY HH:mm AM' or 'MM/DD/YYYY HH:mm PM'
    and updates full_schedule to contain the new interval
    """
    start_time = '11/01/2019 06:00 AM'
    end_time = '11/01/2019 12:00 PM'
    schedule.add_shift(start_time, end_time)
    return schedule


def test_new_schedule(new_schedule):
    assert not new_schedule.full_schedule # Empty lists should return False


def test_add_shift(added_shift):
    correct_schedule = Schedule()
    
    month_year = '11/2019'
    
    work_schedule = []
    
    for i in range(48):
        work_schedule.append(DayAsHalfHours())
        
    for i in range(11, 23):
        work_schedule[0][i] = {True}
        
    name_of_weekday = ['Friday', # 11/01/2019 starts on a Friday
                       'Saturday',
                       'Sunday',
                       'Monday',
                       'Tuesday',
                       'Wednesday',
                       'Thursday',
                       'Friday', # 11/08
                       'Saturday',
                       'Sunday',
                       'Monday',
                       'Tuesday',
                       'Wednesday',
                       'Thursday',
                       'Friday', # 11/15
                       'Saturday',
                       'Sunday',
                       'Monday',
                       'Tuesday',
                       'Wednesday',
                       'Thursday',
                       'Friday', # 11/22
                       'Saturday',
                       'Sunday',
                       'Monday',
                       'Tuesday',
                       'Wednesday',
                       'Thursday',
                       'Friday', # 11/29
                       'Saturday', # 30 days in november                                         
                       ]
    
    correct_schedule.full_schedule.append(
        {
                'month_year': month_year,
                'work_schedule': work_schedule,
                'name_of_weekday': name_of_weekday
        }
    )
    
    assert added_shift.full_schedule == correct_schedule.full_schedule