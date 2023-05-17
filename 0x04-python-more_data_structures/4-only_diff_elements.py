#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    found_elements = []
    found_common = []
    found_diff = []
    for ele1 in set_1:
        for ele2 in set_2:
            if ele1 == ele2:
                found_common.append(ele1)
    for ele1 in set_1:
        for ele in found_common:
            if ele != ele1:
                found_elements.append(ele1)
    for ele2 in set_2:
        for ele in found_common:
            if ele != ele2:
                found_elements.append(ele2)
    return found_elements
