#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            print(f"{chr(ord(c) - 32)}".format(c), end='\0')
        else:
            print(f"{c}".format(c), end='\0')
