import calendar
from calendar import Calendar

class DayAsHalfHours:
    def __init__(self):
        self.daily_half_hours = []
        for i in range(48):
            self.daily_half_hours.append(False)

class Schedule():
    """
    TODO:
        add to database
    
        sort and search methods (prioritize creating a functional product first)

        input validation (may be handled through flask form)

        proper documentaiton

        test cases
    """


    def __init__(self):
        self.full_schedule = list
        """
        [
            {
            month_year : "MM/YYYY",
            work_schedule: DayAsHalfHour[days in this month]
            name_of_weekday: [days in this month]
            },
            {
            month_year...
            },
            ...
        ]
        MM/YYYY represents month and year
        each DayAsHalfHour object contains a daily_half_hours boolean List with 48 elements
        name_of_weekday is a list containing the weekday (ex: 'Monday') associated with each day of the month
        """


    def parse_time(self, time_string):
        """Parses a String of the form 'MM/DD/YYYY HH:mm AM' or 'MM/DD/YYYY HH:mm PM'
            and returns an array of the form [minutesIntoDay, 'month', 'day', 'year']"""

        list1 = time_string.split(' ') # ['MM/DD/YYYY', 'HH:mm', 'AM' or 'PM']
        list2 = list1[2].split(':') # ['HH', 'mm']
        list3 = list[0].split('/') # ['MM, 'DD', YYYY']
        hour = int(list2[0])
        minutes = int(list2[1])

        if hour == 12:
            hour = 0 # 12 AM is the zero point. 
        if [list1[2] == "PM"]:
            hour += 12

        minutesIntoDay = (hour * 60) + minutes
        day = list3[1]
        month = list3[0]
        year = list3[2]
        month_year = month + "/" + year

        return [minutesIntoDay, day, month_year]
  

    def set_schedule_interval(self, time_start:str, time_end:str):
        """
        Accepts a start time and end time of the form 'MM/DD/YYYY HH:mm AM' or 'MM/DD/YYYY HH:mm PM'
        and updates work_schedules to contain the new interval
        """

        
        start_of_shift = self.parse_time(time_start) # [minutesIntoDay, 'day', 'MM/YYYY'(month/year)]
        end_of_shift = self.parse_time(time_end)
        month_year_match_found = True
        months_to_find = []

        months_to_find[0] = start_of_shift[2]
        if start_of_shift[2] != end_of_shift[2]: # if shift starts and ends on diffierent months
            months_to_find.append(end_of_shift[2])
            month_year_match_found = False

        for month_year in months_to_find:
            self.add_to_calendar(month_year) # will not add an new month if it already exists
        
        start_of_shift_index = list
        end_of_shift_index = list
        shift_days = list
        
        start_of_shift_index[0] = (start_of_shift[0] / 30) - 1
        shift_days[0] = start_of_shift[1]
        
        if month_year_match_found:
            # schedule starts and ends on the same day
            end_of_shift_index[0] = (end_of_shift[0] / 30) - 1
        else:
            """
            different start and end days, meaning shift goes past midnight
            split into 2 shifts:
                1) starts at original start time, ends at midnight
                2) starts at midnight, ends at original end time
            """
            shift_days[1] = end_of_shift[1]
            end_of_shift_index[0] = 47 # 11:30 PM - 12:00 AM
            start_of_shift_index[1] = 0 # 12:00 AM - 12:30 AM
            end_of_shift_index[1] = (end_of_shift[0] / 30) - 1
        
        schedule_index = self.get_schedule_index()
        for i in range(len(shift_days)):
            self.wo
            
        # May no longer be relevant
        """start_of_shift_index = (start_of_shift[0] / 30) - 1
        end_of_shift_index = (end_of_shift[0] / 30) - 1
        range_of_shift = end_of_shift_index - start_of_shift_index
        for i in range(range_of_shift):
            self.work_hours[start_of_shift + i] = True
        
        return 1 # Method did not run into errors"""
    

    def add_to_calendar(self, month_year: str):
        month_year_in_schedule = True

        if not self.full_schedule: # if full_schedule is empty
            month_year_in_schedule = False
        else:
            for schedule in self.full_schedule:
                if month_year in schedule.values():
                    break
        
        if month_year_in_schedule:
            return # "MM/YYYY" already exists within schedule, nothing new added
        else:
            self.add_full_schedule_entry(month_year)

    def add_full_schedule_entry(self, month_year: str): 
        month_year_as_list = month_year.split("/") # ["MM, "YYYY"]
        
        month = month_year_as_list[0]
        year = month_year_as_list[1]
        
        days_in_month = calendar.monthrange(year, month)[1]
        weekday = calendar.monthrange(year, month)[0]
        
        work_schedule = list
        name_of_weekday = list
        
        for i in range(days_in_month):
            work_schedule.append(DayAsHalfHours())
            weekday_name = self.get_name_of_weekday(weekday)
            name_of_weekday.append(weekday_name)
            weekday = self.increment_weekday(weekday)
            
        self.full_schedule.append(
            {
                'month_year': month_year,
                'work_schedule': work_schedule,
                'name_of_weekday': name_of_weekday
            }
        )
            
        
            
            
    def get_name_of_weekday(self, number_of_weekday: int):
        """
        takes a value from 0-6 (Monday being 0, Sunday being 6)
        returns the name of the given weekday as a string
        """
        weekday_names = [
                        "Monday",
                         "Tuesday",
                         "Wednesday",
                         "Thursday",
                         "Friday",
                         "Saturday",
                         "Sunday"
                         ]
        
        return weekday_names[number_of_weekday]
    
    def increment_weekday(self, number_of_weekday: int):
        number_of_weekday += 1
        
        if number_of_weekday == 7:
            # Weekdays are from 0-6, and 0 must come after 6
            number_of_weekday = 0
        
        return number_of_weekday
    
    def get_schedule_index(self, day: str)