def multiple_returns(sentence=""):
    if len(sentence) == 0:
        return (None, None)
    else:
        print ("Length: {} - First character: {} ".format(len(sentence), sentence[0]))
        
multiple_returns()