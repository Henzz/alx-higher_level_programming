#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        new_string = list(my_string)
        for i in range(0, len(new_string)):
            if ord(new_string[i]) == 67 or ord(new_string[i]) == 99:
                new_string[i] = ''
        my_string = ''.join(new_string)
    return my_string
