#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        k = -1
        for i in my_list:
            print("{:d}".format(my_list[k]))
            k = k - 1
