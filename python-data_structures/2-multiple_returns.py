
sentence = ''  
def multiple_returns(sentence):
    if len(sentence) == 0:
        return (None, None)  
length = len(sentence)
first = sentence[0]
multiple_returns(sentence)
print("Length: {} - First character: {}".format(length, first))
