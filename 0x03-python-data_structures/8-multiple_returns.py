#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        sentence = ""
    lenght = len(sentence)
    first_char = sentence[0]
    if lenght == 0:
        first_char = None
    return (lenght, first_char)
