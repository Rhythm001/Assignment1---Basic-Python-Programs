#Program to generate a random number.

import random

print("Enter the range between which you want to generate random numbers.")
a = int(input("Start: "))
b = int(input("End: "))
c = random.randint(a, b)
print("Random number:", c)