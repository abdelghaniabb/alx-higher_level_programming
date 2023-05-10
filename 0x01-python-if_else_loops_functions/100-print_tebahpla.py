#!/usr/bin/python3
i = 122
while((i >= 65 and i <= 90) or (i >= 97 and i <= 122)):
    print("{}".format(chr(i)), end="")
    if i >= 65 and i <= 90:
        i = i + 32 - 1
    else:
        i = i - 32 - 1
