#!/usr/bin/python3
"""
     lists all cities from the database hbtn_0e_4_usa
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
cmd = """SELECT cities.id, cities.name, states.name FROM cities, states
        WHERE cities.state_id = states.id ORDER BY cities.id;"""
cursor.execute(cmd)
data = cursor.fetchall()

for state in data:
    print(state)

cursor.close()
db_connection.close()
