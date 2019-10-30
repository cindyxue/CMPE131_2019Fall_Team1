class DayAsHalfHours:
    """TODO:
            IN PROGRESS: move all methods to "Schedule" class in schedule.py
            input validation
            PEP 8 standardized proper documentation
            test cases
            integration with calendar
            BUG: If adding a shift starting before midnight and ending after midnight, errors occur
    """
    def __init__(self):
        self.work_hours = []
        for i in range(48):
            self.work_hours.append(False)