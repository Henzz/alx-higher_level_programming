#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum_result = ()
    for i in range(2):
        #print(tuple_b[i], len(tuple_b), tuple_b[i])
        if len(tuple_b) == 1 and i == 0:
            sum_result = sum_result + (tuple_a[i] + tuple_b[0],)
        elif len(tuple_b) == 1 and i == 1:
            sum_result = sum_result + (tuple_a[i] + 0,)
        elif len(tuple_b) == 0:
            sum_result = sum_result + (tuple_a[i] + 0,)
        elif len(tuple_b) == 2:
            sum_result = sum_result + (tuple_a[i] + tuple_b[i],)
    return sum_result
