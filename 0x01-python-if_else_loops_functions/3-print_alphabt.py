#!/usr/bin/python3
for exc in range(97, 123):
    if (exc != 101 and exc != 113):
        print("{:c}".format(exc), end="")
