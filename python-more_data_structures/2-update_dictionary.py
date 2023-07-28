def print_sorted_dictionary(my_dict):
    if my_dict:
        for key in sorted(my_dict.keys()):
            value = my_dict[key]
            if value is None:
                print(key)
            else:
                print(f"{key}: {value}")