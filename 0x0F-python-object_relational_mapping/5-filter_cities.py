#!/usr/bin/python3
"""
    takes in the name of a state as an argument and lists
    all cities of that state, using the database hbtn_0e_4_usa
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
c = sys.argv[4]

# Use parameterized query to avoid SQL injection
cmd = """SELECT cities.name FROM states, cities
        WHERE cities.state_id = states.id AND states.name = %s
        ORDER BY cities.id;"""
cursor.execute(cmd, (c, ))

data = cursor.fetchall()

arry = list()
for state in data:
    arry.append(state[0])

print(', '.join(arry))

cursor.close()
db_connection.close()
