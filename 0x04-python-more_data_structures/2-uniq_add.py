#!/usr/bin/python3
def uniq_add(my_list=[]):
    un_list = []
    result = 0
    for i in my_list:
        if i not in un_list:
            un_list.append(i)
    for i in un_list:
        result = result + i
    return result
