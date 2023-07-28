def multiple_returns(sentence=""):
    if len(sentence) == 0:
        return (None, None)
    else:
        return (len(sentence), sentence[0])


    
result = multiple_returns()
if result[0] is not None:
    length, first = result
    print("Length: {} - First character: {}".format(length, first))
else:
    print("Length: {} - First character: {}".format(result[0], result[1]))
