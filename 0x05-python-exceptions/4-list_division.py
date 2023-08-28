#!/usr/bin/python3
def list_division(my_list1, my_list2, list_length):
    """divides element by element 2 lists."""
    index = 0
    new = []
    while index < list_length:
        try:
            result = my_list1[index] / my_list2[index]
            index = index + 1
        except Exception:
            try:
                v1 = int(my_list1[index])
                v2 = int(my_list2[index])
                if v2 == 0:
                    print("division by 0")
                    result = 0
                    index = index + 1
            except Exception:
                if len(my_list1) <= index + 1 or len(my_list2) <= index + 1:
                    print("out of range")
                else:
                    print("wrong type")
                result = 0
                index = index + 1
        new.append(result)

    return new
