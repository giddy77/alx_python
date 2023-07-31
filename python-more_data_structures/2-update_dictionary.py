def update_dictionary(a_dictionary, key, value):
    # Check if the key exists in the dictionary
    if key in a_dictionary:
        # Update the existing key with the new value
        a_dictionary[key] = value
    else:
        # Add the new key-value pair to the dictionary
        a_dictionary[key] = value

    # Sort the dictionary by keys and print the key-value pairs
    sorted_dict = {k: a_dictionary[k] for k in sorted(a_dictionary)}
    for k in sorted_dict:
        print("{}: {}".format(k, sorted_dict[k]))

