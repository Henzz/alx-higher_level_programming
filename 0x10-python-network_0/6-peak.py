#!/usr/bin/python3
"""
Contains a function that searches peak of given array of numbers
"""


def find_peak(list_of_integers):
    """
    Finds a peak given a number
    """
    if (len(list_of_integers) != 0):
        peak = 0
        for i in list_of_integers:
            if (peak < i):
                peak = i
        return peak
    else:
        return None
