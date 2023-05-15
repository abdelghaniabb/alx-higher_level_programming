#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        sentence = ""
    lenght = len(sentence)
    if lenght == 0:
        first_char = None
    else:
        first_char = sentence[0]
    return (lenght, first_char)
