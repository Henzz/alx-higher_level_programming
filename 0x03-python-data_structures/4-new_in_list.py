#!/usr/bin/python3
def new_in_lister(my_list=[]):
    if my_list:
        k = -1
        for i in my_list:
            print("{:d}".format(my_list[k]))
            k = k - 1
