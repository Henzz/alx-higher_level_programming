#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in my_list:
            if (count < x):
                print(i, end='')
                count += 1
        print()
        return count
    except IndexError:
        print("Index unknown")
    except Exception:
        print("An unknow error occured")
