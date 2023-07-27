def multiple_returns(sentence):
    if len(sentence) == 0:
        return (None, None)
    else:
        return (len(sentence), sentence[0])

# Call the function and capture the results
length, first = multiple_returns()
print("Length: {} - First character: {}".format(length, first))

# # Test with an empty string
# length, first = multiple_returns("")
# print("Length: {} - First character: {}".format(length, first))
