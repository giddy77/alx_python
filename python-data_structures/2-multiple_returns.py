def multiple_returns(sentence):
    if len(sentence) == 0:
        return (None, None)
    print("Length: {} - First character: {}".format(len(sentence), sentence[0]))

result = multiple_returns("Holberton")
