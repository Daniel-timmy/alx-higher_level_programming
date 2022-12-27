#!/usr/bin/python3
"""
Lists all state in the database
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    curr = db.cursor()
    curr.execute("SELECT * FROM states;")
    state = curr.fetchall()
    for item in state:
        print(item)
