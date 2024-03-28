#!/usr/bin/python3
"""
Contains a function that searches peak of given array of numbers
"""


def find_peak(list_of_integers):
    """
    Finds a peak given a number
    """
    if (len(list_of_integers) != 0):
        length = len(list_of_integers)
        low = 0
        high = length - 1
        while low < high:
            mid = (low + high) // 2

            if list_of_integers[mid] < list_of_integers[mid + 1]:
                low = mid + 1
            else:
                high = mid

        return list_of_integers[low]
    else:
        return None
