#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

l = number % 10
if l == 0:
    print("Last digit of {:d} is {:.0f} and is 0".format(number, l))
elif number < 0:
	l = ((number * -1) % 10) * -1
	print("Last digit of {:d} is {:.0f} and is less than 6 and not 0".format(number, l))
elif l > 5:
    print("Last digit of {:d} is {:.0f} and is greater than 5".format(number, l))
else:
	print("Last digit of {:d} is {:.0f} and is less than 6 and not 0".format(number, l))
