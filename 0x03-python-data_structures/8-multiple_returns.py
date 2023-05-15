#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    first_char = sentence[0]
    if lenght == 0:
        first_char = None
    return (lenght, first_char)
