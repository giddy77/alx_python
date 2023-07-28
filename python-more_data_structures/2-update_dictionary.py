def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value

# Test the function
my_dict = {'name': 'John', 'age': 30}
print("Original Dictionary:", my_dict)

update_dictionary(my_dict, 'name', 'Mike')
print("Updated Dictionary:", my_dict)

update_dictionary(my_dict, 'city', 'New York')
print("Dictionary with added key/value pair:", my_dict)
