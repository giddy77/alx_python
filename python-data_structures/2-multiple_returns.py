sentence = ''
def multiple_returns(sentence):
    if len(sentence) == 0:
        return (None)
    
length = len(sentence)
first = sentence[0]
       
print("Length :{} - First character: {}".format(length, first))