def multiple_returns(sentence):
    if len(sentence) == 0:
        return (None, None)
    return (len(sentence), sentence[0])

result = multiple_returns()
print("Length: {} - First character: {}".format(result[0], result[1]))

