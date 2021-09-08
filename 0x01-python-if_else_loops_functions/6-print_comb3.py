#!/usr/bin/python3
for k in range(0, 10):
    for j in range(0, 10):
        if k < j and k != 8:
            print("{:d}{:d}".format(k, j), end=', ')
        if k < j and k == 8:
            print("{:d}{:d}".format(k, j))
