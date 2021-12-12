
import importlib


class DayFactory:

    class DayChallengeException(Exception):

        def __init__(self, day_value, max_day):
            message = f'Problem not posted yet. ' \
                      f'Max is {max_day}.' \
                      f'Requested day is {day_value}'
            super().__init__(message)

    def __init__(self, max_day):
        self.max_day = max_day

    def get_day(self, day_value):
        if day_value > self.max_day:
            raise DayFactory.DayChallengeException(day_value, self.max_day)
        day_name = "Day%d" % day_value
        day_class = getattr(importlib.import_module(day_name), day_name)
        return day_class()

