#!/usr/bin/python3
def list_division(my_list1, my_list2, list_length):
    """divides element by element 2 lists."""
    index = 0
    new = []
    while index < list_length:
        t = False
        try:
            result = my_list1[index] / my_list2[index]
            index = index + 1
        except Exception:
            try:
                v1 = float(my_list1[index])
                l1 = type(my_list1[index]) in [float, int]
                if not (l1 and type(my_list2[index]) in [float, int]):
                    t = True
                    v2 = float("my_list2[index]")
                v2 = float(my_list2[index])
                if v2 == 0:
                    print("division by 0")
            except Exception:
                if t == True:
                    print("wrong type")
                elif len(my_list1) <= index + 1 or len(my_list2) <= index + 1:
                    print("out of range")
            finally:
                index = index + 1
                result = 0

        new.append(result)

    return new
