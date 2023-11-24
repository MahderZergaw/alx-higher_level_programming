#!/usr/bin/python3
"""lists all states with a name starting with "N" from
 the database hbtn_0e_0_usa"""

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

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY "
                   "'{}' ORDER BY id ASC".format(name))

    rows = cursor.fetchall()
    for r in rows:
        print(r)

    db.close()
