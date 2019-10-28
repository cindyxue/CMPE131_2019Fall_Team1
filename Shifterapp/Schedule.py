class Schedule:
    """TODO:
            input validation
            PEP 8 standardized proper documentation
            test cases
            integration with calendar
    """
    def __init__(self):
        self.day_intervals = []
        for i in range(48):
            self.day_intervals.append(False)
    

    def parse_time(self, time_string):
        """Parses a String of the form '4:30 AM' or '12:30 PM'
            and returns minutes since 12:00 AM"""
        list = time_string(':')
        hour = int(list[0])
        list_2 = list[1].split(' ')
        minutes = int(list_2[0])

        if [list_2[1] == "PM"]:
            hour += 12

        minutesIntoDay = (hour * 60) + minutes
        return minutesIntoDay

    def set_schedule_interval(self, time_start, time_end):
        """Accepts a start time and end time either on the hour or half past the hour
            and updates a schedule to contain that interval"""
        start_of_shift = self.parse_time(time_start)
        end_of_shift = self.parse_time(time_end)

        start_of_shift_index = start_of_shift / 30
        end_of_shift_index = end_of_shift / 30
        range_of_shift = end_of_shift_index - start_of_shift_index
        for i in range(range_of_shift):
            self.day_intervals[start_of_shift + i] = True
        
        return 1 # Method did not run into errors