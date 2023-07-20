# #!/usr/bin/python3
# import random

# number = random.randint(-10000, 10000)
# last_digit = abs(number) % 10

# # if number < 0 and number!=0:
# #     sign = '-'
# # else:
# #     sign = ''

# print('last digit of {} is {} '.format( number,last_digit), end="\n")

# if last_digit > 5:
#     print('and is greater than 5')
# elif last_digit == 0:
#     print('and is 0')
# elif number < 0:
#     last_digit = -last_digit
# else:
#     print('and is less than 6 and not 0')


import random

number = random.randint(-10000, 10000)

# Get the last digit of the number using the modulo operator (%)
last_digit = abs(number) % 10

# Determine the sign of the last digit
last_digit_sign = "-" if number < 0 else ""

# Determine the output message based on the last digit and sign
output_message = f"The string Last digit of {number} is {last_digit_sign}{last_digit}"

if last_digit > 5:
    output_message += " and is greater than 5"
elif last_digit == 0:
    output_message += " and is 0"
else:
    output_message += " and is less than 6 and not 0"

# Print the output message with a new line
print(output_message)

