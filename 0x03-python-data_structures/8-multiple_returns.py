#!/usr/bin/python3
def multiple_returns(sentence):
    n = len(sentence)

    if (n == 0):
        tuplen = (n, None)
    else:
        tuplen = (n, sentence[0])
    
    return (tuplen)
