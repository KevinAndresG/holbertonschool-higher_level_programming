#!/usr/bin/python3
def fizzbuzz():
    for k in range(1, 101):
        if k % 15 == 0:
            print("{}".format("FizzBuzz "), end="")
        elif k % 5 == 0:
            print("{}".format("Buzz "), end="")
        elif k % 3 == 0:
            print("{}".format("Fizz "), end="")
        else:
            print("{:d} ".format(k), end="")
