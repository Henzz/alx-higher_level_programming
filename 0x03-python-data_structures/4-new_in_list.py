#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        if idx >= 0 and len(my_list) > idx:
            new_list = list(my_list)
            new_list[idx] = element
            return new_list
