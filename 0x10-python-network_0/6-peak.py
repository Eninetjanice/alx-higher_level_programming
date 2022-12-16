#!/usr/bin/python3
""" Function that finds the peak in list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds the highest value in list of unsorted integers"""

    my_list = list_of_integers

    if my_list:
        my_list.sort()
        return my_list[-1]
    else:
        return None
