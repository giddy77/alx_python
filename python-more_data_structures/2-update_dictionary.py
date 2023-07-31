def update_dictionary(a_dictionary, key, value):
    # Check if the key exists in the dictionary
    if key in a_dictionary:
        # Update the existing key with the new value
        a_dictionary[key] = value
    else:
        # Add the new key-value pair to the dictionary
        a_dictionary[key] = value
