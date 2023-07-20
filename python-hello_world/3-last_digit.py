# #!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Get the last digit of the number using the modulo operator (%)
last_digit = abs(number) % 10

# Get the sign of the number
sign = "-" if number < 0 else ""

# Determine the output message based on the last digit and sign
output_message = "The string Last digit of {}{} is {}".format(sign, abs(number), sign + str(last_digit))

if last_digit > 5:
    output_message += " and is greater than 5"
elif last_digit == 0:
    output_message += " and is 0"
else:
    output_message += " and is less than 6 and not 0"

# Print the output message with a new line
print(output_message)
