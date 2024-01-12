#!/usr/bin/python3
"""script lists all states from databases hbtn_0e_0_usa"""


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
    print(state)

cursor.close()
db_connection.close()
