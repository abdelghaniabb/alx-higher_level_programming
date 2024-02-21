#!/usr/bin/python3
"""lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa"""


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

cursor.execute("SELECT * FROM states ORDER BY id ASC")
data = cursor.fetchall()

for state in data:
    if state[1].startswith('N'):
        print(state)

cursor.close()
db_connection.close()
