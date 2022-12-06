#!/usr/bin/python3
def element_at(my_list, idx):
    if my_list[idx] == ValueError or my_list[idx] < 0:
        return None
    if my_list[idx] >= 0:
        return my_list[idx]
