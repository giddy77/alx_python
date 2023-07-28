def multiple_returns(sentence):
    len = len(sentence)
    char = sentence[0] if len > 0 else None
    
    return len, char

multiple_returns()
