#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

if number < 0 and number!=0:
    sign = '-'
else:
    sign = ''

print('last digit of {} is {}{} '.format( number, sign,last_digit), end="")

if last_digit > 5:
    print('and is greater than 5')
elif last_digit == 0:
    print('and is 0')
else:
    print('and is less than 6 and not 0')

if number < 0:
    last_digit = number % -10
    print('last digit of {} is {} '.format( number,last_digit), end="\n")

