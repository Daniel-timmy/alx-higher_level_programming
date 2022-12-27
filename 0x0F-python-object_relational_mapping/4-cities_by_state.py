#!/usr/bin/python3
"""
Lists all city according to the cities.id in the database
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    curr = db.cursor()
    curr.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON state_id = states.id ORDER BY cities.id ASC;")
    cities = curr.fetchall()
    for city in cities:
        print(city)
