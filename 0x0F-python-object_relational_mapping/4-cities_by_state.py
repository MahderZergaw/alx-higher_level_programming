#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    Connects to a MySQL server

    Args:
    - sys.argv[1]: MySQL username
    - sys.argv[2]: MySQL password
    - sys.argv[3]: Name of the database containing the states table
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name FROM "
                   "cities INNER JOIN states ON cities.state_id "
                   "= states.id ORDER BY cities.id ASC")

    rows = cursor.fetchall()
    for r in rows:
        print(r)

    db.close()
