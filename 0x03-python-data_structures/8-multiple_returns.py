#!/usr/bin/python3
def multiple_returns(sentence):
    lth = len(sentence)
    f_char = None
    if lth > 0:
        f_char = sentence[0]
    return (lth, f_char)
