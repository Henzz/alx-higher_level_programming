#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    """
    sum_result = ()
    for i in range(2):
        print(tuple_b[i], tuple_a[0])
        if len(tuple_b) == 1 and i == 0:
            sum_result = sum_result + (tuple_a[i] + tuple_b[0],)
        elif len(tuple_a) == 1 and i == 0:
            sum_result = sum_result + (tuple_a[0] + tuple_b[i],)
        elif len(tuple_b) == 1 and i == 1:
            sum_result = sum_result + (tuple_a[i] + 0,)
        elif len(tuple_a) == 1 and i == 1:
            sum_result = sum_result + (0 + tuple_b[i],)
        elif len(tuple_b) == 0:
            sum_result = sum_result + (tuple_a[i] + 0,)
        elif len(tuple_b) >= 2:
            sum_result = sum_result + (tuple_a[i] + tuple_b[i],)
    return sum_result
    """
