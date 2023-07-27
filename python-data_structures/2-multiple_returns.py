def multiple_returns(sentence):
    if len(sentence) == 0:
        return (None, None)
    else:
        return (len(sentence), sentence[0])
    
length,first = len(multiple_returns())
print("Length: {} - First character: {}".format(length, first))
