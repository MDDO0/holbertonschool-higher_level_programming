#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(number,"%s is positive")
elif number == 0:
    print(number,"%s is zero")
else:
    print(number,"%s is negative")
