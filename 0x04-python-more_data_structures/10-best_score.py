#!/usr/bin/python3
def best_score(a_dictionary):
    best_key = None
    score = -100
    if a_dictionary != None:
        for key in a_dictionary:
            if a_dictionary[key] > score:
                score = a_dictionary[key]
                best_key = key
    return best_key