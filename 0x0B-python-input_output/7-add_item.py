#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""


import sys
import json


try:
    with open("add_item.json", "r", encoding="utf-8") as infile:
        my_list = json.loads(infile.read())
    infile.close()
except Exception:
    my_list = []


for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])

with open("add_item.json", "w", encoding="utf-8") as outfile:
    outfile.write(json.dumps(my_list))
