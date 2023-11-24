#!/usr/bin/python3
""" takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    Connects to a MySQL server

    Args:
    - sys.argv[1]: MySQL username
    - sys.argv[2]: MySQL password
    - sys.argv[3]: Name of the database containing the states table
    - sys.argv[4]: Name of the state to search for cities
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)

    cursor = db.cursor()

    cursor.execute("SELECT cities.name FROM cities "
                   "INNER JOIN states ON cities.state_id "
                   "= states.id WHERE states.name = %s "
                   "ORDER BY cities.id ASC", (state_name,))

    rows = cursor.fetchall()
    city = [r[0] for r in rows]
    print(', '.join(city))

    db.close()
