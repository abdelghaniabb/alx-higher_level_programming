#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = []
    for ele1 in set_1:
        for ele2 in set_2:
            if ele1 ==  ele2:
                common.append(ele1)
    return common
