import calendar
from sqlalchemy import func
import sqlalchemy.types as types

class Schedule(types.UserDefinedType):
    """
    Holds daily schedules
    """
    
    """
    TODO:
        add to database
    
        sort and search methods (prioritize creating a functional product first)

        input validation (may be handled through flask form)

        proper documentaiton

        test cases
    """

    def get_col_spec(self, **kw):
        return "Schedule(%s)"%self.precision 

    def bind_processor(self, dialect):
        def process(value):
            return value
        return process

    def result_processor(self, dialect, coltype):
        def process(value):
            return value
        return process
    


    def __init__(self, precision = 8):
        self.precision = precision
        self.full_schedule = []
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

    @staticmethod
    def make_bool_list(size: int, true_or_false: bool):
        bool_list = []
        for i in range(size):
            bool_list.append(true_or_false)
        
        return bool_list
    
    
    @staticmethod
    def make_list_of_bool_lists(size: int, inner_list_size: int, true_or_false: bool):
        list_of_bool_lists = []
        for i in range(size):
            bool_list = Schedule.make_bool_list(inner_list_size, true_or_false)
            list_of_bool_lists.append(bool_list)
            
        return list_of_bool_lists
               


    def parse_time(self, time_string):
        """Parses a String of the form 'MM/DD/YYYY HH:mm AM' or 'MM/DD/YYYY HH:mm PM'
            and returns an array of the form [minutesIntoDay, 'month', 'day', 'year']"""

        list1 = time_string.split(' ') # ['MM/DD/YYYY', 'HH:mm', 'AM' or 'PM']
        list2 = list1[1].split(':') # ['HH', 'mm']
        list3 = list1[0].split('/') # ['MM, 'DD', YYYY']
        hour = int(list2[0])
        minutes = int(list2[1])

        if hour == 12:
            hour = 0 # 12 AM is the zero point. 
        if list1[2] == "PM":
            hour += 12

        minutesIntoDay = (hour * 60) + minutes
        day = list3[1]
        month = list3[0]
        year = list3[2]
        month_year = month + "/" + year

        return [minutesIntoDay, day, month_year]
  

    def edit_shift(self, add_or_remove:str, start_time:str, end_time:str):
        """
        Accepts a start time and end time of the form 'MM/DD/YYYY HH:mm AM' or 'MM/DD/YYYY HH:mm PM'
        and updates full_schedule to contain the new interval
        """
        
        if add_or_remove == 'add':
            working = True
        elif add_or_remove == 'remove':
            working = False
        
        start_of_shift = self.parse_time(start_time) # [minutesIntoDay, 'day', 'MM/YYYY'(month/year)]
        end_of_shift = self.parse_time(end_time)
        
        start_of_shift[1] = int(start_of_shift[1]) # converted 'day' into int for use later
        end_of_shift[1] = int(end_of_shift[1])
        
        month_year_match_found = True
        month_year_list = []
        
        month_year_list.append(start_of_shift[2])        
        month_year_list.append(end_of_shift[2])
        
        month_year_match_found = False

        for month_year in month_year_list:
            self.add_to_calendar(month_year) # will not add a new month if it already exists
        
        day_match_found = True
        day_list = []    
        
        day_list.append(start_of_shift[1])

        if start_of_shift[1] != end_of_shift[1]: # if shift starts and ends on different days
            day_list.append(end_of_shift[1])
            day_match_found = False
        
        start_of_shift_index = []
        end_of_shift_index = []
        shift_days_index = []
        shift_month_years = []
        
        start_of_shift_index.append((int)(start_of_shift[0] / 30)) # index 0
        shift_days_index.append(start_of_shift[1] - 1) # index 0
        
        for month_year in month_year_list:
            shift_month_years.append(month_year)
        
        if day_match_found:
            # schedule starts and ends on the same day
            end_of_shift_index.append((int)(end_of_shift[0] / 30) - 1) # index 0
        else:
            """
            different start and end days, meaning shift goes past midnight
            split into 2 shifts:
                1) starts at original start time, ends at midnight
                2) starts at midnight, ends at original end time
            """
            shift_days_index.append(end_of_shift[1] - 1) # index 1
            shift_month_years.append(end_of_shift[1]) # index 1
            end_of_shift_index.append(47) # 11:30 PM - 12:00 AM, index 0
            start_of_shift_index.append(0) # 12:00 AM - 12:30 AM, index 1
            end_of_shift_index.append((int)(end_of_shift[0] / 30 ) - 1) # index 1

        for i in range(len(shift_days_index)):
            schedule_index = self.get_schedule_index(shift_month_years[i])
            for j in range(start_of_shift_index[i], end_of_shift_index[i] + 1):
                self.full_schedule[schedule_index]['work_schedule'][shift_days_index[i]][j] = working


    def add_to_calendar(self, month_year: str):

        for schedule in self.full_schedule:
            if month_year in schedule.values():
                return # month is already in schedule 
        
        self.add_full_schedule_entry(month_year)

    def add_full_schedule_entry(self, month_year: str):
        month_year_as_list = month_year.split("/") # ["MM, "YYYY"]
        
        month = month_year_as_list[0]
        year = month_year_as_list[1]
        
        days_in_month = calendar.monthrange(int(year), int(month))[1]
        weekday = calendar.monthrange(int(year), int(month))[0]
        
        work_schedule = Schedule.make_list_of_bool_lists(days_in_month, 48, False)
        name_of_weekday = []
        
        for i in range(days_in_month):
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
    
    
    def get_schedule_index(self, month_year: str):
        for i in range(len(self.full_schedule)):
            if self.full_schedule[i].get('month_year') == month_year:
                return i