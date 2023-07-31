#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    # Check if the key exists in the dictionary
    if key in a_dictionary:
        # Update the existing key with the new value
        a_dictionary[key] = value
    else:
        # Add the new key-value pair to the dictionary
        a_dictionary[key] = value

# Define the dictionary
my_dict = {'a': 'A', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e'}

# Call the update_dictionary function
update_dictionary(my_dict, 'xx', None)

# Sort and print the key-value pairs in the dictionary
for k in sorted(my_dict):
    print("{}: {}".format(k, my_dict[k]))
