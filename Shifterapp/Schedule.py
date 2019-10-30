import calendar
import datetime

class Schedule():
    """
    TODO: have work_schedule become a dictionary of dictionaries
          each dictionary should contain 'month', 'year', proper number of days in that month,
            an array of DayAsHalfHour with a length equal to the days in that month
          if user attempts to add work hours to a month, year that does not exist, add new
            dictionary entry
         
    """


    def __init__(self):
        self.work_schedule = {}
        """
        {
            {month 1, year, DayAsHalfHour[days in this month], name_of_weekday[days in this month]},
            {month 2, year, DayAsHalfHour[days in this month], name_of_weekday[days in this month]},
            ...
        }
        months should be of the form 'MM'
        years should be of the form 'YY'
        each DayAsHalfHour object contains a daily_half_hours boolean List with 48 elements
        name_of_weekday is a list containing the weekday (ex: 'Monday') associated with each day of the month
        """

    def parse_time(self, time_string):
        """Parses a String of the form 'MM/DD/YY HH:mm AM' or 'MM/DD/YY HH:mm PM'
            and returns an array of the form [minutesIntoDay, 'month', 'day', 'year']"""

        list = time_string.split(' ') # ['MM/DD/YY', 'HH:mm', 'AM' or 'PM']
        list_2 = list[2].split(':') # ['HH', 'mm']
        list_3 = list[0].split('/') # ['MM, 'DD', YY']
        hour = int(list_2[0])
        minutes = int(list_2[1])

        if hour == 12:
            hour = 0 # 12 AM is the zero point. 
        if [list[2] == "PM"]:
            hour += 12

        minutesIntoDay = (hour * 60) + minutes
        day = list_3[1]
        month = list_3[0]
        year = list_3[2]

        return [minutesIntoDay, month, day, year]
  
    def set_schedule_interval(self, time_start, time_end):
        """
        Accepts a start time and end time of the form 'MM/DD/YY HH:mm AM' or 'MM/DD/YY HH:mm PM'
        and updates work_schedules to contain the new interval
        """

        
        start_of_shift = self.parse_time(time_start) #[minutesIntoDay, 'month', 'day', 'year']
        end_of_shift = self.parse_time(time_end)
        month_match_found = True
        year_match_found = True

        if start_of_shift[2] != end_of_shift[2]:
            month_match_found = False
        if start_of_shift[3] == end_of_shift[3]:
            year_match_found = False
        """
        {
            {month 1, year, DayAsHalfHour[days in this month], name_of_weekday[days in this month]},
            {month 2, year, DayAsHalfHour[days in this month], name_of_weekday[days in this month]},
            ...
        }
        """
        months_to_find[0] = start_of_shift[2]
        if !month_match_found:
            months_to_find.append(end_of_shift[2])

        years_to_find[0] = start_of_shift[3]
        if !year_match_found:
            years_to_find = end_of_shift[3]   

        for i in len(self.work_schedule) {
            month_match_found = work_schedule[i].get('Month') == 
        }
        # May no longer be relevant
        """start_of_shift_index = (start_of_shift[0] / 30) - 1
        end_of_shift_index = (end_of_shift[0] / 30) - 1
        range_of_shift = end_of_shift_index - start_of_shift_index
        for i in range(range_of_shift):
            self.work_hours[start_of_shift + i] = True
        
        return 1 # Method did not run into errors"""
