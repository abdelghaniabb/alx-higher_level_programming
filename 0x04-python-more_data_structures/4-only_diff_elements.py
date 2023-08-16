#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_common = set()
    set_diff = set()
    for item1 in set_1:
        for item2 in set_2:
            if item2 is item1:
                set_common.add(item1)
            set_diff.add(item1)
            set_diff.add(item2)

    for item in set_common:
        set_diff.remove(item)
    return set_diff
