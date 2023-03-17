#!/usr/bin/python3

"""
script to connect to MySQL server running on localhost
on port 3306
"""
import sys
import MySQLdb as db

[USERNAME, PASSWORD, DB_NAME] = sys.argv[1:4]


if __name__ == "__main__":
    try:
        cnx = db.connect(user=USERNAME, passwd=PASSWORD, db=DB_NAME)
        cursor = cnx.cursor(cursorclass=db.cursors.Cursor)
        cursor.execute('SELECT * FROM states ORDER BY `id` ASC;')
        states = cursor.fetchall()

        for state in states:
            print(state)
    except Exception as e:
        print(e)
    finally:
        cnx.close()
        cursor.close()
