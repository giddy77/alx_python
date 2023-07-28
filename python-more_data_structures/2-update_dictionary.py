def print_sorted_dictionary(my_dict):
    if my_dict:
        for key in sorted(my_dict.keys()):
            print("{}: {}".format(key, my_dict[key]))
