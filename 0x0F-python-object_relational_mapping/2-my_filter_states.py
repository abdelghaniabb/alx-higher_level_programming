#!/usr/bin/python3
"""
    takes in an argument and displays all values in the states table of
    hbtn_0e_0_usa where name matches the argument.
"""


import MySQLdb
import sys

# Trying to connect
try:
    db_connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3])
# If connection is not successful
except Exception as e:
    print(e)
    exit()

cursor = db_connection.cursor()
cmd = """SELECT * FROM states WHERE name = '{}'
ORDER BY id ASC""".format(sys.argv[4])
cursor.execute(cmd)
data = cursor.fetchall()

for state in data:
    print(state)

cursor.close()
db_connection.close()
