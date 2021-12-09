import numpy as np


class Subject:
    def __init__(self, name, groups) -> None: # grupy w słowniku utworzone klasą Group
        self.name = name
        self.groups = groups

class Group:
    def __init__(self, subject, name, hours) -> None: # hours w dict godziny przypisane do dni
        self.subject = subject
        self.name = name
        self.hours = self.convert_hours(hours)
        self.days = hours.keys()

    def convert_hours(self, hours):
        new_hours = dict()
        for key, v in hours.items():
            new_hours[key] = np.round(np.arange(v[0], v[1], 0.01), 2)
        return new_hours



class Schedule:
    def __init__(self, groups) -> None:
        pass

    def check_if_right():
        pass

class Schedule_finder:
    def __init__(self, subjects) -> None:
        pass

