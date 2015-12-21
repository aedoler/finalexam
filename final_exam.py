#!user/bin/env python
# -*- coding: utf-8 -*-
"""Fibonacci series"""

import json
import decimal


def loopschools(schooldata):
    """ Finds school with lowest spending and highest grades in dataset.
    Args:
        schooldata (str, filepath): filepath containing dataset
    Returns:
        tuple containing school code and final ratio
    Examples:
        >>> loopschools('schools.json')
        (u'PS2424', Decimal('7484.805460750853242320819113'))
    """
    filehandler = open(str(schooldata), 'r')
    openfile = json.load(filehandler)
    schooldata = openfile['data']
    school_id_list = []
    spending_list = []
    gpa_list = []

    for school in schooldata:

        school_id_list.append(school['school_id'])  # School ID

        spending_list.append(school['per_student_spending'])  # Spending per s

        grade = school['grades']
        gpa = grade['1'] * 1 + grade['2'] * 2 + grade['3'] * 3 + grade['4'] * 4
        # GPA scale
        gpa = decimal.Decimal(gpa)
        total_grades = grade['1'] + grade['2'] + grade['3'] + grade['4']
        # Number of grades
        total_grades = decimal.Decimal(total_grades)
        grade_division = (gpa, total_grades)
        grade_division = (grade_division[0] / grade_division[1])  # Find GPA
        gpa_list.append(grade_division)

    correlate_data = zip(gpa_list, spending_list)
    # Combines GPA and amount spent lists
    correlate_data2 = dict(zip(school_id_list, correlate_data))
    # Combines with ID into dict

    spend_ratio = {key: value[1] / value[0]
                   for key, value in correlate_data2.iteritems()}
    # Finds ratio
    spend_ratio_key = max(spend_ratio)

    return spend_ratio_key, spend_ratio[spend_ratio_key]


def loopdistricts(schooldata):
    """Returns school district with best spending/grades ratio in dataset.
    """
    filehandler = open(str(schooldata), 'r')
    openfile = json.load(filehandler)
    schooldata = openfile['data']
    disdict = {}
    for dictitem in schooldata:
        dict_index = dictitem['district_code']

    for district in schooldata:
        if dict_index not in disdict:
            disdict[dict_index] = district['grades'], district['per_student_spending']
        else:
            disdict[dict_index] += district['grades']

    return disdict


print loopschools('schools.json')
