from classes import Subject, Group, Schedule, Schedule_finder
from dane_z_usos_wnioskowanie import data
import itertools as i
import numpy as np

def load_subjects(data):
    subjects = []
    for key, value in data.items():
        groups = []
        for key2, value2 in value.items():
            group = Group(key, key2, value2)
            groups.append(group)
        subject = Subject(key, groups)
        subjects.append(subject)
    return subjects


def find_combinations(subjects):
    gr = [s.groups for s in subjects]
    combinations = i.product(*gr)
    return [*combinations]


def test_combination(combination):
    days = range(7)
    for day in days:
        s = []
        for gr in combination:
            try:
                s.append(gr.hours[day])
            except KeyError:
                pass
        s = [k for j in s for k in j]
        s2 = set(s)
        if len(s) != len(s2):
            return True

def return_comb_data(combination):
    pri = str()
    for gr in combination:
        data = f'{gr.subject}: {gr.name}\n'
        pri += data
    pri += "-"*20
    return pri

def generate_plan(data):
    subjects = load_subjects(data)
    combs = find_combinations(subjects)
    for combination in combs:
        if test_combination(combination):
            continue
        else:
            print(return_comb_data(combination))


generate_plan(data)



