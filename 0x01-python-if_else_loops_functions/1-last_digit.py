#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit = abs(number) % 10
if number < 0:
    l_digit = -l_digit
print(f"Last digit of {number} is {l_digit} and is ", end="")
if l_digit > 5:
    print("greater than 5")
elif l_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
