#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i == 9:
            if j != 9:
                print(f'{i}{j}'.format(i, j), end=', ')
            else:
                print(f'{i}{j}'.format(i, j))
        else:
            print(f'{i}{j}'.format(i, j), end=', ')
