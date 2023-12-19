#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        i = 0
        no_printed = 0
        while i < x:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end='')
                no_printed += 1
            i += 1
        print()
        return no_printed
    except IndexError:
        print(end='')
        raise
    except Exception:
        print("An unknow error has occured")
