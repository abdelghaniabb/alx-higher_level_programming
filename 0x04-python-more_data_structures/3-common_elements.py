#!/usr/bin/python3
def common_elements(set_1, set_2):
    set0 = set()
    for item1 in set_1:
        for item2 in set_2:
            if item2 is item1:
                set0.add(item1)
    return set0
