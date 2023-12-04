#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx >= 0 and len(my_list) != 0 and len(my_list) - 1 >= idx:
        my_list.remove(my_list[idx])
        return my_list
    else:
        return my_list
