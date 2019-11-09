import pytest
from app.schedule import *

@pytest.fixture(scope='module')
def new_schedule():
    schedule = Schedule()
    
    return schedule


def test_new_schedule(new_schedule):
    assert not new_schedule.full_schedule # Empty lists should return False


@pytest.fixture(scope='module')
def bool_list_maker():
    true_or_false = False
    bool_list = Schedule.make_bool_list(6, true_or_false)
    list_of_bool_lists = Schedule.make_list_of_bool_lists(3, 6, true_or_false)
    
    return bool_list, list_of_bool_lists


def test_bool_list_maker(bool_list_maker):
    correct_bool_list = [False, False, False, False, False, False]
    correct_list_of_bool_lists = [[False, False, False, False, False, False,],
                                  [False, False, False, False, False, False,],
                                  [False, False, False, False, False, False,]
                                  ]
    
    assert bool_list_maker[0] == correct_bool_list
    assert bool_list_maker[1] == correct_list_of_bool_lists

@pytest.fixture(scope='module')
def added_shift():
    schedule = Schedule()
    
    start_time = '11/01/2019 06:00 AM'
    end_time = '11/01/2019 12:00 PM'
    schedule.add_shift(start_time, end_time)
    
    return schedule


def test_add_shift(added_shift):
    correct_schedule = Schedule()
    
    month_year = '11/2019'
    true_or_false = False
    
    work_schedule = Schedule.make_list_of_bool_lists(30, 48, true_or_false) # 30 days in november, 48 half hours per day
        
    for i in range(11, 23): # Represents 06:00 AM to 12:00 PM
        work_schedule[0][i] = True
        
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
    
@pytest.fixture(scope='module')
def removed_shift():
    schedule = Schedule()
    
    start_time = '11/01/2019 06:00 AM'
    end_time = '11/01/2019 12:00 PM'
    
    schedule.add_shift(start_time, end_time)
    
    start_time_of_change = '11/01/2019 09:00 AM'
    end_time_of_change = '11/01/2019 12:00 PM'
    
    schedule.remove_shift(start_time_of_change, end_time_of_change)
    
    return schedule


def test_removed_shift(removed_shift):
    correct_schedule = Schedule()
    
    month_year = '11/2019'
    true_or_false = False
    
    work_schedule =  Schedule.make_list_of_bool_lists(30, 48, true_or_false)# 30 days in november, 48 half hours per day
        
    for i in range(11, 17): # Represents 06:00 AM to 9:00 PM
        work_schedule[0][i] = True
        
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
    
    assert removed_shift.full_schedule == correct_schedule.full_schedule