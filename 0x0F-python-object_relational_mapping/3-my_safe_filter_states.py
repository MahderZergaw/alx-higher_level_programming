#!/usr/bin/python3
""" write a script that takes in arguments and displays all
 values in the states table of hbtn_0e_0_usa where name matches
 the argument. But this time, write one that is safe from MySQL
 injections!"""

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
    name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name=%s "
                   "ORDER BY id ASC", (name,))

    rows = cursor.fetchall()
    for r in rows:
        print(r)

    db.close()
