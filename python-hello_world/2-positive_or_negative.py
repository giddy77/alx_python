#!/usr/bin/python3
import random
number = random.randint(-10, 10)

print(number)

if number > 0:
    print('is postive')
elif number == 0:
    print('is zero')
else:
    print('is negative')